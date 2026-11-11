# Nine dimensions: SO(32) labels, winding labels and the exceptional groups

10 November 2026. Blackboard entry: exact lattice computations with conditional readings, unreviewed.

**Provenance.** Written by Claude (model Fable 5.2) in the same Claude Code session as [012](012_so32_gauge_field_scalars.md), [013](013_colour_from_thooft_twist.md) and [014](014_three_label_states_baryons_in_e8.md). The user had said that the relation between SO(32) and E8 × E8 has to be understood, and 014 listed the explicit nine-dimensional map as an open point, with its section B8 argued and left uncomputed. The session took up that point on its own initiative during a pause; the user did not ask for this step separately. Lattice statements are computed by the script of section 6. Statements about the type I′ description, Vinberg's theorem and the literature are quoted from memory and marked. Two web searches located the main reference; no paper was re-read. No second model reviewed this entry.

**Units.** Radii and masses appear through the dimensionless combinations r = R²/α′ and α′M², with α′ the Regge slope of the heterotic string and ħ = c = 1. Everything else is dimensionless.

## 1. Question

In nine dimensions the two heterotic strings are one theory. Where do the nine labels of E8 ⊃ SU(9) (014 B1) sit in SO(32) variables? Which nine-dimensional vacua keep the labels, colour and charge that 012 uses?

## 2. Setting

The charges of the heterotic string on a circle form the even self-dual lattice of signature (17,1). In SO(32) variables a vector is

    v = (π; n, w),        v² = π² + 2nw,

with π in the lattice of Spin(32)/Z₂ (the sixteen label charges), n the momentum and w the winding number. A vacuum is a Wilson line A (sixteen numbers) and a radius, combined in

    t = (−A; −(A²/2 + r), 1),        t² = −2r.

A vector with v² = 2 is a state with α′M² = (v·t)²/r and physical label charges π + wA. The massless ones, v·t = 0, are the charged gauge bosons. Two labels whose Wilson-line values agree up to sign and integers stay related by zero-winding roots, so each label is characterized by its folded value, the distance of A_a to the nearest integer, between 0 and 1/2.

As I recall the type I′ description of the same theory: the folded values are the positions of sixteen D8-branes on an interval between two orientifold planes, the zero-winding two-label states are open strings between D8-branes, and the winding number is the number of D0-branes.

## 3. Results

### N1. The nineteen simple roots in SO(32) labels

    g1  = (0; −1, −1)
    a0  = (−e1 − e2; 1, 0)
    a_i = (e_i − e_(i+1); 0, 0),   i = 1, …, 15
    a16 = (e15 + e16; 0, 0)
    g2  = ((−1/2)^16; 1, −1)

Their Gram matrix is the diagram of Vinberg for this lattice: a chain of seventeen, g1 – a0 – a2 – a3 – … – a14 – a16 – g2, with a1 attached to a2 and a15 attached to a14. Eighteen of the nineteen form a basis of the lattice. Two of them carry winding.

- Removing a8 leaves two affine E8 diagrams with the same null vector z = ((−1)^8, 0^8; 2, −2). The decompactification limit of the E8 × E8 frame is a state of winding 2 in SO(32) variables. The quotient z⊥/z has the roots of E8 × E8: 224 classes of even winding and 256 of odd winding.
- Removing g1 and g2 leaves the affine D16 diagram, with null vector k = (0; 1, 0), pure momentum.
- Deleting two nodes so that a finite diagram remains gives the points of maximal gauge symmetry. There are 80 such pairs, 44 up to the left–right symmetry of the diagram. At each of the 80 the script solves for t, enumerates every root orthogonal to it and finds the group read from the diagram.

All later statements refer to this frame unless another is named.

### N2. Exceptional groups come from at most seven labels and the circle

Take m labels at folded Wilson-line value 1/2, the other 16 − m at 0, and r = (8 − m)/8.

| m | R²/α′ | gauge group | at zero winding | roots at \|w\| = 0, 1, 2 |
|---|---|---|---|---|
| 3 | 5/8 | SU(5) × SO(26) | SU(4) × SO(26) | 324, 8, 0 |
| 4 | 1/2 | SO(10) × SO(24) | SO(8) × SO(24) | 288, 16, 0 |
| 5 | 3/8 | E6 × SO(22) | SO(10) × SO(22) | 260, 32, 0 |
| 6 | 1/4 | E7 × SO(20) | SO(12) × SO(20) | 240, 64, 2 |
| 7 | 1/8 | E8 × SO(18) | SO(14) × SO(18) | 228, 128, 28 |

