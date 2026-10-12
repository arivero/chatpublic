# One justified numerical observable

**Model role:** GPT-6 Sol for implementation, with parent research model deciding the scientific claim.

**Inputs:** `{{BASE_COMMIT}}`, exact `{{OBSERVABLE}}`, `{{PARAMETER_DOMAIN}}`, `{{ERROR_BUDGET}}`, and `{{INDEPENDENT_CHECK}}` supplied by parent. `{{OUTPUT_PATH}}` is the report file; `{{ARTIFACT_DIR}}` for code, data and useful plots must be declared in `{{OWNED_PATHS}}`.

**Task:** Compute the specified new quantitative observable in the smallest adequate submodel. Document equations, units with physical $\hbar$, regulator and boundary conditions, numerical method, convergence/error budget, and independent physical or analytic check. Keep raw numerical outputs on disk and give a compact interpretable result. If the inputs do not define a calculable observable, state the missing specification and stop without coding.

**Deliverable and stop:** Reproducible artifacts in `{{ARTIFACT_DIR}}` and one bounded scientific inference in `{{OUTPUT_PATH}}`; stop when the declared error and independent check are satisfied or a specific obstruction is found.

**Pitfall:** No scripts that merely replay known identities, optimizer reward hacking, or multiplication of check counts as evidence.
