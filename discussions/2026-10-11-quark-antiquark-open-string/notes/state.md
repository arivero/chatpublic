# Current research state

Last updated 12 October 2026 for the conversation begun on 11 October. This is a handoff summary, not a verbatim transcript.

## Goal

Find a mechanism making the **whole fermionic color string** approximately pointlike in scattering while the bosonic string remains extended. The user's controlling assignment is meson = bosonic string q/qbar, diquark = bosonic string q/q, lepton = fermionic string q/qbar, and quark = fermionic string qbar/qbar. The selected total colors are 1, anti-3, 1 and 3; internal SU(3) flux does not make the meson or lepton colored. A preformed meson plus an inert spectator and the later promotion of a contact trimer to the main goal were both assistant drift.

**Current result:** [007](../blackboard/007_pointlike_current_mechanism.md) and the living paper calculate a conditional whole-mode elastic-current hierarchy using different warped radial profiles. At Q=10Λ_had, a c=1 fermion profile reaches F_F²=0.99 at Λ_UV/Λ_had≈2888.50, with F_B≈0.0399872 for the extended comparison profile. A second analytic test shows that weaker localization cannot achieve this efficiently and that c≥1/2 needs a physical UV boundary/completion. This is one assumed current, not a derived common string, full scattering matrix or experimental bound. Next derive the boundary mode and both sector profiles within a common string or Seiberg-dual dictionary, then test another observable. See [progress](progress.md) and the [idea bank](../blackboard/ideas.md).

[005](../blackboard/005_fermionic_binding_and_seiberg.md) proves binding in a restricted global-color, fixed-number contact Hamiltonian; [006](../blackboard/006_scalar_completion_test.md) matches a scalar completion and excludes its weak, far-detuned binding regime. These remain useful supporting calculations, now in paper appendices.

The user explicitly wants active research rather than a restriction to the simplest flat Ramond-string construction. Alternative dual strong theories and Kaluza–Klein geometry are in scope.

The user also frames this as frontier-model-assisted research, naming GPT Astra and future models. The objective is useful new physics, with honest provenance and novelty assessment. Script counts, benchmark anecdotes, and repeated known identities are not substitutes for a result.

## User decisions and clarifications

- Keep readable notes in this repository for later agents, at two levels: curated `notes/` and a working `blackboard/`.
- Keep milestones short and cross them with results. Store half-baked ideas separately with objections and revival conditions, without favoring orthodoxy or agreement with the user.
- Update the living paper and built PDF after each research step; notebook updates alone do not complete a step.
- The fermion is to participate in binding the endpoints. Distinguish exchange with endpoint conversion from a retained binding constituent; neither is an inert spectator. Seiberg duality / a super-QCD string is now an explicit avenue.
- The two uploaded Markdown conversations are references. Copies have been preserved unchanged and their SHA-256 hashes recorded.
- “Non-Dirac quarks” in an earlier message was a typo. The intended quarks are **non-chiral in gauge representation, Dirac quarks**.
- A chiral weak sector need not be constructed at this stage. This does not remove the need for approximate global chiral flavor symmetry if the pion's Goldstone mechanism is to be reproduced.
- Consider a dual description of QCD-like dynamics and a geometric route based on CP² × S¹, including the spinᶜ/bundle ingredients necessary to make it meaningful.
- Physical motivation: bosonic statistics permit a classical/coherent field associated with binding; the user suspects the absence of an analogous fermionic field could restrict its effect to contact and conceal the fermionic string. This is a working hypothesis to refine and test, not an established implication of statistics.
- The user requested an independent PRD-style reconstruction before supplying the previous preprints. Version 0.1 is preserved in Git at `333e537`; the current paper evolves as version 0.2. The PRL, PRD, and addendum PDFs have arrived, been preserved, extracted, and compared. The reconstruction used the earlier detailed conversations, so it was not a blind rediscovery experiment.
- The historical target is Schwarz's 1971 *Dual quark-gluon model of hadrons*, with related early work involving Joel Scherk to identify. The user provided this title; the primary text has not been retrieved here.
- On 12 October the user explicitly requested pushing, in addition to commits. The first notebook checkpoint is published on `origin/work`; `main` remains unchanged.
- The user asks to build flavor/generation content in stages: explain what each addition is needed for, and retain useful models with fewer flavors. Do not attempt the complete three-generation Standard Model as one indivisible target.
- The user cautions against Python scripts that merely recheck known results and against reward hacking. Use new numerical work only for a concrete quantitative need; delegate routine justified scripts and PDF extraction to a smaller model, save outputs to disk, and keep reports concise. The earlier 24 check groups are reproducibility records, not discoveries.

