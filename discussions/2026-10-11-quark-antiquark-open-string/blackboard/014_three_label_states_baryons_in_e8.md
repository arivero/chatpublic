# Three-label states: baryon labels in E8 and in the spinor class of SO(32)

10 November 2026. Blackboard entry: representation results with conditional readings, unreviewed.

**Provenance.** Written by Claude (model Fable 5.2) in the same Claude Code session as [012](012_so32_gauge_field_scalars.md) and [013](013_colour_from_thooft_twist.md). The user remarked that the relation between SO(32) and E8 × E8 has to be understood at some point. The session answered that E8 contains SU(9) with a three-index tensor that holds baryon labels; the user called that idea new and asked for it to be worked out and pushed. While the work was running the user added that "our 3-index" is also the index structure of the M5-brane and its dual; section B7 records that. Statements about the classic Z₃ orbifold, the non-BPS D-particle and U-duality are quoted from memory and are marked; the representation content was computed here. No second model reviewed this entry.

**Units.** All statements are dimensionless.

## 1. Question

In 012 the adjoint of SO(32) organizes two-label states: meson-like (a label and an anti-label) and diquark-like (two labels). The March draft `sbootstrap_v4d.tex` notes that E8 × E8 cannot hold the symmetric diquark 15. What does E8 hold instead, and where are three-label states on the SO(32) side?

## 2. Results

### B1. E8 in its SU(9) form holds the baryon decuplet labels

Write the 240 roots of E8 in R⁹ as

    e_i − e_j  (72),        ±( e_i + e_j + e_k − (1/3) Σ e )  (84 + 84).

Then 248 = 80 ⊕ 84 ⊕ 84bar under SU(9), with 84 = Λ³(9). Read the nine labels as (flavour, colour) with three flavours and three colours. By comparison of weight multisets,

    84 = (10,1) ⊕ (8,8) ⊕ (1,10),
    80 = (8,1) ⊕ (1,8) ⊕ (8,8).

The (10,1) is the product S³(3_f) ⊗ Λ³(3_c): three labels, symmetric in flavour, antisymmetric in colour. That is the label content of the baryon decuplet, with the colour structure that the quark model needs. The (8,1) is the meson octet and the (1,8) the gluons. The remaining components are coloured: three copies of (8,8) in the 248, and (1,10) ⊕ (1,10bar).

### B2. For (u,d,s) the electric charge is a generator of E8

Q = diag(2/3, −1/3, −1/3) ⊗ 1₃ is traceless on the nine labels, so it lies in SU(3)_f ⊂ SU(9) ⊂ E8 and needs no extra U(1). The colour singlets then carry

- in the 84: charges 2, 1, 0, −1 with multiplicities 1, 2, 3, 4, the decuplet pattern (Δ, Σ*, Ξ*, Ω);
- in the 80: charges −1, 0, +1 with multiplicities 2, 4, 2, the meson octet.

For the triplet (d,s,b) of the sBootstrap the charge is proportional to the identity on the nine labels and has to come from outside SU(9). For (u,c), six labels give Λ³(6) = (4,1) ⊕ (2,8): four colour singlets uuu, uuc, ucc, ccc.

### B3. Label number is conserved modulo 9

The decomposition is a Z₃ grading of E8: the sum of two roots of the 84 is a root of the 84bar whenever it is a root. Two three-label states compose into a state with six labels, which is an anti-three-label state by the ε tensor of SU(9). Baryon number, read as label number over three, is conserved modulo 3.

### B4. What E8 does not hold

- **No baryon octet.** Labels without spin force a totally symmetric flavour state once colour is antisymmetric. The octet needs spin labels: eighteen labels 3 × 2 × 3, with Λ³ containing the (56,1) of flavour-spin SU(6). That needs SU(18), outside E8.
- **No diquark-like states.** There is no Λ²(9) in the 248. This is the obstruction the March draft found for the 15.
- **No single home for five flavours.** Fifteen labels exceed the rank. The six (u,c) labels and the nine (d,s,b) labels would have to sit in different E8 factors.

### B5. A string model: the classic Z₃ orbifold with SU(9)

The Z₃ orbifold of the E8 × E8 heterotic string with shift V = (1,1,1,1,2,0,0,0 ; 2,0,…,0)/3 has gauge group SU(9) × SO(14) × U(1). Its massless charged spectrum, computed here with the rules of 012 adapted to the lattice Γ₈ ⊕ Γ₈, is

    untwisted:  3 × [ (84,1) ⊕ (1,14) ⊕ (1,64) ]
    twisted:   27 × (9bar,1)

and the SU(9) cubic anomaly cancels between the sectors, 3 × 9 − 27 = 0. This agrees with the spectrum of that model as I recall it from the literature.

With the nine labels read as (flavour, colour):

| | SO(32), Z₃ model of 012 | E8 × E8, this model |
|---|---|---|
| gauge group | U(15) × SO(2) | SU(9) × SO(14) × U(1) |
| gauge bosons | meson-like labels, gluons | meson octet labels, gluons |
| untwisted matter, 3 copies | diquark-like labels (15bar,3) ⊕ (10bar,6bar), one-label states | baryon-like labels (10,1) ⊕ (8,8) ⊕ (1,10) |
| twisted matter, 27 copies | one-label states (5,3) | anti-label states (3bar,3bar) |

In both models the three copies of the untwisted matter come from the three complex planes, and flavour is gauged together with colour, as discussed in 012 and 013.

### B6. On the SO(32) side the three-label states are in the spinor class

The lattice of Spin(32)/Z₂ contains the weights (±1/2)¹⁶ with an even number of minus signs. A weight is a subset S of the sixteen labels (the labels with +1/2), with |S| even. These states are massive at the string scale in ten dimensions. As I recall, their type I dual is the non-BPS D-particle, whose zero modes are one fermion per label.