The factor E_(m+1) consists of the SO(2m) of the m labels at zero winding, the spinor of SO(2m) at winding ±1 and, for m = 6 and 7, a singlet or the vector at winding ±2. The winding-one states have π equal to a subset of the m labels of even size and physical charges (±1/2)^m. For m = 0, 1, 2 the same construction gives SU(2), SU(2) × U(1) and SU(3) × SU(2); m = 8 is the cusp of N1 at r → 0. This is the series E4 = SU(5), E5 = SO(10), E6, E7, E8. As I recall, in type I′ it is m D8-branes on an orientifold plane where the coupling diverges, the winding-one states being a D0-brane with one fermionic zero mode per D8-brane.

### N3. E8 at the E8 × SO(18) point

248 = 14 + 64 + 92 + 64 + 14 at winding −2, …, 2.

- Zero winding: SO(14) × U(1) on seven labels, the meson-like and diquark-like two-label states of those labels.
- Winding ±1: subsets of the seven labels of even size, 1 + 21 + 35 + 7.
- Winding ±2: the vector of SO(14), a single label or anti-label in physical charges.

Read the seven labels as (u,c) × colour and n. The winding-one states are then

| coloured labels | n | states | colour singlets |
|---|---|---|---|
| 0 | no | 1 | 1 |
| 1 | yes | 6 | 0 |
| 2 | no | 15 | 0 |
| 3 | yes | 20 | 4 |
| 4 | no | 15 | 0 |
| 5 | yes | 6 | 0 |
| 6 | no | 1 | 1 |

The four colour singlets with three coloured labels are the flavour-symmetric uuu, uuc, ucc, ccc, each with n. The rule of 014 B6, that n accompanies odd baryon number, holds here for massless states.

### N4. The nine labels of E8 in SO(32) variables

An SU(9) inside this E8 has simple roots g1, a0, a2, …, a6 and −θ = (e1 + … + e6 + 2e7; −2, 2). Its nine labels are seven SO(32) labels, one of them reversed and taken as n, and two labels that differ from those by winding. The winding carried by the nine labels is (1/3)^7, −2/3, −5/3.

- The 84 splits as 35 + 21 + 21 + 7 at winding 1, 0, −1, −2.
- The 21 at zero winding are SO(32) two-label states: the 15 diquark-like states e_i + e_j of the six coloured labels and 6 states e_i − e_n. **A diquark-like state of SO(32) is a three-label state of E8 whose third label is a winding label.**
- The 35 at winding one are the 15 subsets with two coloured labels and the 20 with three coloured labels and n.

The winding functional restricted to E8 is a vector of norm 4. Relative to an SU(9) it sits in one of three positions, and the nine labels split by winding as 7+1+1, 4+4+1 or 5+2+2 (144, 1260 and 756 of the 2160 vectors of norm 4). The 84 then has 21, 30 or 30 members at zero winding.

Other duality frames give other gradings. Among 6000 null vectors obtained from k by reflections, all of SO(32) type, the zero-winding part of E8 is SO(14) in 3377, SU(8) in 1935, SO(12) in 598, SU(7) × SU(2) in 64, SU(7) in 25 and SO(10) × SU(3) in 1. In the SU(8) frames eight of the nine labels are SO(32) labels of that frame and the ninth differs from them by three units of winding. Section N5 shows that nine never are.

This replaces 014 B8 by a computation.

### N5. Colour

**Lemma.** Let an E8 factor be unbroken and take any frame of SO(32) type. The roots of E8 at zero winding embed isometrically in the roots of Spin(32)/Z₂, which are those of D16, and D16 has no subsystem of type E (at a branch node of D16 two of the three arms cannot be extended). For nine labels read as 3_f ⊗ 3_c, a colour-blind direction (a,a,a,b,b,b,d,d,d) is orthogonal to the 72 roots of an E6, and its centralizer is E6, E6 × SU(2) or E7. So the winding number never commutes with the colour group of 014 B1: in every SO(32) frame some of its gluons carry winding. The winding functional also cannot vanish on E8, because the lattice of Spin(32)/Z₂ has no E8 summand.

