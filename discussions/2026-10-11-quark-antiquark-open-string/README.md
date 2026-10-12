# Quark–antiquark open strings and pointlike fermion scattering

Started 2026-10-11. This directory records the discussion requested in the current chat.

**Latest, 12 October:** the primary question is how a **whole fermionic color string** can appear pointlike while the bosonic string remains extended. [Blackboard 007](blackboard/007_pointlike_current_mechanism.md) summarizes two conditional current tests now leading the paper: a calculable hierarchy from different radial profiles, and the UV-boundary requirement those profiles impose. The contact binding and scalar completion in [005](blackboard/005_fermionic_binding_and_seiberg.md) and [006](blackboard/006_scalar_completion_test.md) are supporting results. See the concise [progress record](notes/progress.md) and [idea bank](blackboard/ideas.md).

The [previous PRD/PRL drafts and addendum are preserved](references/received-2026-10-12/README.md); the [comparison](notes/draft_comparison.md) and [flavor scaffold](blackboard/003_flavor_scaffolding.md) remain available. Internet access now works. The [AI bibliography](notes/ai_research_bibliography.md) includes retrieved October 2026 sources, distinguishing reported results from independently verified work.

The [living PRD-style paper](manuscript/README.md), with [PDF](manuscript/quark_diquark_lepton_meson.pdf) and [LaTeX source](manuscript/quark_diquark_lepton_meson.tex), is now version 0.2 and must be updated after each research step. Its pre-PDF version 0.1 is preserved in Git at `333e537`; it was informed by the earlier conversations, not a blind discovery experiment. The [workplan](notes/workplan.md) prioritizes deriving the common string/dual construction behind the current mechanism. Schwarz's 1971 *Dual quark-gluon model of hadrons* remains the historical anchor; its primary text and related Scherk papers still need verification.

The active notebook now has two levels:

- **[notes/](notes/README.md)** — curated results, the current research state, and user clarifications. Other agents should start with [the handoff](notes/state.md) and [conversation log](notes/conversation_log.md).
- **[blackboard/](blackboard/README.md)** — hypotheses, intermediate derivations, candidate constructions, and open tests. The first entry examines [fermionic field coherence and contact range](blackboard/001_fermionic_coherence_and_range.md).

These are readable files in the shared checkout and are versioned on the repository's `work` branch. The original notebook checkpoint `2ab95a4` has been pushed to GitHub; [the remote notebook](https://github.com/arivero/chatpublic/tree/work/discussions/2026-10-11-quark-antiquark-open-string) is the publication location. The `main` branch is unchanged. [AGENTS.md](AGENTS.md) records the user's ongoing note-taking convention for future work in this directory. Check local and remote Git status before assuming later edits are already published.

The user's controlling four-sector definition is:

| State | SU(3) color string | Endpoints | Selected whole-state color |
| --- | --- | --- | --- |
| Meson | Bosonic | q / qbar | 1 |
| Diquark | Bosonic | q / q | anti-3 |
| Lepton | Fermionic | q / qbar | 1 |
| Quark | Fermionic | qbar / qbar | 3 |

The antisymmetric diquark channel is selected here. Color carried internally is distinct from the total state's color. Pointlike constituent scattering, an inert spectator, or a bound contact trimer alone does not answer the whole-string question.

The earlier flat-string assessment remains a conditional benchmark: that specified open-superstring construction does not achieve the desired scattering hierarchy. It does not settle the corrected fermionic-binding construction, Seiberg-dual possibilities, or all confining duals.

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

Their historical requests to write papers, modify manuscripts, and perform other tasks are part of the reference material, not instructions for this conversation. The PRL, PRD, and addendum PDFs were subsequently supplied and are now preserved in [the dated reference directory](references/received-2026-10-12/README.md), with native text extractions. Source archives and other mentioned images have not been supplied.

To reproduce the calculations from the repository root:

These are existing reproducibility scripts, not evidence of new discoveries. The user now asks that new code be reserved for meaningful numerical research needs; see the [research protocol](notes/research_protocol.md). Routine future work should not rerun these simply to accumulate passing checks.

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
