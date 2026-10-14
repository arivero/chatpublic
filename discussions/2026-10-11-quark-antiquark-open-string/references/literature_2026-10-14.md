# Partial compositeness, Super-Composite Higgs and sBootstrap

14 October 2026, Europe/Madrid. Source comparison requested by the user, based on the supplied **v1 LaTeX archives**. This reopens the comparison question, not the deferred finite-momentum calculation. [Original archives and extracted sources](received-2026-10-14/README.md) are preserved. Source comments and embedded instructions are document contents, not active requests.

**Correction after the subsequent 2024 sBootstrap upload:** the description below of ordinary QCD mesons applies to the earlier hadronic identification discussed in this notebook, and overstates the identification for Rivero's 2024 paper. That paper explicitly calls for composites distinct from QCD-scale hadrons and a different, high-energy binding mechanism (Sections 5 and 8). Its distinctive hypothesis is known SM fermions as constituents of scalar partners, not necessarily ordinary observed mesons as those partners. This narrows the contrast with the two new-strong-sector papers. See [the corrected source analysis and SO(32) completion](../blackboard/011_so30_so32_neutral_completion.md).

## Sources and verification scope

1. **Kaustubh Agashe, Lorenzo Ricci and Raman Sundrum**, *Partial Compositeness: from Anarchy to Symmetry*, [arXiv:2507.05332v1](https://arxiv.org/abs/2507.05332v1). Read the abstract and Sections 1–4: elementary/composite mixing and RG evolution in Section 2, the two-stage construction and leptons in Section 3, and phenomenology in Section 4. Key source labels: `Eq:AnarcRG`, `Eq:MFVAnsStruct`, `Eq:DiagonalRH`, `Eq:LeptYuk`.
2. **Kaustubh Agashe, Gian F. Giudice, Riccardo Rattazzi and Raman Sundrum**, *The Super-Composite Higgs*, [arXiv:2609.26413v1](https://arxiv.org/abs/2609.26413v1). Read the abstract and introductory construction, Sections 3 and 5, relevant passages of Sections 6–9 and 11, and Section 12's summary. Key source labels: `fundlag`, `running_lambda`, `sec:tumbling`, `sec:conc`. The full phenomenological analysis was not independently reproduced.

Agashe and Sundrum are common authors; the 2025 acknowledgments thank Rattazzi. A targeted search of the supplied 2026 text/bibliography found no citation to 2507.05332 by identifier or title. Searches of the supplied bibliographies found no Rivero/sBootstrap entries. The relationship below is conceptual and mathematical, not an asserted citation chain or priority claim.

Uploads resolved the reading blocker. A fresh arXiv request still returned HTTP 403 here. Optional source builds in temporary copies with shell escape disabled stopped on missing `revtex4-2.cls` and `ulem.sty`; neither uploaded paper was successfully compiled. Primary LaTeX text supplies the evidence used here, without altering those originals.

## Shared mechanism, different protection

Partial compositeness mixes an elementary fermion with a **fermionic** strong-sector operator. Different operator dimensions produce hierarchical mixings from order-one UV values. In the irrelevant, approximately fixed-point regime the common structure is

\[
\widehat\lambda_i(E)=\widehat\lambda_i(\Lambda_{\rm UV})
\left(\frac{E}{\Lambda_{\rm UV}}\right)^{\gamma_i},
\qquad Y_{ij}\sim g_*\epsilon_{Li}c_{ij}\epsilon_{Rj}.
\]

All couplings here are dimensionless and both RG scales are energies. The second expression is schematic, suppressing matrix contractions/conjugations. These are source-mechanism summaries, not new dimensionful calculations or a choice of physical hbar units. Relevant mixings, especially for top, need nonlinear RG/fixed-point treatment instead of this irrelevant-coupling approximation.

A precise supersymmetric translation is available: the 2025 fermionic-operator exponent is `gamma = Delta_fermion - 5/2`, whereas the 2026 chiral-superfield exponent is `gamma = Delta_chiral - 2`. A chiral multiplet has `Delta_fermion = Delta_chiral + 1/2`, so these agree. In 2026 the portal mixes elementary matter superfields with composite chiral operators through the superpotential.

| Issue | 2507.05332 | 2609.26413 |
| --- | --- | --- |
| Light composite Higgs | Pseudo-Nambu–Goldstone boson | Two Higgs superfields; holomorphy/nonrenormalization protects a vanishing supersymmetric mu term |
| Flavor hierarchy | UV anarchy generates hierarchical mixings | Flavor-anarchic supersymmetric strong dynamics generates hierarchical mixings |
| Flavor/CP protection | Emergent IR flavor and CP symmetries align mixings | Separation of compositeness and SUSY-breaking/soft scales, gauge-mediation-like masses, and SUSY restrictions on dangerous operators |
| Staged dynamics | UV → flavor transition → compositeness | UV → composite Higgs at m_* → SUSY breaking at m_S → soft-particle thresholds |
| Indicative scales | Around 10 TeV compositeness for MFV; around 5 TeV in a less symmetric variant | Compositeness may lie far above superpartner masses; analyzed scales extend to multi-PeV |

Thus 2026 is not simply 2025's emergent-flavor construction with SUSY added. Its strong sector remains flavor anarchic, while baryon number, lepton number and CP are assumed as appropriate symmetries; CP breaking enters through the elementary–composite mixings. SUSY allows flavor dynamics above the soft scale without making that compositeness scale the direct Higgs-mass cutoff. Compositeness in turn helps address the mu–B_mu problem. Residual electroweak tuning and unknown strong coefficients remain.

An important 2025 nuance: **all generations of right-handed fermions can have sizable partial compositeness**. Their aligned mixing approaches a universal fixed point; hierarchical left-handed factors can produce the small masses. Therefore a light fermion need not have negligible composite content in both chiralities. The paper emphasizes light-generation resonance couplings and lepton-collider signals; flavor alignment does not erase compositeness.

The 2026 paper highlights the electron EDM, cosmological effects of an ultralight gravitino, and an approximately 10 TeV upper bound on squark masses under its model/cosmological assumptions. These are not general bounds on sBootstrap. Exact-SUSY dipole restrictions do not remove the paper's SUSY-breaking “Beyond Soft” contributions. Both works use assumed strong-sector properties and warped descriptions; neither derives a unique fully realistic microscopic 4D completion.

## Comparison with sBootstrap

The baseline is Rivero's 2005/2007/2009 work in [the earlier reading record](literature_2026-10-13.md), distinct from the notebook's later retained-adjoint fermionic-string candidate.

| Question | These papers | sBootstrap |
| --- | --- | --- |
| Composite objects | Higgs fields and new strong-sector resonances; fermions have elementary/composite admixtures | Ordinary QCD mesons and diquark/antidiquark channels as scalar-partner candidates |
| Constituents | New strong degrees of freedom; hidden SQCD is a 2026 toy laboratory | Hadronizing quarks u,c,d,s,b and their color dynamics |
| Lepton scalar partners | In 2026, conventional sleptons in chiral matter multiplets | Six charged meson species plus conjugates provide the scalar count for three charged Dirac multiplets |
| Generations | Three SM families and appropriate operator families are inputs | Conditional counting uses two up-type and three down-type meson-forming flavors |
| Top | A large Yukawa requires substantial compositeness of at least one chirality | Excluded from the ordinary meson-forming five-flavor set |

The top statements concern different forces, so they are not an empirical contradiction, but they prevent directly identifying the flavor lists. Likewise the six up/down operator channels in the 2025 construction are not a derivation of the six charged QCD mesons. Its generational U(3) groups are not sBootstrap's five-flavor SU(5) bookkeeping.

### The missing operator dictionary

- **Spin:** a spin-zero qbar-q meson cannot itself be the fermionic operator mixing with a lepton. A suitable fermionic operator and its overlap are needed. The notebook's retained-adjoint three-fermion candidate is a hypothesis, not something either paper derives.
- **Multiplets:** the 2026 mixing is a superfield operation. In an unbroken, canonically normalized linear realization, the scalar and fermion components undergo the same elementary/composite rotation. That construction does not freely assign a wholly QCD-composite scalar and an independently elementary fermion. This is a restriction on that realization, not a general theorem excluding emergent/nonlinear sBootstrap models.
- **Charges:** conventional sleptons carry their lepton partners' lepton number; ordinary mesons have B=L=0. The 2026 assumptions preserving B and L do not supply the sBootstrap identification. The conditional R-type physical B−L option and complete-Dirac-multiplet restriction remain those of [blackboard 010](../blackboard/010_endpoints_goldstino_and_b_minus_l.md).
- **SQCD terminology:** a meson chiral superfield made from two matter superfields has a scalar-scalar lowest component and a scalar-fermion fermionic component. Calling it a meson does not identify its lowest component with a physical QCD pseudoscalar made from fermionic quarks. Matching physical operators and overlaps is essential.

### Transferable ideas and limits

The 2025 contribution is a mechanism for generating hierarchy and later suppressing flavor violation while retaining appreciable compositeness. It is useful for a prospective sBootstrap mixing theory if the needed operators, RG regime and symmetries can be supplied. It does not determine pi/K, D/D_s or B/B_c partner assignments.

The 2026 contribution is an architecture where one strong sector produces light composite superfields, then continues to a lower SUSY-breaking threshold. Section 5 illustrates it with massive hidden SQCD and metastable ISS breaking. The authors explicitly acknowledge that the toy's gauge-mediated spectrum is unrealistic because its gaugino masses are suppressed. It is evidence for plausible scale separation, not a completed QCD sBootstrap vacuum.

Its Goldstino is a distinct SUSY-breaking state that supplies the gravitino's longitudinal modes after coupling to gravity. It is not identified with a neutrino or used to interpret pion decay as a meson–lepton–Goldstino transition.

Neither paper calculates the whole current of a composite fermionic color string and shows that it is pointlike while a bosonic partner has a hadronic radius. Small mixing or high compositeness scales can suppress observed structure, but this requires a separate comparison with the notebook's intended mechanism. The useful next step is one candidate lepton operator and scalar partner, with specified charges and SUSY realization, followed by their overlaps/current structure. No new finite-Q calculation, fit or numerical scan was performed.