## Supported results, with scope

1. **Ordinary QCD operator parity.** A local/bilocal meson interpolator `qbar W q`, with a bosonic QCD Wilson line, has even fermion parity. An odd candidate needs additional structure. Exact duality preserves parity but may represent an odd sector using nonlocal/disorder variables.
2. **Flat-string benchmark.** In the specified charged massless open-superstring embedding, the same-sign disk amplitude has `M = M_point V(t,u)`. Its first oscillator correction is dimension eight. Corresponding NS amplitudes share the string factor in that simple sector.
3. **Conditional scale obstruction.** Assigning that benchmark the slope 0.9 GeV⁻² gives a cross-section ratio 9.2763 × 10⁻⁵³ at 10 GeV and 90°. This is not a theorem about every QCD string dual.
4. **Radial toy average.** The transcript's positive hard-wall average with ν = 2 gives 1.3149 × 10⁻⁶ for the same ratio. The integral is checked; its derivation from a complete physical compactification is absent. Under a positive amplitude-weight ansatz, 1% agreement limits the hadronic weight to about 0.5% at that energy. This is not a Fock-space probability bound.
5. **Dirac quarks and pions.** Massless vectorlike Dirac quarks have global chiral flavor symmetry. Its spontaneous breaking and small explicit Dirac masses allow the usual pion mechanism without gauged weak interactions.
6. **CP² geometry.** Ordinary scalar harmonics have representations (p,p), hence no triplet. Line bundles and appropriate spinᶜ Dirac operators admit triplet zero modes. CP² × S¹ is non-spin; the product circle does not cure it. The spinᶜ connection and its charge lattice are extra physical data.
7. **KK limitations.** Circle zero modes can support four-dimensional Dirac fields, but assigning up/down electric charges to ordinary nonzero circle momenta generically gives large KK masses. A complete bundle/gauge embedding, light spectrum, and background remain missing.
8. **Fermionic coherence versus propagation.** Fermion parity prevents a conventional c-number expectation value of a fermionic field, but not a nonlocal two-point function. Allowed fermion exchange conserves angular momentum and can generate finite-range off-diagonal interactions. Contact behavior requires an appropriate gap/low-momentum limit or an auxiliary-field construction; it does not follow from exclusion statistics.
9. **Two-branch charge accounting.** With conventional separately conserved B and L, an antidiquark-to-quark carrier needs `(B,L)=(1,0)`, whereas a meson-to-lepton carrier needs `(0,1)`. One fixed carrier cannot fill both roles. If only B−L is preserved, the antilepton orientation can align the shifts; this is a different charge assumption requiring explicit dynamics.
10. **Pauli and mixing checks.** The S-wave scalar color-3 antidiquark is flavor antisymmetric: 3 components for Nf=3 and 10 for Nf=5. In a restricted elementary/composite mixing model with diagonal probe currents, the light radius is suppressed by a composite fraction η and a vector-induced four-fermion coefficient by η². This demonstrates a weak dressing correspondence, not an emergent wholly composite pointlike fermion.
11. **Flavor stages.** Two light Dirac flavors suffice for the non-Abelian pion symmetry and a charged/neutral meson branch. Full scalar-antidiquark flavor closure with one flavor-singlet carrier instead selects Nf=3 through `Λ²(3bar)=3`; a neutral carrier also requires the three endpoint charges to sum to zero. This is a conditional reason to add a strange-like flavor, not an explanation of three weak generations. Lower-flavor alternatives can change the spin/carrier assumptions.
12. **Draft review and radial boundary case.** The supplied PRL beta-function prefactor and PRD alternating pole-residue sign need correction. The addendum's Eq. (111) is correctly positive in the PDF; text extraction loses its absolute-value bars. The omitted b=2 case of its finite-cutoff ansatz gives an intermediate `δ² log(1/δ)` amplitude deficit, derived analytically. This completes a toy formula, not a physical background or a novelty claim.

## Current research conjecture

