# Current research state

Last updated 12 October 2026 for the conversation begun on 11 October. This is a handoff summary, not a verbatim transcript.

## Goal

Investigate whether an open string with quark–antiquark endpoint structure can have a bosonic sector behaving as a standard meson and a fermionic sector whose whole-state hard scattering is approximately pointlike. The related two-antiquark/diquark branch may model quark-like states; its color and baryon-number accounting differs from the meson/lepton branch.

The user explicitly wants active research rather than a restriction to the simplest flat Ramond-string construction. Alternative dual strong theories and Kaluza–Klein geometry are in scope.

## User decisions and clarifications

- Keep readable notes in this repository for later agents, at two levels: curated `notes/` and a working `blackboard/`.
- The two uploaded Markdown conversations are references. Copies have been preserved unchanged and their SHA-256 hashes recorded.
- “Non-Dirac quarks” in an earlier message was a typo. The intended quarks are **non-chiral in gauge representation, Dirac quarks**.
- A chiral weak sector need not be constructed at this stage. This does not remove the need for approximate global chiral flavor symmetry if the pion's Goldstone mechanism is to be reproduced.
- Consider a dual description of QCD-like dynamics and a geometric route based on CP² × S¹, including the spinᶜ/bundle ingredients necessary to make it meaningful.
- Physical motivation: bosonic statistics permit a classical/coherent field associated with binding; the user suspects the absence of an analogous fermionic field could restrict its effect to contact and conceal the fermionic string. This is a working hypothesis to refine and test, not an established implication of statistics.
- The user requested an independent PRD-style reconstruction before supplying the preprint drafts referenced by the two transcripts. Preserve the resulting version before comparison; do not imply the missing drafts were read.
- The historical target is Schwarz's 1971 *Dual quark-gluon model of hadrons*, with related early work involving Joel Scherk to identify. The user provided this title; the primary text has not been retrieved here.
- On 12 October the user explicitly requested pushing, in addition to commits. The first notebook checkpoint is published on `origin/work`; `main` remains unchanged.

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

## Current research conjecture

Can a dual/geometric construction allow strong extended bosonic binding while suppressing the candidate fermion's coupling to the hadronic excitation spectrum? The latest suggestion is to investigate whether parity-changing transition structure helps cause that suppression.

The correct target is a calculation of current matrix elements, relevant spectral weights/gaps, and hard scattering. A missing classical fermionic mean field by itself does not remove bosonic exchanges, form-factor corrections, or Regge states from fermion scattering.

The [independent manuscript](../manuscript/README.md) gathers the constraints and candidate mechanisms into a research draft. The [workplan](workplan.md) prioritizes a complete operator dictionary and a minimal spectral/current/scattering calculation before a full dual or compactification construction. It distinguishes elementary hadronic dressing from the stronger intended theory.

## Not yet established

- A complete dual of nonsupersymmetric QCD realizing the proposed identification.
- A compactification vacuum, flux/gauge embedding, and light up/down charge spectrum on CP² × S¹ or its proposed fibered variants.
- An operator dictionary for both the meson and the odd-parity hard-scattering state.
- A mechanism protecting approximate pointlike scattering well above the hadronic scale while reproducing the boson's pion/chiral and mesonic behavior.
- Current experimental limits specific to any completed model. No data fit was performed.

## Files and reproducibility

- [Conversation progression](conversation_log.md)
- [Version 0.1 validation record](validation.md)
- [Latest curated result on fermion exchange](fermion_exchange.md)
- [Working blackboard](../blackboard/README.md)
- [Flat/radial calculations](../scripts/scattering_checks.py): six check groups recorded in [results.json](../calculations/results.json).
- [Geometry/representation calculations](../scripts/geometry_checks.py): seven check groups recorded in [geometry_results.json](../calculations/geometry_results.json).
- [Fermion exchange calculations](../scripts/fermion_exchange_checks.py): propagator, spatial kernel, contact expansion, and coupled-channel checks; output in [fermion_exchange_results.json](../calculations/fermion_exchange_results.json).
- [Branch and mixing checks](../scripts/branch_checks.py): five check groups, including 32 numerical mass/current diagonalizations; output in [branch_results.json](../calculations/branch_results.json).

The earlier primary-paper downloads and the 12 October INSPIRE metadata request were blocked by the network proxy. References are labeled as reading pointers where they were not retrieved. The paper PDFs, ZIPs, and images mentioned within the uploaded conversations were not supplied in this chat. The newly generated manuscript PDF is our reconstruction, not one of those missing documents.

## Persistence

The original notebook checkpoint `2ab95a4` is committed and pushed to `origin/work`. The manuscript and follow-up notes are maintained on that same branch. The user asked for both commits and pushes. Use `git status`, `git log`, and the remote ref to establish whether a particular later version is published; do not assume `main` contains the work. The [remote notebook](https://github.com/arivero/chatpublic/tree/work/discussions/2026-10-11-quark-antiquark-open-string) is the shared reading location.