**The SO(32) colour inside E8.** With the seven labels read as in N3, the colour group of 012 is at zero winding. It acts on the nine labels as 3 + 3 + 1 + 1 + 1: two coloured flavours and three colourless labels, n and the two winding labels. The colour singlets in the 248 number 22, with 6, 6, 6, 2, 2 at winding 0, 1, −1, 2, −2, and they form G2 × SU(3):

- the SU(3) acts on the three colourless labels;
- the long roots of the G2 are the three-label states uuu and ccc, the state made of the three colourless labels, and their conjugates;
- its short roots are uuc, ucc, their conjugates and the flavour change between u and c.

In E7, with six labels and no n, the colour singlets number 11 and no three-label state appears. Adding n to the up-type block is what brings in the baryon-like quartet.

### N6. Vacua that respect colour and charge

Colour test: the sixteen folded Wilson-line values contain five disjoint triples of equal values, so that the colour group of 012 is unbroken at zero winding. Charge test: the Wilson line is constant on six labels (u,c) and on nine labels (d,s,b), with n free.

Of the 44 points of maximal symmetry, 24 pass the colour test and 11 pass the charge test:

| labels | gauge group | R²/α′ | folded Wilson line |
|---|---|---|---|
| all sixteen together | SO(32) × SU(2) | 1 | 0 |
| | SO(34) | 1/2 | 0, with a sign on the spinor class |
| | SU(16) × SU(2) × SU(2) | 1/2 | 1/4 |
| | SU(17) × SU(2) | 17/49 | 3/14 |
| | SU(18) | 1/4 | 1/4 |
| (u,c,n \| d,s,b) | E8 × SO(18) | 1/8 | 1/2 \| 0 |
| | E8 × SU(9) × SU(2) | 1/9 | 1/2 \| 1/18 |
| | E8 × SU(10) | 5/49 | 1/2 \| 1/14 |
| (u,c \| d,s,b,n) | E7 × SO(20) | 1/4 | 1/2 \| 0 |
| | E7 × SU(10) × SU(2) | 1/5 | 1/2 \| 1/10 |
| | E7 × SU(11) | 11/64 | 1/2 \| 1/8 |

A Wilson line that depends only on electric charge produces exceptional symmetry only as E7 or E8, and always on the up-type block: E7 from the six (u,c) labels, E8 when n joins them. The nine or ten labels of the other block exceed seven and give SO(18), SU(9), SU(10), SO(20) or SU(11). E6 would need a block of five labels and fails the colour test.

Five further points with an exceptional factor pass the colour test and split the labels in three blocks: E8 × E7 × SU(3) (7, 3, 6), E8 × SU(6) × SU(5) (7, 6, 3), E7 × E7 × SU(4) (6, 4, 6), E7 × SO(10) × SU(6) (6, 6, 4) and E7 × SU(7) × SU(5) (6, 7, 3).

### N7. The down-type block at the E8 × SO(18) point

The lightest massive states at this point are 256 + 256 states with α′M² = 1/2. They have winding ±1, are neutral under E8 and form the spinor of SO(18). They are vectors of the spinor class of 014 B6 with one unit of winding. At winding +1 an odd number of the nine labels (d,s,b) × colour is present: 9 + 84 + 126 + 36 + 1.

The 84 = Λ³(9) is the multiplet of 014 B1 with the flavours (d,s,b). It contains ten colour singlets, the decuplet labels ddd, dds, …, bbb. The state with all nine labels is the eleventh colour singlet.

So three-label states of both blocks are winding-one states at this point: massless and part of E8 for the up-type block, massive for the down-type block. The states at α′M² = 2 include the charged meson-like and the ud-type diquark-like two-label states, which the Wilson line lifts.

### N8. The SU(18) point

All sixteen labels sit at folded Wilson-line value 1/4 and r = 1/4. The eighteen labels of SU(18) are the sixteen SO(32) labels and two winding labels, of winding −1 and +1. The 306 roots have winding 0 (240, the U(16) of the sixteen labels), ±1 (32 each) and ±2 (1 each).

