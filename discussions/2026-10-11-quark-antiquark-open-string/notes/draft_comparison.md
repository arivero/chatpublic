# Comparison with the newly supplied PRL/PRD drafts

12 October 2026. Sources: the [12-page PRD, 4-page PRL, and 8-page addendum](../references/received-2026-10-12/README.md). These are supplied drafts, not evidence of journal publication. The independently reconstructed version remains at commit `333e537`, before these PDFs arrived; it was already informed by the two earlier conversations, so agreement is not a blind discovery result.

The originals and the version 0.1 PDF/source are preserved. This note is the first comparison and correction ledger, not a claim that every citation or phenomenological estimate has been audited. Equations susceptible to text-extraction errors were checked on the PDF pages.

## Main comparison

| Topic | Supplied drafts | Independent reconstruction / present assessment | Action |
| --- | --- | --- | --- |
| Charged four-Ramond benchmark | PRD III–V; PRL Eqs. (8)–(22): a gauge amplitude times V(t,u), dimension-eight leading oscillator correction | Agreement within a specified charged same-stack massless sector. This is established amplitude technology, not by itself a new string theory or a universal fermionic suppression. | Retain as the benchmark; explicitly credit Cullen–Perelstein–Peskin and specify the internal state/projection and field-theory exchanges. Chan–Paton charges alone do not fix all compactification-dependent interactions. |
| Common hadronic slope | PRD X; PRL final section: hadronic-scale flat NS/R partners fail the hard-scattering test | Agreement for this benchmark. The source drafts already state much of the limited obstruction; the reconstruction did not discover it from scratch. | Keep the conclusion conditional. It does not exclude every dual QCD, geometric, or noncritical-string route. |
| Fermionic exchange | PRD VI–VII; PRL mixed-channel discussion | Agreement that a fermion can propagate in boson–fermion conversion channels and give a local low-energy limit when heavy. The reconstruction additionally separates an odd mean field, exchange range, and bound-state radius. | Keep these distinctions; do not infer contact range from exclusion statistics or pointlike states from contact forces. |
| Scalar antidiquark and B | PRD VIII–IX has the correct three-flavor Pauli channel and the missing unit of baryon number | Agreement. The reconstruction spells out physical-operator parity and the different B/L requirements of the two branches. | Do not correct the PRD as though it had chosen the wrong scalar Pauli channel; its VIII A is already careful. Distinguish it from the separate SU(5) label-bookkeeping example. |
| Warped average | Addendum 15 develops the radial/Mellin ansatz, UV cutoff, and near-free limits | The reconstruction retained a conservative positive-average calculation and did not promote the weight-to-twist assignment into a derived spinor amplitude. | Preserve useful integral formulas. Derive actual profiles, currents, spinor measures, and a regime of validity before calling this a completed holographic embedding. |
| Lepton branch | Addendum 16 gives chiral bilinears, oriented labels, channels, and candidate observables | This contains more electroweak and phenomenological detail than our deliberately restricted vectorlike construction. Some of it is useful as a later target, not an early requirement. | Separate a two-flavor Dirac/chiral-flavor model from the later weak-sector embedding. Do not make three generations a prerequisite. |
| Generation-dependent labels | Addendum 16.2 contrasts disjoint versus shared endpoint labels in e–mu scattering | A meaningful possible discriminator in a specified brane/gauge embedding; not a derivation of the number of families. | Verify the gauge bosons, mixing, charges, projections, and all surviving amplitudes in a complete example before applying the table universally. |
| KK geometry and weak mixing | CP² × S¹/spinᶜ ingredients, parity/coherence analysis, and the explicit two-state mixing diagnostic are developed further in our notebook | These additions are not a completed model. They identify concrete obstructions and a weaker dressed-elementary interpretation. | Keep them as candidate routes with separate decision points. |

## Corrections that can be made now

### PRL Eq. (11), page 2: beta-function sign

With the printed convention `a+b+c=0`, the gamma recurrence gives

```math
V(a,b)=\frac{\alpha'ab}{c}B(-\alpha'a,-\alpha'b),
```

not the printed denominator `−c`. The gamma-ratio definition and its low-energy limit remain the reference. The short derivation is in [blackboard 004](../blackboard/004_draft_equations.md).

### PRD Eq. (36), page 4: alternating residue sign

For the printed definition of V, the residue is

```math
V(a,b)\sim\frac{\prod_{k=0}^{n-1}(\alpha'b+k)}
{(n-1)!\,\alpha'(a-nM_s^2)}.
```

Remove the extra `(-1)^(n−1)`. This relative level-dependent sign cannot be absorbed in an overall amplitude convention. PRL Eq. (12) already uses the corrected expression. Any physical spin or positivity analysis must include the field-theory numerator and channel structure as well.

### PRL citation numbering

The same-stack/intersecting-brane paragraph on page 2 cites `[9]`, but the printed bibliography lists Antoniadis–Benakli–Laugier as `[8]` and Dosch et al. as `[9]`. The light-front discussion points to `[10]`, which is the PDG entry, while body references to `[11]` have no corresponding bibliography entry in the supplied four-page file. Rebuild citations from stable bibliographic keys when source is available. These are internal citation problems visible in the supplied PDF; no external retrieval is needed to identify them.

### Addendum Eq. (111): preserve its absolute value

The **PDF is correct on this sign**: it prints `b |M(−b;x)|`. The native extraction omits the bars. Since the analytically continued Mellin function is negative for `0<b<2`, using the extracted text alone would falsely suggest an error. We inspected page 3 and did not classify this as a draft mistake.

