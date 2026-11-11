#!/usr/bin/env python3
"""Read a campaign and archive completed observations; never launch/alter jobs."""
import argparse
import csv
import datetime as dt
import json
from pathlib import Path
import shutil

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--run',type=Path,required=True)
p.add_argument('--output',type=Path,required=True)
a=p.parse_args()
a.output.mkdir(parents=True,exist_ok=True)
status=json.loads((a.run/'status.json').read_text())
events=[json.loads(x) for x in (a.run/'manifest.jsonl').read_text().splitlines() if x.strip()]
finished={x['case_id']:x for x in events if x['event']=='case_finished'}
for name in ['run.json','status.json','manifest.jsonl']:
    shutil.copy2(a.run/name,a.output/name)
rows=[]
incomplete=[]
for case in sorted((a.run/'cases').iterdir()):
    dest=a.output/'cases'/case.name
    dest.mkdir(parents=True,exist_ok=True)
    for name in ['result.json','result.json.progress.json','stdout.log','stderr.log']:
        src=case/name
        if src.exists():shutil.copy2(src,dest/name)
    source=case/'result.json'
    if not source.exists():source=case/'result.json.progress.json'
    if not source.exists():continue
    data=json.loads(source.read_text())
    execution=finished.get(int(case.name),{}).get('state','active_or_unknown')
    for r in data['levels']:
        if not r['complete']:
            incomplete.append({'case':case.name,'execution_state':execution,'N':r['N'],'momenta_done':r['momenta_done'],'momenta_total':r['momenta_total']})
            continue
        scale=max(abs(r['omega_anti5_left']),abs(r['omega_10_left']))
        rows.append({'case':case.name,'seed':data['seed'],'execution_state':execution,'N':r['N'],
            'omega_anti5_left':r['omega_anti5_left'],'omega_10_left':r['omega_10_left'],
            'omega_chiral_sum':r['omega_chiral_sum'],'omega_vectorlike_sum':r['omega_vectorlike_sum'],
            'cancellation_ratio':abs(r['omega_chiral_sum'])/scale if scale else None,
            'minimum_gap':min(r['min_wilson_gap']),
            'dirac_weyl_log_error':r['max_point_dirac_weyl_logabs_error'],
            'dirac_weyl_phase_error':r['max_point_dirac_weyl_phase_error'],
            'arithmetic_scale_proxy_not_bound':sum(r['arithmetic_scale_proxy_not_error_bound'])})
with (a.output/'completed-levels.csv').open('w',newline='') as f:
    if rows:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
fine=[r for r in rows if r['N']==27]
def bounds(key,absolute=False):
    values=[abs(r[key]) if absolute else r[key] for r in fine if r[key] is not None]
    return [min(values),max(values)] if values else None
summary={'observed_utc':dt.datetime.now(dt.timezone.utc).isoformat(),'run_state':status['state'],
    'elapsed_seconds':status['elapsed_seconds'],'remaining_seconds':status['remaining_seconds'],
    'case_counts':status['counts'],'completed_N27_grids':len(fine),'complete_level_rows':len(rows),
    'N27_abs_chiral_range':bounds('omega_chiral_sum',True),
    'N27_cancellation_ratio_range':bounds('cancellation_ratio'),
    'N27_max_abs_vectorlike':max((abs(r['omega_vectorlike_sum']) for r in fine),default=None),
    'max_dirac_weyl_log_error':max((r['dirac_weyl_log_error'] for r in rows),default=None),
    'max_dirac_weyl_phase_error':max((r['dirac_weyl_phase_error'] for r in rows),default=None),
    'minimum_sampled_gap':min((r['minimum_gap'] for r in rows),default=None),
    'incomplete_levels':incomplete,
    'scope':'Fixed-frame homogeneous 4D backgrounds, not Craig full current or theorem; arithmetic proxies are not error bounds.'}
(a.output/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
(a.output/'status-report.txt').write_text(json.dumps(summary,indent=2)+'\n')
(a.output/'snapshot.json').write_text(json.dumps({'snapshot_utc':summary['observed_utc'],'live_run_path':str(a.run),'deadline_utc':'2026-10-14T07:28:55Z','snapshot_is_final':status['state']=='budget_exhausted','interpretation':summary['scope']},indent=2)+'\n')
lines=['# Campaign results snapshot','',f"Observed: {summary['observed_utc']}. State: **{status['state']}**.",'',
    f"Execution counts: `{status['counts']}`. Complete N=27 grids: **{len(fine)}**.",
    f"Elapsed: {status['elapsed_seconds']/3600:.6f} hours; remaining: {status['remaining_seconds']/60:.2f} minutes.",'',
    'Only complete momentum sums appear in [completed-levels.csv](completed-levels.csv). Final partial cases retain their execution classification and progress files. See [summary.json](summary.json), [manifest.jsonl](manifest.jsonl) and [run configuration/hashes](run.json).','',
    '| Statistic | Observed value |','|---|---|',
    f"| N=27 absolute chiral residual range | `{summary['N27_abs_chiral_range']}` |",
    f"| N=27 chiral/component magnitude ratio range | `{summary['N27_cancellation_ratio_range']}` |",
    f"| Maximum absolute N=27 vectorlike residual | `{summary['N27_max_abs_vectorlike']}` |",
    f"| Maximum per-block Dirac/Weyl log discrepancy | `{summary['max_dirac_weyl_log_error']}` |",
    f"| Maximum per-block Dirac/Weyl phase discrepancy | `{summary['max_dirac_weyl_phase_error']}` |",
    f"| Minimum sampled Wilson gap | `{summary['minimum_sampled_gap']}` |",'',
    'These are floating-point observations on prescribed homogeneous fields. No general error enclosure, inherited-frame current, global measure proof, dynamical gauge ensemble or interacting continuum theory is established. The sums use long-double accumulators but the matrix algebra is double precision. The arithmetic-scale proxies omit eigensolver error and must not be treated as certificates.','',
    'Earlier hourly task prompts arrived while model usage was exhausted; those scheduled inspections were not executed. The supervisor continued logging and checkpointing. Actual later inspections have their own timestamps; no earlier report is backdated.','']
(a.output/'README.md').write_text('\n'.join(lines))
print(json.dumps(summary,indent=2))
