# Suggested research delegation prompts

Seventeen bounded task prompts for this project, with one shared contract. **These are locally authored adaptations, not prompts recovered verbatim from OpenAI and not tasks already executed.** The retained-adjoint model remains the active research priority; the other routes are available assignments, not a demand to launch everything.

**Direct physics relevance:** the inspected openai/math material has supplied no theorem, amplitude or binding mechanism used in our current retained-adjoint calculation. The user explicitly questioned this relevance, and the library does not propose a physics detour through those results. Its source study is methodological background; the task menu comes from our existing research questions. Revisit a source result only if a concrete usable connection is identified.

Sol inspected `openai/math` at commit `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb` on 12 October 2026. The [source audit](source_audit.md) contains immutable links, prompt excerpts, PDF pages and reading limits; the [manifest](source_manifest.json) records the snapshot. Published excerpts exist for spin glasses, the quantum Heisenberg ferromagnet and Vlasov–Maxwell. The separately inspected BFSS/QFT manuscripts did not supply original prompts. The repository's released material does **not** establish a multiagent calling protocol.

## The common pattern, and what we add

| Published evidence | Adaptation for our agents |
| --- | --- |
| Exact prove/refute targets with assumptions: audit patterns 1–2, original prompt excerpts | One explicit question, physical object, units and observable; allow a counterexample or a precise unresolved gap. |
| Supplied premises separated from candidate proofs: pattern 3, prompt/synopsis evidence | Pin inputs and state what is inherited, assumed, calculated or still missing. |
| Concrete weaknesses examined: pattern 4, published reasoning synopsis | A focused reviewer tests the new claim's weakest step instead of rereading the entire project. |
| Necessary estimates and limits tracked: pattern 5, synopsis | State the dependencies of a conditional result; do not promote a missing estimate into a conclusion. |
| Small checks that distinguish alternatives: pattern 6, synopsis | Use a relevant analytic limit or independent numerical criterion; stop when the assigned question is answered. |

The synopsis patterns are observations about the released account, not recovered instructions. Our additions are bounded subagents, explicit hbar, restricted file ownership, cheap document checks, disk outputs, short parent reports and paper integration. We do not infer that a particular prompt caused a reported success, or that every reported result is correct. Unlike a forced prove/refute request, our contract explicitly permits an honest incomplete result.

## How to dispatch one task

1. Choose **one** template from the table below. Fill its placeholders and the [common contract](common_contract.md), including the exact question, baseline commit, inputs, output path and effort bound. Do not leave essential choices implicit.
2. Start a fresh agent context where available, supplying the filled contract and task text or their explicit file paths and filled parameters. Default to `fork_turns: "none"` to avoid copying the whole conversation. This reduces context cost; it does not by itself make a review blind.
3. For derivations and constructions, inherit the current research model. For source retrieval, numerical implementation and document work, use the user's requested Sol/Luna roles. Model availability can change; do not invent a backend identity.
4. Give one agent ownership of each output file. The parent integrates accepted results; parallel agents should write separate artifacts. Run an independent branch in parallel only when its inputs and ownership permit it.
5. After a new physics result, commission at most one focused mathematical review when useful and one applicable document check. Integrate the accepted result in the living paper. Do not launch the whole library as a checklist.

A typical research call uses `collaboration.spawn_agent` with `task_name`, `fork_turns: "none"`, and `message` containing the filled assignment; omit a model override to inherit the research model. A routine call adds `model: "gpt-6-sol"` or `"gpt-6-luna"` when available. No orchestration script or background jobs are created by this folder.

For the next radius calculation, the assignment can be as short as this **after filling paths and the actual baseline**:

