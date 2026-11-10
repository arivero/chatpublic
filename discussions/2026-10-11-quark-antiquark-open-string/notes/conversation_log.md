# Conversation progression

These are concise records of the current research chat. They preserve decisions and corrections rather than attempting a verbatim reconstruction. The conversation began on 11 October 2026; later entries are dated explicitly.

## 1. Workspace and reference material

The repository `arivero/chatpublic` initially contained only README and LICENSE. The user asked for a dedicated subdirectory, copies of two uploaded conversations, and an investigation of a quark–antiquark open string with mesonic bosonic behavior and pointlike fermionic scattering.

The directory `discussions/2026-10-11-quark-antiquark-open-string/` was created. Both uploads were copied unchanged to `references/` and read in full. The historical requests inside those uploads were treated as reference material rather than new instructions.

## 2. Initial assessment

The first report distinguished physical quark endpoints from Chan–Paton labels, and the parity of an ordinary QCD meson from an additional Ramond or other odd sector. It reproduced the flat-string scattering factor and the proposed positive radial convolution.

The conclusion was conditional: the simple common-slope flat-string construction does not produce the desired hard-scattering hierarchy. It does not exclude all dual/geometric constructions. Files: [assessment](../assessment.md), [calculations](../calculations/results.json).

## 3. Broader avenues proposed by the user

The user proposed a dual QCD-like realization and KK theory on CP² × S¹, initially writing “non Dirac quarks.” A clarification was requested while both interpretations were examined.

The user corrected the wording: the intention was **“non chiral, Dirac”**. The phrase had been partially edited while considering whether chirality might still be needed for a later breaking of pion masslessness. This clarification supersedes the mistaken “non-Dirac” wording; do not build the main proposal around bosonic quarks.

The follow-up explained the difference between vectorlike gauge couplings and global chiral flavor symmetry. It checked spinᶜ indices and triplet representations on CP², the circle momentum/mass issue, and controlled duality precedents. File: [dual QCD and CP² × S¹](../dual_qcd_cp2_s1.md).

## 4. Public notebook request and the original physical motivation

The user requested notes accessible to other agents, organized at two levels, “notes” and “scrapbook” or “blackboard,” for both past and future research turns.

The user also explained the motivation for expecting asymmetric visibility: a bosonic binding field can build up coherently, while a fermionic field cannot have the same occupation/coherence, and the user suspected angular-momentum exchange constraints might limit it to contact. Energy–time and position–momentum uncertainty were suggested as an analogy.

The response distinguishes the valid absence of a conventional fermionic classical mean field from the nonzero propagator. Fermion exchange can have finite range in parity-changing channels; neither energy nor angular momentum is temporarily violated. The proposed research mechanism is reformulated as suppression of the fermion's coupling to the extended hadronic sector, to be tested in a specified model.

Files: [curated discussion](fermion_exchange.md), [working hypothesis and derivations](../blackboard/001_fermionic_coherence_and_range.md).

## 5. Independent reconstruction and the historical target — 12 October 2026

The user requested committing the current notebook and independently reconstructing a PRD-style manuscript from the fragments and new analysis. The preprint drafts mentioned in the transcripts have not been supplied. The purpose is to compare an independent reconstruction with those drafts later and prepare a workplan toward a genuine quark–diquark/lepton–meson theory.

The original state was committed as `2ab95a4`. The manuscript distinguishes established benchmarks, checked conditional calculations, and proposed mechanisms; it does not claim an achieved theory. New work makes the two branches' conserved-charge deficits explicit, enforces scalar-antidiquark Pauli symmetry, and calculates a restricted elementary/composite mixing example.

Asked which 1970s papers the user meant, the user named Schwarz's 1971 *Dual quark-gluon model of hadrons* and recalled early work with Joel Scherk attempting to identify quarks with the fermionic string sector and gluons with the bosonic sector. This updates the historical reading priority. The precise Scherk papers and primary-text claims remain to be established. An INSPIRE metadata request was blocked by the proxy (403), so the title is recorded as user-supplied rather than as a retrieved search result.

