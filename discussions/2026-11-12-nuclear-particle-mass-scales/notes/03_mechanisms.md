# Mechanisms: requirements and the state of the candidates

Numbers come from `../calculations/audit_output.txt`; section labels (E1 ... E10) refer to `02_checks.md`. The complete catalogue of suggested explanations, with attribution to the brief, the 2003 text and feedbacks A and B, is `05_review.md`, section 5.

## 0. What a mechanism has to deliver

| Relation | Content | Precision to reproduce | Parameter pinned |
| --- | --- | --- | --- |
| R1 | v = 2 M(132Sn) | +0.19%, which is delta alpha_s(M_Z) = 3.9e-5; neighbouring mass numbers are 7.9e-5 apart (E4) | v / Lambda_QCD |
| R2 | (M_Z + M_H)/v = 29/33 | measured to 4.5e-4 today; crossing point shared with R1 to 0.008% in ln v (E8) | lambda at given g, g' |
| R3 | 2 m(D0) = M(alpha) | remainder 2.30 MeV, a 0.09% shift of m_c (E5) | y_c v / Lambda_QCD |

Three constraints from the brief shape every candidate. Baryon number forbids the mixing of a B = 0 boson with a nucleus. The exchange propagators carry the momentum transfer (about 250 MeV) and contain no nuclear rest mass. The Higgs couples coherently to a nucleus with K_A = d ln M_A / d ln v near 0.3 (2/9 from the trace anomaly plus the sigma term), giving g_hAA = 0.154 for 132Sn. Ordinary variation of v at fixed couplings passes through the tin equalities with slope 1 - K_A = 0.7 and no stationary point.

## 1. Relations among parameters

* **Infrared matching.** The logarithm ln(v / Lambda_QCD) is near 7, so 0.19% in v / Lambda_QCD is 0.033% in alpha_s. A relation imposed in the ultraviolet (unification, a calculable coupling in a string vacuum, a fixed point) reaches the infrared through threshold and two-loop terms uncertain at about 1e-3 in alpha_s. A candidate formula reproduces R1 when it comes with the infrared calculation at the 3e-5 level.
* **Scheme.** M_Z/v and M_H/v at tree level depend on the scheme at the 1e-3 level. The 34 MeV between the Breit-Wigner and the pole Z mass alone shifts (M_Z + M_H)/v by 1.4e-4, which exceeds the 5e-5 agreement of PDG 2025. A relation stated for physical observables (G_F, pole masses) removes this freedom; the exact-rational prediction then reads M_H = 125.187 or 125.221 GeV depending on the Z mass used.
* **The Higgs slot.** M_H/v = 0.5085, so lambda = 0.1293 lies 3.4% above 1/8 and M_H lies 1.7% above v/2. R1 gives v/2 = 1.0019 M(132Sn). The 2003 association of the Higgs with 132Sn therefore equals R1 together with lambda near 1/8, and the 2.09 GeV displacement of M_H above v/2 is the radiative correction to be accounted for. R2 states that the Z is displaced below 100Sn by 1.90 GeV, within 0.19 GeV of the displacement of M_H above v/2.
* **Trace reading of R2.** Two levels with diagonal entries M(100Sn) and M(132Sn) and an off-diagonal element V have eigenvalues whose sum equals the sum of the diagonal entries. The measured pair (M_Z, M_H) flanks the diagonal entries, and the sum differs by 0.19%. The pattern is the Schur-Horn pattern for a 2 x 2 Hermitian matrix. A physical realisation requires a B = 0 and a B = 100 or 132 state to mix, which the first constraint excludes. The reading remains a bookkeeping device with one free number (V^2 = 67 GeV^2 from the difference, 22 GeV^2 from the product, a spread that shows the 0.19% trace mismatch).

## 2. States carrying the nucleus's own baryon number

