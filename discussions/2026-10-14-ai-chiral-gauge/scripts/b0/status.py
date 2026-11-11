"""Read-only B0 campaign status. Partial quadratures are never observables."""
import json
from pathlib import Path

base=Path('/workspace/work/craig/b0-campaign')
active=json.loads((base/'active-run.json').read_text());run=Path(active['directory'])
status=json.loads((run/'status.json').read_text())
print(json.dumps(dict(run=str(run),status=status),indent=2))
for case in sorted((run/'cases').glob('*')):
    if (case/'result.json').exists():
        r=json.loads((case/'result.json').read_text())
        print(json.dumps(dict(case=case.name,complete=True,config=r['config'],
                              chiral_integrals=r['chiral_integrals'],
                              vectorlike_integrals=r['vectorlike_integrals'],
                              ward_residual=r['chiral_gauge_ward_residual'])))
    elif (case/'progress.json').exists():
        r=json.loads((case/'progress.json').read_text())
        print(json.dumps(dict(case=case.name,complete=False,stage=r['stage'],
                              geometry_evaluations=len(r['geometry']),
                              completed_nodes=len(r['nodes']),note='Partial quadrature is not a complete current.')))
