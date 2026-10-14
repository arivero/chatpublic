# Quark–antiquark open strings and pointlike fermion scattering

Started 2026-10-11. This directory records the discussion requested in the current chat.

**2024 sBootstrap follow-up, 14 October 2026:** [SO(30), SO(32) and the missing neutral-sector selection](blackboard/011_so30_so32_neutral_completion.md), based on the user's supplied EPJC paper, corrects the earlier comparison's identification with QCD-scale hadrons. Paper v0.7 incorporates this source correction and conditional representation analysis.

**Targeted follow-up, 14 October 2026:** [comparison of the supplied partial-compositeness papers with sBootstrap](references/literature_2026-10-14.md), incorporated in paper v0.6. The user reopened this source question; the finite-momentum calculation remains deferred. [Original source archives and extracted files](references/received-2026-10-14/README.md).

**Cycle closed, 13 October 2026 (Europe/Madrid), pending new models.** The final physics consolidation is paper v0.5 at commit `210d0b4`; the remaining tasks below are a handoff for a future cycle, not running or scheduled work. The whole-fermion pointlike-scattering mechanism remains unresolved. The [chronological recap](notes/conversation_recap.md) records all 28 available substantive user turns.

Shared conversation links supplied by the user at closure:

- [This research conversation](https://chatgpt.com/s/cx_6acd8e76200c8191a4529d36db233c91).
- [Additional shared conversation](https://chatgpt.com/share/6acd8ea8-2e3c-83ed-8797-9c54344755e8).

These links are preserved as supplied; their contents were not newly retrieved or merged into the local transcript during closure. Uploaded originals remain archived separately under `references/`.

[Future-agent task prompts](delegation_prompts/README.md): seventeen bounded assignments, a common contract, and Sol's pinned audit of published openai/math prompt excerpts. The library covers active retained-adjoint calculations and the wider string/dual/geometric program; its creation does not execute those tasks.

**Latest, 13 October:** the user selects the retained adjoint fermion binding both fermionic endpoints through contact interactions, without a direct endpoint force, as the most interesting concrete model. The broader four-string goal remains. [Blackboard 008](blackboard/008_retained_adjoint_hbar.md) and the focused version 0.5 paper give the retained-adjoint results with explicit $\hbar$; [009](blackboard/009_anharmonic_radius.md) derives a positive leading anharmonic radius correction. [010](blackboard/010_endpoints_goldstino_and_b_minus_l.md) records a distinct, conditional scalar-endpoint and supersymmetry branch. The next quantitative task is the anharmonic finite-$Q$ current shape. See [progress](notes/progress.md).

The [previous PRD/PRL drafts and addendum are preserved](references/received-2026-10-12/README.md); the [comparison](notes/draft_comparison.md) and [flavor scaffold](blackboard/003_flavor_scaffolding.md) remain available. Internet access now works. The [AI bibliography](notes/ai_research_bibliography.md) includes retrieved October 2026 sources, distinguishing reported results from independently verified work.

The [living paper](manuscript/README.md), with [PDF](manuscript/quark_diquark_lepton_meson.pdf) and [LaTeX source](manuscript/quark_diquark_lepton_meson.tex), is now version 0.5. Version 0.2 is preserved in Git at `6b73d29`; the pre-PDF version 0.1 at `333e537`. New calculations keep physical $\hbar$ explicit, and the [workplan](notes/workplan.md) names the next calculation. [Focused source reading](references/literature_2026-10-13.md) documents Rivero prior art and the Volkov–Akulov source; the [1983 Greenberg–Mohapatra–Yasue assessment](references/greenberg_mohapatra_yasue.md) compares a different composite-fermion mass-protection mechanism. A [chronological recap](notes/conversation_recap.md) preserves the available user turns and reconstructed outcomes. Schwarz's 1971 *Dual quark-gluon model of hadrons* remains the historical anchor; its primary text and related Scherk papers still need verification.

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