- **Label number is a multiple of three.** The simple roots a1 and a15, deleted at this point, have label number 15 and 3 modulo 18, and the nineteen roots span the lattice. The gauge group is SU(18)/Z₃: single-label states and antisymmetric two-label states of the eighteen labels are absent from the whole spectrum.
- **The lightest massive states are three-label states.** They are the 816 states of Λ³(18) and their conjugates, at α′M² = 1.
- **The diquarks are among them.** The 816 have winding 0, −1, −2 with multiplicities 120, 576, 120. The 120 at zero winding are the diquark-like states e_i + e_j of SO(32), which the Wilson line has lifted. As in N4, a diquark-like state is a three-label state with a winding label.
- Under the colour group of 012 the eighteen labels are fifteen coloured ones and three colourless ones, n and the two winding labels.

## 4. Reading for the sBootstrap

1. The diquark-like states, which the sBootstrap pairs with quarks, are three-label states of the enhanced groups, with a winding label as third constituent. This holds in E8 and in SU(18)/Z₃. In the type I′ picture a winding label is a D-particle.
2. When the Wilson line follows electric charge, exceptional groups arise only on the up-type side, and the label n decides between E7 and E8.
3. Baryon-like three-label states are winding-one states in SO(32) variables: massless inside E8 for (u,c) with n, massive for the (d,s,b) decuplet labels, and the lightest massive states at the SU(18) point.
4. The decuplet reading of 014 B1, nine labels (u,d,s) × colour in one E8, has no expression in SO(32) labels: its colour carries winding in every frame. What SO(32) variables give for E8 is two coloured flavours and three colourless labels, with colour singlets G2 × SU(3).
5. All these vacua have sixteen supercharges and only adjoint matter. They organize labels. Chirality and the selection of a vacuum are outside this entry.

## 5. Open points

- The charge of winding states. A charge that is neutral on momentum has the form Q = q·π + b·w, with one new number b. The type I′ picture may fix it.
- The three colourless labels at the E8 and SU(18) points, and the SU(3) acting on them in E8: a possible lepton-label reading was not examined.
- A sixth coloured flavour at the SU(18) point needs a colour group that carries winding, since the colour of 012 leaves the two winding labels colourless.
- The algebra of the 11 colour singlets of E7, and the global forms at points other than SU(18), were not computed.
- The type I′ statements, in particular the D-particle spectrum on the two blocks of D8-branes, should be checked against the literature.
- N4 sampled 6000 duality frames. A classification of the possible zero-winding parts of E8 was not attempted.

## 6. Files and reproduction

[`scripts/nine_dim_frames/nine_dim_frames.py`](../scripts/nine_dim_frames/nine_dim_frames.py) writes [`calculations/nine_dim_frames/nine_dim_frames.txt`](../calculations/nine_dim_frames/nine_dim_frames.txt). Exact arithmetic, about ninety seconds. Part A checks N1, part B the cusp, part C the table of N2, part D sections N3–N5 and N7, part E the 44 points with the two tests of N6, part F the SU(18) point, part G the other duality frames.

The independent consistency criteria are: the agreement between the diagram and a direct enumeration of roots at each of the 80 points; the count 44; the E8 × E8 root system of z⊥/z; the dimensions 84, 816 and 256 of the multiplets found by enumeration; and the root system G2 + A2 of the colour-singlet weights.

## 7. Status

- **Known and restated:** the diagram of the lattice (Vinberg) and its use for the nine-dimensional heterotic string, with the list of points of maximal symmetry, in Font, Fraiman, Graña, Núñez and Parra De Freitas, JHEP 10 (2020) 194, arXiv:2007.10358; I recall the number 44 from that paper and did not re-read it. The series E_(m+1) from m D8-branes in type I′. The equivalence of the two heterotic frames on a circle. A quotient by Z₃ for SU(18) appears in the literature on eight dimensions as I recall; the abstract of the 2020 paper describes the nine-dimensional groups as simply connected, and I have not reconciled the two statements.
- **New in this notebook, unreviewed:** the nine-label dictionary with its winding gradings (N4); the lemma on colour and the G2 × SU(3) of colour singlets (N5); the colour and charge tests on the 44 points (N6); the readings of N7 and N8. Explicit expressions of the roots in the sixteen labels probably exist in the literature in other conventions.
- **Conditional:** every identification of labels with flavour, colour and charge.
- **Replaced:** 014 B8, now computed and sharpened: seven labels in the frame of largest radius, eight in other frames, never nine.
