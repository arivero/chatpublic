# Finite recoil near breakup

**Model role:** inherit the parent research model.

**Inputs:** [focused paper](../../manuscript/retained_adjoint_hbar.tex), its recoil resolvent and dimer threshold; `{{BASE_COMMIT}}`. Write only `{{OUTPUT_PATH}}`.

**Task:** For one specified regime outside the deep Gaussian limit, calculate a trimer pole energy or a quantitative binding gap at finite $\eta$. Existence below breakup whenever the dimer binds is already proved: do not repeat that proof as the new result. Alternatively, in a regime with no bound dimer, test for a trimer below the three-free-particle threshold. Use a controlled bound, resolvent estimate, or justified numerical method with a separate error criterion. Distinguish changing $M$ at fixed $m$ from varying $\eta$ at fixed $\mu$. If discussing $R\to0$, state the fixed two-body input and whether a three-body counterterm is required.

**Deliverable and stop:** A bounded claim for one regime, including threshold, assumptions, and uncertainty, in `{{OUTPUT_PATH}}`. Stop before mapping the whole phase diagram.

**Pitfall:** Comparing $E_3$ with zero instead of the dimer threshold can falsely report stable binding.
