# Current research state

Last updated 12 October 2026 for the conversation begun on 11 October. This is a handoff summary, not a verbatim transcript.

## Goal

Investigate **two physical fermionic endpoints bound through a fermionic color carrier**, and whether the resulting odd state can have approximately pointlike whole-state scattering. The user clarified that the binding carrier replaces bosonic glue; a preformed meson plus an inert neutral spectator was assistant drift. For a retained adjoint carrier the endpoint pair is an octet, not an ordinary color-singlet meson. The quark–diquark branch and the original comparison with bosonic string behavior remain longer-term targets.

**Current result:** [blackboard 005](../blackboard/005_fermionic_binding_and_seiberg.md) constructs a finite-range contact Hamiltonian of q, qbar and an active adjoint fermion. In its global-color, fixed-number singlet sector, a variational proof gives E₃≤2ε₂<ε₂ below dimer breakup, without a direct q qbar force. It establishes a restricted binding example; its coupling, UV completion, flux tube and pointlike scattering are not derived. The same entry supplies the SQCD component dictionary and flavor-phase choices requested by the user's Seiberg-duality suggestion. See [progress](progress.md) and the [idea bank](../blackboard/ideas.md).

The user explicitly wants active research rather than a restriction to the simplest flat Ramond-string construction. Alternative dual strong theories and Kaluza–Klein geometry are in scope.

The user also frames this as frontier-model-assisted research, naming GPT Astra and future models. The objective is useful new physics, with honest provenance and novelty assessment. Script counts, benchmark anecdotes, and repeated known identities are not substitutes for a result.

## User decisions and clarifications

- Keep readable notes in this repository for later agents, at two levels: curated `notes/` and a working `blackboard/`.
- Keep milestones short and cross them with results. Store half-baked ideas separately with objections and revival conditions, without favoring orthodoxy or agreement with the user.
- The fermion is to participate in binding the endpoints. Distinguish exchange with endpoint conversion from a retained binding constituent; neither is an inert spectator. Seiberg duality / a super-QCD string is now an explicit avenue.
- The two uploaded Markdown conversations are references. Copies have been preserved unchanged and their SHA-256 hashes recorded.
- “Non-Dirac quarks” in an earlier message was a typo. The intended quarks are **non-chiral in gauge representation, Dirac quarks**.
- A chiral weak sector need not be constructed at this stage. This does not remove the need for approximate global chiral flavor symmetry if the pion's Goldstone mechanism is to be reproduced.
- Consider a dual description of QCD-like dynamics and a geometric route based on CP² × S¹, including the spinᶜ/bundle ingredients necessary to make it meaningful.
- Physical motivation: bosonic statistics permit a classical/coherent field associated with binding; the user suspects the absence of an analogous fermionic field could restrict its effect to contact and conceal the fermionic string. This is a working hypothesis to refine and test, not an established implication of statistics.
- The user requested an independent PRD-style reconstruction before supplying the previous preprints. That version is preserved at `333e537`. The PRL, PRD, and addendum PDFs have now arrived, been preserved, extracted, and compared; the original reconstruction PDF/source is unchanged. It used the earlier detailed conversations, so it was not a blind rediscovery experiment.
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

Can a completion of the demonstrated fermion-only contact interaction connect a two-fermion-plus-adjoint bound state to a controlled dual description and ultimately the desired scattering behavior? In SQCD, H=(ψtilde Tᵃψ)λᵃ shares the mesino's exact charges, but its overlap is uncalculated and depends on the operator prescription. The usual mesino ψ_M=φtilde ψ+ψtilde φ must not be relabeled as the proposed constituent structure.

The correct target is a calculation of current matrix elements, relevant spectral weights/gaps, and hard scattering. A missing classical fermionic mean field by itself does not remove bosonic exchanges, form-factor corrections, or Regge states from fermion scattering.

The [independent manuscript](../manuscript/README.md) remains the historical reconstruction, not a revision incorporating this correction. Earlier colorless-carrier and elementary/composite mixing examples are comparisons, not the active binding ansatz. The [workplan](workplan.md) prioritizes matching an explicit completion to the contact interaction, then its current. SU(3),N_f=4 offers an s-confining SQCD laboratory; those extra flavors serve phase control, not an explanation of weak generations.

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
- [Flat/radial calculations](../scripts/scattering_checks.py): six check groups recorded in [results.json](../calculations/results.json).
- [Geometry/representation calculations](../scripts/geometry_checks.py): seven check groups recorded in [geometry_results.json](../calculations/geometry_results.json).
- [Fermion exchange calculations](../scripts/fermion_exchange_checks.py): propagator, spatial kernel, contact expansion, and coupled-channel checks; output in [fermion_exchange_results.json](../calculations/fermion_exchange_results.json).
- [Branch and mixing checks](../scripts/branch_checks.py): five check groups, including 32 numerical mass/current diagonalizations; output in [branch_results.json](../calculations/branch_results.json).

The original conversation copies remain unchanged. The [previous PRL/PRD/addendum PDFs](../references/received-2026-10-12/README.md) are now available; source archives and other mentioned images remain absent. Luna performed native PDF text extraction, without OCR. The reuploaded `fermion_force_mediation.md` is byte-identical to the earlier copy.

Network retrieval was restored after the user enabled full access. Seiberg's paper, FunSearch, the 6 October OpenAI mathematics release and its pinned repository README, and selected September AI-assisted physics papers were retrieved; Schwarz's bibliographic metadata and abstract were verified. See the [reading record](../references/literature_2026-10-12.md). This is a selective update, not a comprehensive survey or independent verification of the reported new proofs/calculations. The supplied drafts' other recent citations and experimental numbers remain unchecked.

## Persistence

The original notebook checkpoint `2ab95a4` is committed and pushed to `origin/work`. The manuscript and follow-up notes are maintained on that same branch. The user asked for both commits and pushes. Use `git status`, `git log`, and the remote ref to establish whether a particular later version is published; do not assume `main` contains the work. The [remote notebook](https://github.com/arivero/chatpublic/tree/work/discussions/2026-10-11-quark-antiquark-open-string) is the shared reading location.
