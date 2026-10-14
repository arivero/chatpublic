#!/usr/bin/env python3
"""Read-only status/report for the bounded 4D campaign. No jobs are launched."""
import argparse
import csv
import datetime as dt
import json
from pathlib import Path
from zoneinfo import ZoneInfo

base = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--run', type=Path)
parser.add_argument('--csv', type=Path, help='export complete momentum sums only')
args = parser.parse_args()
run = args.run or Path(json.loads((base / 'active-run.json').read_text())['directory'])
status = json.loads((run / 'status.json').read_text())
print('Run:', run)
print('State:', status['state'], '| supervisor PID:', status['supervisor_pid'])
print('Elapsed: %.1f min | remaining: %.1f min' % (status['elapsed_seconds']/60, status['remaining_seconds']/60))
print('Case execution counts:', status['counts'])
stamp = dt.datetime.fromisoformat(status['updated_utc'])
print('Status updated:', stamp.astimezone(ZoneInfo('Europe/Madrid')).isoformat())
rows = []
for case in sorted((run/'cases').iterdir()):
    result = case/'result.json'
    progress = case/'result.json.progress.json'
    source = result if result.exists() else progress
    if not source.exists():
        print('Case', case.name, ': initializing or failed; see stderr.log')
        continue
    data = json.loads(source.read_text())
    print('Case', case.name, '| seed', data['seed'], '| execution result:', 'written' if result.exists() else 'not yet written')
    for row in data['levels']:
        if not row['complete']:
            print('  N=%d: %d/%d momentum blocks; partial sums are not reported as observables' % (row['N'],row['momenta_done'],row['momenta_total']))
            continue
        left5, left10 = row['omega_anti5_left'], row['omega_10_left']
        scale = max(abs(left5),abs(left10))
        ratio = abs(row['omega_chiral_sum'])/scale if scale else None
        print('  N=%d: chiral=%+.9e; anti5=%+.9e; 10=%+.9e; vectorlike=%+.2e' % (row['N'],row['omega_chiral_sum'],left5,left10,row['omega_vectorlike_sum']))
        print('        cancellation ratio=%s; max Dirac/Weyl log discrepancy=%.2e; gaps=%s' % ('%.4g'%ratio if ratio is not None else 'undefined',row['max_point_dirac_weyl_logabs_error'],row['min_wilson_gap']))
        rows.append({'case':case.name,'seed':data['seed'],'N':row['N'],
                     'omega_anti5_left':left5,'omega_10_left':left10,
                     'omega_chiral_sum':row['omega_chiral_sum'],
                     'omega_vectorlike_sum':row['omega_vectorlike_sum'],
                     'chiral_to_component_ratio':ratio,
                     'dirac_weyl_max_log_error':row['max_point_dirac_weyl_logabs_error'],
                     'dirac_weyl_max_phase_error':row['max_point_dirac_weyl_phase_error']})
if args.csv and rows:
    with args.csv.open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
print('Scientific scope: homogeneous noncommuting 4D backgrounds; fixed frames; no full Craig measure, Monte Carlo gauge ensemble, or theorem certificate.')
