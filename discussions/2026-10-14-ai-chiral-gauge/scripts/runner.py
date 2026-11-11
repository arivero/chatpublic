#!/usr/bin/env python3
"""Bounded, resumable local numerical campaign supervisor (Python stdlib).

Example (shell redirection is outside this program):
  nohup python3 runner.py --seconds 18000 --workers 2 --seed 261009093 \
      --output /workspace/work/craig/campaign/run --code worker.c \
      --worker /absolute/path/worker > launch.log 2>&1 < /dev/null &

The worker receives --seed SEED --output CASE_DIR/result.json. Exit zero plus
valid JSON means execution completed, not that any scientific claim passed.
Resume preserves the ORIGINAL total wall-clock budget; it never adds hours:
  python3 runner.py --resume --output RUN_DIR --code worker.c --worker WORKER
A killed supervisor is recoverable: status is checkpointed every five seconds,
and unfinished cases are explicitly marked interrupted on the next invocation.
"""
import argparse
import ctypes
import datetime as dt
import fcntl
import hashlib
import json
import math
import os
from pathlib import Path
import resource
import shlex
import shutil
import signal
import subprocess
import sys
import time

VERSION = 1
THREAD_DEFAULTS = {k: '1' for k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS',
    'MKL_NUM_THREADS', 'BLIS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS',
    'NUMEXPR_NUM_THREADS')}
STOP_SIGNAL = None


def utc():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def digest(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def atomic_json(path, value):
    tmp = path.with_name(path.name + '.tmp')
    with open(tmp, 'w') as f:
        json.dump(value, f, indent=2, sort_keys=True, allow_nan=False)
        f.write('\n')
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


def append_event(path, value):
    data = (json.dumps(value, sort_keys=True, allow_nan=False) + '\n').encode()
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o600)
    try:
        while data:
            n = os.write(fd, data)
            data = data[n:]
        os.fsync(fd)
    finally:
        os.close(fd)


def load_events(path):
    if not path.exists():
        return []
    data = path.read_bytes()
    records = []
    good = 0
    for line in data.splitlines(keepends=True):
        if not line.endswith(b'\n'):
            break
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError:
            raise SystemExit('Manifest has invalid complete record; investigate before resume.')
        good += len(line)
    if good != len(data):
        # Retain a torn final record for inspection; only truncate that record.
        path.with_name('manifest.torn.' + str(time.time_ns())).write_bytes(data[good:])
        with open(path, 'r+b') as f:
            f.truncate(good)
    return records


def case_seed(base, number):
    return int.from_bytes(hashlib.sha256(f'{base}:{number}'.encode()).digest()[:8], 'big') & ((1 << 63) - 1)


def child_setup():
    # Linux parent-death signal avoids leaving a CPU worker if the supervisor
    # is killed unexpectedly. Workers are session leaders, so group cleanup
    # also reaches their children on normal interruption or deadline.
    parent = os.getppid()
    try:
        libc = ctypes.CDLL(None)
        libc.prctl(1, signal.SIGTERM, 0, 0, 0)  # PR_SET_PDEATHSIG
        if os.getppid() != parent or parent == 1:
            os._exit(128 + signal.SIGTERM)
    except (AttributeError, OSError):
        pass
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
    os.nice(5)


def kill_group(proc, sig):
    try:
        os.killpg(proc.pid, sig)
    except ProcessLookupError:
        pass


def stop_handler(signum, _frame):
    global STOP_SIGNAL
    STOP_SIGNAL = signum


def cpu_default():
    try:
        return min(2, len(os.sched_getaffinity(0)))
    except AttributeError:
        return min(2, os.cpu_count() or 1)