The omitted boundary case `b=2` has a logarithmic intermediate-regime correction. [Blackboard 004](../blackboard/004_draft_equations.md) derives the finite-cutoff normalization and `δ² log(1/δ)` behavior analytically. This completes the ansatz's cases; it is not a new numerical result or proof of a physical background.

## Claims that need narrower assumptions or a real calculation

**Twist, unitarity, and normalizability (addendum 15.2–15.5).** The four-dimensional conformal spinor bound is a statement about gauge-invariant local conformal operators. It cannot be applied directly to an arbitrary gauge-charged quark. The radial exponent and measure need an actual spinor/background derivation, and a source-plus-normalizable mode decomposition must be specified. The two limiting ways to approach an elementary-looking average are properties of this ansatz, not an exhaustive theorem about possible QCD duals.

**Constituent counting.** The addendum assigns twist two to a state with two resolved antiquarks. If the extra odd carrier is also resolved, it must be counted or otherwise represented in the hard operator. If it is topological or nonlocal, explain the appropriate counting instead of treating it simultaneously as a physical constituent and as absent. The extra power-law estimates are illustrative until the full colored amplitudes and observable definitions are given.

**B−L versus separate B and L (addendum 16.1).** The table uses left-handed fields, including the antiquark fields `u^c,d^c`. Its common `Δ(B−L)=−1` is compatible with that orientation. Our physical-quark map instead needs `Δ(B−L)=+1`; switching to it requires conjugating the relevant carrier or switching the lepton orientation. Moreover, equal B−L does not establish equal B and L separately. A neutrino-like carrier and a baryonic carrier are not automatically the same object when those charges are conserved. Preserve both the charge convention and the chosen global symmetries.

**“One generation” and antisymmetric bilinears (addendum Table 1).** Rows containing flavor-antisymmetric `(d^c d^c)*` or `(LL)*` require at least two distinct copies in those channels; they vanish for a single identical species. The table can list the gauge representations of one generation, but should not imply that all its operators are nonzero using only one generation. Conversely, adding a second copy for one operator does not prove that three generations are required. [Blackboard 003](../blackboard/003_flavor_scaffolding.md) turns this into a staged construction question.

**Extra Chan–Paton partners (addendum 16.2).** The color-octet and sextet decompositions are useful warnings for the stated unprojected label spaces. Mass degeneracy, allowed projections, gauge realization, and phenomenological couplings depend on the actual construction. “The tensor product contains an octet” alone does not establish an unavoidable degenerate lepton-octet in every possible dual model.

**Experimental numbers (PRD XI; addendum Table 2 and 16.4–16.5).** Keep historical fits, other-model exclusion limits, and coupling-based sensitivity estimates separate. Neither a dimension-six limit nor an ADD dimension-eight limit transfers automatically to the string amplitude. Excited-particle limits need production and branching assumptions; magnetic moments need a defined chirality-breaking coupling. The 2025–2026 references in the PDFs have not been verified externally in this session. Nothing in this comparison upgrades their numbers into current model-independent bounds.

**The pion-decay operator (addendum 16.5).** The lepton–meson dictionary can motivate

```math
\frac{c}{\Lambda^2}(\bar u_R d_L)(\bar e_L N_R),
```

but does not by itself imply a nonzero coefficient, `c=1`, or a fixed matching scale. Up to phase conventions,

```math
\left|\langle0|\bar u_R d_L|\pi^-\rangle\right|
=\frac{f_\pi m_\pi^2}{2(m_u+m_d)}.
```

This makes a potentially useful chiral-enhancement test once the operator exists. The decay calculation must state the new neutral state's mass, phase space, and whether it can interfere with the Standard Model final state. A distinct light sterile state, or an orthogonal massless helicity, generally contributes incoherently. The quoted `Λ ≳ 60 TeV` estimate therefore remains conditional and has not been recomputed here. This is a later observable to match, not a reason to force a weak sector into the first strong-sector toy model.

## What the reconstruction adds, and what it does not

The pre-PDF reconstruction provides a readable synthesis of physical endpoint parity, explicit two-branch carriers, the positive-average bound, vectorlike chiral symmetry, spinᶜ/KK obstacles, and an elementary/composite mixing diagnostic. Much of its scattering content was already in the supplied conversations and drafts. It does not establish new priority for the Veneziano factor, its low-energy expansion, or a QCD dual.

The current useful development is a clearer staged question: two flavors suffice for a pion/lepton–meson test, while three flavors give full scalar-antidiquark closure with one neutral flavor-singlet carrier. This is a model-building constraint with explicit alternatives, not a proof of three Standard Model generations. The next substantive target remains a model-derived odd-state current or amplitude, with a reason for the required suppression of hadronic structure.

## Revision priorities

1. Correct the two displayed signs and repair PRL citation numbering in a future source revision; retain the originals for comparison.
2. Reframe the initial physics target as the smallest viable two-flavor meson/odd-sector theory and an optional three-flavor antidiquark extension.
3. Supply a real operator/current calculation before promoting the radial weight or a carrier label to a construction.
4. Keep the addendum's weak-sector and experimental material as conditional later tests, with source retrieval and matching still required.
5. Add a concise AI-assisted-research provenance paragraph, using the [annotated bibliography](ai_research_bibliography.md) and [research protocol](research_protocol.md), without presenting script counts or benchmark success as proof of new physics.
