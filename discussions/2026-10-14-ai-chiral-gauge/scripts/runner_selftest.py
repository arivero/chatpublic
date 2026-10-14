#!/usr/bin/env python3
"""Bounded supervisor safety checks; no physics claims."""
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import time

HERE = Path(__file__).resolve().parent
BASE = Path(tempfile.mkdtemp(prefix='runner-selftest-', dir=HERE))
WORKER = BASE / 'fake_worker.py'
WORKER.write_text('''import argparse,json,time,os
p=argparse.ArgumentParser();p.add_argument('--seed',type=int);p.add_argument('--output');p.add_argument('--delay',type=float,default=.3);a=p.parse_args()
time.sleep(a.delay)
with open(a.output,'w') as f:json.dump({'seed':a.seed,'OMP_NUM_THREADS':os.environ.get('OMP_NUM_THREADS')},f)
''')
RUNNER = HERE / 'runner.py'

def command(name, budget, delay=.3, resume=False):
    return [sys.executable,str(RUNNER),'--seconds',str(budget),'--workers','2','--output',str(BASE/name)] + (['--resume'] if resume else []) + ['--worker',sys.executable,str(WORKER),'--delay',str(delay)]

def state(name):
    return json.loads((BASE/name/'status.json').read_text())

p=subprocess.run(command('deadline',1.3),capture_output=True,text=True,timeout=5)
assert p.returncode == 0, p.stderr
s=state('deadline')
assert s['state']=='budget_exhausted' and s['counts']['completed']>=2 and s['counts']['timed_out']==2,s
for f in (BASE/'deadline'/'cases').glob('*/result.json'):
    assert json.loads(f.read_text())['OMP_NUM_THREADS']=='1'
p=subprocess.Popen(command('resume',3),stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
while not (BASE/'resume'/'status.json').exists():
    time.sleep(.02)
time.sleep(.4)
p.send_signal(signal.SIGTERM)
out,err=p.communicate(timeout=5)
assert p.returncode==130,(out,err)
first=state('resume')
assert first['state']=='interrupted',first
p=subprocess.run(command('resume',3,resume=True),capture_output=True,text=True,timeout=6)
assert p.returncode==0,p.stderr
s=state('resume')
assert s['state']=='budget_exhausted' and s['total_budget_seconds']==3 and s['remaining_seconds']==0,s
p=subprocess.run(command('resume',4,resume=True),capture_output=True,text=True,timeout=3)
assert p.returncode!=0 and 'no silent budget extension' in p.stderr,p.stderr
WORKER.write_text(WORKER.read_text()+'\n# altered hash\n')
p=subprocess.run(command('resume',3,resume=True),capture_output=True,text=True,timeout=3)
assert p.returncode!=0 and 'exact code hashes changed' in p.stderr,p.stderr
NAN_WORKER=BASE/'nonfinite_worker.py'
NAN_WORKER.write_text("import argparse\np=argparse.ArgumentParser();p.add_argument('--seed');p.add_argument('--output');a=p.parse_args()\nopen(a.output,'w').write('{\"value\":NaN}')\n")
p=subprocess.run([sys.executable,str(RUNNER),'--seconds','3','--workers','1','--output',str(BASE/'nonfinite'),'--worker',sys.executable,str(NAN_WORKER)],capture_output=True,text=True,timeout=5)
assert p.returncode==1,p.stderr
assert state('nonfinite')['counts']['invalid_result']==3,state('nonfinite')
print(json.dumps({'selftest':'passed','directory':str(BASE),'checks':['parallel completion','hard deadline/partial case state','BLAS thread limit','signal cleanup','remaining-budget resume','extension rejection','changed-code rejection','nonfinite JSON rejection/error circuit breaker']},indent=2))
