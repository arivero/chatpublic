# Checks: executed and proposed

Numbers in this note come from `../calculations/audit_output.txt` (script `../calculations/audit.py`, inputs in `../data/`). Labels: R1 is v = 2 M(132Sn); R2 is M_Z + M_H = M(100Sn) + M(132Sn); R3 is 2 m(D0) = M(alpha). "Atomic" masses are the AME2020 values; "nuclear" masses subtract the Z electrons and add their binding energy.

## What the executed checks establish

1. The headline offsets of R1 and R2 belong to one convention (atomic masses, Breit-Wigner Z mass, PDG 2025). Legitimate alternatives give +0.11% to +0.22% for R2 and +0.19% to +0.21% for R1.
2. In units of u the offsets of R1 and R2 are 0.25 u and 0.45 u, which is 49% and 89% of the nucleon-number rounding limit. The distinguishing content of the tin relations sits in the equality of their two fractional offsets and in the fact that 132 and 232 are sums of magic numbers fixed in 2003.
3. That equality, written as (M_Z + M_H)/v against 29/33, has stayed within 1 sigma of the measured Higgs mass in every PDG edition since 2016, with the closest agreement in 2018, and now sits at -0.5 sigma (PDG 2026) and -1.4 sigma (LHCP 2026 preliminary combination).
4. A change of v at fixed dimensionless couplings makes R1 and R2 exact at the same point to 0.008% in ln v. R3 becomes exact about 0.16% away from that point (K_D = 0.85).
5. The ground-state Q-value of binary fission is largest for a tin-like heavy fragment (A_H = 130 to 132, Z_H = 50) across the actinides. The Te branch (A_H = 134, Z_H = 52) lies within 0.2 to 4 MeV.
6. The measured Standard I position is constant in charge, Z_H = 52.7 +- 0.6 over 15 neutron-deficient systems. The masses implied by the unchanged-charge-density rule average 132.6 u, which is 1.8 u below the Higgs value and 0.6 u above the mass number of 132Sn.

## Executed

### E1. Offsets across conventions

| masses | Z mass | R1 | R2, M_H = 125.20 | 125.13 | 125.09 |
| --- | --- | --- | --- | --- | --- |
| atomic | Breit-Wigner 91.1880 | +0.186% | +0.192% | +0.160% | +0.141% |
| atomic | pole 91.1539 | +0.186% | +0.176% | +0.144% | +0.125% |
| nuclear | Breit-Wigner | +0.207% | +0.216% | +0.183% | +0.165% |
| nuclear | pole | +0.207% | +0.200% | +0.168% | +0.149% |

The ratio (M_Z + M_H)/v minus 29/33 depends only on the boson inputs: +0.53e-4, -2.31e-4, -3.93e-4 (Breit-Wigner Z mass, M_H = 125.20, 125.13, 125.09) and -0.85e-4, -3.69e-4, -5.32e-4 (pole Z mass). The tin ratio (M(100Sn) + M(132Sn))/(2 M(132Sn)) equals 0.878791 with atomic masses (29/33 + 3.9 ppm) and 0.878766 with nuclear masses (29/33 - 24.6 ppm). The Z-mass convention alone moves the exact-rational prediction M_H = (29/33) v - M_Z from 125.187 to 125.221 GeV.

### E2. The ratio through the PDG editions

| Edition | M_H (GeV) | R2 offset | (M_Z + M_H)/v - 29/33 | sigma |
| --- | --- | --- | --- | --- |
| 2014 | 125.7 +- 0.4 | +0.424% | +2.08e-3 | +1.28 |
| 2016 | 125.09 +- 0.24 | +0.141% | -3.95e-4 | -0.41 |
| 2018 | 125.18 +- 0.16 | +0.183% | -2.9e-5 | -0.05 |
| 2020 | 125.10 +- 0.14 | +0.146% | -3.54e-4 | -0.62 |
| 2022 | 125.25 +- 0.17 | +0.215% | +2.55e-4 | +0.37 |
| 2024 and 2025 | 125.20 +- 0.11 | +0.192% | +5.35e-5 | +0.12 |
| 2026 | 125.13 +- 0.11 | +0.160% | -2.31e-4 | -0.52 |
| LHCP 2026 preliminary ATLAS+CMS | 125.09 +- 0.07 | +0.141% | -3.94e-4 | -1.38 |
| CMS, 2 November 2026 | 125.065 +- 0.088 | +0.130% | -4.95e-4 | -1.39 |