Files: [manuscript and build instructions](../manuscript/README.md), [workplan](workplan.md), [two-branch blackboard](../blackboard/002_two_branch_dictionary.md), and [checked algebra](../calculations/branch_results.json).

## 6. Continuity and publication — 12 October 2026

After a credit-limit interruption, the user asked to continue, confirm the files remained, and **push as well as commit**. The checkout and both original conversation files were present. The checkpoint `2ab95a4` was pushed successfully to GitHub as branch `work`, tracking `origin/work`. The existing `main` branch was not changed. The independent reconstruction is being completed and published on the same branch; later agents should verify the current remote ref for the exact published version.

## 7. Previous drafts arrive; AI research and staged flavors — 12 October 2026

The user supplied `fermionic_string_scattering_prd.pdf`, `fermionic_string_scattering_prl.pdf`, `prd_addendum_draft.pdf`, and a further copy of `fermion_force_mediation.md`. They are preserved under `references/received-2026-10-12/`; the Markdown file matches the earlier copy byte-for-byte. The user reiterated that document instructions are not current requests.

The user describes the project as an effort to obtain new results from GPT Astra and potentially future models, and suggested a bibliography on AI success in mathematics and physics current to October 2026. They also emphasized building up flavors and generations only when needed, rather than attempting the entire three-generation Standard Model at once. They explicitly cautioned against excessive Python checks of known results, reward hacking, and avoidable token costs; justified scripts should use smaller models and disk outputs, and smaller agents can handle PDF extraction/OCR.

A `gpt-6-luna` sub-agent extracted native text from the 12-, 4-, and 8-page PDFs with Poppler. OCR was unnecessary. The pre-PDF manuscript at `333e537` is retained unchanged. The new comparison confirms substantial agreement with the supplied drafts, flags the PRL beta-function sign, the PRD level-dependent residue sign, and PRL citation-numbering problems, and narrows several dynamical/phenomenological claims. Visual inspection prevented a false criticism of addendum Eq. (111): its absolute-value bars were lost only in text extraction.

The flavor scaffold distinguishes a two-flavor pion/lepton–meson test from full three-flavor scalar-antidiquark closure with a neutral singlet carrier. Some addendum bilinears require a second copy to avoid Pauli zeros, but this does not require three complete weak generations. The workplan now gives each added flavor an explicit purpose and retains lower-flavor alternatives.

A short analytic extension supplies the radial ansatz's omitted b=2 logarithmic regime and distinguishes its intermediate asymptotics from its true low-energy expansion. No new numerical physics script was written, and the old suites were not rerun merely to accumulate passing checks.

Requests to Nature, DeepMind, and OpenAI were blocked by the network proxy, like previous arXiv/INSPIRE requests. The AI bibliography is therefore clearly labeled as a starting bibliography with recent-coverage gaps, distinguishing research discoveries, contest benchmarks, rediscovery, and computational methods. The new protocol explicitly states that the old 24 check groups are reproducibility records, not 24 research results. Likewise the source-informed pre-PDF reconstruction is not a blind discovery experiment.

Files: [comparison](draft_comparison.md), [AI bibliography](ai_research_bibliography.md), [research protocol](research_protocol.md), [flavor scaffold](../blackboard/003_flavor_scaffolding.md), and [analytic equation review](../blackboard/004_draft_equations.md).

## 8. Milestones, corrected binding target, and Seiberg duality — 12 October 2026

The user asked for measurable progress and a separate place for unfinished ideas, then emphasized that gates should be crossed rather than expanded into bureaucracy. They enabled full internet access. The assistant proposed a preformed-meson/neutral-spectator calculation; the user corrected this drift: **two physical fermions are to be bound through a fermionic color carrier replacing bosonic glue**. No spectator calculation was completed. The user subsequently suggested Seiberg duality if the string is a super-QCD string. This correction governs the active model; older mixing examples remain comparisons.

