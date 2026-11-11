# Bounded campaign supervisor

`runner.py` uses the Python standard library. It schedules independent seeded
worker processes; it does not decide whether a scientific result passes.

## Interface

The last option is `--worker`, followed by an executable and its fixed arguments.
The supervisor appends `--seed SEED --output CASE_DIRECTORY/result.json` to each
invocation. Seeds are reproducible 63-bit integers derived from the campaign
seed and case index. A completed execution requires exit code zero and a valid
finite JSON output file. Scientific rejection/control outcomes should be
recorded inside that JSON rather than conflated with execution failure.

Example (replace WORKER and SOURCE with actual absolute paths):

```bash
cd /workspace/work/craig/campaign
nohup python3 runner.py --seconds 18000 --workers 2 --seed 261009093 \
  --output /workspace/work/craig/campaign/run-5h \
  --code SOURCE \
  --worker WORKER \
  > /workspace/work/craig/campaign/run-5h-launch.log 2>&1 < /dev/null &
```

The launch shell exits immediately. Verify `status.json` and the process after
launch; a successful launch is not a completed campaign. Local persistence was
checked with a short detached process that survived its launching tool call.
A cloud environment shutdown can still end all local processes.

`--env KEY=VALUE` supplies repeatable worker environment overrides before
`--worker`. OMP, OpenBLAS, MKL, BLIS, Accelerate, and NumExpr thread counts default
to one. Two concurrent single-threaded workers use the environment's two-CPU
allocation. `--case-seconds` optionally imposes a shorter per-case timeout.

## Outputs and termination

- `run.json`: immutable launch settings, command, source/executable SHA256s.
- `code_snapshot/`: copies of hashed source/executable files.
- `status.json`: atomic status and remaining budget, updated at least every
  five seconds and on case transitions.
- `manifest.jsonl`: single-writer, fsynced start/finish records.
- `cases/NNNNNNNN/`: `stdout.log`, `stderr.log`, and worker `result.json`.

At 18,000 elapsed campaign wall seconds, active worker process groups receive
SIGKILL. The final partial cases remain on disk and are marked `timed_out`,
never `completed`. A finite JSON result file appearing just at the deadline is
still classified conservatively as timed out if its process was still active.
Three consecutive execution errors stop the campaign to avoid repeated wasted
compute. Scientific outcomes inside successful JSON results do not trigger
this execution-error circuit breaker.

Send SIGTERM to the supervisor PID in `status.json` to stop early. All active
case process groups are killed and marked `interrupted`. The supervisor uses
a Linux parent-death signal for workers and a lock to prevent two supervisors
from sharing the same output directory.

## Resume

Repeat the exact original working directory, source paths, worker command,
environment overrides, and per-case/error limits, adding `--resume`:

```bash
python3 runner.py --resume --output /workspace/work/craig/campaign/run-5h \
  --code SOURCE --worker WORKER
```

The original total wall-clock budget remains 18,000 seconds. Completed cases
are retained and new deterministic case IDs follow existing ones. Interrupted
cases are retained distinctly; they are not counted as completed or retried
silently. Source or executable hash changes reject resumption. When recovering
from an unexpected supervisor death, up to five seconds of uncheckpointed
runtime are charged conservatively to the remaining budget.

## Validation performed

`python3 runner_selftest.py` passed: parallel completion, strict JSON result
handling, hard campaign deadline, timeout classification, thread environment,
signal cleanup, remaining-budget resumption, budget-extension rejection, and
source-hash-change rejection. Tests use bounded fake workers, not physics.