The value quoted for 2025 (5e-5) sits among several of similar size; the 2018 edition was closer. The statistical resolution of the ratio is 4.5e-4 at the present PDG M_H uncertainty, 8.4 times the 2025 deviation. The pulls of the four exact completions against the newest values are listed in audit section 7 and in `05_review.md`.

### E3. Offsets in units of u

| Quantity | Offset | In u | Fraction of the 0.5 u limit |
| --- | --- | --- | --- |
| R1: v/2 - M(132Sn) | +229.1 MeV | +0.246 | 0.49 |
| R2: M_Z + M_H - M(100Sn) - M(132Sn) | +415.1 MeV | +0.446 | 0.89 |
| M_H - M(132Sn) | +2319 MeV | +2.490 | 4.98 |
| M_Z - M(100Sn) | -1904 MeV | -2.044 | 4.09 |

The limit of 0.5 u corresponds to 0.215% of M_Z + M_H, 0.378% of v/2 and 0.372% of M_H. Without mass defects the offsets of v/(2u) from 132 and of (M_Z + M_H)/u from 232 are +0.164 u and +0.302 u. The integers 132 and 232 are therefore the nearest integers to the two boson combinations, and the pair sum reaches the rounding limit of its own granularity; the single offsets (+2.49 u and -2.04 u) cancel down to it. The second feature is the common fractional offset: v/(264 u) - 1 = +0.124% and (M_Z + M_H)/(232 u) - 1 = +0.130%. Both combinations are multiples of one unit, v/264 = 932.65 MeV and (M_Z + M_H)/232 = 932.71 MeV, which exceeds u by 0.12% and M(132Sn)/132 = 930.91 MeV by 0.19%. The charm relation has no integer freedom, so the rounding limit is irrelevant for R3.

### E4. R1 expressed as alpha_s(M_Z)

Two-loop running with n_f = 5 gives d ln Lambda_5 / d alpha_s = 56 at alpha_s = 0.118. The thresholds at m_b and m_c carry this to the nucleon scale with Lambda_3 proportional to Lambda_5^(23/27), giving d ln m_N / d alpha_s = 48. The R1 offset (0.186%) is then delta alpha_s = 3.9e-5, and one unit of mass number at A = 264 (0.38%) is delta alpha_s = 7.9e-5. The PDG uncertainty (+-9e-4) spans about 23 consecutive integers. Running alone therefore carries no preference for 132 over its neighbours; the preference enters through the doubly magic character of 132Sn.

### E5. The charm remainder in context

2 m(D0) - M(alpha) = 2.301 MeV (0.0617%), 23 standard deviations of the D0 mass (+-0.05 MeV in PDG 2025 and +-0.04 in PDG 2026, central value 1864.84 in both). The same remainder equals 8.1% of B(alpha) = 28.296 MeV, a shift of the charm mass by 1.15 MeV (0.09% of the MSbar mass 1.273 GeV, y_c = 7.31e-3), 1.78 times m_n - m_p (1.293 MeV) and 0.48 times m(D+-) - m(D0) (4.822 MeV). m(D0) lies 1.150 MeV above M(alpha)/2. The charged threshold 2 m(D+) lies 11.94 MeV above M(alpha). Corollaries of R1 and R3 together: v/m(D0) = 132.03 (observed) against 4 M(132Sn)/M(alpha) = 131.87; the two differ by the factor (1 + R1 offset)/(1 + R3 offset) = 1.00125.

### E6. Q-value landscape of binary fission (AME2020, best Z_H for each A_H)

| Parent | Local maxima of Q over even A_H (MeV) | Q at A_H = 132, 134, 138, 140 | Symmetric Q |
| --- | --- | --- | --- |
| 226Th | A_H = 130 (Z_H = 50) 188.8; 134 (Z_H = 52) 188.6 | 187.2, 188.6, 182.9, 179.4 | 180.7 |
| 232Th | 132 (Z_H = 50) 188.4 | 188.4, 184.4, 180.0, 177.2 | 179.3 |
| 236U | 132 (Z_H = 50) 199.3 | 199.3, 196.6, 189.4, 188.3 | 193.2 |
| 240Pu | 132 (Z_H = 50) 210.3 | 210.3, 208.8, 201.7, 199.5 | 204.4 |
| 252Cf | 130 (Z_H = 50) 236.8 | 236.5, 234.0, 226.2, 224.7 | 234.3 |

The cold-energy ridge sits at the tin-like split (A_H = 130 to 132); for 226Th the Te branch at A_H = 134 matches it within 0.2 MeV. The symmetric split of the fermium isotopes into two tin isotopes has Q = 248.8, 252.2, 252.5, 251.6 (estimated), 254.4 (estimated), 256.0 (estimated) MeV for A = 252, 256, 257, 258, 259, 260: a smooth rise with no feature at 258Fm. The sharp change at 258Fm is a barrier and shape phenomenon, with partial spontaneous-fission half-lives of 131 years (257Fm, from the 0.210% branch in NUBASE2020) and 0.37 ms (258Fm).

