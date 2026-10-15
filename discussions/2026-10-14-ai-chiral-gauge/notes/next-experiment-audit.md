# Audit after the five-hour 4D campaign

## What was actually computed

The supervisor finished its 18,000-second wall-clock budget with 42 complete seeds and two interrupted seeds. Each complete seed evaluated all 81, 6,561, and 531,441 momenta on N=3,9,27. The complete cases therefore contain 22,599,486 momentum points, each with separate anti5 and 10 kernels. Partial final-level momentum sums are not observables.

`physics4d.c` samples homogeneous links U_mu=exp(i K_mu/N), with generic noncommuting Hermitian traceless K_mu of Frobenius norm1.25. It evaluates ordinary positive-band overlap-projector curvature on constant continuum tangents X_0,Y_1. It does not construct Craig's original-link measure current B_n or perform a gauge-field Monte Carlo simulation.

The reported complete-case residuals decrease from N3 to9 and from9 to27. At N27 the physical sum lies in absolute magnitude between1.52e-12 and7.86e-11 while individual anomalous-representation responses can remain of order1e-3. This is real numerical evidence that the implemented chiral representation sum cancels a leading response. It is not direct evidence about the missing comparison current.

The checks are appropriate but have specific limits:

* Opposite spectral-band curvatures sum to zero identically for any complementary projectors. Their separate numerical sums are useful implementation controls, not an independent prediction of Craig's construction.
* Weyl recombination and full massless Dirac LU share H and its eigensystem. The determinant basis phase is included correctly. This is an independent assembly/linear-algebra check rather than an independent fermion solver.
* The gauge-covariance calibration uses a constant global SU(5) conjugation. It does not evaluate a local gauge transformation or the Ward identity.
* The arithmetic proxy omits eigensolver and derivative errors and is not a certified uncertainty. The smallest residuals need additional precision or an independently justified error budget before an asymptotic exponent is assigned.

## Why the decrease can be much faster than h²

The N9→27 ratios lie roughly between6.7e-7 and1.9e-5. Three levels do not identify a unique physical mechanism for this suppression.

First, h² in the main refinement theorem is an upper bound in a uniform norm that includes arbitrary original-link derivatives and inherited frames. Our selected observable uses smooth, fixed-frame continuum tangents. Main Appendix F, source lines7160–7246, separately claims O(a^6) for the exact measure response on smooth classical background families, preserving fixed background-parameter derivatives. Combined with the claimed curvature identity, this permits substantially stronger suppression for ordinary smooth-background curvature. This is a prediction conditional on that analytic argument, not an independent proof furnished by the present calculation.

Second, homogeneous backgrounds make the calculation a complete sum of analytic momentum-block functions. Finite-grid sums of such functions can contain very small winding/alias terms. The code changes both h=1/N and the momentum-grid count N together, so it does not separate local cutoff powers from finite-volume/momentum-sampling effects. Special source and translation symmetries can also remove leading terms.

A low-cost diagnostic, if desired, is to hold h fixed and separately vary the momentum-grid count M and boundary twist. Compare normalized Brillouin-zone means M^-4 sum f_h(p), multiplying by the original fixed N^4 only after that comparison. This distinguishes grid aliases from a persistent bulk contribution. It changes the physical torus if interpreted as a lattice system, so it must be explicitly labeled a momentum-integration diagnostic. It is more informative than dozens of additional random seeds, but remains auxiliary to the real missing test.

## Highest-value next experiment

Implement one **literal nonflat finite comparison B0** from Craig's prescription, with a genuinely original-link variation and all induced geometric derivatives. Required operations are:

1. Build the specified smooth weights and polar-normalized short transports.
2. Form the geometric matrix K, select its five-dimensional spectral cluster, construct the safe local frames, synchronize determinant phases, and use the traceless projected connection.
3. Integrate its spatial transports and inherit frames from each parent to its children. Differentiate the initial frames, connection, and all inherited transports when an original link changes.
4. Retain U itself as the coarse endpoint. Form H_s from that endpoint and the reconstructed fine sample with the specified constant-copy embedding.
5. Calculate B0 directly from projector derivatives and quadrature. Check its Ward response against separately computed endpoint moments, retaining the fine terminal moment. Add a direct nongauge response or curl comparison and a short full-phase loop if resources permit.

Controls should deliberately freeze inherited-frame derivatives, omit a parent contribution, and replace the correct first coarse endpoint by the reconstructed spacing-one sample. A control only counts if it changes a well-resolved nonzero observable. Ward/curl/loop identities alone cannot uniquely identify the prescribed current: an exact gauge-invariant one-form can preserve them, so direct nongauge evaluation and faithful reconstruction remain necessary.

## Realistic five-to-six-hour scope

The present Fourier shortcut does not survive a generic literal reconstructed nonflat field. A single original site refined isotropically to3^4 sites gives fine Hermitian Wilson matrices of size1620 for anti5 and3240 for10. The geometric ambient matrix can have up to256 active vertices times five colors at a generic point, although selected paths have smaller supports. Repeated dense diagonalizations, transport quadrature, and derivative validation are a different workload from the completed20/40-dimensional momentum blocks.

Consequently implementation and calibration must precede a new promised compute budget. Benchmark the literal kernel and select a finite set of sources/quadratures that fit. A two-dimensional nonflat prototype reduces the first fine matrices to90/180 and is a sensible geometry validation stage, but it must not be presented as the requested four-dimensional result. A reduced or perturbative 4D test can be valuable if its exact restrictions and equivalence to the prescribed operations are derived explicitly.

A successful next finite experiment would establish that the missing reconstruction/current machinery works on its tested field and variations. It would still leave infinite refinement, uniform locality, all derivatives, and arbitrary global histories outside the numerical conclusion.
