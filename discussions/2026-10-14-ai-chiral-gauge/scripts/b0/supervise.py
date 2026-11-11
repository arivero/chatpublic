"""Bounded sequential B0 experiment. Never touches the previous campaign."""
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time
from worker import atomic

SOURCE=Path(__file__).resolve().parent


def utc():return dt.datetime.now(dt.timezone.utc).isoformat()
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--run',type=Path,required=True)
    p.add_argument('--seconds',type=int,default=18000);a=p.parse_args()
    a.run.mkdir(parents=True,exist_ok=False)
    preflight=json.loads((SOURCE/'preflight.json').read_text())
    if not preflight['passed']:raise ValueError('preflight has not passed')
    hashes={p.name:digest(p) for p in SOURCE.glob('*.py')}
    start=time.monotonic();deadline=start+a.seconds
    queue=[]
    # Refinement of each independent numerical approximation comes first.
    for mesh,n in [(2,4),(2,8),(2,16),(4,8),(4,16),(8,16),(8,32),(16,32)]:
        queue.append(dict(mesh=mesh,quadrature=n,a=0.,b=0.,purpose='base_convergence'))
    # One finite nongauge curl; no complete curl is claimed unless all four finish.
    for aa,bb in [(.01,0),(-.01,0),(0,.01),(0,-.01)]:
        queue.append(dict(mesh=8,quadrature=16,a=aa,b=bb,purpose='curl_step_0.01'))
    for aa,bb in [(.005,0),(-.005,0),(0,.005),(0,-.005)]:
        queue.append(dict(mesh=8,quadrature=16,a=aa,b=bb,purpose='curl_step_0.005'))
    for mesh,n,h in [(16,32,.005),(16,64,.005),(32,64,.005),(32,64,.0025)]:
        queue.append(dict(mesh=mesh,quadrature=n,a=0.,b=0.,source_step=h,purpose='finer_error_controls'))
    for item in queue:
        item.setdefault('source_step',.01);item.update(seed=261009093,amplitude=.4,weight_nodes=96)
    config=dict(started_utc=utc(),wall_budget_seconds=a.seconds,supervisor_pid=os.getpid(),
                deadline_utc=(dt.datetime.now(dt.timezone.utc)+dt.timedelta(seconds=a.seconds)).isoformat(),
                queue=queue,source_hashes=hashes,preflight=preflight,
                scope='Finite literal reconstructed 4D B0 only, no infinite current/theorem certificate.')
    atomic(a.run/'run.json',config)
    atomic(a.run.parent/'active-run.json',dict(directory=str(a.run),pid=os.getpid(),started_utc=config['started_utc'],deadline_utc=config['deadline_utc']))
    status=dict(state='running',completed_cases=[],interrupted_cases=[],active=None,errors=[],
                elapsed_seconds=0.,remaining_seconds=a.seconds,supervisor_pid=os.getpid())
    proc=None;stop=False
    def handler(*_):
        nonlocal stop
        stop=True
    signal.signal(signal.SIGTERM,handler);signal.signal(signal.SIGINT,handler)
    manifest=(a.run/'manifest.jsonl').open('a',buffering=1)
    def event(kind,**values):
        manifest.write(json.dumps(dict(event=kind,utc=utc(),**values))+'\n');manifest.flush();os.fsync(manifest.fileno())
    def update():
        status['elapsed_seconds']=min(a.seconds,time.monotonic()-start)
        status['remaining_seconds']=max(0.,deadline-time.monotonic())
        status['updated_utc']=utc();atomic(a.run/'status.json',status)
    def hourly():
        report=dict(observed_utc=utc(),status=status.copy(),supervisor_executing=True,
                    worker_executing=proc is not None and proc.poll() is None,
                    scope=config['scope'],note='Worker liveness checked by the supervisor; unfinished quadratures are not observables.')
        out=a.run.parent/'hourly-reports';out.mkdir(exist_ok=True)
        atomic(out/(dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'.json'),report)
    event('supervisor_started',budget=a.seconds);update();hourly();next_report=start+3600
    try:
        for index,item in enumerate(queue):
            if stop or time.monotonic()>=deadline:break
            for name,sha in hashes.items():
                if digest(SOURCE/name)!=sha:raise RuntimeError('source changed during campaign: '+name)
            case=a.run/'cases'/f'{index:04d}';case.mkdir(parents=True)
            atomic(case/'config.json',item)
            env=os.environ.copy();env.update(OPENBLAS_NUM_THREADS='2',OMP_NUM_THREADS='2',MKL_NUM_THREADS='2')
            log=(case/'stdout.log').open('w');err=(case/'stderr.log').open('w')
            proc=subprocess.Popen([sys.executable,str(SOURCE/'worker.py'),'--config',str(case/'config.json'),'--output',str(case)],stdout=log,stderr=err,env=env,start_new_session=True)
            status['active']=dict(case=index,pid=proc.pid,config=item);event('case_started',case=index,pid=proc.pid,config=item);update()
            while proc.poll() is None and not stop and time.monotonic()<deadline:
                update()
                if time.monotonic()>=next_report:hourly();next_report+=3600
                time.sleep(min(2.,max(0.,deadline-time.monotonic())))
            interrupted=proc.poll() is None
            if interrupted:
                os.killpg(proc.pid,signal.SIGKILL);proc.wait()
                state='timed_out' if time.monotonic()>=deadline else 'stopped'
                status['interrupted_cases'].append(dict(case=index,state=state))
            elif proc.returncode==0 and (case/'result.json').exists():
                state='completed';status['completed_cases'].append(index)
            else:
                state='failed';status['errors'].append(dict(case=index,returncode=proc.returncode))
            log.close();err.close();event('case_finished',case=index,state=state,returncode=proc.returncode)
            status['active']=None;update()
            if interrupted or state=='failed':break
        status['state']=('failed' if status['errors'] else 'stopped' if stop else
                         'budget_exhausted' if time.monotonic()>=deadline else 'queue_completed')
    except Exception as exc:
        status['errors'].append(dict(supervisor_exception=repr(exc)));status['state']='failed'
        if proc is not None and proc.poll() is None:
            os.killpg(proc.pid,signal.SIGKILL);proc.wait()
        event('supervisor_exception',error=repr(exc))
    finally:
        status['active']=None;update();hourly();event('supervisor_finished',status=status);manifest.close()


if __name__=='__main__':main()