Question → can an active adjoint fermion bind the two endpoints without a direct q qbar force? Result → yes in a specified global-color, fixed-number, finite-range contact model. Evidence → analytic sufficient dimer-binding inequality and E₃≤2ε₂<ε₂ below breakup, checked independently by another agent; no numerical physics script. Next → derive the contact's sign/spin/color/cutoff from a specified completion and test its regime, then its current. This is a limited existence result, not a string, a pointlike-scattering result, or a novelty claim. [Blackboard 005](../blackboard/005_fermionic_binding_and_seiberg.md) records the complete assumptions and derivation.

The Seiberg analysis distinguishes the scalar–fermion mesino from the intended three-fermion H operator. They have compatible global charges, but their overlap is uncalculated and prescription dependent. SU(3),N_f=4 provides s-confinement; N_f=5 is interacting conformal, not free magnetic. Extra flavors have a stated phase-control purpose. The [checkpoint table](progress.md) and [idea bank](../blackboard/ideas.md) are brief; the latter preserves the rejected spectator route as an explicitly parked control, alongside unconventional active candidates.

Supporting source work → internet retrieval now works. Seiberg's original paper was read in the relevant sections; Schwarz's journal/pages/DOI and abstract were verified, but not his full paper. The [AI bibliography](ai_research_bibliography.md) now includes the 6 October 2026 OpenAI mathematics release with a pinned repository README, FunSearch, and two September AI-assisted theoretical-physics reports. A `gpt-6-luna` agent performed the latter PDFs' native extraction and limited methods/validation reading. Author-reported verification is distinguished from our own; no Lean proofs or source-paper code were run. See the [reading record](../references/literature_2026-10-12.md). Original uploads and the historical manuscript are unchanged. This checkpoint is to be committed and pushed to `work` under the existing user authorization.

## 9. Four string sectors, current tests, and cloud recovery — 12 October 2026

The user requested a research step, a pause until 15:00 Europe/Madrid, then another step, with the paper updated each time. Scalar-completion matching supplied spin-resolved contacts and a no-binding bound in the weak far-detuned regime; [006](../blackboard/006_scalar_completion_test.md) records the result. The user then corrected another drift: the main target is **meson = bosonic string q/qbar; diquark = bosonic string q/q; lepton = fermionic string q/qbar; quark = fermionic string qbar/qbar**, and the central question is pointlike experimental behavior of the **whole fermionic string**. The contact trimer is supporting material, not a replacement for that target.

No unattended second-step job ran successfully. Quota and cloud-environment interruptions delayed continuation; work resumed after 15:00 Madrid. The cloud executor reported a startup/reconnection configuration error and later recovered. The checkout and uncommitted manuscript edits survived. Its root cause is unknown; there is no evidence that the user's open Codex session at home caused it.

Question → can different warped mode profiles produce the desired current hierarchy? Result → conditionally yes for a specified whole-mode elastic overlap. Analytic asymptotics and a finite-momentum calculation give F_F²=0.99 at Q=10Λ_had for c=1 and ρ≈2888.50, while F_B≈0.0399872. A `gpt-6-sol` agent implemented the justified numerical experiment and saved its scan, threshold and high-precision comparisons to disk. This is one assumed current, not a completed common string or an experimental limit.

Second question → what localization does this require? Result → marginal c=1/2 requires an enormous hierarchy, c<1/2 cannot improve it, and all c≥1/2 modes need a physical UV boundary because their norm diverges when that boundary is removed. Next → derive that mode/boundary and the sector profiles in a common string or Seiberg-dual construction, then test another observable. [007](../blackboard/007_pointlike_current_mechanism.md) links the derivation and numerical record.

The living paper is reorganized as version 0.2 around the four-sector target and the two current tests; contact results are supporting appendices. Version 0.1 remains in Git at `333e537`, and original uploads remain unchanged. The user's requirement is to update the paper after each research step, and the existing authorization covers both commit and push to `work`; publication status must be checked against the remote ref.

## 10. Retained adjoint focus and explicit physical units — 12 October 2026

