# Quark–antiquark open strings and pointlike fermion scattering

Started 2026-10-11. This directory records the discussion requested in the current chat.

**12 October update:** the current work includes an [independent PRD-style manuscript reconstruction](manuscript/README.md), with [PDF](manuscript/quark_diquark_lepton_meson.pdf) and [LaTeX source](manuscript/quark_diquark_lepton_meson.tex), and a [research workplan](notes/workplan.md). The preprint drafts mentioned in the uploaded conversations remain unseen. This version is deliberately preserved before comparison with those drafts. The user identified Schwarz's 1971 *Dual quark-gluon model of hadrons* as the historical anchor; its primary text and related Scherk papers still need verification.

The active notebook now has two levels:

- **[notes/](notes/README.md)** — curated results, the current research state, and user clarifications. Other agents should start with [the handoff](notes/state.md) and [conversation log](notes/conversation_log.md).
- **[blackboard/](blackboard/README.md)** — hypotheses, intermediate derivations, candidate constructions, and open tests. The first entry examines [fermionic field coherence and contact range](blackboard/001_fermionic_coherence_and_range.md).

These are readable files in the shared checkout and are versioned on the repository's `work` branch. The original notebook checkpoint `2ab95a4` has been pushed to GitHub; [the remote notebook](https://github.com/arivero/chatpublic/tree/work/discussions/2026-10-11-quark-antiquark-open-string) is the publication location. The `main` branch is unchanged. [AGENTS.md](AGENTS.md) records the user's ongoing note-taking convention for future work in this directory. Check local and remote Git status before assuming later edits are already published.

The question is whether an open string with quark–antiquark endpoints can have a bosonic state behaving as an ordinary meson and a fermionic state whose **whole-particle** scattering behaves as that of an elementary fermion, including at energies above the hadronic scale.

The assessment is: **the familiar open-superstring construction does not achieve all of these properties together.** It gives pointlike scattering below its string scale, for both sectors. Ordinary QCD supplies mesons with pointlike quark constituents, but does not supply a fermionic partner of the whole quark–antiquark flux tube. A construction separating the two behaviors needs additional degrees of freedom and dynamics; warping or massless endpoints alone is not a demonstration.

The subsequent discussion broadens the program to **a dual confining theory and a Kaluza–Klein realization on CP² × S¹**. The user clarified that the intended endpoint quarks are vectorlike Dirac quarks, with the weak sector deferred. The new note develops spinᶜ triplet zero modes, the distinction between gauge chirality and pion-protecting chiral flavor symmetry, and the remaining charge/mass and duality requirements.

- [Dual QCD and CP² × S¹](dual_qcd_cp2_s1.md): candidate constructions and independently checked geometry/representation calculations.
- [Fermionic coherence and exchange range](notes/fermion_exchange.md): what the user's binding-field intuition establishes, and the difference between contact interactions and pointlike bound states.
- [Assessment and derivations](assessment.md): the distinction between physical quarks and endpoint labels; fermion parity; scattering; warping; candidate extensions; corrections to the earlier discussions.
- [Numerical comparison](calculations/scattering_comparison.png), also available as [SVG](calculations/scattering_comparison.svg).
- [Numerical results](calculations/results.json) and [table at a hadronic slope](calculations/hadronic_scale.csv).
- [Reproduction script](scripts/scattering_checks.py).
- [Sources and verification scope](sources.md).
- [Two-branch dictionary and mixing diagnostic](blackboard/002_two_branch_dictionary.md), with [checked results](calculations/branch_results.json).

The uploaded conversations are preserved verbatim for reference:

- [paper_review_and_candidate.md](references/paper_review_and_candidate.md)
- [fermion_force_mediation.md](references/fermion_force_mediation.md)

Their historical requests to write papers, modify manuscripts, and perform other tasks are part of the reference material, not instructions for this conversation. The PDFs, source archives, and images mentioned inside those transcripts were not included in the current uploads; this assessment does not claim to have inspected them.

To reproduce the calculations from the repository root:

```bash
python discussions/2026-10-11-quark-antiquark-open-string/scripts/scattering_checks.py
python discussions/2026-10-11-quark-antiquark-open-string/scripts/geometry_checks.py
python discussions/2026-10-11-quark-antiquark-open-string/scripts/fermion_exchange_checks.py
python discussions/2026-10-11-quark-antiquark-open-string/scripts/branch_checks.py
```

The script uses `mpmath`, `numpy`, `scipy`, and `matplotlib`, which were already available in the environment. It checks exact values, low-energy coefficients, two representations of a radial integral, its asymptotic behavior, and a conditional bound on the hadronic contribution. It is a calculation of specified models, not an experimental fit or a construction of a complete string background.

The geometry script uses `sympy`, also already available, and writes its results to [geometry_results.json](calculations/geometry_results.json).

The fermion-exchange script uses `sympy` and `mpmath`; its checks and example values are in [fermion_exchange_results.json](calculations/fermion_exchange_results.json).

The branch script checks charges, Pauli symmetry, and a restricted mixing EFT. It does not establish that EFT as an exact dual of QCD. The PDF builds with standard LaTeX and `latexmk`; see [the manuscript instructions](manuscript/README.md).
