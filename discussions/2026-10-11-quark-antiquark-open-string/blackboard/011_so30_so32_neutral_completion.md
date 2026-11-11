# What selects SO(32) rather than SO(30)?

14 October 2026. The user supplied Alejandro Rivero, *An interpretation of scalars in SO(32)*, Eur. Phys. J. C **84**, 1058 (2024), [DOI](https://doi.org/10.1140/epjc/s10052-024-13368-3), and asked what is lacking to obtain exactly SO(32). [Preserved original](../references/received-2026-10-14/s10052-024-13368-3.pdf); [native extracted text](../references/received-2026-10-14/s10052-024-13368-3.txt). The parent read the representation/construction sections and discussion; equations and consequential passages on PDF pages 1, 3 and 7 were checked against page images. The mass-formula fits were not independently reviewed.

## Source correction and scope

The previous comparison overidentified the sBootstrap composites with ordinary QCD mesons and diquarks. Section 8, PDF page 7, explicitly says the proposed composite scalars should **not** be those found at the QCD scale and suggests a different, high-energy binding mechanism. Section 5 also says ordinary QCD binding does not apply. The common constituent labels and analogous multiplet counts do not make the physical bound states identical. This places the 2024 proposal closer to the new strong dynamics of the 2025/2026 partial-compositeness papers, while retaining a distinctive requirement: a subset of observed SM fermions supplies the constituents of scalar partners.

Section 3 derives five participating quark flavors from its scalar-counting postulates. Section 3.2 explicitly identifies SU(15) as the minimal color–flavor candidate and says one can pass through SO(30) to SO(32) by adding singlets. Section 7.1 also notes that SO(30) suffices for similar decompositions. The original particle-counting argument therefore does not by itself uniquely select SO(32).

## Minimal algebraic completion

Let V=(5,3) under SU(5)_f × SU(3)_c. Its complex dimension is 15. Its underlying real representation has dimension 30, with complexification V ⊕ V*. Consequently the natural orthogonal group for these internal labels is SO(30).

To reach SO(32) minimally, add **one complex internal singlet**, or equivalently two real singlet directions:

\[
16=(5,3)\oplus(1,1),\qquad
32_{\mathbb C}=(5,3)\oplus(\bar5,\bar3)\oplus1\oplus1.
\]

The notation counts internal representation labels, not spinor components or physical on-shell particle degrees of freedom. A sterile-neutrino-like constituent N and its conjugate are a possible physical interpretation, provided the two internal directions and their symmetries actually exist. This interpretation is a **guess**, not a deduction from a dimensional equality.

In particular, the fifteen labels here are the five quark flavors times three colors. They are not the fifteen Weyl fermions of one SM generation. The familiar “add a right-handed neutrino to complete sixteen” argument for a different family embedding cannot simply be transferred. Nor does restoring the excluded colored top do the job: six quark flavors times three colors give 18 complex labels and naturally SO(36), not SO(32).

The adjoint completion is larger than adding two isolated scalar states. From the exterior square,

\[
\Lambda^2(\mathbb R^{30}\oplus\mathbb R^2)
=\Lambda^2\mathbb R^{30}\oplus(\mathbb R^{30}\otimes\mathbb R^2)
\oplus\Lambda^2\mathbb R^2,
\]

so

\[
496=(435,1)\oplus(30,2)\oplus(1,1)
\quad\text{under }SO(30)\times SO(2).
\]

The 61 additional adjoint components are two real SO(30) vectors plus one generator. Complexifying and restricting to color–flavor gives

\[
496=435\oplus2(5,3)\oplus2(\bar5,\bar3)\oplus(1,1).
\]

These are exactly the mixed terms and one extra singlet visible in the paper's Eq. (1). A physical extension must account for the mixed colored composites, as well as for the added neutral endpoint. If that endpoint is electrically neutral under the chosen charge embedding, its mixed channels carry the quark-like charges of V and V*; neutrality is an assignment to specify, not a consequence of being an SU(5)_f × SU(3)_c singlet alone.

The already-selected sfermion-like channels occur within SO(30):

\[
435=224\oplus105\oplus\overline{105}\oplus1,
\]
\[
224=(24,1)\oplus(1,8)\oplus(24,8),\quad
105=(15,\bar3)\oplus(10,6).
\]

Their presence therefore cannot distinguish 30 from 32. All these equations are dimensionless representation identities; they use no convention setting physical hbar to one.

## Why U(3) alone does not select 32

The paper suggests enlarging color from SU(3) to U(3). This may be part of a physical completion, but the enlargement alone is not a dimension-selection argument. The action

\[
(A,B)\longmapsto A\otimes B,
\quad A\in SU(5),\ B\in U(3),
\]

is unitary on C^15 and therefore orthogonal on R^30. Its real determinant is |det_C(A ⊗ B)|²=1. Thus the image of SU(5) × U(3), modulo its finite kernel, already embeds in U(15) ⊂ SO(30). The extra central color phase needs no extra real vector directions.

One can choose a larger embedding with additional singlets, but then a further physical requirement is doing the selecting. Likewise SO(30) × SO(2) is only a subgroup of SO(32); additional directions do not by themselves prove interactions respect the full larger algebra or require its mixed generators.

## What could force exactly 32?

Two levels of missing input should be distinguished:

1. **Four-dimensional constituent completion:** motivate exactly one complex neutral endpoint, explain its charges and its mixed composites, and establish why the full orthogonal symmetry acts. Neither the present bootstrap count nor weak-isospin completion as yet derives this.
2. **A string/ten-dimensional consistency condition:** for standard ten-dimensional N=1 supergravity coupled to super-Yang–Mills with Green–Schwarz anomaly cancellation, gravitational anomaly cancellation requires 496 gauge generators. Within SO(n), n(n−1)/2=496 selects n=32. Gauge/mixed anomaly factorization must also hold. In the corresponding type-I construction, tadpole cancellation is the complementary way to obtain 32 Chan–Paton labels.

The second route is an external, conditional selector, not a consequence of the paper's four-dimensional scalar counting. A scalar multiplet with 496 entries is not by itself the ten-dimensional gauge sector to which the anomaly condition applies. E8 × E8 provides another familiar 496-dimensional string gauge algebra, so dimension 496 alone does not establish the orthogonal realization or its global form.

The sharpest working hypothesis is therefore a missing neutral constituent sector, with an anomaly/tadpole or other dynamical condition needed to **force** its minimal completion. No specific neutral particle, binding dynamics, electroweak embedding or full string compactification has been derived in this step.