Counting colour singlets among the subsets, with fifteen coloured labels (five flavours) and the label n:

| coloured labels | n present | colour singlets | B | flavour content |
|---|---|---|---|---|
| 0 | no | 1 | 0 | 1 |
| 3 | yes | 35 | 1 | S³(5) |
| 6 | no | 175 | 2 | S_(3,3)(5) |
| 9 | yes | 175 | 3 | conjugate of the previous |
| 12 | no | 35 | 4 | conjugate of S³(5) |
| 15 | yes | 1 | 5 | 1 |

422 colour singlets in total. Three consequences:

1. **Baryon labels exist in the SO(32) theory**, as the 35 with three coloured labels: flavour-symmetric, colour-antisymmetric. They come with a tower of multi-baryon label states up to B = 5.
2. **The label n accompanies odd baryon number.** The lattice condition |S| even reads 3B + L even if n carries lepton number 1, which is the condition (−1)^F = +1 of the Standard Model quantum numbers. The B = 1 states have B − L = 0.
3. **The charge of the sixteenth label is fixed.** A subset S has charge Σ_{a∈S} q_a − (1/2) Σ_{all} q_a. The fifteen coloured labels sum to +1, so the offset is −(1 + q_n)/2. With q_n = 0 every colour singlet of the class has half-integer charge. With q_n = −1 the offset vanishes and all 422 have integer charge. Integer charge for colour singlets therefore gives the trace condition that 012 R6 had to assume.

With q_n = −1 the B = 1 states have charges 1, 0, −1, −2: for example the labels of uud with n are neutral.

### B7. The same three-index structure in M-theory

Recorded at the user's prompt. The decomposition 248 = 80 ⊕ 84 ⊕ 84bar also organizes the U-duality algebra of M-theory on an eight-torus, E8(8) ⊃ SL(9,R), as I recall it: the 80 is the geometric part, the 84 = Λ³ holds the components of the three-form, to which the M2-brane couples, and the 84bar = Λ⁶ those of the dual six-form, to which the M5-brane couples. The relation of B3, that two elements of the 84 bracket into the 84bar, is there the statement that two three-forms source the six-form.

Under that dictionary a label is a direction, a baryon-labelled state a three-form component, and an anti-baryon-labelled state a six-form component. The 2009 preprint (arXiv:0910.4793, section III) already singled out the 84 of the three-form and matched it with the 84 degrees of freedom of the light Standard Model fermions.

This is the same complex algebra in a different real form and a different role: a gauge algebra in B1–B5, a duality algebra here. Nothing in this entry connects the two uses.

### B8. Correction to a remark made in the session

Before this entry the session suggested that in nine dimensions the U(9) of nine SO(32) labels could enhance either to SO(18) or to E8. The first is right. The second is wrong as stated: an E8 containing that SU(9) would have the same rank, so its roots would lie in the span of the nine-label root lattice, and those roots are absent from the lattice of the SO(32) frame at zero winding. The two heterotic theories are one theory on a circle, but the duality between the frames mixes gauge labels with the circle direction and does not carry nine labels to nine labels. In the SO(32) frame the three-label states are the spinor class of B6. This is lattice reasoning and was not computed.

## 3. Reading for the sBootstrap

- SO(32) holds mesons and diquarks as massless two-label states and baryons as massive spinor-class states. E8 holds mesons and baryons as massless states and has no diquarks.
- An odd number of labels does not make a state a fermion here. Both multiplets contain both statistics. The correlation that does appear is B6.2, between baryon number and the sixteenth label.
- B6.3 strengthens blackboard 012 R6: the charge −1 for the sixteenth label follows from integer charges of colour singlets in the spinor class.
- The count 84 appears three times: Λ³(9) in E8, the three-form in eleven dimensions, and the light fermion degrees of freedom in the 2009 preprint.

## 4. Open points

- Whether the multi-baryon tower of B6 has a role, and what the non-BPS D-particle description says about its masses and stability with these labels.
- A realization of the octet: spin labels and SU(18), which as I recall appears among the rank-17 enhancements of the nine-dimensional heterotic string. Not examined.
- The explicit duality map between the frames in nine dimensions, replacing the argument of B8 by a computation.
- Whether B7 is more than a shared decomposition.

## 5. Files and reproduction

[`scripts/e8_baryons/e8_baryons.py`](../scripts/e8_baryons/e8_baryons.py) writes [`calculations/e8_baryons/e8_baryons.txt`](../calculations/e8_baryons/e8_baryons.txt). Exact arithmetic. Part A checks the root system and the decompositions of B1–B3, part B counts the colour singlets of B6 for q_n = 0 and −1, part C computes the spectrum and anomaly of B5. The independent consistency criteria are the weight-multiset comparison in A, the agreement of the singlet counts with the dimensions 35 and 175, and the anomaly cancellation in C.

## 6. Status

- **Known and restated:** E8 ⊃ SU(9) with 248 = 80 ⊕ 84 ⊕ 84bar; the Z₃ orbifold with SU(9) × SO(14) × U(1); the spinor class of Spin(32)/Z₂; the SL(9) decomposition in U-duality. The family-unification literature that uses SU(9) ⊂ E8, cited in the 2024 paper, was not checked for the reading of B1.
- **New in this notebook, unreviewed:** the reading 9 = 3_f ⊗ 3_c with the decuplet and octet charges (B1, B2); the comparison table of B5; the multi-baryon tower, the relation between baryon number and the sixteenth label, and the derivation of q_n = −1 (B6).
- **Conditional:** every identification of labels with flavour, colour and charge.
- **Corrected:** the nine-dimensional remark, B8.