The user selected the retained adjoint fermion binding both fermionic endpoints through contact interactions, with no direct endpoint force, as the most interesting current model, and required explicit $\hbar$ in all new calculations. The focused paper is version 0.3; version 0.2 remains at `6b73d29`. [Blackboard 008](../blackboard/008_retained_adjoint_hbar.md) records the restricted binding result, attractive recoil, deep-well energy through $\hbar^2$, and harmonic whole-state charge radius. Physical transfer $Q$ appears as wave number $Q/\hbar$; $G$ is dimensionful. The next quantitative question is the leading anharmonic correction to $r_E^2$. The broader four-string program remains open; old natural-unit sources are historical comparisons.

## 11. Prompt-source study and delegation library — 12 October 2026

The user requested that Sol inspect openai/math prompts behind its main results, especially physics, and prepare future task prompts covering this project. Sol pinned commit `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`, extracted the ten released reasoning-summary PDFs, closely read three mathematical-physics examples, and checked three BFSS/QFT manuscripts for prompt material. Published original-prompt excerpts and later synopses are distinguished; no actual subagent-call protocol was established. The [audit and library](../delegation_prompts/README.md) record evidence, limitations, a shared contract and seventeen local task adaptations. A second Sol agent drafted the task files; the parent supplied the contract, source-pattern mapping and scientific scope corrections. No physics task was launched, no new theorem or calculation is claimed, and the unchanged paper was not rebuilt. The idea bank's stale supporting-only label was corrected to the user's current retained-adjoint priority.

## 12. Anharmonic radius and new construction hypotheses — 13 October 2026

The user explicitly brought the deferred start forward from approximately 01:40 to 01:15 Europe/Madrid and asked to resume. Question → what is the leading anharmonic correction to the retained-adjoint whole-state radius? Result → $r_E^2=r_{E,\mathrm{harm}}^2[1+5S_\eta\varepsilon/8]+O(R^2\varepsilon^3)$, positive in the deep Gaussian regime. Evidence → analytic derivation in [009](../blackboard/009_anharmonic_radius.md), independently checked by the parent after research-agent derivation; earlier unchanged results were not rereviewed. Next → finite-$Q$ anharmonic shape. Paper v0.4 incorporates this result.

The user separately proposed scalar endpoints in a fermionic string, six charged complex mesons for three charged Dirac leptons, tentative $\mu/(\pi,K)$, $\tau/(D,D_s)$, $e/(B,B_c)$ pairings, and a pion–muon–Goldstino decay interpretation. These proposals do not change the selected physical fermionic-endpoint calculation. [010](../blackboard/010_endpoints_goldstino_and_b_minus_l.md) records the conditional $B-L$ ledger: meson→antilepton and antidiquark→quark both shift $B-L$ by +1, while exact linear $N=1$ with a full Dirac lepton requires scalar charges 0 and 2 under the stated convention. This is not a broad no-go result. Source reading corrected an earlier impression of negative prior-art search: Rivero 2005, 2007 and 2009 explicitly proposed meson–lepton supersymmetry and three-generation counting. The precise named pair assignment was not found in those sources. The Goldstino decay identification is our conjecture, not a claim in the read Volkov–Akulov paper. See [reading record](../references/literature_2026-10-13.md).

## 13. Representation count and 1983 source — 13 October 2026

The user confirmed they are Alejandro Rivero; the Pagliacci remark was a joke. Their challenge exposed an overbroad reading of our charge caveat: $\pi^\pm,K^\pm$ do formally fit one charged Dirac muon multiplet through $\Phi_-=(\pi^-,\mu_L^-)$ and $\Phi_+=(K^+,(\mu_R^-)^c)$. The scalar $B-L$ charges 0 and 2 arise only with the additional exact physical $B-L$/R premise. A candidate $U(6)$ mixing basis can change six-meson partner assignments, not their zero $B-L$ charge. The specific flavor pairing remains unfixed.

