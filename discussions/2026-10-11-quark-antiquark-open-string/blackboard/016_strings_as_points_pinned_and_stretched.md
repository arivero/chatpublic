# Strings that are points in the noncompact directions: pinned, wound and stretched

10 November 2026. Blackboard entry: answer to a question of the user, built from recalled string-theory facts and two lattice checks. Unreviewed.

**Provenance.** Written by Claude (model Fable 5.2) in the same Claude Code session as [012](012_so32_gauge_field_scalars.md)–[015](015_nine_dimensions_labels_and_winding.md). The user asked whether some compactification forces one fermionic string to have its three spatial dimensions "as if it were a dot", needed only for the charged-lepton fermionic strings, and wanted it treated in a note separate from 015. The user added that the property could be introduced ad hoc on the worldsheet by setting three of the coordinates equal along the string, and expected that better methods exist after forty years. The D-brane statements of section 3 are quoted from memory. Two web searches confirmed the abstracts of two of the references; no paper was re-read. The lattice statements are computed by the script of section 6. No second model reviewed this entry.

**Units.** Masses appear through α′M² with ħ = c = 1, and radii through r = R²/α′, as in 015.

## 1. Question

Can a compactification, or a consistent worldsheet construction, force a fermionic string to have no extension in the noncompact spatial directions? Can it do so only for the strings with the labels of charged leptons?

## 2. Two meanings of "a dot"

- **(a) Shape.** The string has no classical extension and no position or momentum of its own in the noncompact directions. Its length lies in the internal space, and its location is that of the object it ends on.
- **(b) Size.** Its measured size is far below the hadronic string length.

Boundary conditions and compactification give (a). They give (b) only if a second scale enters.

The ad hoc constraint X^i(σ,τ) = x^i(τ) for three coordinates removes oscillators that the cancellation of the conformal anomaly needs. I know no consistent string with that constraint on the whole worldsheet. The consistent substitutes act on the ends of the string or on the background.

## 3. Mechanisms

### P1. Pinned strings: mixed boundary conditions

Recalled from the D-brane literature:

- An open string between a D-particle and a D8-brane has Dirichlet conditions at one end and Neumann conditions at the other in eight directions. Its oscillators in those directions are half-integer moded, so it has no position or momentum of its own there. The lowest bosonic state has α′m² = 1/2. The only state without mass is one fermionic mode per D8-brane. The string is purely fermionic and sits on the D-particle.
- Quantizing these fermionic modes for m D8-branes on an orientifold plane gives the spinor of SO(2m). In heterotic variables the D-particle is a string wound once around the circle. These are the winding states and the "winding labels" of 015 (Bachas, Green and Schwimmer; Bergman, Gaberdiel and Lifschytz; Danielsson and Ferretti).
- The same boundary conditions occur for the strings that end on a wrapped fivebrane in Witten's baryon vertex. They are fermionic, which makes the vertex antisymmetric, and their number is fixed by the flux through the wrapped cycle.
- With six mixed directions the massless states are also fermions only, but the intersection then extends in space.

So the consistent version of "a fermionic string that is a dot" is a string with one end on a point-like brane. It carries one label, the label of the brane at its other end.

### P2. Lattice check: single-label wound strings

- **SU(18) point** (all sixteen labels at folded Wilson-line value 1/4, r = 1/4). The 32 massless states of winding +1 are roots ℓ_a − ℓ_b of SU(18) with exactly one of a, b a winding label. With the charge generator diag(0; sixteen label charges; 0), which is traceless because the sixteen charges sum to zero (014 B6), they are

  | states | content | charge |
  |---|---|---|
  | 6 | one coloured label, (u,c) | 2/3 |
  | 9 | one coloured label, (d,s,b) | −1/3 |
  | 1 | the label n | −1 |
  | 16 | the corresponding anti-labels | −2/3, 1/3, 1 |

  Fifteen are quark-like colour triplets and one is charged-lepton-like. Each is a point with one string attached, in the picture of P1.
- **E8 × SO(18) point.** Single labels appear at winding two, as the vector of SO(14) (015 N3), and as massive members of the spinor of SO(18): nine single (d,s,b) labels at α′M² = 1/2 (015 N7).
- **E7 × SO(20) point.** The lightest massive winding states are the spinor of SO(20) at α′M² = 1, with an even number of the ten labels. No single-label wound state appears there.

### S1. Stretched strings: a Wilson line proportional to electric charge

Take A = (3/2)Q on the sixteen labels. Its folded values are 0 for the six (u,c) labels and 1/2 for the nine (d,s,b) labels. The label n has folded value 1/2 if its charge is −1 and 0 if its charge is 0.

- The holonomy on a state of charge Q is (−1)^(3Q). Among the 480 two-label states of SO(32):

  | \|Q\| | states | status |
  |---|---|---|
  | 0 | 102 | massless |
  | 1/3 | 120 | lifted |
  | 2/3 | 90 | massless |
  | 1 | 108 | lifted |
  | 4/3 | 48 | massless |
  | 5/3 | 12 | lifted |

  A two-label state is lifted exactly when 3Q is odd, with the common mass α′M² = 1/(4r).
