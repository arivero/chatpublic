# Campaign results snapshot

Observed: 2026-10-14T07:29:43.220437+00:00. State: **budget_exhausted**.

Execution counts: `{'completed': 42, 'timed_out': 2}`. Complete N=27 grids: **42**.
Elapsed: 5.000000 hours; remaining: 0.00 minutes.

Only complete momentum sums appear in [completed-levels.csv](completed-levels.csv). Final partial cases retain their execution classification and progress files. See [summary.json](summary.json), [manifest.jsonl](manifest.jsonl) and [run configuration/hashes](run.json).

| Statistic | Observed value |
|---|---|
| N=27 absolute chiral residual range | `[1.5240461042906031e-12, 7.857535635957602e-11]` |
| N=27 chiral/component magnitude ratio range | `[8.799206080868412e-10, 6.14469888875364e-05]` |
| Maximum absolute N=27 vectorlike residual | `2.391581644704756e-17` |
| Maximum per-block Dirac/Weyl log discrepancy | `3.552713678800501e-14` |
| Maximum per-block Dirac/Weyl phase discrepancy | `2.4158453015843406e-13` |
| Minimum sampled Wilson gap | `0.9988388067857921` |

These are floating-point observations on prescribed homogeneous fields. No general error enclosure, inherited-frame current, global measure proof, dynamical gauge ensemble or interacting continuum theory is established. The sums use long-double accumulators but the matrix algebra is double precision. The arithmetic-scale proxies omit eigensolver error and must not be treated as certificates.

Earlier hourly task prompts arrived while model usage was exhausted; those scheduled inspections were not executed. The supervisor continued logging and checkpointing. Actual later inspections have their own timestamps; no earlier report is backdated.
