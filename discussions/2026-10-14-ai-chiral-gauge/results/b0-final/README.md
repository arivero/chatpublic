# Final B0 campaign archive

The campaign ended at its five-hour wall-time limit on **15 October 2026 at
15:24:50 UTC / 17:24:50 Europe/Madrid**. It completed **16 cases**, or 32
representation quadratures, containing **520 integration nodes**. Case **0016**
was interrupted at the deadline with 40/64 nodes saved and an incomplete 10
representation. Its partial data are retained under `cases/0016`, but excluded
from the completed-case CSV and all complete chiral-current comparisons.

- [Final analysis](../../notes/b0-final-results.md)
- [Machine-readable final report](summary.json)
- [Completed-case table](completed-cases.csv)
- [Execution status](status.json), [event manifest](manifest.jsonl), and
  [configuration/source hashes](run.json)
- [Archive provenance](snapshot.json) and [copied-file checksums](SHA256SUMS)
- [Cases, raw nodes and reconstructed fields](cases/)
- [Actual timestamped reports](hourly-reports/)

Each case retains its original configuration, result/progress JSON, node JSON,
stdout/stderr, and `fields.npz` where present. The NPZ contains the original and
fine links, inherited coordinates and derivative inputs, not a completed result
by itself. Files were copied without changing the live campaign and verified by
SHA-256. Completed weighted integrals were independently re-summed with
`math.fsum` as an archival consistency check; this is not a numerical error bound.

The original [launch snapshot](../b0-launch/) remains a historical snapshot.
These results concern one finite first comparison, approximate transport and
source derivatives, and a one-site original 4D torus. They do not establish an
infinite current, spatial locality, general admissibility, or Craig's theorem.
