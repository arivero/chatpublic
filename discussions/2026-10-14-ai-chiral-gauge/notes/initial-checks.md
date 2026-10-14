# Independent numerical checks of Craig 2610.09093v1

Run date: 13 October 2026. This is a new implementation from the equations,
not a run of the author's archived code. The primary deliverable is the
explanation in chat; this directory preserves the reproduction workspace.

Sources:

- https://arxiv.org/abs/2610.09093
- https://arxiv.org/html/2610.09093v1 (main paper Appendix B, equations 176–180)
- https://arxiv.org/src/2610.09093v1/anc/two-dimensional-supplement.pdf
  (S1.15, S2.1–S2.4, S3.4 and Appendix B.7)

## Run

Requires GCC and the LAPACK and BLAS runtime libraries. Tested with GCC
14.2.0 on the user's cloud environment. This links the versioned runtime
libraries because the unversioned development symlinks are absent here.

```sh
gcc -O3 -std=c11 -Wall -Wextra -Werror check.c -l:liblapack.so.3 -l:libblas.so.3 -lm -o check
./check > results.txt
```

The optional argument `2d` or `4d` runs just that part. No downloads,
Python packages, GPU, or author's code are required to execute check.c.
The source includes a deterministic random seed and exits nonzero if its
numerical calibration and acceptance checks fail. These tolerances are
diagnostic thresholds, not mathematically certified error bounds.

## 1. Four-dimensional comparison gap

The free Wilson kernel is H(p)=sum Gamma_mu sin(p_mu)+gamma5 M(p),
M=sum(1-cos(p_mu))-1. We construct the full 324 by 324 comparison matrix
at each coarse momentum, including the signed real inclusion amplitudes
w(k)=product[(1+2 cos(k_mu))/3] for all 81 fine momenta 3k=p modulo 2pi.

H_s=(1-s)H_f+s[I H_c I^dagger+gamma5(1-I I^dagger)].

We sample the 16 corners p_mu in {0,pi} at eleven interpolation values,
plus 256 seeded random points in momentum and interpolation parameter.
This is 432 matrices, not a certified search over the continuous domain.
Color is an identity factor in this free test and is suppressed.

An intentional omission of the rank-four coarse correction produces a
zero mode at p=0,s=1/2. The correct interpolation has a smallest sampled
gap of 0.5. This verifies a building block of the 4D construction, not
the interacting non-Abelian measure.

## 2. Direct current versus endpoint phases in two dimensions

The supplement uses the anomaly-free two-dimensional matter content
3 anti5 left + 10 right + 5 neutral right. This is DIFFERENT from the
four-dimensional 10+anti5 chiral matter content. We include the charged
sectors with their correct signs; neutral spectators have zero response
on these loops and a field-independent reference.

Take the original one-site torus with antiperiodic spin signs in both
directions and commuting SU(5) holonomies U1=exp(i a W), U2=exp(i b W),
W=diag(2,2,2,-3,-3). Use the closed loop
a=0.23+0.17 cos(t), b=0.37+0.17 sin(t), 0<=t<=2pi.
All spatial plaquettes equal the identity, so this is inside the
admissibility domain even for nontrivial holonomies.

Refine once to a centered 3 by 3 torus. In inherited parent frames the
internal links are 1 and the boundary links carry the original holonomies.
The inclusion is the constant spin-preserving copy with amplitude 1/3.
This follows from exact flat reconstruction (supplement S3.4); it is not
an approximation to the general nonflat reconstruction. AP signs are
applied once at each seam.

Compute B0 independently as the double integral of
i Tr P [partial_s P,partial_t P], P=(1+sign H_s)/2.
Projector derivatives are obtained from the exact divided differences of
the positive spectral projector. Gauss-Legendre quadrature integrates s;
a periodic trapezoid rule integrates t. Both coarse and fine link
derivatives are retained. The orientation is calibrated against the
supplement's Pauli example, which must give -1/2.

Separately diagonalize the coarse and fine Wilson matrices around the
loop. Products of normalized determinants det[V(t+dt)^dagger V(t)] give
the polygon approximation to their parallel-transport phases. This does
not use the current integrand or derive a phase from the current.
Compare the current to coarse phase minus fine phase, retaining the
nonzero terminal fine phase. The literal polygon errors converge as
O(dt^2). A Richardson estimate from the 256- and 512-step endpoint
calculations removes the leading error. Its reported discrepancy is an
observed extrapolation discrepancy, not a certified error bound.

Controls include omitting the incoming coarse derivative, checking the
flat Wilson spectrum against its analytic momenta, and comparing the
full comparison derivative to a centered finite difference.

## 3. Parameter-space Chern diagnostic

On a one-site torus let a,b independently cover [0,2pi]. For 32 by 32 and
64 by 64 parameter meshes and all four spin structures, the normalized
occupied-eigenvector overlap products give Chern numbers +30 for anti5
and -90 for the right-handed 10. Thus the physical combination 3*30-90
vanishes; an extra left anti5 leaves +30. This reproduces the supplement's
Appendix B.7 diagnostic. Random independent eigenvector phases check
invariance under occupied-frame choices.

These are parameter-space Chern numbers, not the spacetime overlap index.
Their integer proximity and mesh stability do not certify a continuum
discretization error or prove a global measure exists. In particular,
zero Chern number alone would not establish trivial holonomy.

## Scope

These tests probe a 4D free comparison and a 2D commuting flat-holonomy
family. They do not test the nonlinear reconstructed connection on
noncommuting curved gauge fields, all original-link derivatives, uniform
locality, the infinite refinement tail, or arbitrary global histories.
The finite transgression identity is geometric and also holds for
anomalous matter; its passing alone does not establish anomaly cancellation.
The Chern control is a separate, anomaly-sensitive diagnostic.

We do not claim to verify the full theorem, the Lean formalization, a
continuum interacting theory, reflection positivity, practical Standard
Model simulation, or agreement with experimental data. The paper itself
describes its formulation as one of principle and leaves important
continuum and practical questions open.