def parse():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--seconds', type=float, default=None, help='total campaign wall budget; default 18000; resume does not extend it')
    p.add_argument('--seed', type=int, default=None, help='campaign seed; default 261009093')
    p.add_argument('--workers', type=int, default=None, help='parallel cases; default min(2, CPU affinity count)')
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--resume', action='store_true')
    p.add_argument('--code', type=Path, action='append', default=[], help='additional scientific source/config file to hash, repeatable')
    p.add_argument('--env', action='append', default=[], metavar='KEY=VALUE', help='worker environment override, repeatable')
    p.add_argument('--case-seconds', type=float, default=None, help='optional per-case limit; campaign deadline always wins')
    p.add_argument('--max-consecutive-errors', type=int, default=3, help='stop after this many worker execution errors')
    p.add_argument('--worker', nargs=argparse.REMAINDER, required=True, help='worker command and arguments; must be last option')
    a = p.parse_args()
    if not a.worker:
        p.error('--worker needs a command')
    if a.seconds is not None and (not math.isfinite(a.seconds) or a.seconds <= 0):
        p.error('--seconds must be positive and finite')
    if a.workers is not None and not 1 <= a.workers <= 16:
        p.error('--workers must be between 1 and 16')
    if a.case_seconds is not None and (not math.isfinite(a.case_seconds) or a.case_seconds <= 0):
        p.error('--case-seconds must be positive and finite')
    if a.max_consecutive_errors < 1:
        p.error('--max-consecutive-errors must be positive')
    return a


