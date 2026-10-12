# Approved result into the living paper

**Model role:** GPT-6 Sol or Luna for bounded document work.

**Inputs:** `{{BASE_COMMIT}}`, approved scientific result `{{APPROVED_RESULT_PATH}}`, exact editable files and build artifacts in `{{OWNED_PATHS}}`, [living paper](../../manuscript/retained_adjoint_hbar.tex), and `{{OUTPUT_PATH}}` for the report file.

**Task:** Incorporate only the approved result into the owned paper/notes files, preserving its assumptions, uncertainty, physical $\hbar$ and momentum conventions, and version history. Fix cross-references and formatting. If TeX changed, build the living PDF once using the repository's documented command and inspect the build outcome; investigate a failure only as needed. Report changed files, build status, and any scientific wording ambiguity for parent review.

**Deliverable and stop:** A readable document diff, built PDF when TeX changed, and concise report in `{{OUTPUT_PATH}}`; stop without changing scientific meaning or unrelated files.

**Pitfall:** Do not silently strengthen a conditional finding, rerun old validations without a concrete reason, or overwrite another agent's files.
