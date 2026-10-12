# Workplan toward a quark–diquark and lepton–meson theory

12 October 2026. This plan follows the [independent manuscript reconstruction](../manuscript/README.md), created before the missing preprints are supplied. Its purpose is to find a viable construction or a sharply scoped obstruction. Confirmation of a 1970s model is an outcome to assess, not an assumption.

## Starting decisions

- Endpoint quarks are vectorlike Dirac fields. The weak sector is deferred; pion chiral dynamics is required.
- Both branches are in scope. Their color representations and missing B/L charges differ.
- A mostly elementary fermion with hadronic dressing is a weaker result than deriving the complete fermion from one string/dual theory.
- Exact duality preserves parity, charges, and physical observables. Shared mass formulas or representation counts are preliminary evidence at most.
- The historical anchor is J. H. Schwarz, *Dual quark-gluon model of hadrons* (1971), supplied by the user, plus the related work with Joel Scherk to identify. Keep separate records for quark–gluon, quark–diquark, and lepton–meson proposals.

## Stages, deliverables, and decision points

| Stage | Concrete work and deliverable | Advance when | Reject or revise when |
| --- | --- | --- | --- |
| 0. Sources and independent baseline | Preserve this version in Git. Obtain Schwarz's primary text and identify the Scherk papers. When the user's drafts arrive, create a comparison matrix: operator definitions, equations, claims, evidence, and genuine differences. | The historical target and missing-draft comparison are traceable to actual text. | A recalled claim is not in the source; correct the attribution without changing the physics to force agreement. |
| 1. One complete operator dictionary | Write the fields/charges, gauge group and its global quotient, fermion parity, spin/parity and chiral representations, and all carrier sectors. Specify physical endpoints versus Chan–Paton labels. Apply Pauli symmetry. | Both odd branches exist with consistent interactions and no concealed charge deficits. | The same conserved carrier is assigned incompatible B/L, an even operator is called odd, or a forbidden scalar flavor channel is used. |
| 2. Minimal dynamical model | Choose a 4D EFT or controlled dual model. Compute the renormalized matrix of two-point functions for elementary and candidate composite operators, then a probe-current three-point function and one four-point process. Report poles, residues, Ward identities, and extra states. | The proposed fermion is a specified state with calculable currents, and the extent of elementary input is explicit. | The “new particle” is just an existing quark with even dressing, or the only pointlike component was independently inserted without explanation. Such a result may still support the weaker correspondence. |
| 3. Scale and coupling separation | Fix a hadronic spectrum/slope and declare a fermion scattering interval, angular range, and tolerance. Compute finite-energy behavior, resonance production, transitions, and radiative stability of any small overlap. | Extended bosons and the desired fermion behavior coexist over that interval in the same model. | A low-energy contact expansion is used above its gap, warping is mistaken for exact elementary scattering, or a tuned cancellation fails loops/channels. |
| 4. Pion and light masses | Derive axial Ward identities and the chiral effective action, including the condensate, chiral-limit pion, explicit-mass dependence, and couplings to the odd sector. Track current, endpoint, constituent, and whole-state masses separately. | The pion's lightness follows from approximate global symmetry and small explicit breaking; fermion masses have their own protection. | A spectral zero or a massless endpoint replaces the Goldstone mechanism, or an odd-sector coupling destroys the needed chiral symmetry. |
| 5A. Controlled gauge dual | Start from a fully specified electric/magnetic example. Track global symmetries, anomalies, superpotential, all light fields, phase changes under deformations, and the scale range of the weak variables. | A controlled path produces the required non-supersymmetric/vectorlike spectrum and both branches, with a shared observable regime. | Decoupling assumed superpartners/flavors changes the phase or rank, or an infrared weak variable is extrapolated above its matching scale. |
| 5B. Geometric alternative | Specify the CP² spinᶜ bundle and gauge embedding, solve background equations and stabilization, compute the full light Dirac spectrum and charge lattice, and derive 4D couplings and masses. | Both up/down charges are light without the minimal circle-momentum obstruction, unwanted modes are accounted for, and the vacuum is supported. | An index is taken as a complete spectrum, an isometry algebra as the full gauge group, or a circle bundle is substituted without recalculating zero modes. |
| 6. Observables and historical assessment | Match the completed candidate to EFT operators or finite-energy amplitudes with conventions. Apply identified datasets/likelihoods for lepton scattering and infrared-safe quark observables. Compare precisely with the historical predictions and missing drafts. | A quantitative viable region and an actual new discriminating prediction exist. | Incompatible benchmark bounds are mixed, an unverified recent number is called a limit, or similarity of terminology is presented as confirmation. |

Stages 5A and 5B are alternative ultraviolet routes. Neither should be assumed to complete the other. Source recovery can proceed alongside stages 1–4, which already have enough information for useful work. A failure at one stage should produce a documented obstruction with its assumptions, not a universal claim against all dual descriptions.

## The next calculation to prioritize

Start with a single vectorlike 4D candidate containing a color-singlet meson sector, the allowed scalar color-3 antidiquark sector, and explicit odd carrier sectors. Before attempting a full compactification:

1. Specify an action or a controlled effective action, its cutoff, and its exact global charges. Decide whether ordinary B and L are separately conserved; this choice changes the number of carriers.
2. Construct the two candidate interpolators and a complete mixing basis. For the colored branch state the gauge/factorization prescription and the physical observable ultimately used.
3. Compute enough of the spectral matrix and current vertices to determine whether the odd pole is emergent, elementary, or an existing quark pole with additional overlap.
4. Calculate one whole-fermion scattering amplitude with the same parameters that control the bosonic sector. Include bosonic exchange, which parity does not forbid. Test the entire claimed energy range, not just its zero-momentum limit.
5. If this produces a protected regime, compute the axial Ward identities and the first radiative corrections to its separation of scales. If it does not, document which assumption failed before enlarging the model.

An ordinary mixing EFT, worked out in [blackboard 002](../blackboard/002_two_branch_dictionary.md), is already a useful calibration: it suppresses the light-state radius by a composite fraction η and one vector-induced four-fermion coefficient by η². It currently fulfills only the weak description. The research task is to derive those ingredients and their stability in the strong description.

## Evidence that would change the current assessment

Positive evidence would include an explicit conserved-charge dictionary, a controlled odd state with a pointlike current over a declared scale window, a simultaneously extended bosonic sector with the pion Ward identities, and a quantitative reason for small unwanted couplings. A fully matched dual pair would be substantially stronger than any one of these checks.

Negative evidence includes a required odd carrier that carries the wrong exact charge; a light hadronic resonance with unsuppressed fermion coupling; unavoidable extra light states; or the absence of a supported light-quark compactification. Each eliminates a specified candidate, not the entire research direction.

## When the missing drafts arrive

Preserve the independent PDF/source version and its commit. Add the supplied drafts as new references and record their provenance. Compare claims with this reconstruction before editing either. Classify each important difference as: already established prior work; independent agreement; correction; genuinely new mechanism; or unresolved claim requiring calculation. Only then select the next manuscript version and priority calculation.
