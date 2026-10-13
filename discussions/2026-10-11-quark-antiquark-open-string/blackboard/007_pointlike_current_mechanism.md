# Whole-string pointlike current: two mechanism tests

12 October 2026. The user's controlling sectors are bosonic q/qbar meson, bosonic q/q diquark, fermionic q/qbar lepton and fermionic qbar/qbar quark. The main question is why the **whole fermionic string** could appear pointlike while the bosonic string remains extended. Contact binding in [005](005_fermionic_binding_and_seiberg.md) and [006](006_scalar_completion_test.md) is supporting material.

The full derivation is in the living paper, [pointlike_current.tex](../manuscript/pointlike_current.tex), with [numerical results](../calculations/warped_current_experiment.json) and [script](../scripts/warped_current_experiment.py). This entry records the result and next construction task without duplicating that argument.

## Test 1: finite-momentum current hierarchy

Use an AdS slice z₀=1/Λ_UV, z₁=1/Λ_had, ρ=z₁/z₀, a normalized hard-wall probe current and assumed sector densities. The fermion density is the effective Dirac zero-mode density P_F∝z⁻²ᶜ; the bosonic comparison is P_B∝z. A five-dimensional mass m₅=c/ℓ_AdS can coexist with a massless four-dimensional mode. These profiles have not been derived from one string background.

For c=1 and Q=10Λ_had, the finite-momentum integral gives:

| Quantity | Result |
| --- | --- |
| Hierarchy for F_F²=0.99 | ρ≈2888.50 |
| Bosonic overlap at that hierarchy | F_B≈0.0399872 |
| F_F at ρ=3000 | 0.99517133 |
| Marginal c=1/2 overlap at ρ=3000 | 0.72691357 |

The illustrative 1% tolerance concerns one spacelike elastic current insertion at Born level. It is not a data limit or a full string S-matrix result. A `gpt-6-sol` agent implemented the quantitative experiment and saved outputs to disk. SciPy integration was compared with fixed Gauss–Legendre quadrature using double-precision nodes and weights, different quadrature orders, and mpmath Bessel evaluations at 40 and 60 digits; results were stored as floats. Differences were at most 4×10⁻¹⁶ at the checked points. This supports floating-point agreement, not full 40- or 60-digit accuracy, and evaluates the assumed model rather than establishing its physical realization.

## Test 2: which localization can work?

The marginal c=1/2 profile reaches the same tolerance at Q=10Λ_had only for an estimated hierarchy of order 10¹⁸⁹–10¹⁹⁰. Exact ordering of the overlap densities shows c<1/2 cannot do better at fixed Q and ρ. All c≥1/2 profiles have divergent unnormalized bulk norm as z₀→0: a physical UV boundary/completion is required.

Different profiles can therefore separate the currents, but statistics alone cannot. Holographically, UV localization may signify elementary-source admixture. The extended bosonic comparison density also does not yet establish a meson spectrum or pion dynamics.

## Next result sought

Derive the physical UV mode/boundary and both sector profiles from a common string or Seiberg-dual construction with the specified endpoint and charge dictionary. Then compute a second observable, such as a transition current or resonance coupling, to determine whether the hierarchy survives beyond this elastic overlap. This advances the main question; further contact-trimer variations are optional supporting work.
