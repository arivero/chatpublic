# Are the sBootstrap scalars internal components of the ten-dimensional SO(32) gauge field?

10 November 2026. Blackboard entry: a hypothesis with conditional results, unreviewed.

**Provenance.** Written by Claude (model Fable 5.2) in a Claude Code session, at the user's request to work on one sentence from that session: *compactifying the 10D gauge field gives adjoint scalars with exactly these labels*. The session had read the 2024 EPJC paper, the 2005, 2007 and 2009 preprints, the March 2026 draft `sbootstrap_v4d.tex` of the separate `physres2` repository, and [blackboard 011](011_so30_so32_neutral_completion.md). This is source-informed work by a single model; no second model reviewed it. The enumeration scripts were written and run by the same model, and their outputs are on disk.

**Units.** Sections R1–R3, R5 and R6 are dimensionless representation statements. R4 contains the only dimensionful formula and keeps ħ and c explicit.

## 1. Question

The EPJC paper (A. Rivero, Eur. Phys. J. C 84, 1058 (2024), arXiv:2407.05397)
places the scalars of a three-generation supersymmetric Standard Model in three
pieces of the adjoint of SO(32), under SU(5) flavour × SU(3) colour:

    (24,1) ⊕ (15,3bar) ⊕ (15bar,3)   ⊂   496.

Two earlier records leave a gap that this note addresses.

- The March 2026 draft `sbootstrap_v4d.tex` (repository `physres2`, section
  "Physical content and the projection problem") lists as open which mechanism
  removes or lifts the other 442 states: "an orbifold, a GSO-type condition,
  or a flux background".
- [Blackboard 011](011_so30_so32_neutral_completion.md) points out that a
  496-component scalar multiplet is a different object from the
  ten-dimensional gauge sector that anomaly cancellation constrains.

Hypothesis tested here: the scalars are the components of the ten-dimensional
SO(32) gauge field along compact directions.

## 2. Conventions

- Cartan directions e_1 ... e_16. Fifteen carry a pair (flavour, colour) with
  flavour in {u, c, d, s, b}; the sixteenth, n, is colourless.
  32 = (5,3) ⊕ (5bar,3bar) ⊕ 1 ⊕ 1.
- The 480 roots ±e_a ± e_b fall into open-string-like sectors:

  | Sector | Roots | SU(5) × SU(3) content |
  |---|---|---|
  | M(i jbar), "meson" | e_(i,c) − e_(j,d) | (24,1) ⊕ (24,8) ⊕ (1,8), with the Cartan generators |
  | D(ij), "diquark" | e_(i,c) + e_(j,d) | (15,3bar) ⊕ (10,6) |
  | Q(i n), Q(i nbar) | e_(i,c) ± e_n | 2 × (5,3) |

  Conjugate sectors carry the opposite roots.
- Electric charge is the Cartan generator Q = Σ_a q_a H_a with q = 2/3 on u, c
  labels, −1/3 on d, s, b labels, and q_n = 0 (an assumption). It gives
  q_i − q_j on mesons and q_i + q_j on diquarks, which reproduces the charges
  of Eqs. (5)–(6) of the paper.

## 3. Results

### R1. In nine dimensions the count is exact

The vector multiplet of nine-dimensional N=1 supersymmetry contains one real
scalar. For the heterotic or type I string on a circle that scalar is the
gauge-field component A_9, in the 496. In the type I' picture it is the
position of the sixteen D8-branes. Restricted to the three pieces it has
24 + 2 × 45 = 114 real components:

| Piece | Real scalars | Reading in the paper |
|---|---|---|
| (24,1): (3,2) ⊕ (3bar,2) | 12 | six complex charged sleptons |
| (24,1): (1,1) ⊕ (1,3) ⊕ (8,1) | 12 | six complex sneutrinos |
| (15,3bar) ⊕ c.c.: the (3,2) | 36 | six complex squarks of charge 1/3, per colour |
| (15,3bar) ⊕ c.c.: the (6,1) | 36 | six complex squarks of charge 2/3, per colour |
| (15,3bar) ⊕ c.c.: the (1,3) | 18 | the three extra states of charge 4/3, per colour |

This is the paper's "two scalars per Dirac fermion" with no extra copies. Each
further compact dimension adds one real scalar per generator: 10 − D in
dimension D, six on a six-torus.

The 2009 preprint (arXiv:0910.4793, section III) already singles out nine
dimensions as the non-chiral stage that carries SU(3) × U(1).

Consequence for blackboard 011: under this hypothesis the scalar multiplet is
the gauge sector, so ten-dimensional anomaly cancellation (496 generators,
n = 32 within SO(n)) becomes the selector of SO(32) over SO(30).

### R2. The labels have the right symmetry, with no Pauli problem

