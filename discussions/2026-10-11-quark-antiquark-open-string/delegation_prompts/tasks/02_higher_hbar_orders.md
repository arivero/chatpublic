# One higher semiclassical energy order

**Model role:** inherit the parent research model.

**Inputs:** [focused paper](../../manuscript/retained_adjoint_hbar.tex), especially its $\hbar^2$ result; `{{BASE_COMMIT}}`. Write only `{{OUTPUT_PATH}}`.

**Task:** Calculate the retained-adjoint trimer ground energy through physical order $\hbar^3$ at fixed finite Gaussian regulator, $V_0,R,\mu$, and $0\leq\eta<1$. Include the sextic potential at first order and quartic potential at second order, with all recoil correlations in the harmonic basis. Give dimensionally consistent coefficients and an analytic $\eta\to0$ comparison with two dimers. If the complete coefficient is too large, isolate one mathematically correct component and explicitly mark the total incomplete.

**Deliverable and stop:** One transparent derivation and checked coefficient, or a precisely scoped incomplete result, in `{{OUTPUT_PATH}}`; stop at $\hbar^3$.

**Pitfall:** Do not assign a positive $\hbar$ power to each contact iteration or call the fixed-number Schrödinger Born series a field-theory loop expansion.
