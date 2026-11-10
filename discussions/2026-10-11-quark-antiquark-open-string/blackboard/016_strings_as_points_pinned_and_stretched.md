# Strings that are points in the noncompact directions: pinned, wound and stretched

10 November 2026. Blackboard entry: answer to a question of the user, built from recalled string-theory facts and two lattice checks. Unreviewed.

**Provenance.** Written by Claude (model Fable 5.2) in the same Claude Code session as [012](012_so32_gauge_field_scalars.md)–[015](015_nine_dimensions_labels_and_winding.md). The user asked whether some compactification forces one fermionic string to have its three spatial dimensions "as if it were a dot", needed only for the charged-lepton fermionic strings, and wanted it treated in a note separate from 015. The user added that the property could be introduced ad hoc on the worldsheet by setting three of the coordinates equal along the string, and expected that better methods exist after forty years. The D-brane statements of section 3 are quoted from memory. Two web searches confirmed the abstracts of two of the references; no paper was re-read. The lattice statements are computed by the script of section 6. No second model reviewed this entry. The paragraphs on size were rewritten on 11 November, after the user objected that size is no issue for a string that is a point in the three spatial dimensions.

**Units.** Masses appear through α′M² with ħ = c = 1, and radii through r = R²/α′, as in 015.

## 1. Question

Can a compactification, or a consistent worldsheet construction, force a fermionic string to have no extension in the noncompact spatial directions? Can it do so only for the strings with the labels of charged leptons?

## 2. Two meanings of "a dot"

- **(a) Shape.** The string has no classical extension and no position or momentum of its own in the noncompact directions. Its length lies in the internal space, and its location is that of the object it ends on.
- **(b) Size.** Its measured size in the noncompact directions.

Boundary conditions and compactification give (a). For a string with property (a), the size (b) is the zero-point motion of its vibration modes, which depends on the tension of the string alone (section 3, "Size").

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

- **Size.** A string that is a point in the noncompact directions classically still vibrates there quantum mechanically. Each transverse vibration mode is a harmonic oscillator, and its ground state has zero-point motion. For a string of tension T stretched over a length L, mode n has frequency ω_n = nπc/L and effective mass TL/(2c²), so its zero-point amplitude is ⟨q_n²⟩ = ħ/(2mω_n) = ħc/(πTn), independent of L. A point of the string is therefore displaced from the classical position by ⟨(X − x)²⟩ = (ħc/2πT) Σ_{n ≤ N} 1/n = α′ Σ_{n ≤ N} 1/n per direction, with α′ the slope of that string in units ħ = c = 1 and N the number of modes that a probe is fast enough to resolve. This spread is the same for a stretched, a wound and a pinned string, and the internal length of the string does not enter. It is the effect that gives a flux tube its width. Equivalently, the first vibrational excitation costs 1/α′ in M², and a probe below that energy sees a point. For the fundamental string of this setting the spread is far below any measured bound, so these states are point-like for every practical purpose. The user made this point against the first wording of this entry, which called the size an open problem. The size becomes a problem only if the same string is required to have the hadronic slope, α′ ≈ 0.9 GeV⁻²: the spread is then about 0.2 fm, some 10⁴ times the length of about 2 × 10⁻⁵ fm that corresponds to the limits on contact interactions of charged leptons, near 10 TeV as I recall.
- **Relation to zitterbewegung** (a question of the user). The trembling of a Dirac particle has amplitude ħ/2mc, about 190 fm for the electron, and the electron is still a point in scattering. So the amplitude of a trembling does not decide whether a state looks point-like. What decides is what the trembling can turn into. Zitterbewegung belongs to the spin part of a structureless particle; its only excitation is pair creation at 2mc², which enters the scattering of the electron through loops, at relative order α. The vibration above belongs to shape modes, which a point particle lacks. Exciting one gives a single-particle state of the same charge, higher spin and M² higher by 1/α′, produced and exchanged at tree level with the coupling of the ground state. The amplitude is then the point-particle one times Γ(1 − α′s)Γ(1 − α′t)/Γ(1 − α′s − α′t), whose Regge limit exp(α′ t ln α′s) is the sum α′ Σ 1/n above. In the superstring the two are relatives: the zero modes of the worldsheet fermions are the Dirac matrices and give the zitterbewegung, and the non-zero modes give the shape vibration. The test for a physical size is therefore the existence of excited states at spacing 1/α′. With the hadronic slope the first excited charged lepton, of spin 3/2, would lie near 1 GeV.
- **The hadronic length.** With a fundamental string every massless state is point-like, the scalar partners included. The size of the mesons, 0.66 fm for the charged pion, has to enter somewhere, and for the bosonic states only. This is the problem of [007](007_pointlike_current_mechanism.md) and of the state file seen from the other side. The pinned string of P1 has the right asymmetry, since its only light state is fermionic. The stretched string of S1 does not, since both partners are stretched.
- **Partners.** With sixteen supercharges each state above is a full multiplet. The string of P1 is fermionic as a string, and the D-particle it sits on carries both statistics.
- **Masses.** At these points the stretched states have string-scale masses. Light charged states need a small separation of the two stacks, away from the points of maximal symmetry.
- **Dimension.** Everything here is in nine dimensions. A reduction to four keeps these statements while the D-particle stays a particle and the D8-branes fill the three noncompact directions.