def main():
    args = parse()
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=True)
    lock = open(out / '.runner.lock', 'a+')
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        raise SystemExit('Another supervisor already holds this output directory.')
    manifest = out / 'manifest.jsonl'
    config_path = out / 'run.json'
    status_path = out / 'status.json'
    exe = shutil.which(args.worker[0])
    if not exe:
        raise SystemExit('Worker executable not found: ' + args.worker[0])
    command = [str(Path(exe).resolve()), *args.worker[1:]]
    overrides = dict(THREAD_DEFAULTS)
    for item in args.env:
        if '=' not in item or not item.split('=', 1)[0]:
            raise SystemExit('--env requires KEY=VALUE')
        k, v = item.split('=', 1)
        overrides[k] = v
    files = {Path(__file__).resolve(), Path(exe).resolve()}
    for file in args.code:
        if not file.is_file():
            raise SystemExit('Code/config file not found: ' + str(file))
        files.add(file.resolve())
    for argument in command[1:]:
        if Path(argument).is_file():
            files.add(Path(argument).resolve())
    hashes = {str(file): digest(file) for file in sorted(files)}
    identity = {'command': command, 'cwd': os.getcwd(), 'environment_overrides': overrides,
                'sha256': hashes, 'case_seconds': args.case_seconds,
                'max_consecutive_errors': args.max_consecutive_errors}
    if args.resume:
        if not config_path.exists() or not status_path.exists():
            raise SystemExit('--resume requires existing run.json and status.json')
        config = json.loads(config_path.read_text())
        if config['identity'] != identity:
            raise SystemExit('Resume rejected: command, environment, working directory, limits, or exact code hashes changed.')
        for key in ('seconds', 'seed', 'workers'):
            supplied = getattr(args, key)
            if supplied is not None and supplied != config[key]:
                raise SystemExit(f'Resume rejected: {key} differs from original campaign; no silent budget extension.')
        old_status = json.loads(status_path.read_text())
        consumed = float(old_status['elapsed_seconds'])
        events = load_events(manifest)
        started = {e['case_id']: e for e in events if e['event'] == 'case_started'}
        ended = {e['case_id'] for e in events if e['event'] == 'case_finished'}
        for case_id in sorted(set(started) - ended):
            append_event(manifest, {'event': 'case_finished', 'case_id': case_id,
                'seed': started[case_id]['seed'], 'state': 'interrupted_after_supervisor_restart',
                'utc': utc(), 'note': 'Incomplete output retained; this case is not counted as completed.'})
        # A crash can lose <=5s checkpoint time. Charge it conservatively so
        # resuming cannot silently purchase additional runtime.
        if old_status.get('state') == 'running':
            consumed = min(config['seconds'], consumed + 5.0)
    else:
        if config_path.exists() or manifest.exists():
            raise SystemExit('Output already contains a campaign; use --resume or a fresh directory.')
        config = {'version': VERSION, 'created_utc': utc(), 'seconds': args.seconds or 18000.0,
                  'seed': args.seed if args.seed is not None else 261009093,
                  'workers': args.workers or cpu_default(), 'identity': identity,
                  'supervisor_python': sys.version, 'host': os.uname()._asdict() if hasattr(os.uname(), '_asdict') else list(os.uname())}
        consumed = 0.0
        atomic_json(config_path, config)
        # Exact executable/source copies make provenance inspectable even if
        # later work edits the originals. Repeated names remain unambiguous.
        (out / 'code_snapshot').mkdir(exist_ok=True)
        for n, file in enumerate(sorted(files)):
            shutil.copyfile(file, out / 'code_snapshot' / f'{n:02d}_{file.name}')
    events = load_events(manifest)
    next_case = max((e['case_id'] for e in events if 'case_id' in e), default=-1) + 1
    counts = {}
    for e in events:
        if e['event'] == 'case_finished':
            counts[e['state']] = counts.get(e['state'], 0) + 1
    total = float(config['seconds'])
    started_at = time.monotonic()
    deadline = started_at + max(0.0, total - consumed)
    active = {}
    consecutive_errors = 0
    final_state = None
    env = os.environ.copy()
    env.update(overrides)
    for sig in (signal.SIGINT, signal.SIGTERM, signal.SIGHUP):
        # nohup intentionally ignores SIGHUP; preserve that behavior.
        if sig != signal.SIGHUP or signal.getsignal(sig) != signal.SIG_IGN:
            signal.signal(sig, stop_handler)
    append_event(manifest, {'event': 'supervisor_started', 'utc': utc(), 'pid': os.getpid(),
                           'remaining_seconds': max(0.0, total - consumed), 'resume': args.resume})

    def checkpoint(state):
        elapsed = min(total, consumed + time.monotonic() - started_at)
        atomic_json(status_path, {'state': state, 'updated_utc': utc(), 'supervisor_pid': os.getpid(),
            'total_budget_seconds': total, 'elapsed_seconds': elapsed,
            'remaining_seconds': max(0.0, total - elapsed), 'counts': counts,
            'active': [{'case_id': n, 'seed': j['seed'], 'pid': j['proc'].pid,
                        'elapsed_seconds': time.monotonic() - j['started']} for n, j in active.items()],
            'next_case_id': next_case,
            'scientific_interpretation': 'Execution status only; inspect worker results and controls.'})

    def finish(number, state=None):
        job = active.pop(number)
        proc = job['proc']
        rc = proc.wait()
        # Ensure descendants cannot outlive their case, even after a leader exits.
        kill_group(proc, signal.SIGKILL)
        job['stdout'].close()
        job['stderr'].close()
        result = job['directory'] / 'result.json'
        invalid = None
        if state is None:
            if rc != 0:
                state = 'worker_error'
            elif not result.exists():
                state = 'missing_result'
            else:
                try:
                    with open(result) as f:
                        json.load(f, parse_constant=lambda s: (_ for _ in ()).throw(ValueError('nonfinite JSON: ' + s)))
                    state = 'completed'
                except (ValueError, OSError) as exc:
                    state = 'invalid_result'
                    invalid = str(exc)
        event = {'event': 'case_finished', 'case_id': number, 'seed': job['seed'],
                 'state': state, 'returncode': rc, 'utc': utc(),
                 'elapsed_seconds': time.monotonic() - job['started'],
                 'result_exists': result.exists()}
        if result.exists():
            event['result_sha256'] = digest(result)
        if invalid:
            event['error'] = invalid
        append_event(manifest, event)
        counts[state] = counts.get(state, 0) + 1
        return state

    checkpoint('running')
    last_checkpoint = time.monotonic()
    print(json.dumps({'state': 'running', 'pid': os.getpid(), 'output': str(out),
                      'remaining_seconds': max(0.0, total-consumed), 'workers': config['workers']}), flush=True)
    try:
        while True:
            now = time.monotonic()
            if now >= deadline:
                final_state = 'budget_exhausted'
                break
            if STOP_SIGNAL:
                final_state = 'interrupted'
                break
            for number, job in list(active.items()):
                timed_out = args.case_seconds is not None and now - job['started'] >= args.case_seconds
                if timed_out and job['proc'].poll() is None:
                    kill_group(job['proc'], signal.SIGKILL)
                    state = finish(number, 'case_timed_out')
                elif job['proc'].poll() is not None:
                    state = finish(number)
                else:
                    continue
                if state == 'completed':
                    consecutive_errors = 0
                else:
                    consecutive_errors += 1
            if consecutive_errors >= args.max_consecutive_errors:
                final_state = 'stopped_worker_errors'
                break
            while len(active) < config['workers'] and time.monotonic() < deadline:
                number = next_case
                next_case += 1
                seed = case_seed(config['seed'], number)
                directory = out / 'cases' / f'{number:08d}'
                directory.mkdir(parents=True, exist_ok=False)
                stdout = open(directory / 'stdout.log', 'wb')
                stderr = open(directory / 'stderr.log', 'wb')
                argv = command + ['--seed', str(seed), '--output', str(directory / 'result.json')]
                t0 = time.monotonic()
                try:
                    proc = subprocess.Popen(argv, stdout=stdout, stderr=stderr, stdin=subprocess.DEVNULL,
                        env=env, start_new_session=True, preexec_fn=child_setup)
                except Exception:
                    stdout.close()
                    stderr.close()
                    raise
                active[number] = {'proc': proc, 'seed': seed, 'started': t0, 'directory': directory,
                                  'stdout': stdout, 'stderr': stderr}
                append_event(manifest, {'event': 'case_started', 'case_id': number, 'seed': seed,
                    'pid': proc.pid, 'utc': utc(), 'argv': argv})
                checkpoint('running')
                last_checkpoint = time.monotonic()
            if time.monotonic() - last_checkpoint >= 5.0:
                checkpoint('running')
                last_checkpoint = time.monotonic()
            # Modest polling; never sleeps beyond the hard deadline.
            time.sleep(max(0.0, min(0.25, deadline - time.monotonic())))
    except BaseException as exc:
        final_state = 'supervisor_error'
        append_event(manifest, {'event': 'supervisor_exception', 'utc': utc(), 'error': repr(exc)})
        raise
    finally:
        if final_state is None:
            final_state = 'supervisor_error'
        # No grace period at the hard wall-clock cutoff. Partial files are kept.
        for job in active.values():
            kill_group(job['proc'], signal.SIGKILL)
        for number in list(active):
            state = 'timed_out' if final_state == 'budget_exhausted' else 'interrupted'
            finish(number, state)
        changed = {p: {'before': h, 'after': digest(p) if Path(p).exists() else None}
                   for p, h in hashes.items() if not Path(p).exists() or digest(p) != h}
        if changed:
            append_event(manifest, {'event': 'code_changed_during_run', 'utc': utc(), 'files': changed})
            final_state = 'code_changed_during_run'
        checkpoint(final_state)
        append_event(manifest, {'event': 'supervisor_finished', 'state': final_state, 'utc': utc(), 'counts': counts})
        print(json.dumps({'state': final_state, 'counts': counts, 'output': str(out)}), flush=True)
    return 0 if final_state == 'budget_exhausted' else 130 if final_state == 'interrupted' else 1


if __name__ == '__main__':
    sys.exit(main())
