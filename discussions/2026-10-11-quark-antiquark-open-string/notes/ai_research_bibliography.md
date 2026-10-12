# AI-assisted mathematics and physics: a bibliography for this project

Research date: **12 October 2026**. The user describes this project as an attempt to obtain new results from GPT Astra and potentially later models. That motivation belongs in the provenance of the work. It does not establish that any present result is new, or that a named model independently discovered it.

## Coverage and access

This is an annotated starting bibliography, **not a verified survey through October 2026**. In this session HTTPS requests to Nature, DeepMind, and OpenAI returned proxy `CONNECT tunnel failed, response 403`; earlier arXiv and INSPIRE requests were also blocked. The entries below are established literature pointers, with sources to retrieve, rather than papers freshly read in this session. Recent 2025–2026 claims need a subsequent literature update. No unspecified “Astra success,” 2026 breakthrough, or current leaderboard result is being invented to fill that gap.

The most relevant distinction is between a new scientific result, solving a previously set benchmark, rediscovering a known law, and accelerating a calculation. All can be useful; they support different claims about this research program.

## Mathematical research and algorithm discovery

| Reference | What kind of achievement it reports | What it suggests for our workflow |
| --- | --- | --- |
| A. Davies et al., *Advancing mathematics by guiding human intuition with AI*, Nature **600**, 70–74 (2021). [DOI:10.1038/s41586-021-04086-x](https://doi.org/10.1038/s41586-021-04086-x) | Machine learning helped mathematicians find useful relations in knot theory and representation theory, followed by human mathematical development. | A model can guide a promising conjecture or invariant without being credited with an unassisted proof. Seek a useful new relation, then expose its assumptions and prove it. |
| A. Fawzi et al., *Discovering faster matrix multiplication algorithms with reinforcement learning*, Nature **610**, 47–53 (2022). [DOI:10.1038/s41586-022-05172-4](https://doi.org/10.1038/s41586-022-05172-4) | AlphaTensor searches for new algorithms with a precise algebraic objective; this is specialized reinforcement learning, not an unrestricted conversational theorist. | A well-defined verifier can make search productive. A verifier of a matrix identity does not thereby verify a physical model or its novelty. |
| B. Romera-Paredes et al., *Mathematical discoveries from program search with large language models*, Nature **625**, 468–475 (2024). [DOI:10.1038/s41586-023-06924-6](https://doi.org/10.1038/s41586-023-06924-6) | FunSearch combines LLM-generated programs with evaluation, including improved combinatorial constructions. This is a close precedent for obtaining new outputs from language models with independently specified checks. | Use computation when the target is an actual new construction or quantitative result. Preserve the evaluator and unsuccessful candidates; do not redefine success around whatever the model produced. |

These are examples of AI-assisted research, not evidence that one model can replace the dynamical derivation of a QCD dual. Their results should be cited with the actual division of labor among models, search procedures, evaluators, and researchers.

## Proof and contest performance: a separate evidence category

- T. H. Trinh et al., *Solving olympiad geometry without human demonstrations*, Nature **625**, 476–482 (2024), [DOI:10.1038/s41586-023-06747-5](https://doi.org/10.1038/s41586-023-06747-5). AlphaGeometry combines learned guidance with symbolic reasoning. It is evidence about solving specified problems in a defined domain; that is different from discovering a new physical theory.
- Google DeepMind, [*AI solves IMO problems at silver-medal level*](https://deepmind.google/discover/blog/ai-solves-imo-problems-at-silver-medal-level/) (2024), describing AlphaProof and AlphaGeometry 2. This is a developer report of contest-problem performance. Details of formalization, compute, timing, and human involvement matter when interpreting it; the post was not retrieved here.
- **Update needed:** subsequent IMO results, newer proof systems, and 2025–October 2026 claims of research-level mathematics. Record whether a source is a paper, independent verification, or a model developer announcement. A contest score, even a very strong one, does not by itself establish research novelty.

Formal verification is particularly useful when a candidate statement has an exact formal specification. It checks the encoded theorem relative to its assumptions and proof kernel; it does not certify that the specification is the intended physical problem or that the theorem was previously unknown.

## Physics and quantum research

| Reference | What it contributes | Relevant limitation |
| --- | --- | --- |
| M. Krenn, M. Malik, R. Fickler, R. Lapkiewicz, and A. Zeilinger, *Automated Search for new Quantum Experiments*, Phys. Rev. Lett. **116**, 090405 (2016). [DOI:10.1103/PhysRevLett.116.090405](https://doi.org/10.1103/PhysRevLett.116.090405) | Automated search for quantum-optical experimental designs, associated with MELVIN. A useful precedent for discovery by constrained search. | This is not a modern LLM result. A proposed experimental arrangement and its later experimental realization are distinct evidence levels. |
| G. Carleo and M. Troyer, *Solving the quantum many-body problem with artificial neural networks*, Science **355**, 602–606 (2017). [DOI:10.1126/science.aag2302](https://doi.org/10.1126/science.aag2302) | Neural-network representations of quantum states provide a numerical many-body method. | A successful variational approximation is a computational advance; it is not a proof of a new fundamental theory. |
| S.-M. Udrescu and M. Tegmark, *AI Feynman: A physics-inspired method for symbolic regression*, Science Advances **6**, eaay2631 (2020). [DOI:10.1126/sciadv.aay2631](https://doi.org/10.1126/sciadv.aay2631) | Symbolic regression exploits physical structure to recover compact equations from data. | Recovery of known benchmark formulas demonstrates capability but must be described as recovery, not discovery of those laws. |
| R. Iten, T. Metger, H. Wilming, L. del Rio, and R. Renner, *Discovering Physical Concepts with Neural Networks*, Phys. Rev. Lett. **124**, 010508 (2020). [DOI:10.1103/PhysRevLett.124.010508](https://doi.org/10.1103/PhysRevLett.124.010508) | Learned representations can expose compact physical variables in controlled problems. | A learned latent variable needs physical interpretation and out-of-training tests; interpretable structure alone is not a new law. |

For the present project, a stronger physics success would be a new, well-defined amplitude, protected spectrum, or consistent operator construction, followed by an independent derivation or a meaningful numerical prediction. Reproducing the gamma-function expansion of a known string amplitude is useful preparation, but not that result.

## More recent leads to retrieve

The 2025 AlphaEvolve announcement, [*AlphaEvolve: A Gemini-powered coding agent for designing advanced algorithms*](https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/), is a relevant continuation of program search with language models. Treat the announcement as a reading lead until its associated technical report, specific results, and independent assessments have been examined. Do not import its reported gains as evidence for this project's model.

For a genuinely current October 2026 update, search primary sources for LLM-assisted mathematical discoveries and theoretical-physics calculations, keeping for each claimed result: exact statement, first-public version/date, prior literature, human/model contribution, verifier or independent derivation, negative results, and subsequent corrections. A broad vendor claim about “science” is insufficient. The present access limitation leaves that update unfinished; the user-supplied 2026 physics citations inside the drafts are likewise citations to check, not externally verified literature.

## How this belongs in the eventual paper

A short methods/provenance paragraph can explain that the project explores frontier-model-assisted theoretical research and cite a few genuinely relevant precedents, especially Davies, FunSearch, and an appropriate physics example. Keep contest performance separate. Cite the actual model/version and role when recorded, without inventing backend details for “GPT Astra.” AI assistance is not a physics argument and does not validate the proposed quark–diquark/lepton–meson theory.

The pre-PDF commit is valuable provenance, but the model already had two conversations containing many equations and conclusions. It therefore cannot support a claim of blind rediscovery. The [research protocol](research_protocol.md) records what should count as a new result in this notebook.