## 4. Reading for the sBootstrap

1. A fermionic string that is a dot exists in this setting as a one-label object: one end on a label brane, the other on a point. For the fifteen coloured labels it is quark-like, and for n it is charged-lepton-like. The notebook's working picture of a lepton is a two-label fermionic string, so this is a different assignment, closer to 012 R6, where n was read as a lepton-like label.
2. For two-label states, stretching selects the charged ones. A Wilson line that follows charge lifts the twelve charged slepton-like labels and leaves the twelve neutral ones, with no further input.
3. Both mechanisms give a state that is a point in the noncompact directions, with a spread set by the fundamental string length. What stays open is the origin of the hadronic length of the bosonic partners.

## 5. Open points

- Check the statements of P1 against the sources, in particular the fermionic spectrum of the strings between a D-particle and a D8-brane and its relation to the single-label states of P2.
- As I recall, a D-particle in a region of Romans mass k must carry |k| strings, and between two orientifold planes holding m and 16 − m D8-branes the Romans mass is m − 8. That would give one string in a (7 | 9) vacuum and two in a (6 | 10) vacuum. Not verified and not compared with the lattice.
- A supersymmetry breaking that keeps the fermionic member light and lifts its partners.
- Where the hadronic length enters for the bosonic partners. If one insists instead on a single string with the hadronic slope, a background is needed in which the pinned or stretched string sits at large effective tension (a warped throat, or a plane-wave potential on the worldsheet).
- The reduction to four dimensions on the five-dimensional space the user expects, CP² × S¹: which wrapped branes are particles there, and how many mixed directions their strings have.
- The charge and statistics of the single-label states at the SU(18) point as members of vector multiplets.

## 6. Files and reproduction

[`scripts/nine_dim_frames/charge_wilson_line.py`](../scripts/nine_dim_frames/charge_wilson_line.py) writes [`calculations/nine_dim_frames/charge_wilson_line.txt`](../calculations/nine_dim_frames/charge_wilson_line.txt). Exact arithmetic, a few seconds, same lattice and conventions as the script of 015. Part A gives the gauge groups for A = (3/2)Q and the table of S1. Part B gives the single-label states of P2. The consistency checks are the gauge groups E7 × SO(20) and E8 × SO(18), which agree with 015, and the Cartan matrix of the SU(18) chain.

## 7. Status

- **Known, recalled and unchecked here:** the spectrum of strings with eight mixed directions; D-particles of type I′ as heterotic winding states (Bachas, Green and Schwimmer, JHEP 01 (1998) 006, arXiv:hep-th/9712086; Bergman, Gaberdiel and Lifschytz, Nucl. Phys. B 524 (1998) 524, arXiv:hep-th/9711098; abstracts confirmed by search); the baryon vertex; Wilson lines as brane separation; warping as the source of point-like hard scattering.
- **New in this notebook, unreviewed:** the observation that A = (3/2)Q lifts exactly the states with odd 3Q, the 12 + 12 split of the meson-like labels, and its identification with the E7 × SO(20) and E8 × SO(18) points; the table of single-label wound states at the SU(18) point with the traceless charge.
- **Conditional:** every identification of labels with flavour, colour and charge, and the type I′ reading.
- **Open:** where the hadronic length enters for the bosonic partners.