The adjoint is Λ²(32), and
Λ²(5,3) = S²(5)⊗Λ²(3) ⊕ Λ²(5)⊗S²(3) = (15,3bar) ⊕ (10,6). The March draft
has this identity and its type I reading.

The heterotic fermionic formulation makes the composite picture literal. The
32 labels are carried by 32 left-moving worldsheet fermions λ^I, and the
adjoint states are the bilinears λ^I_{-1/2} λ^J_{-1/2}|0>, antisymmetric by
worldsheet Fermi statistics. Space-time spin comes from the right-movers:
ψ^μ_{-1/2} for the vector, ψ^i_{-1/2} with i internal for the scalars. The
scalar is a bilinear of two label-carrying fermions, and space-time statistics
plays no part in the symmetry of the labels.

The same language counts the labels. The left-moving internal central charge
must be 16, which is 16 complex fermions = 5 × 3 + 1. A sixth coloured flavour
would need 18.

### R3. What comes with the scalars

1. A vector and gauginos with the same labels, in every sector that keeps the
   scalar, as long as the sixteen supercharges of the torus are kept.
2. The colour partners: (24,8) with (24,1), and (10,6) with (15,3bar). A
   colour-blind operation acts on a root through its flavour labels only.
3. The mixed states 2 × (5,3): strings from a coloured label to n. They carry
   the colour and charge of the five quarks.

### R4. The paper's mass formula has the Coulomb-branch form