### E7. Heavy-fragment mass if the proton number is fixed

Prediction table for parents beyond those of Table 1. Unchanged charge density with the round values Z_H = 52.5 (Standard I) and 55 (Standard II) quoted in the text of the GSI paper, against a fixed A_H = 134.4 for the Higgs mass:

| Parent | A/Z | A_H (S1) | A_H (S2) |
| --- | --- | --- | --- |
| 222Th | 2.467 | 129.5 | 135.7 |
| 226Th | 2.511 | 131.8 | 138.1 |
| 230Th | 2.556 | 134.2 | 140.6 |
| 232Th | 2.578 | 135.3 | 141.8 |
| 233U | 2.533 | 133.0 | 139.3 |
| 235U | 2.554 | 134.1 | 140.5 |
| 238U | 2.587 | 135.8 | 142.3 |
| 239Pu | 2.543 | 133.5 | 139.8 |
| 252Cf | 2.571 | 135.0 | 141.4 |
| 258Fm | 2.580 | 135.4 | 141.9 |

A fixed proton number moves A_H(S1) by 6.3 u across these parents; a fixed mass keeps it at 134.4. The S1 line reaches 134.4 at A/Z = 2.560 (230Th, 235.5 for U). The two hypotheses separate most clearly in the neutron-deficient thorium isotopes (222Th to 226Th: 129.5 to 131.8 against 134.4).

### E7b. What the measured heavy-fragment positions say

Table 1 of Boeckstiegel et al. (Nucl. Phys. A 802 (2008) 12, arXiv:0712.3808) lists 15 neutron-deficient systems (222 to 226 and 228Th, 228 to 232Pa, 232 to 234U, 223Ac). The measured quantity is the nuclear charge of the heavy fragment: Z_H(S1) = 52.73 +- 0.58 (range 51.8 to 53.8) and Z_H(S2) = 55.18 +- 0.57 (range 54.4 to 56.2), which is the constancy in element number reported in the abstract. Masses follow from the unchanged-charge-density rule A_H = Z_H A/Z with evaporation neglected, as in the paper. The conversion gives A_H(S1) = 132.60 +- 1.40 (range 130.3 to 134.6) and A_H(S2) = 138.75 +- 1.36. Five systems (234U, 232Pa, 228Th, 226Th, 225Th) have A_H(S1) within 1 u of the Higgs value 134.4; the mean lies 1.8 u below it (123.5 GeV against 125.2 GeV) and 0.6 u above the mass number of 132Sn. The asymmetric share (100 minus the super-long yield) reproduces the series quoted in feedback A: 11.8, 16.0, 24.2, 31.4, 44.4, 62.5% for 222, 223, 224, 225, 226, 228Th and 82.1, 86.2, 88.8% for 232, 233, 234U. For 226Th the table gives S1 31.2 +- 7.4%, S2 13.2 +- 7.3%, super long 55.6 +- 0.4%, with Z_H = 53.6 +- 0.3 and 55.7 +- 0.3, so the mass conversions of feedback A (134.6 and 139.9) are reproduced. The paper states that the relative weights of the two asymmetric channels carry large errors because the dispersion of the kinetic energy was not measured.

Reading: the data fix Z_H and the masses carry the model dependence of the conversion (about 2 u for neutron-deficient parents, where charge polarization and the N = 82 shell pull the neutron number up). A decision between a fixed-mass and a fixed-charge ridge needs mass- and charge-resolved yields (Lohengrin for thermal fission, VAMOS for transfer-induced fission, SOFIA in inverse kinematics).

### E8. One-parameter family

Vary v with Yukawas, gauge couplings, lambda and the ultraviolet QCD coupling held fixed. Then v, M_Z, M_H and the quark masses scale as v, while nuclear masses scale as v^K_A with K_A near 0.3 (trace anomaly 2/9 plus the sigma term). The ratios R1 = 1.001865 and R2 = 1.001922 fall below unity as v decreases, with exponent 1 - K_A. For K_A = 0.27, 0.30, 0.33 the equalities R1 and R2 become exact at delta ln v = -0.255%, -0.266%, -0.278% and -0.263%, -0.274%, -0.287%, separated by 0.008% in every case. The location of the common crossing moves by 0.02% across this range of K_A, and the separation between the two crossings stays at 0.008%. For R3 the exponent difference is K_D - K_alpha with K_D from the heavy-quark expansion m_D = m_c + Lambda-bar (0.75 to 0.92): the crossing lies at -0.137%, -0.112%, -0.100%. R3 would cross together with R1 and R2 if K_D were 0.53.