Can one string or controlled dual construction derive an ultraviolet-concentrated fermionic mode and an extended bosonic mode with the specified endpoints? The warped overlap calculation makes the needed hierarchy quantitative. It does not yet explain the UV boundary or exclude elementary-source admixture. In SQCD, H=(ψtilde Tᵃψ)λᵃ shares the mesino's exact charges, but its overlap is uncalculated and depends on the operator prescription. The usual mesino ψ_M=φtilde ψ+ψtilde φ must not be relabeled as the intended fermionic string.

The correct target is a calculation of current matrix elements, relevant spectral weights/gaps, and hard scattering. A missing classical fermionic mean field by itself does not remove bosonic exchanges, form-factor corrections, or Regge states from fermion scattering.

The [living manuscript](../manuscript/README.md) now leads with the corrected four-sector goal and both current tests. Earlier colorless-carrier and elementary/composite mixing examples remain comparisons; contact binding is supporting material. The [workplan](workplan.md) prioritizes a physical UV mode and common sector construction. SU(3),N_f=4 offers an s-confining SQCD laboratory; those extra flavors serve phase control, not an explanation of weak generations.

## Not yet established

- A complete dual of nonsupersymmetric QCD realizing the proposed identification.
- A compactification vacuum, flux/gauge embedding, and light up/down charge spectrum on CP² × S¹ or its proposed fibered variants.
- An operator dictionary for both the meson and the odd-parity hard-scattering state.
- A mechanism protecting approximate pointlike scattering well above the hadronic scale while reproducing the boson's pion/chiral and mesonic behavior.
- Current experimental limits specific to any completed model. No data fit was performed.

## Files and reproducibility

- [Conversation progression](conversation_log.md)
- [Version 0.1 validation record](validation.md)
- [Comparison with the supplied drafts](draft_comparison.md)
- [Flavor/generation scaffold](../blackboard/003_flavor_scaffolding.md)
- [Analytic draft corrections and radial boundary case](../blackboard/004_draft_equations.md)
- [AI research bibliography and October source update](ai_research_bibliography.md)
- [Research protocol and restrained computation](research_protocol.md)
- [Latest curated result on fermion exchange](fermion_exchange.md)
- [Working blackboard](../blackboard/README.md)
- [Finite-momentum current experiment](../calculations/warped_current_experiment.json), with [script](../scripts/warped_current_experiment.py) and [interpretation](../blackboard/007_pointlike_current_mechanism.md).
- [Flat/radial calculations](../scripts/scattering_checks.py): six check groups recorded in [results.json](../calculations/results.json).
- [Geometry/representation calculations](../scripts/geometry_checks.py): seven check groups recorded in [geometry_results.json](../calculations/geometry_results.json).
- [Fermion exchange calculations](../scripts/fermion_exchange_checks.py): propagator, spatial kernel, contact expansion, and coupled-channel checks; output in [fermion_exchange_results.json](../calculations/fermion_exchange_results.json).
- [Branch and mixing checks](../scripts/branch_checks.py): five check groups, including 32 numerical mass/current diagonalizations; output in [branch_results.json](../calculations/branch_results.json).

The original conversation copies remain unchanged. The [previous PRL/PRD/addendum PDFs](../references/received-2026-10-12/README.md) are now available; source archives and other mentioned images remain absent. Luna performed native PDF text extraction, without OCR. The reuploaded `fermion_force_mediation.md` is byte-identical to the earlier copy.

Network retrieval was restored after the user enabled full access. Seiberg's paper, FunSearch, the 6 October OpenAI mathematics release and its pinned repository README, and selected September AI-assisted physics papers were retrieved; Schwarz's bibliographic metadata and abstract were verified. See the [reading record](../references/literature_2026-10-12.md). This is a selective update, not a comprehensive survey or independent verification of the reported new proofs/calculations. The supplied drafts' other recent citations and experimental numbers remain unchecked.

## Persistence

The original notebook checkpoint `2ab95a4` is committed and pushed to `origin/work`. The manuscript and follow-up notes are maintained on that same branch. The user asked for both commits and pushes. Use `git status`, `git log`, and the remote ref to establish whether a particular later version is published; do not assume `main` contains the work. The [remote notebook](https://github.com/arivero/chatpublic/tree/work/discussions/2026-10-11-quark-antiquark-open-string) is the shared reading location.