Take a branch X_A with B = A and the quantum numbers of the nucleus, with mass M_X proportional to v^K_X. The crossing M_X = M_A is a point in v. At the observed v the splitting is M_X - M_A = (K_X - K_A) x 0.27% x M_A = 0.33 GeV x (K_X - K_A). A state whose mass comes entirely from the Higgs (K_X = 1) at this splitting has a Yukawa coupling y_X = sqrt2 M_A / v = 0.71 for 132Sn, which makes M_X = v/2 a restatement of R1. Nuclear excited states differ from the ground state by slopes of a few MeV per unit ln v, so K_X - K_A is of order 4e-5 and a crossing within 0.3% of v requires the excitation to start within about 15 keV of the ground state. No B = 132 state of the Standard Model other than the nucleus and its excitations exists near 123 GeV. A hidden baryonic sector with a B = A bound state would need a portal that carries the baryon number across, and the audit finds no such candidate.

## 3. Selection with a sharp feature

A dynamical v (relaxion-like scan, cosmological selection) needs a weight W(v) with a feature of width at most 0.3% in v: R1 and R2 sit at -0.27% from the crossing, R3 at -0.11% (K_D = 0.85).

* **Nuclear thresholds.** A separation energy of 8 MeV scaling as Lambda_QCD, v^(2/9), has the sensitivity 1.8 MeV per unit ln v, so a nuclide within 5 keV of a threshold flips within 0.3% of v. The experimental entries of AME2020 hold no nuclide within 6 keV of a one- or two-nucleon or alpha threshold; within 60 keV there are one for S_n, three for S_p (one within 20 keV) and five for S_alpha (E10). Two isobar pairs lie within 6 keV of a weak-decay threshold: 187Re -> 187Os (Q = +2.47 keV) and 163Ho -> 163Dy (Q_EC = +2.83 keV). Weak thresholds depend on v through m_d - m_u and m_e with a slope of order 1 to 5 MeV per unit ln v, so these two flip within 0.05% to 0.3% of v. The sharpest threshold features in the table are therefore as narrow as the offsets of R1 to R3, and no link of either pair to tin or charm is known.
* **Windows.** The published windows cited in the brief are 8 to 90 times wider than the offsets, which makes them about 1.5% to 17% of v.
* **Charm.** The open-charm threshold coincides with the alpha mass; no nuclear process depends on 2 m(D0) - M(alpha).

## 4. Light or hidden mediators

* **Dilaton-like Higgs.** A scalar with decay constant f = v coupling to the trace of the energy-momentum tensor couples to a nucleus with M_A / v = 0.50 for 132Sn (0.154 in the Standard Model). The nucleon-pair contact strength (m_N/v)^2 / m_H^2 = 9.3e-10 GeV^-2 stays 2.8e-12 of sigma exchange (330 GeV^-2 for g_sigma = 10, m_sigma = 0.55 GeV). The effect on nuclear structure stays negligible; the larger coupling would matter for the Higgs interaction with a coherent nuclear source.
* **Z coupling.** The coherent vector coupling of 132Sn is g_Z Q_W = 14.8, above 4 pi. The nuclear form factor cuts the amplitude at q of order 1/R, about 30 MeV, three thousand times below M_Z. The contact energy is 0.9 eV per nucleon (feedback B).

## 5. Summary

| Class | Respects the constraints | Needed sharpness | Status |
| --- | --- | --- | --- |
| Parameter relation | yes | infrared matching at 3e-5 in alpha_s, scheme-free statement for lambda | no formula; the exact-rational M_H prediction is testable |
| Baryon-number branch | yes if a B = A state exists | splitting below 0.3 GeV at the crossing | no candidate state; trace reading is formal |
| Selection | yes | feature of width 0.3% in v | the sharpest known features (187Re, 163Ho) are 0.05% to 0.3% wide and unrelated to tin or charm |
| Light mediator | yes | contact strength within a few orders of sigma exchange | the dilaton-like Higgs reaches 3e-12 of sigma exchange; negligible for nuclear structure |

## 6. What would change the assessment

1. An explicit B = A state or collective branch with K_X - K_A of order 1 near 123 GeV.
2. A complete ultraviolet-to-infrared calculation that returns v / Lambda_QCD (or alpha_s) to 3e-5 and a selection rule for the integer 132.
3. A measurement of M_H at 0.02 to 0.03 GeV, which fixes the Z-mass convention and tests the exact rational.
4. Mass-resolved Standard I yields along isotopic chains (fixed mass against fixed charge).
5. A threshold feature tied to 132Sn or to the charm mass with a width below 0.3% in v.