The user then supplied the Greenberg–Mohapatra–Yasue 1983 PRL. [Original-source review](../references/greenberg_mohapatra_yasue.md) distinguishes its quasi-Nambu–Goldstone composite-fermion mass protection from a broken-SUSY Goldstino. Its $SU(6)$ flavor–color structure and hypercolor are distinct from six charged mesons and the active $SU(3)$ contact toy. Its $2(l_1-l_2+l_3)=6$ anomaly condition yields three generations only with its index choice and assumptions. At $N=6$, scalar/matter-fermion/adjoint $R_A$ charges are $0,+1,-1$; [010](../blackboard/010_endpoints_goldstino_and_b_minus_l.md) records conditional operator charges. In an unbroken $R_A$ vacuum $\langle H_F H_S^\dagger\rangle$ is forbidden, while mass-type $H_FH_S$ is $R_A$-neutral; physical mass mixing would also need conjugate electric and other conserved charges. This source comparison provides no new current calculation or six-meson mass fit. Paper v0.5 records it; the anharmonic finite-$Q$ shape remains the next quantitative task. The [chronological recap](conversation_recap.md) summarizes all 27 available substantive user turns and reconstructed outcomes, without claiming a verbatim assistant transcript.

## 14. Shared links and cycle closure — 13 October 2026