> Read the applicable AGENTS.md, common_contract.md and tasks/01_anharmonic_radius.md. MODE: derive. QUESTION: find the leading anharmonic correction to the charged retained-adjoint state's mean-square radius at fixed mu, V0, R and eta. BASE_COMMIT: [actual scientific baseline; the initial version is 4b3a830]. INPUTS: the retained_adjoint_hbar.tex source at that baseline, with any subsequent changes disclosed. RESEARCH_ROOT: [absolute notebook directory]. OUTPUT_PATH and OWNED_PATHS: [one new blackboard result path]. EFFORT_BOUND: one analytic correction and one relevant limiting check; report a precise partial result if the general coefficient is not obtained. Preserve explicit hbar and the stated charge assumptions. Do not edit the living paper or launch other agents. Return the result and path in at most 200 words.

This folder deliberately does not start that calculation: the current assignment is to prepare future prompts.

## Task menu

| Prompt | Concrete question / needed input | Role |
| --- | --- | --- |
| [01 — Anharmonic radius](tasks/01_anharmonic_radius.md) | Next active step: leading correction to the existing harmonic whole-state radius | Research |
| [02 — Higher hbar order](tasks/02_higher_hbar_orders.md) | Complete the energy's next semiclassical order, including both required perturbation terms | Research |
| [03 — Finite recoil and thresholds](tasks/03_finite_recoil_and_thresholds.md) | One quantitative pole/gap or no-dimer regime; avoid repeating the existing existence proof | Research; Sol if computation is justified |
| [04 — Whole-state scattering](tasks/04_whole_state_scattering.md) | One declared current, transition or scattering channel and physical momentum window | Research |
| [05 — Completion and stability](tasks/05_contact_completion_and_stability.md) | One matching, radiative or stability question in a specified completion | Research |
| [06 — Four-sector dictionary](tasks/06_four_sector_color_charge_dictionary.md) | One minimal charge/color/parity assignment, including identical endpoints | Research |
| [07 — Seiberg matching](tasks/07_seiberg_operator_and_scale_matching.md) | A named electric/magnetic pair and one operator/scale bridge | Research |
| [08 — Warped boundary](tasks/08_warped_boundary_construction.md) | A physical background and boundary producing the profiles, not another fitted ansatz | Research |
| [09 — Fermionic string mechanism](tasks/09_fermionic_string_mechanism.md) | One worldsheet, boundary, conversion or defect mechanism with a calculable diagnostic | Research |
| [10 — CP² × S¹ modes](tasks/10_cp2_s1_vectorlike_modes.md) | A specified bundle/embedding and one light vectorlike mode calculation | Research |
| [11 — Flavor and pions](tasks/11_flavor_and_pion_scaffold.md) | Two-flavor chiral scaffold with a specified odd-sector coupling | Research |
| [12 — Primary sources](tasks/12_primary_sources_and_provenance.md) | One historical or AI-research claim and a precise primary-source locator | Sol; escalate technical interpretation |
| [13 — Experimental matching](tasks/13_experimental_matching.md) | An actual prediction and one dataset; otherwise identify the missing observable | Research; Sol for bounded retrieval/computation |
| [14 — Unconventional candidates](tasks/14_unconventional_candidate_search.md) | At most three mechanisms for one bottleneck, developing one to a diagnostic | Research |
| [15 — New-math review](tasks/15_review_new_mathematics.md) | One changed result and its assumptions; record the reviewer's source exposure | Research |
| [16 — Justified numerics](tasks/16_justified_numerical_task.md) | Exact observable, domain, error budget and independent check supplied first | Sol |
| [17 — Paper and document update](tasks/17_document_and_paper_update.md) | An approved result, owned files and only the applicable build/presentation checks | Sol / Luna |

The fresh-context review should receive a neutrally stated problem and explicit premises. If a genuinely independent derivation is desired, withhold the candidate calculation until that derivation is recorded; otherwise call it a source-informed review. Neither procedure substitutes for a proof or experimental evidence.

The templates are suggestions, not a new bureaucracy. The parent should shorten or specialize a task when the answer needs less work. Keep exploratory failures in the existing blackboard/idea bank, established scoped results in notes, and the integrated physics argument in the paper.