### E9. The subshell rectangles of the November 2003 text

Reading the construction of `sources`-cited arXiv:nucl-th/0312003v1 (section 4 to 5): proton and neutron subshells below each doubly magic corner give the mass-number intervals [82, 100] (5g9/2 square), [112, 132] (5g9/2 protons by 6h11/2 neutrons, the "10 x 12 rectangle") and [184, 208] (6h11/2 by 7i13/2). Positions in mass number: W 86.3, Z 97.9 and the top 187.1 (2003 values) or 185.3 (PDG 2025) lie inside their intervals; the LEP hint (115 GeV, 123.46 u) lies inside [112, 132] with 8.5 u to spare; the measured Higgs mass (134.41 u) lies 2.4 u above the upper edge. The tin relations R1 and R2 therefore carry a different statement from the 2003 bracketing: nearest-nucleus mass matches to the corner nuclei.

### E10. Near-zero thresholds in AME2020

Experimental entries only, with combined uncertainty below half the window. Particle thresholds within 6 keV: none for S_n, S_p, S_2n, S_2p and S_alpha. Within 20 keV: one entry (S_p). Within 60 keV: S_n one, S_p three, S_alpha five, S_2n and S_2p none. Weak-decay thresholds within 6 keV: 187Re -> 187Os (Q = +2.47 keV) and 163Ho -> 163Dy (Q_EC = +2.83 keV); the next pairs lie at 6.15 keV (222Rn, 222Fr), 6.93 keV (243Am, 243Cm) and 18.59 keV (3H -> 3He). A separation energy of 8 MeV scaling as Lambda_QCD, v^(2/9), has a sensitivity of 1.8 MeV per unit ln v, so a nuclide 5.3 keV from a threshold changes status within 0.3% of v. Weak thresholds respond more strongly, through m_d - m_u and m_e, with slopes of order 1 to 5 MeV per unit ln v. This table supplies the width scale for any selection argument built on a nuclear threshold (`03_mechanisms.md`, section 3).

### E11 and E12 (second pass)

The fusion-side comparisons (all heavy-meson masses and pair thresholds against light nuclei; the charm remainder against 19 light-nucleus and fusion energies) are audit section 14. The asymmetric share against parent mass and neutron number is audit section 15. Both are discussed in `05_review.md`, sections 3 and 4. The ENDF/B-VIII.0 yield centroids and maxima are in `../calculations/fission_yields_output.txt`.

## Proposed

1. **Exact-rational test of M_H.** The relation (M_Z + M_H)/v = 29/33 predicts M_H = 125.187 GeV (Breit-Wigner M_Z) or 125.221 GeV (pole M_Z). PDG 2026 gives 125.13 +- 0.11 and the LHCP 2026 preliminary combination 125.09 +- 0.07. A resolution of 0.02 to 0.03 GeV separates the two conventions and tests the relation at the 0.1 sigma level; published projections for the HL-LHC and for an e+e- Higgs factory are in that range (to be confirmed before quoting).
2. **Mass against charge in the heavy fragment.** Compare measured primary A_H and Z_H of the Standard I mode along isotopic chains (thorium 222 to 232, uranium 232 to 238) with the two columns of E7. The GSI secondary-beam data (Schmidt et al. 2000; Boeckstiegel et al. 2008) fix the charge; the mass- and charge-resolved yields of Lohengrin, VAMOS and SOFIA decide. A branch that stays at A_H = 134.4 while the parent N/Z changes supports a fixed-mass mechanism; a branch that follows Z_H = 52.5 supports the shell-structure reading.
3. **State the convention.** Quote R1 and R2 with nuclear masses (electron binding included), the Z pole mass and the Higgs mass value, together with the edition. The 0.19% of the brief equals the atomic, Breit-Wigner, PDG 2025 member of a family spanning 0.11% to 0.22%.
4. **Ratio form.** Express the sharp content as (M_Z + M_H)/v = (A_1 + A_2)/(2 A_H) with the quantity on the left written for physical observables (G_F, pole masses). Both sides then carry convention-free uncertainties; today the left side is 4.5e-4.
5. **Repeat E2 and E8 with each new Higgs-mass, W-mass and top-mass release.** The inputs for E8 (K_A, K_D) can be tightened with chiral-EFT sensitivities of the binding energy to the pion mass.