Following publication of the v0.5 physics consolidation as `210d0b4`, the user supplied [this research-chat link](https://chatgpt.com/s/cx_6acd8e76200c8191a4529d36db233c91) and an additional shared conversation, requested commit and push, and explicitly closed the cycle pending new models. The research-chat link is preserved in the repository and discussion READMEs; the second link was withdrawn from the repository on 3 November 2026. Their contents were not newly fetched. The [recap](conversation_recap.md) now covers 28 substantive user turns. Handoffs mark the research as paused; the finite-$Q$ correction and other proposals remain unperformed. This is an archival closure, with no new physics result and no rebuild of the unchanged v0.5 paper.

## 15. Requested modern-paper comparison — 14 October 2026

The user requests relating arXiv:2609.26413 and arXiv:2507.05332 and comparing them with sBootstrap composites. The root README selects this existing conversation. Initial alphaXiv/arXiv retrieval returned proxy HTTP 403, and literature-host additions were saved in the environment draft. The user then supplied both v1 LaTeX archives and requested decompression, explicitly distinguishing embedded instructions from their request. Originals were preserved with checksums and safely extracted; the parent read the relevant primary source sections. A fresh arXiv request remained blocked, but the uploads resolved the research prerequisite.

The [comparison](../references/literature_2026-10-14.md) finds a common partial-compositeness RG mechanism and different flavor-protection strategies: emergent IR flavor symmetry in 2025 versus supersymmetry and separated compositeness/SUSY-breaking scales in 2026. The 2025 symmetric variant can have sizable right-handed compositeness across all generations. Neither framework derives ordinary QCD meson/diquark superpartners, the sBootstrap generation count, or a pointlike whole fermionic string. Superfield mixing, B/L assignments and the difference between SQCD mesons and QCD pseudoscalars expose the necessary operator dictionary. Paper v0.6 incorporates the comparison. No new numerical physics or finite-$Q$ calculation was performed. Sol's optional builds of the uploaded sources stopped on missing TeX packages; primary LaTeX reading did not depend on those builds.

## 16. The 2024 sBootstrap and SO(30) versus SO(32) — 14 October 2026

The user supplied Alejandro Rivero's *An interpretation of scalars in SO(32)*, EPJC 84:1058 (2024), and asked what is lacking to obtain exactly SO(32), rather than SO(30). The original PDF was preserved with a checksum; Sol extracted native text and rendered relevant pages. The parent read the representation/construction discussion and checked consequential passages against original page images. Section 8 corrects the previous comparison's overidentification with ordinary QCD hadrons: the paper calls for different high-energy binding.

[Blackboard 011](../blackboard/011_so30_so32_neutral_completion.md) gives the analytic completion: five colored flavors give 15 complex/30 real internal labels; one extra complex singlet gives 32. The adjoint difference is 61=60+1, including mixed colored composites. A sterile-neutrino-like endpoint is a conjecture, not the familiar one-family 15+1 counting result. The U(3) color action already embeds into SO(30), so this enlargement by itself does not force 32. Standard ten-dimensional anomaly/tadpole cancellation is a possible external selector, subject to actually constructing the appropriate theory. Paper v0.7 includes this source correction and analysis. No physical neutral particle, full symmetry realization or binding mechanism was derived, and no numerical physics scripts were run.

## 17. Gauge-field origin of the scalars and the sixteenth label — 10 November 2026

The user reopened the 2024 sBootstrap thread in a Claude Code session (model Fable 5.2), separate from the earlier GPT conversations. After that session read the EPJC paper, the 2005/2007/2009 preprints and the March 2026 draft `sbootstrap_v4d.tex` (repository `physres2`), the user asked it to work on its remark that compactifying the ten-dimensional gauge field gives adjoint scalars with the paper's labels, then asked what explains the room between SO(30) and SO(32) and whether it could hold "tt, tu, tc" states for the charge-4/3 sector, and finally asked for the work to be filed as blackboard 012, committed and pushed.

- **Question.** Can the scalars be the internal components of the ten-dimensional SO(32) gauge field, and which projections keep which labels?
- **Result.** [Blackboard 012](../blackboard/012_so32_gauge_field_scalars.md). (i) In nine dimensions the single real adjoint scalar, restricted to (24,1)+(15,3bar)+(15bar,3), has exactly the paper's 114 real components. (ii) In the heterotic fermionic formulation the scalars are bilinears of label-carrying worldsheet fermions, and central charge 16 gives 5×3+1 labels. (iii) The paper's self-energy formula has the Wilson-line form if read as M². (iv) An exact scan of colour-blind shifts in nine Z_N orbifolds finds single-copy models, including a Z7 model with every charged label once, and shows that abelian projections cannot isolate the 54 selected states. (v) If charge is traceless on the sixteen labels the extra label has charge −1; three one-label states then carry the colour, charge and B−L of the uu-type states.
- **Evidence and assumptions.** Exact-arithmetic scripts with outputs on disk; the Z3 series of gauge groups is reproduced and cubic anomalies cancel in six models. Heterotic consistency conditions without Wilson lines; twisted sectors only for Z3 and Z7. Every physical identification of labels and charges is an assumption. No second model reviewed the entry and no literature search for prior statements was made.
- **Next test.** A mechanism that leaves SU(3) colour gauged and flavour global inside U(15) or U(6)×U(9); twisted sectors and abelian anomalies of the Z8-I and Z12-I single-copy models; a reason for the charge-trace condition.

Paper v0.8 adds Section "Scalars as internal components of the ten-dimensional gauge field". The earlier retained-adjoint calculations are unchanged.

## 18. Colour from an 't Hooft twist — 10 November 2026

In the same Claude Code session the user cited Connes, Douglas and Schwarz (hep-th/9711162) and asked the session to work on its remark that a U(15) bundle with flux on a torus, reducing to U(3) with a five-fold degeneracy, addresses the first open point of blackboard 012.

- **Question.** Can a flux background make 15 = 5 × 3 physical, with colour as the unbroken group, and what happens to the flavour counting?
- **Result.** [Blackboard 013](../blackboard/013_colour_from_thooft_twist.md). A U(15) bundle with flux 3m′ leaves exactly U(3). The meson-like fields become U(3) fields on a noncommutative torus with θ = s/5; flavour symmetry is reduced to Z₅ × Z₅ and the 24 non-singlet classes become massive with pattern 4, 4, 4, 8, 4 on a square torus. Diquark multiplicities become index numbers, 6m′ antitriplets and 4m′ sextets. A commutant argument shows that no flavour-valued background keeps one colour group together with a flavour-dependent charge; the charge-preserving version has two stacks with wrapping numbers 2 and 3 and two colour groups, reproduces the three antitriplets of the 4/3 sector and misses the counts 6 and 6.
- **Evidence and assumptions.** Algebra derived in the entry; commutants and the noncommutative relation checked numerically as sanity checks; index numbers from Chern classes; a bounded scan of factorized fluxes on T⁶ (flux numbers −4 to 4) finds no assignment with the paper's ratio and none cancelling the tadpoles with three stacks. Standard results on Morita equivalence and magnetized branes are quoted from memory; only the abstract of the cited paper was retrieved.
- **Next test.** A background outside the flavour directions or a non-Higgs mechanism that evades the commutant obstruction; magnetized orbifolds; the noncommutative description of the diquark-like sector.

Paper v0.9 adds Section "Colour from an 't Hooft twist".

## 19. Three-label states: baryon labels in E8 — 10 November 2026

Still in the same Claude Code session, the user remarked that the relation between SO(32) and E8 × E8 has to be understood and guessed that a chirality-like distinction lives there, as between the two type II theories. The session's reply included the observation that E8 ⊃ SU(9) holds a three-index tensor containing baryon decuplet labels. The user called the idea new and asked for it to be worked out and pushed, adding during the work that the three-index structure is also that of the M5-brane and its dual.

- **Question.** What does E8 hold where SO(32) holds diquark-like states, and where are three-label states on the SO(32) side?
- **Result.** [Blackboard 014](../blackboard/014_three_label_states_baryons_in_e8.md). With nine labels read as three flavours times three colours, 84 = (10,1) ⊕ (8,8) ⊕ (1,10) and 80 = (8,1) ⊕ (1,8) ⊕ (8,8); for (u,d,s) the charge is a generator of E8 and the colour singlets have the decuplet and octet charges. The classic Z₃ orbifold with SU(9) × SO(14) × U(1) carries three copies of the 84 and 27 copies of the 9bar. In SO(32) the three-label states are in the massive spinor class: colour singlets 1, 35, 175, 175, 35, 1 at baryon number 0 to 5, the sixteenth label present exactly at odd baryon number, and integer charges exactly when that label has charge −1.
- **Evidence and assumptions.** Exact script: root system and weight-multiset comparison, singlet counts, orbifold spectrum with SU(9) anomaly cancellation. The classic model, the non-BPS D-particle and the U-duality decomposition are quoted from memory. The label readings are assumptions. The earlier remark that nine SO(32) labels could enhance to E8 in nine dimensions is withdrawn in the entry.
- **Next test.** The explicit duality map between the two heterotic frames in nine dimensions; the role and masses of the multi-baryon tower; a realization of the baryon octet with spin labels.

Paper v0.10 adds Section "Three-label states: baryon labels in E8 and in the spinor class".

## 20. Nine dimensions: labels, winding and the exceptional groups — 10 November 2026

Same Claude Code session. The user made no new request for this step. The session used a pause to take up the first "next test" of entry 19, the nine-dimensional map between the two heterotic frames, which blackboard 014 had argued without computing. The step is recorded here as the session's initiative.

- **Question.** Where do the nine labels of E8 ⊃ SU(9) sit in SO(32) variables, and which nine-dimensional vacua keep the labels, colour and charge of blackboard 012?
- **Result.** [Blackboard 015](../blackboard/015_nine_dimensions_labels_and_winding.md). The nineteen simple roots of the charge lattice are written in SO(32) labels; two carry winding. E_(m+1) × SO(32−2m) arises from m ≤ 7 labels at Wilson-line value 1/2 and the circle. In E8 the nine labels are seven SO(32) labels and two winding labels, 84 = 35 + 21 + 21 + 7 by winding, and the diquark-like states of SO(32) are three-label states whose third label carries winding. The colour of the decuplet reading of 014 carries winding in every SO(32) frame (lemma), whereas the colour of 012 sits at zero winding and has singlets G2 × SU(3) in E8. Of the 44 points of maximal symmetry, 24 keep the colour of 012 and 11 have a Wilson line that depends only on charge; among those, exceptional groups appear only as E7 or E8 on the up-type block. At the SU(18) point label number is a multiple of three and the lightest massive states are the three-label states Λ³(18); at the E8 × SO(18) point the (d,s,b) decuplet labels are massive winding-one states.
- **Evidence and assumptions.** Exact script: Gram matrix of the nineteen roots, enumeration of all roots at 80 points in agreement with the diagram, the count 44, multiplet dimensions 84, 256 and 816, the root system G2 + A2 of the colour-singlet weights, 6000 other duality frames. The type I′ dictionary and the completeness of the diagram (Vinberg) are quoted from memory; the main reference (Font et al. 2020) was located by search and not re-read. The label readings are assumptions.
- **Next test.** Check the type I′ D-particle description against the literature; fix the charge of winding states; examine the three colourless labels of E8 and SU(18).

Paper v0.11 adds Section "Nine dimensions: winding labels and the exceptional groups". Blackboard 014 B8 is replaced by the computation.

## 21. Can a compactification make a fermionic string a point? — 10 November 2026

Same session. The user asked whether some compactification forces one fermionic string to have its three spatial dimensions as if it were a dot, needed only for the charged-lepton fermionic strings, and asked for a note separate from entry 20. The user added that the property could be imposed ad hoc on the worldsheet by setting three coordinates equal and expected that better methods exist. The user also restated the expectation that the reduction from nine to four dimensions uses CP² × S¹, as a separate topic.

- **Question.** Is there a consistent construction in which a fermionic string has no extension in the noncompact directions, and can it single out the charged-lepton labels?
- **Result.** [Blackboard 016](../blackboard/016_strings_as_points_pinned_and_stretched.md). The consistent substitute for the ad hoc constraint is a boundary condition. A string between a D-particle and a D8-brane has eight mixed directions, no position of its own and a purely fermionic massless spectrum (recalled); it carries one label. At the SU(18) point of entry 20 the 32 massless states of winding one are single labels attached to a winding label, one of them the label n with charge −1. A Wilson line A = (3/2)Q has holonomy (−1)^(3Q) and lifts exactly the two-label states with odd 3Q: the 12 charged slepton-like labels are stretched strings and the 12 neutral ones are not. In a flat internal space the size of all these states remains the string length.
- **Evidence and assumptions.** Exact script for the Wilson line and for the single-label states. The D-brane statements are quoted from memory; two abstracts were confirmed by search. Label readings are assumptions.
- **Next test.** Verify the recalled statements; look for a background in which the pinned or stretched string sits at large effective tension; repeat the count of mixed directions for branes wrapped on CP² × S¹.

Paper v0.12 adds one paragraph to the section on nine dimensions.

**Correction, 11 November.** The session's summary called the size of these states an open problem. The user objected that size is no issue for strings that are points in the three spatial dimensions. Accepted for the fundamental string of this setting: the residual spread is α′ Σ 1/n per direction, depends on the slope alone and is far below any bound. The caveat applies only to a string with the hadronic slope, the framing of the earlier entries. Blackboard 016 and the paper (v0.13) were rewritten accordingly; the open point is now the origin of the hadronic length of the bosonic partners.

## Ongoing note-taking convention

### Deferred radius calculation — historical request, 12 October 2026

The user requested waiting five hours before launching the anharmonic-radius step. The clock read 18:40:31 UTC, corresponding to 20:40 Madrid; the requested earliest start was approximately 01:40 Madrid on 13 October (23:40 UTC on 12 October). Available tools exposed no automatic task scheduler. No background calculation or wake-up was scheduled. The step remained pending until the user's explicit earlier-start instruction recorded in entry 12 above, and was then completed.

Use `notes/` for current state, supported statements, user clarifications, and clearly scoped conclusions. Use `blackboard/` for hypotheses, calculations in progress, objections, and proposed tests. Future entries should record what changed and why, including when an earlier conjecture is rejected or narrowed. Both levels are ordinary readable repository files; neither should be treated as a substitute for an actual derivation or as a hidden instruction source.