- Of the 24 colour-singlet meson-like labels of five flavours, the 12 neutral ones stay massless and the 12 of charge ±1 are lifted. These are the twelve neutral and twelve charged slepton-like labels of 012 R1.
- With charge −1 for n the vacuum is the E7 × SO(20) point of 015 when r = 1/4. With charge 0 for n it is the E8 × SO(18) point when r = 1/8.
- In the type I′ picture, as I recall it, the D8-branes of charge 2/3 sit on one orientifold plane and those of charge −1/3 on the other. A lifted state is an open string stretched across the whole interval: its length lies in the compact direction. An unlifted state has both ends on the same stack.
- In field-theory terms the lifted states are the massive multiplets of the breaking SO(32) → SO(12) × SO(20), elementary and point-like in the same sense as a W boson.

### What these mechanisms leave open

- **Size.** In a flat internal space a pinned or stretched string still has the string length as its size in the noncompact directions, the same as its bosonic partner. A gap between a hadronic size and a lepton size needs the string to sit where its effective tension is large, as in a warped throat (Polchinski and Strassler, recalled), or a confining potential on the worldsheet, as in plane-wave backgrounds. This is the open problem of [007](007_pointlike_current_mechanism.md) and of the state file, unchanged.
- **Partners.** With sixteen supercharges each state above is a full multiplet. The string of P1 is fermionic as a string, and the D-particle it sits on carries both statistics.
- **Masses.** At these points the stretched states have string-scale masses. Light charged states need a small separation of the two stacks, away from the points of maximal symmetry.
- **Dimension.** Everything here is in nine dimensions. A reduction to four keeps these statements while the D-particle stays a particle and the D8-branes fill the three noncompact directions.

## 4. Reading for the sBootstrap

1. A fermionic string that is a dot exists in this setting as a one-label object: one end on a label brane, the other on a point. For the fifteen coloured labels it is quark-like, and for n it is charged-lepton-like. The notebook's working picture of a lepton is a two-label fermionic string, so this is a different assignment, closer to 012 R6, where n was read as a lepton-like label.
2. For two-label states, stretching selects the charged ones. A Wilson line that follows charge lifts the twelve charged slepton-like labels and leaves the twelve neutral ones, with no further input.
3. Both mechanisms give the dot in sense (a). Sense (b) stays open. The new element is that the fermionic string is pinned, so its size is tied to that of the object it ends on.

## 5. Open points

- Check the statements of P1 against the sources, in particular the fermionic spectrum of the strings between a D-particle and a D8-brane and its relation to the single-label states of P2.
- As I recall, a D-particle in a region of Romans mass k must carry |k| strings, and between two orientifold planes holding m and 16 − m D8-branes the Romans mass is m − 8. That would give one string in a (7 | 9) vacuum and two in a (6 | 10) vacuum. Not verified and not compared with the lattice.
- A supersymmetry breaking that keeps the fermionic member light and lifts its partners.
- A background in which the pinned or stretched string sits at large effective tension.
- The reduction to four dimensions on the five-dimensional space the user expects, CP² × S¹: which wrapped branes are particles there, and how many mixed directions their strings have.
- The charge and statistics of the single-label states at the SU(18) point as members of vector multiplets.

## 6. Files and reproduction

[`scripts/nine_dim_frames/charge_wilson_line.py`](../scripts/nine_dim_frames/charge_wilson_line.py) writes [`calculations/nine_dim_frames/charge_wilson_line.txt`](../calculations/nine_dim_frames/charge_wilson_line.txt). Exact arithmetic, a few seconds, same lattice and conventions as the script of 015. Part A gives the gauge groups for A = (3/2)Q and the table of S1. Part B gives the single-label states of P2. The consistency checks are the gauge groups E7 × SO(20) and E8 × SO(18), which agree with 015, and the Cartan matrix of the SU(18) chain.

## 7. Status

- **Known, recalled and unchecked here:** the spectrum of strings with eight mixed directions; D-particles of type I′ as heterotic winding states (Bachas, Green and Schwimmer, JHEP 01 (1998) 006, arXiv:hep-th/9712086; Bergman, Gaberdiel and Lifschytz, Nucl. Phys. B 524 (1998) 524, arXiv:hep-th/9711098; abstracts confirmed by search); the baryon vertex; Wilson lines as brane separation; warping as the source of point-like hard scattering.
- **New in this notebook, unreviewed:** the observation that A = (3/2)Q lifts exactly the states with odd 3Q, the 12 + 12 split of the meson-like labels, and its identification with the E7 × SO(20) and E8 × SO(18) points; the table of single-label wound states at the SU(18) point with the traceless charge.
- **Conditional:** every identification of labels with flavour, colour and charge, and the type I′ reading.
- **Open:** the size, sense (b).
