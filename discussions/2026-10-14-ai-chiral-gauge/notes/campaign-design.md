# Five-hour 4D chiral-curvature campaign

Launched 14 October 2026 at 02:28:55 UTC / 04:28:55 Europe/Madrid.
The hard deadline is five wall-clock hours later. Two single-threaded C
workers run concurrently; no interactive model turns are needed while they run.

## Read the running results

```sh
python3 /workspace/work/craig/campaign/status.py
```

`active-run.json` points to the current run. `status.json` records the
supervisor PID, remaining budget, active cases, and completed/failed counts.
Each case has `stdout.log`, `stderr.log`, atomic JSON progress, and binary
checkpoints. Complete execution writes `result.json`. The last interrupted
cases are explicitly marked timed_out when the budget expires. A completed
level is usable even when its containing case is interrupted at a later level.
Partial momentum sums must not be interpreted as full observables.

Source: `physics4d.c`. Compiler: GCC 14.2; C11 with warnings treated as errors.
Linear algebra: the system LAPACK/BLAS runtime libraries. Exact source,
executable and supervisor hashes/copies are recorded by the runner. The
background job has no network dependency and needs no downloaded author code.

## What is being calculated

This is a **four-dimensional fixed-background fermion calculation**, not a
Monte Carlo simulation of the gauge-field probability measure. Each seeded
case generates four noncommuting Hermitian traceless 5 by 5 matrices K_mu,
each with Frobenius norm 1.25. The smooth SU(5) connection is A_mu=i K_mu
on a unit four-torus. With h=1/N, the links are U_mu=exp(i K_mu/N).
Independent tangent matrices X and Y vary directions 0 and 1. The matrices
are generic in su(5), not restricted to an SU(2) subgroup. All four fermion
boundary conditions are antiperiodic to avoid free zero-momentum modes.

The three grids are N=3,9,27: 81, 6561 and 531441 momentum points. Every
momentum block is evaluated, with **no stochastic trace estimator**. A
homogeneous background permits Fourier reduction of the enormous position
space operator into 20 by 20 (anti5) and 40 by 40 (10) matrices. Space still
has four dimensions: all four momentum sums and all four gauge links enter.

For each representation the Hermitian Wilson kernel has mass shift -1.
We diagonalize it and compute the positive chiral projector P=(1+sign H)/2.
The exact Fréchet derivative of each link exponential supplies the source;
spectral divided differences supply the projector derivatives. The primary
observable is the full fixed-volume trace

    Omega_h(X,Y) = i Tr P [d_X P, d_Y P].

No 1/N^4 factor divides this trace. The factors h from sampling the fixed
connection already enter the link derivatives. Curvatures are evaluated for:

1. left-handed anti5 and left-handed 10 separately (anomalous controls);
2. their sum (the anomaly-free 4D chiral SU(5) multiplet);
3. equal-coupling left/right sectors in each representation (vectorlike).

The negative-band curvature is computed independently from its own spectral
sum, not set to minus the positive-band answer. Floating-point sums across
momenta use long double accumulators. The reported arithmetic-scale proxy
is based on absolute summands; it is **not** an eigensolver/quadrature error
certificate. Background plaquette Frobenius deviations and smallest observed
Wilson eigenvalues are logged.

## Matched Dirac calculation

At each of the same momenta and in the same representations, independently
assemble the massless overlap Dirac matrix

    D = 1 + gamma5 sign(H)

and calculate its determinant by LU. Separately construct the two Weyl
blocks, M_L=2 V_(gamma5+,H+) and M_R=2 V_(gamma5-,H-), and calculate their
determinants. Recombine with the full eigenbasis determinant phase:

    det D = det M_L det M_R conjugate(det V).

The eigencolumn permutation sign is +1 for the dimensions used here.
Omitting the eigenbasis phase would give an invalid comparison. The two
assemblies share H and its eigensystem, so this is an independent determinant
assembly/LU control, not an independent end-to-end fermion solver.