With a Wilson line a on the circle of radius R (D8-brane positions in type
I'), a state on root p has mass M = ħ |p·a| / (R c) at the lowest
Kaluza–Klein level. So M² ∝ (a_a − a_b)² for mesons and (a_a + a_b)² for
diquarks. Eq. (14) of the paper, E(q_a, q_b) = K (q_a + q_b)², is this form
with q ↔ a, if E is read as M².

- Eq. (15), z_1 + z_2 + z_3 = 0, is a Wilson line in the Cartan subalgebra of
  the SU(3) acting on the (d, s, b) labels. The angle α of the paper is its
  direction in the (T_3, T_8) plane.
- Eq. (16), z_0² = <z_i²>, is an extra condition on a fourth eigenvalue.
  Nothing here derives it.
- Reflecting a label, e_a → −e_a, is a Weyl reflection of SO(32) and exchanges
  meson and diquark sectors. This is the remark under Table II of the paper,
  that a change of sign of some charges exchanges the (3,2) of sleptons and
  squarks.

Two cautions. The paper applies the formula to fermion masses m, and here it
gives M². In nine dimensions the scalar on a root with p·a ≠ 0 is eaten by
the massive vector; physical scalars with these masses need D ≤ 8, where
9 − D remain per broken generator.

### R5. Orbifold projections: which labels survive as chiral scalars

Setting: T⁶/Z_N orbifolds preserving four-dimensional N=1, heterotic
consistency conditions (N V in Γ_16, N (V² − v²) even), no Wilson lines, and
colour-blind shifts V = (w_u³, w_c³, w_d³, w_s³, w_b³, w_n). A root p gives a
gauge boson if p·V is an integer, one chiral multiplet from the internal
component A_{z_k} if p·V = v_k mod 1, and is projected out otherwise.

**(a) Admissible colour-blind shifts** (pairs (w, w_n), before identifying
equivalent models): Z3 42, Z4 96, Z6-I 492, Z7 930, Z8-I 1512, Z8-II 1656,
Z12-I 9408. Z6-II and Z12-II admit none.

**(b) Z3** reproduces the series U(3k) × SO(32 − 6k), k = 0 ... 5. The k = 5
member, V = (1^14, 2, 0)/3, has gauge group U(15) × SO(2), the paper's
SO(2) × SU(15) stage. Its complete massless charged spectrum is

    untwisted:  3 × [ 105bar ⊕ 15_(+1) ⊕ 15_(−1) ]
    twisted:   27 × [ 15_(−1/2) ⊕ 3 singlets ]

So the internal gauge-field components give three copies of
(15bar,3) ⊕ (10bar,6bar), one per complex plane, and the meson labels are the
U(15) gauge bosons.

**(c) Single copies exist.** With flavour-universal shifts, Z4 and Z6-I give
U(15) × U(1) with two chiral multiplets in the 105, and Z8-I, Z8-II and Z12-I
give it with one. With the
(u,c | d,s,b) split of the paper the gauge group is U(6) × U(9) × U(1):

| Orbifold | (w_u, w_d; w_n) | uu | ud | dd | charged mesons |
|---|---|---|---|---|---|
| Z8-I, v = (1,2,−3)/8 | (1/16, 9/16; 5/16) | plane 1 | plane 3 | plane 1 | projected out |
| Z12-I, v = (1,4,−5)/12 | (1/24, 7/24; 1/8) | plane 1 | plane 2 | plane 3 | projected out |
| Z12-I | (1/24, 13/24; 3/8) | plane 1 | plane 3 | plane 1 | projected out |

Each entry is one chiral multiplet, all with the same orientation. The
twisted sectors of these non-prime orbifolds were not computed.

**(d) A Z7 model keeps every charged label once.** V = (1^6, 2^9, 0)/7, gauge
group U(6) × U(9) × SO(2), complete massless charged spectrum:

| Sector | Copies | U(6) × U(9), SO(2) charge | Labels |
|---|---|---|---|
| untwisted, plane 1 | 1 | (6bar, 9) | charged mesons d ubar |
| untwisted, plane 1 | 1 + 1 | (6, 1), charge ±1 | u n, u nbar |
| untwisted, plane 2 | 1 | (15, 1) | uu diquarks, charge 4/3 |
| untwisted, plane 2 | 1 + 1 | (1, 9), charge ±1 | d n, d nbar |
| untwisted, plane 3 | 1 | (1, 36) | dd diquarks, charge −2/3 |
| untwisted, plane 3 | 1 | (6bar, 9bar) | ubar dbar antidiquarks, charge −1/3 |
| twisted θ | 21 | singlets | |
| twisted θ² | 7, 7, 21 | (6, 1), (1, 9bar), singlets | |
| twisted θ⁴ | 7, 7 | (6, 1), singlets | |

Every charged label of the 496 appears exactly once as an internal
gauge-field component. The twelve neutral meson labels of (24,1) are the gauge
bosons of U(1) × SU(2) × SU(3) flavour inside U(6) × U(9). On the coloured
labels the shift is V = (5 N_q/3 − Q)/7, with N_q the label number and Q the
electric charge.

**(e) A restriction.** In the whole scan, 96 shifts make all fifteen diquark
labels chiral with one orientation. None of them keeps any meson label as
matter. The Z7 model evades this by carrying ud with the opposite orientation,
which changes the fermion chirality and leaves the scalar content the same.

**(f) Flavour-diagonal neutral labels are always gauge.** Their roots have
p·V = 0, so the four diagonal neutral meson labels of (24,1) never become
chiral scalars. With the two-block split this extends to all twelve neutral
labels, and the charged mesons are the only meson labels that can become
matter. A finer shift, with w_u ≠ w_c or unequal w_d, w_s, w_b, can turn the
off-diagonal neutral labels (u cbar, d sbar, ...) into matter at the price of
breaking U(6) or U(9) further.

### R6. The sixteenth label: what SO(30) → SO(32) adds

The user asked on 10 November what explains the extra room, and whether it
could hold "tt, tu, tc" states that would cure the odd count of the charge
4/3 sector.

1. **The count is forced, by R2.** Sixteen complex labels are needed and five
   coloured flavours use fifteen. One colourless complex label remains.
2. **Its content is the one-label sector.** The 61 extra generators are
   2 × (5,3), their conjugates and one singlet: every state with exactly one
   coloured label. Write so(32) = k ⊕ p with k = so(30) ⊕ so(2), the two-label
   generators, and p = (30,2), the one-label generators. Then [p,p] ⊂ k: two
   one-label states compose into a meson or a diquark label. The enlargement
   puts the constituents in the same multiplet as their composites.
3. **Its charge.** The charge formula of the paper has no component along
   so(2), so it gives q_n = 0 and the one-label states carry the quark
   charges. A second choice is to require Q traceless on the sixteen complex
   labels, Q in su(16). The fifteen coloured labels sum to
   3 × (2/3 + 2/3 − 1/3 − 1/3 − 1/3) = +1, so tracelessness gives q_n = −1:
   the sixteenth label has the charge of a charged lepton. With all six
   flavours the sum would be 3.
4. **With q_n = −1 the one-label states are leptoquark-like.** In colour 3bar
   their charges are +4/3 (dbar nbar, three flavours), +1/3 (ubar nbar, two),
   −2/3 (dbar n, three) and −5/3 (ubar n, two).
5. **Relation to tt, tu, tc.** A coloured top needs three more labels and
   SO(36), and a single label has no antisymmetric square, so n cannot supply
   tt. What n supplies, for q_n = −1 and lepton number 1, is three states with
   the colour, charge and B − L of tt, tu, tc: the labels dbar ℓ⁺, sbar ℓ⁺,
   bbar ℓ⁺, in colour 3bar with charge 4/3 and B − L = 2/3. This is the
   X-boson pattern of SU(5), uu ~ e⁺ dbar, which Section IV of the paper
   notes for one generation. These three states complete the 4/3 sector to
   six. Their conjugates have the colour and charge needed to pair a chiral
   4/3 fermion into Dirac fermions.
6. **Costs.** Their flavour content is (3bar,1) under SU(3) × SU(2), against
   (1,3) for uu, uc, cc. Their companions raise the 1/3 sector to eight and
   the 2/3 sector to nine and add two states of charge 5/3, unless a
   projection removes them. Example: the first Z12-I model of R5(c) keeps the
   one-label multiplets ubar n and dbar nbar only. With the sixteen taken as
   the coloured labels plus n and q_n = −1, that is the three states of charge
   4/3 together with two of charge −5/3.
7. **Independent of this,** the orbifold spectra are anomaly-free with the
   chiral 4/3 states present. In the Z7 model the (15,1) is chiral and the
   SU(6) cubic anomaly cancels against the other multiplets.

Items 3 to 6 are conditional on the tracelessness requirement, which nothing
here derives.

## 4. Checks

- The Z3 scan returns exactly the series U(3k) × SO(32 − 6k), which is the
  classification of Z3 SO(32) models as I recall it from the literature. I did
  not re-fetch a reference.
- Cubic non-abelian anomalies cancel between untwisted and twisted sectors in
  six models: the five non-trivial Z3 models and the Z7 model (SU(6) and
  SU(9) separately). The opposite orientation convention for untwisted matter
  fails this test in five of the six, which fixes the convention.
- Level matching for the Z8-I and Z12-I shifts in (c) was verified by hand.

## 5. Open points

1. **Colour is not singled out.** The gauge groups are U(15) or U(6) × U(9);
   the product structure 15 = 5 × 3 is a choice of basis. A mechanism that
   leaves SU(3) colour gauged and flavour global is missing. Unexamined
   candidates: magnetic flux or an 't Hooft twist in U(15), which reduces the
   rank to U(3) and turns the five-fold index into a degeneracy; branes at
   singularities; non-abelian orbifolds; Higgsing along flat directions.
2. **Fermion partners.** Ordinary supersymmetry pairs each scalar with a
   fermion of the same labels. The sBootstrap pairs a two-label scalar with a
   one-label fermion. Inside so(32) the one-label generators p = (30,2) and
   the two-label generators k = so(30) ⊕ so(2) form a Z2-graded algebra with
   [p,p] ⊂ k. Its analogue with odd one-label generators is osp(30|2), the
   N = 30 superconformal quantum-mechanics algebra: {Q,Q} = 2H, and so(30),
   which holds the meson and diquark labels, appears in {Q,S}. This is an
   algebraic observation with no dynamics behind it.
3. **The neutral sector.** All twelve neutral labels are scalars on a torus
   (D = 9 down to D = 4 with sixteen supercharges). In the N=1 orbifolds the
   flavour-diagonal ones are gauge bosons, see R5(f).
4. **Not computed:** twisted sectors for non-prime orders, abelian anomalies
   and the fate of U(1) charge, Wilson lines, type I duals. As I recall, the
   perturbative type I Z3 orientifold fixes U(12) × SO(8), so the U(15) models
   live on the heterotic side.
5. **Selection of the 54.** Abelian projections sort labels by a charge and
   keep or remove whole classes: (10,6) always travels with (15,3bar), and
   (24,8) with (24,1). They cannot isolate the three pieces of the paper.

## 6. Files and reproduction

Scripts in [`scripts/so32_gauge_scalars/`](../scripts/so32_gauge_scalars/), outputs in [`calculations/so32_gauge_scalars/`](../calculations/so32_gauge_scalars/). All arithmetic is exact (Python fractions).

- `orbifold_scan.py` → [`scan_summary.txt`](../calculations/so32_gauge_scalars/scan_summary.txt): admissible shifts and gauge groups.
- `split_models.py` → [`split_models.txt`](../calculations/so32_gauge_scalars/split_models.txt), `split_models.json`: the (u,c | d,s,b) split.
- `full_spectrum.py` → [`anomaly_check.txt`](../calculations/so32_gauge_scalars/anomaly_check.txt): twisted sectors and cubic anomalies for Z3 and Z7.
- `report_models.py` → [`selected_spectra.txt`](../calculations/so32_gauge_scalars/selected_spectra.txt): the two spectra quoted in R5.

Why scripts: the enumeration of admissible shifts and the twisted spectra are new finite computations for this question. The independent consistency criteria are the reproduction of the Z3 series and the cancellation of cubic anomalies between sectors computed by different rules.

## 7. Status

- **Known and restated:** the decomposition of the 496, vector-multiplet contents, heterotic orbifold rules, the fermionic construction, the Z3 series. The models found belong to classified families; whether the specific Z7, Z8 and Z12 shifts are tabulated in the literature was not checked.
- **New in this notebook, unreviewed:** R1, R4, the scan and its readings in R5, the charge-trace observation in R6, the osp(30|2) remark.
- **Conditional:** every physical identification (which fifteen labels are flavour × colour, the charge generator, q_n), and R4 on reading the paper's E as M².
- **No literature search** was made for prior statements of R1, R4 or R6.
