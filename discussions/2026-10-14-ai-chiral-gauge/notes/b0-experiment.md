# Launched finite B0 experiment

**Final update:** this campaign ended at its deadline with 16 completed cases and
one interrupted case. See the [final results](b0-final-results.md) and
[raw archive](../results/b0-final/README.md). The launch details below are retained
as the original experiment specification.

The user authorized launching the follow-up on 15 October 2026. This is a new
experiment, separate from the completed homogeneous momentum campaign.

- Started: **2026-10-15 10:24:50 UTC / 12:24:50 Europe/Madrid**.
- Hard deadline: **15:24:50 UTC / 17:24:50 Europe/Madrid**, 18,000 wall seconds.
- Live directory: `/workspace/work/craig/b0-campaign/run-5h-20261015T102450Z`.
- Supervisor PID at launch: 1737. The first worker PID was 1740.
- Current pointer: `/workspace/work/craig/b0-campaign/active-run.json`.
- Read-only status: `python3 /workspace/work/craig/b0-pilot/status.py`.
- Hourly conversation checks: 13:30 through 17:30 Madrid, five occurrences.
  The supervisor also saves its own timestamped reports at launch, hourly,
  and on exit under `/workspace/work/craig/b0-campaign/hourly-reports`.

The [launch snapshot](../results/b0-launch/) is explicitly **not a final result**.
It records the queue, source hashes, preflight evidence, and runtime versions.
Future reports must inspect the live status and complete per-case results.

## What changed from the first campaign

We now implement the first finite comparison prescribed by the submitted main
source, rather than only the curvature of a supplied smooth background:

1. The original torus has one site in each of four directions, four generic
   noncommuting SU(5) links, and AP fermion signs in every direction. The seed is
   261009093; each original anti-Hermitian exponent has Frobenius norm 0.4.
2. We retain lifted lattice vertices as separate ambient components, even when
   they represent the same torus vertex. The Appendix A bump-convolution weights,
   all 24 coordinate-path orders, polar and determinant normalizations, rank-five
   spectral subspace, and determinant-synchronized safe frames are implemented.
3. Products of special-unitary polar factors of successive corrected-frame
   overlaps approximate transport for the prescribed traceless projected
   connection. This is a convergent path discretization, not an exact ODE solver;
   the queue increases the number of path subdivisions independently.
4. Each of the 81 centered children inherits the original parent's transported
   frame. Fine links include both inherited endpoint frames and the fine edge.
   Integer translations of the ambient components and AP fermion signs are
   handled separately. The first coarse endpoint is the actual original U.
5. Original-link source derivatives recompute the entire pipeline at positive and
   negative source steps. This includes the initial color frames, projection,
   connection, parent paths and fine edge. We use steps 0.01 and 0.005 initially;
   finer source steps are queued later. Representation tangents are then taken
   analytically from these fundamental-link tangents.
6. Full position-space Wilson matrices have dimensions **1620 for anti5** and
   **3240 for 10**. There is no momentum-block shortcut. The comparison is

   `H_s=(1-s)H_f+s[I H_c I†+gamma5(1-II†)]`, with `I psi=psi/9` on 81 children.

   Dense LAPACK eigensystems supply the positive projector. Its curvature with
   arguments `partial_s` and the original-link source is integrated over s to
   obtain a numerical B0 coefficient. NumPy/SciPy invoke compiled BLAS/LAPACK;
   two BLAS threads fit the measured two-core quota.

## Queue and checks

The first eight cases refine the path mesh and Gauss-Legendre quadrature:
`(mesh,nodes)=(2,4),(2,8),(2,16),(4,8),(4,16),(8,16),(8,32),(16,32)`.
Each eigensystem is reused for two source-step estimates, a second nongauge
source, a deliberately frozen-inherited-coordinate derivative, and a gauge
direction. Complete individual representation values are retained before their
chiral sum.

The frozen control holds the parent-transport coordinate matrices fixed in the
varying local canonical frames. It omits that inherited contribution; it does
not claim to hold changing ambient fibers fixed. Its numerical effect must be
compared with source and transport errors.

The worker separately evaluates endpoint gauge moments and endpoint curvature.
Its integrated gauge direction is checked against the coarse-minus-fine moment.
A whole-reconstruction global conjugation test precedes every case. On a
one-site original torus this is only a common original-site gauge transformation;
it cannot establish spatial locality or local covariance on a larger lattice.
The vectorlike control reverses the spectral-band blocks of the same matrices,
so its cancellation is an algebraic implementation control, not independent
physics evidence.

After the base cases, four displaced original-field fixtures at each of two
parameter steps are queued for a nongauge curl. A curl requires **all four cases
at matching settings**, plus comparison with the corresponding base endpoint
curvature difference. Later cases refine path mesh, quadrature and source step
again. These tasks may not all fit; the wall-time bound takes priority.

The supervisor kills an unfinished worker at the deadline, records an interrupted
case distinctly, and never promotes its partial quadrature or single completed
representation to a full chiral B0 value. Every completed quadrature node and each
geometry stage is saved. A failed implementation gate stops the campaign. There
is no automatic restart or extension; a completed queue may finish early.

## Preflight evidence and limits

The archived [preflight](../results/b0-launch/preflight.json) passed representation
tangent checks, Clifford algebra, a spectral-versus-direct-projector curvature
comparison, reconstructed-frame gauge covariance, nontrivial flat holonomy, and
the analytic periodic free comparison gap `sqrt(3)/2` at s=1/2. The flat holonomy
check is sensitive to inherited seam links, unlike an all-identity fixture.
A separate generic 3240-dimensional comparison benchmark took about 29 seconds;
its eigenpair residual was about 1.5e-14 and its sampled gap about 1.15.

Finite-difference, path-mesh and s-quadrature errors still require the queued
convergence comparisons. Observed spectral margins and residuals are floating
point diagnostics, not interval certificates. There is no supplied numerical
universal 4D admissibility threshold with which to certify the chosen field.
This tests **one finite first comparison**. It provides no infinite-refinement
tail bound, uniform locality proof, arbitrary global-loop test, gauge ensemble,
or interacting continuum limit, and cannot establish Craig's theorem.

## Reproduce

With Python, NumPy, SciPy and threadpoolctl installed, from `scripts/b0`:

```sh
OPENBLAS_NUM_THREADS=2 OMP_NUM_THREADS=2 python3 preflight.py
OPENBLAS_NUM_THREADS=2 OMP_NUM_THREADS=2 python3 supervise.py --run /absolute/path/to/new-b0-run --seconds 18000
```

The second command runs in the foreground; the live cloud launch used a detached
session with redirected logs. The run directory must not already exist. Source
hashes and the preflight record are captured by the supervisor. Do not run this
again merely to inspect the active campaign.