We record per-momentum magnitude/phase discrepancies, total log magnitudes,
and differences relative to the analytic zero-background Dirac determinant.
The latter are regulator-dependent fermionic background responses; they are
not claimed to be continuum-renormalized observables. No fermion mass is
introduced: multiplying two massive Weyl determinants would be incorrect
because a Dirac mass mixes the sectors.

## Calibration and preliminary results

Before running a case, the program checks the Clifford algebra, the link
exponential derivative against finite differences, constant SU(5) gauge
covariance of the curvature, and the Dirac/Weyl reconstruction. An independent
code review checked the kernel signs, representations, trace normalization,
and determinant basis phases. The supervisor passed bounded tests of its
deadline, child cleanup, resumability, code-hash checking and error handling.

Pilot seed 20261014:

| N | anti5 curvature | 10 curvature | chiral sum |
|---|---:|---:|---:|
| 3 | -7.75708252290e-6 | +2.18851291242e-5 | +1.41280466013e-5 |
| 9 | -1.79417115774e-4 | +1.80543594110e-4 | +1.12647833579e-6 |

The paired vectorlike sum is below 8e-18 in the pilot, and the maximum
Dirac/Weyl log-determinant discrepancy is below 3e-14. This is calibration
evidence, not the five-hour result. The long run samples additional seeded
connections and reaches N=27, which is needed to assess further refinement.

## Relation to Craig's paper — and limits

Craig's theorem requires more than anomaly cancellation or a decreasing
number. It proposes a particular original-link current built from comparisons
between successive refinements of a reconstructed smooth connection, using
inherited, field-dependent frames. Uniform locality and derivative bounds,
summability, Ward identities and all-loop phase integrability are essential.

Our connection is prescribed directly and uses a fixed global frame. It is
**not** the paper's literal original-link reconstruction F_h[U], and its
derivatives do not include that reconstruction's inherited-frame variations.
Field-dependent frame changes add Berry connection terms. Thus this campaign
probes the smooth-background cancellation mechanism; it is not a computation
of Craig's B_n or a numerical verification of his full measure.

The relevant expected O(h^2) curvature suppression is an upper-bound
mechanism, not a mandated fitted exponent for every selected source. Signs
may change, leading coefficients may vanish, coarse grids may not be
asymptotic, and observed plateaux may reflect arithmetic limitations. Failures
require checking these conditions before interpreting them as a counterexample.

No universal admissibility membership is asserted for the coarse random
fields. Their plaquette deviations are measured; their sampled Wilson gaps
are measured, not proved over all fields or histories. The infinite current,
locality of all original-link derivatives, volume-uniform bounds, global
holonomy and interacting continuum limit are outside this experiment.

Author sources:

- https://arxiv.org/abs/2610.09093
- https://arxiv.org/html/2610.09093v1
- https://arxiv.org/src/2610.09093v1/anc/two-dimensional-supplement.pdf

The arXiv ancillary README identifies the numerical archive as
`calculation_archive_2026_10_05.tar.gz` at
https://doi.org/10.5281/zenodo.23196101 . The Zenodo API returned 404 with
“The persistent identifier is not registered”; the direct archive URL also
returned 404. This is an unregistered identifier, not evidence of an access
restriction. We have no evidence that this archive ever existed; the user
also reports that it never existed. The saved `.tar.gz` in the neighboring
archive research folder is that error response, not usable source. No
verified GitHub mirror has been found; GitHub connector searches in this
session timed out. Do not describe this campaign as reproduction of an
author-provided implementation.

## Checkpoints and stopping

The source's checkpoint is tied to version, seed and maximum grid. To resume
one interrupted case manually, repeat its exact command and output path with
the unchanged executable; it reloads its binary checkpoint. Do not run two
processes on the same case path. Resuming individual cases is separate from
resuming the overall bounded supervisor. See RUNNER.md for that procedure;
the supervisor never silently extends the original time budget.

To stop before the deadline, send SIGTERM to the supervisor PID recorded in
the run status. It cleans up its workers and preserves checkpoints. No
automatic scientific conclusion or message is sent when the job ends.
