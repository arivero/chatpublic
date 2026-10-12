# One whole-state scattering observable

**Model role:** inherit the parent research model.

**Inputs:** [focused paper](../../manuscript/retained_adjoint_hbar.tex), [historical current test](../../blackboard/007_pointlike_current_mechanism.md), `{{BASE_COMMIT}}`; parent fills `{{OBSERVABLE}}`, `{{Q_WINDOW}}`, and tolerance `{{TOLERANCE}}`. Write only `{{OUTPUT_PATH}}`.

**Task:** Evaluate exactly one of elastic current, Pauli response, inelastic transition, or four-point scattering for the retained-adjoint state over the declared physical momentum interval. Specify probe charges, state normalization, Ward constraints, accessible breakup/resonances, and the approximation's domain. Compare with the extended bosonic sector only where a common model supplies both currents. If a small fermionic overlap is assumed, test whether its leading correction is stable under the interactions actually specified.

**Deliverable and stop:** A calculated observable or sharp missing-ingredient result, with a precise pointlike criterion, in `{{OUTPUT_PATH}}`. Stop after one channel.

**Pitfall:** One low-$Q$ radius or fitted profile cannot establish pointlike whole-state scattering across `{{Q_WINDOW}}`.
