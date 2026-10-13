# Delta review of one new derivation

**Model role:** inherit the parent research model, preferably a distinct reviewer from the author.

**Inputs:** `{{BASE_COMMIT}}`, `{{CHANGED_RESULT_PATH}}`, one explicit `{{CLAIM_TO_REVIEW}}`; [focused paper](../../manuscript/retained_adjoint_hbar.tex) only as needed. Write only `{{OUTPUT_PATH}}`.

**Task:** State the premises and desired observable neutrally before assessing the candidate derivation, especially if this is a fresh fork. Review only mathematics or assumptions changed since `{{BASE_COMMIT}}`: algebra, units with physical $\hbar$, limiting cases, physical interpretation, and whether evidence supports `{{CLAIM_TO_REVIEW}}`. Record which source and author analysis you actually saw, so the report never implies blind independent discovery. Supply a counterexample or concrete correction for each substantive defect.

**Deliverable and stop:** A short ranked finding list and corrected claim if needed in `{{OUTPUT_PATH}}`; stop after the delta review.

**Pitfall:** Do not rerun the old paper's entire derivation or treat passing consistency checks as a new research result.
