# AI, chiral gauge theories, and Craig's lattice measure

Conversation: [01a136ff-1cb1-7630-9ebf-a2cadf002050](https://chatgpt.com/local/01a136ff-1cb1-7630-9ebf-a2cadf002050), the exact link supplied by the user. External public access to that link has not been independently verified.

This notebook records the Craig-focused part of a discussion begun on 13 October 2026 about scientific questions suited to AI. It distinguishes the paper's claims, our reading of its supplied evidence, and computations actually performed in this cloud.

**Final status:** the independent 4D background-field campaign ran on 14 October from 02:28:55 to 07:28:55 UTC (04:28:55–09:28:55 Madrid), reaching its 18,000-second wall-time budget. **42 cases completed all grids through N=27; two cases were interrupted at the deadline.** Their completed N=3 and N=9 levels are retained separately from their incomplete N=27 momentum sums. The committed snapshot records the final execution state, `budget_exhausted`.

**Resumed inspection, 15 October:** the original calculation remains finished. The credit interruption occurred after the follow-up feasibility analyses were written, before any B0 pilot code or new experiment was saved or launched. Those analyses are now archived below as proposals, with no pilot timing or numerical result claimed.

**New B0 launch, 15 October:** after the user authorized the follow-up, the reconstruction, inherited-frame derivatives and full position-space first comparison were implemented and passed preflight checks. A separate bounded campaign started at **12:24:50 Madrid**, with a hard deadline of **17:24:50 Madrid**. See the [implementation, controls and limitations](notes/b0-experiment.md), [source](scripts/b0/) and [launch-time snapshot](results/b0-launch/). This launch statement is not a completed B0 result.

**Final B0 status:** the campaign stopped at **17:24:50 Madrid**, with **16 completed cases and one interrupted case**. Both matching nongauge curl tests completed; their endpoint discrepancy fell from **0.0556% to 0.0151%** on halving the outer step. The inherited-frame control changes the tested Bx coefficient by about **36%**. See the [final analysis and limitations](notes/b0-final-results.md) and [complete raw archive](results/b0-final/README.md). The interrupted finer source-step case is excluded from full-current comparisons.

## Contents

- [Conversation recap and corrections](notes/conversation.md)
- [Light composite fermions and the retained adjoint](notes/composite-fermions.md)
- [Review of the uploaded main source](notes/submission-main-review.md)
- [Review of the three supplementary documents](notes/submission-supplements-review.md)
- [Initial finite checks and their limits](notes/initial-checks.md), with [raw output](results/initial-checks/results.txt)
- [Five-hour campaign design](notes/campaign-design.md) and [supervisor operations](notes/runner-operations.md)
- [User-uploaded arXiv submission](references/arxiv-2610.09093v1/), [provenance](references/README.md), and [SHA-256 manifest](references/submission-manifest.json)
- [4D C source](scripts/physics4d.c), [finite-check C source](scripts/finite_checks.c), [bounded supervisor](scripts/runner.py), and [status reader](scripts/status.py)
- [Committed campaign snapshot](results/campaign-snapshot/README.md) and [numerical audit](notes/completed-results-audit.md)
- [Interpretation of the finished run and next-test priorities](notes/next-experiment-audit.md)
- [Proposed literal B0 reconstruction and resource assessment](notes/next-experiment-main.md), with [supplement-based algorithms and controls](notes/next-experiment-supplements.md)
- [Timestamped actual progress reports](results/hourly-reports/)
- [Measured cloud resource limits](results/cloud-resources.json)

## What the experiment measures

For homogeneous, noncommuting SU(5) connections on a **four-dimensional** unit torus, we sample links at N=3,9,27 and sum over all N^4 momenta. Fourier symmetry reduces each momentum to 20-dimensional anti5 and 40-dimensional 10 Wilson matrices; it does not remove spacetime dimensions.

We compute the chiral projector curvature `Omega(X,Y)=i Tr P[d_X P,d_Y P]` for the left-handed `10 + anti5` multiplet and its individual anomalous components. Complementary left/right bands give an equal-coupling vectorlike control. At the same momenta, a directly assembled massless overlap Dirac determinant is compared with recombined Weyl determinants including the eigenbasis phase. These share the Wilson eigensystem; the determinant assembly and LU routes are separate.

**This is not Craig's full measure evaluator.** We prescribe a smooth connection directly and keep fixed frames. We do not implement his original-link reconstruction, inherited-frame derivatives, infinite comparison current, locality bounds, or arbitrary global histories. The calculation also does not integrate a dynamical gauge-field ensemble. Success tests a cancellation mechanism and vectorlike recovery; it cannot certify the theorem or an interacting continuum theory.

The first pilot gave chiral curvature `1.41280466013e-5` at N=3 and `1.12647833579e-6` at N=9. The component responses are nonzero, so the chiral test is not merely a symmetry-forced zero. Vectorlike cancellation and the Dirac comparison are implementation controls, not evidence of a new theorem. Later results must be read from completed sums; partial momentum sums are not final observables.

## Reproduce or inspect

From this directory:

```sh
make
./build/finite_checks
./build/physics4d --seed 20261014 --nmax 9 --output pilot.json
```

The C programs need GCC and LAPACK/BLAS. The Makefile links versioned runtime libraries because the cloud lacks unversioned development symlinks. On another system, change `LDLIBS` if necessary. The 4D source is byte-identical to the launched worker; the exact run hashes are preserved in the result snapshot.

To inspect the original cloud job's final status, without starting another:

```sh
python3 /workspace/work/craig/campaign/status.py
```

From another checkout, the archived status reader accepts an explicit run directory:

```sh
python3 scripts/status.py --run /workspace/work/craig/campaign/run-5h-20261014T022855Z
```

Hourly progress checks were scheduled in the conversation for **05:37, 06:37, 07:37, 08:37 and 09:37 Europe/Madrid on 14 October**. The final check follows the hard deadline. Local hourly reports, when produced, go under `/workspace/work/craig/campaign/hourly-reports`; this Git snapshot does not automatically update itself.

## Source availability

The uploaded submission includes the main TeX, bibliography, styles, figures and three PDF supplements. It includes neither the Lean project nor numerical calculation source. Its ancillary README points to separate deposits, including the calculation DOI that returned an unregistered-identifier response. We have no evidence that this calculation deposit ever existed. No author implementation was run.

The paper's claimed advance is not refinement or decreasing residuals alone. It is the simultaneous construction of a gapped comparison, a summable local current with original-link derivative bounds, and full global phase consistency. The source reviews identify where each obligation is addressed and what remains unverified by this notebook.
