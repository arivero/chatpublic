# Audit and errata

Scope: every number of the brief and of the two feedback transcripts (`../sources/`) was recomputed with `../calculations/audit.py` from the inputs in `../data/`, and every literature claim was compared with a primary source (PDG tables, NUBASE2020, arXiv and journal texts). A background agent read the fission papers, ENSDF levels and the evaluated yield libraries; its findings are marked "(agent)" where this note relies on them without having re-read the source. Labels: ok, convention (the number holds in one convention), qualified, corrected, unverified. A second pass (`04_error_check.md`) reversed three verdicts on feedback B and revised two statements about the brief; the rows below carry those revisions.

## 1. The brief

### 1.1 Numbers that reproduce

| Statement | Brief | Recomputed | Label |
| --- | --- | --- | --- |
| v from G_F | 246.220 GeV | 246.2196 | ok |
| 2 M(132Sn) | 245.761 GeV | 245.761 (atomic) | ok |
| v / 2M(132Sn) - 1 | +0.19% | +0.186% atomic, +0.207% nuclear | convention |
| M(100Sn) + M(132Sn) | 215.973 GeV | 215.973 atomic, 215.922 nuclear | ok |
| (M_Z + M_H) / sum - 1 | +0.19% | +0.192% atomic, +0.216% nuclear | convention |
| M_Z against 100Sn, M_H against 132Sn | -2.0%, +1.9% | -2.05%, +1.89% | ok |
| W, Z, H, top in mass number | 86.3, 97.9, 134.4, 185.3 | 86.28, 97.89, 134.41, 185.25 (PDG 2025) | ok |
| top against 208Pb | -11% | -10.9% | ok |
| 115 GeV against 132Sn | -6.4% | -6.41% | ok |
| v / u | 264.3 | 264.33 | ok |
| lambda = M_H^2 / 2v^2 | 0.129 | 0.1293 | ok |
| g_hNN = 0.305 m_N / v; 132 g_hNN | 1.2e-3; 0.15 | 1.16e-3; 0.154 | ok |
| 2 m(D0) - M(alpha) | 2.3 MeV (0.06%) | 2.301 MeV (0.0617%) | ok |
| D0 against the deuteron | -10.8 MeV (0.6%) | -10.77 MeV (-0.57%) | ok |

Not recomputed in detail: the contact-strength ratios (4e-8 and 2e-13; hand estimates with g_omega^2 of 112 to 250, g_sigma^2 = 100 and g_hNN = 1.16e-3 give 1e-8 and 3e-13, the same orders), the anthropic-window factors, the chiral-EFT and lattice statements.

### 1.2 Qualifications and corrections

1. **Convention of the 0.19%.** Both offsets belong to atomic masses, the Breit-Wigner Z mass and PDG 2025. Nuclear masses give +0.207% and +0.216%; the Z pole mass lowers R2 by 0.016%; the PDG 2026 Higgs mass lowers it by 0.032%. The family of legitimate choices spans +0.11% to +0.22% (`02_checks.md`, E1).
2. **The sentence on sharp statements.** The brief names the pair sums at 0.19% as sharp. In mass-number units the R2 offset is 0.446 u, which is 89% of the 0.5 u granularity limit (0.215% of M_Z + M_H); the R1 offset is 0.246 u, 49% of the limit. The two single offsets (+2.49 u for H, -2.04 u for Z) exceed the limit four to five times and cancel down to it. The features that exceed the granularity are the equality of the two fractional offsets (v/(264 u) - 1 = +0.124% against (M_Z + M_H)/(232 u) - 1 = +0.130%) and the charm remainder of 2.30 MeV, which has no integer freedom. Quoting the ratio form (M_Z + M_H)/v = 29/33 puts the sharp content in one line. Second pass: this bookkeeping applies to a pair chosen to fit. The pair of the brief was named in 2003, before the Higgs mass was known, so the 0.19% measures the distance to a preset target, and the sentence of the brief holds in that reading.
3. **The 2003 criterion.** The text of arXiv:nucl-th/0312003v1 (30 November 2003) compares the boson masses with the mass-number intervals of the subshell rectangles that end at the doubly magic corners: [82, 100], [112, 132] and [184, 208]. The 115 GeV hint (123.46 u) lies inside [112, 132]. W (86.3 u), Z (97.9 u) and the top (187.1 u in 2003, 185.3 u now) lie inside their intervals. The measured Higgs mass (134.41 u) lies 2.4 u above the upper edge. The named nuclei serve as the corners of the intervals; the nearest-nucleus matches R1 and R2 (2026) form a second statement. The abstract of hep-ph/0405076 (10 May 2004) lists 246 GeV among the drip-line masses 45, 68, 92, 115, 175 and 246 GeV.
4. **Fermium.** NUBASE2020: 256Fm 157.1 min (SF 91.9%), 257Fm 100.5 d (alpha 99.790%, SF 0.210%), 258Fm 370 microseconds (SF about 100%), 259Fm 1.5 s (SF 100%); 260Fm is unmeasured. The spontaneous-fission partial half-life of 257Fm is 131 y, so the step to 258Fm is a factor 1.1e13. The fragments of symmetric 258Fm fission have A = 129 (Z = 50, N = 79); the AME2020 table ends at 260Fm, with the masses of 258Fm to 260Fm estimated from systematics, and has no entry for 264Fm.
5. **The heavy-fragment ridge.** In the GSI secondary-beam data the measured quantity is the charge; for U, Pu and Cf the fragment masses are measured directly. In 15 neutron-deficient systems Z_H(S1) = 52.73 +- 0.58 and Z_H(S2) = 55.18 +- 0.57 (Boeckstiegel et al. 2008, Table 1). The mass numbers 133 to 136 hold for U to Cf parents when the charge is converted; for the thorium and protactinium systems of Table 1 the conversion gives 130.3 to 134.6 (mean 132.6). Literature positions of the modes: S1 132.0 to 135.7, S2 138.0 to 143.3 (agent; a compilation that includes Brosa et al. 1990).
6. **Pre-neutron and post-neutron masses.** The fragment masses quoted from radiochemistry and from yield libraries are post-neutron values, lower than the primary masses at scission by about 1 to 2 u for the heavy fragment. Every A_H quoted against the Higgs mass should carry that label. ENDF/B-VIII.0 gives the single-mass maximum of the 235U thermal heavy yield at A = 134 (post-neutron) and the heavy hump centroid at 138.7 (agent).

## 2. Feedback A

| Claim | Check | Label |
| --- | --- | --- |
| v - 2M(132Sn) = 458.68 MeV; sum offset 414.69 MeV | 458.3 and 415.06 MeV (differences 0.4 MeV from v and M_Z rounding) | ok |
| m_H = v - m_Z + M(100Sn) - M(132Sn) = 125.244 GeV; residual -44 MeV | 125.243 GeV; -43.2 MeV | ok |
| 2 m_p + 2 m_n - 2 m_D0 = 25.995; B_alpha = 28.296; remainder 2.301; charged threshold 11.945 MeV above | 25.995; 28.296; 2.301; 11.941 | ok |
| Lambda_3 proportional to Lambda_4^(25/27) m_c^(2/27) | follows from continuity of alpha_s at m_c with 9 ln(m_c/Lambda_3) = (25/3) ln(m_c/Lambda_4) | ok |
| 257Fm: alpha dominated, SF 0.210%, partial half-life about 131 y | NUBASE2020 | ok |
| lobe table (132Sn+100Zr, 134Te+98Sr, 134Sn+98Zr offsets) and 19.22 MeV for 100Sn to 100Zr | reproduced to 1 MeV; sums 0.434, 0.430, 0.429 GeV | ok |
| 226Th channels 55.6 / 31.2 / 13.2%; masses 134.6 and 139.9 | Table 1 of arXiv:0712.3808 (S1 53.6, S2 55.7 in Z; UCD conversion) | ok |
| asymmetric shares 11.8 ... 62.5% (Th) and 82.1, 86.2, 88.8% (U) | equal to 100 minus the super-long yields of Table 1 | ok |
| heavy charge uncertainty of 0.75 nucleons | 0.3 charge units times A/Z = 2.51 | ok |
| Dubray et al.: minima 113+113, 132+94, 145+81; fragments compact near A = 86 and 130 | arXiv:0712.0252 (Gogny D1S, 226Th and 256,258,260Fm) (agent) | ok |
| Bernard et al. on 264Fm; 2026 symmetric peak | EPJ A 60, 192 (2024); Chen et al., PRC 114, 024329 (2026) (agent) | ok |
| 232Th hyperdeformed state resembles 132Sn + 100Zr | Zhang, Schuetrumpf, Nazarewicz, PRC 94, 064323 (2016) (agent) | ok |
| neutron 2d splitting 1.65 MeV, proton 1.48 MeV | ENSDF levels of 131Sn (5/2+ at 1654.5 keV) and 133Sb (962.3 and 2439.6 keV) (agent) | ok |
| +-0.5 u marks the rounding scale of a match that names a nucleus | correct for a single match; the pair sum sits at 89% of its own limit (item 1.2.2) | qualified |
| Kaiser-Weise cancellation, rho tensor coupling, neutron-only energy functional | literature statements, not checked | unverified |

## 3. Feedback B

| Claim | Check | Label |
| --- | --- | --- |
| (M_Z + M_H)/v = 0.878841 against 29/33 = 0.878788; 0.0060%; 13.1 MeV | 0.878841; +5.3e-5 (0.0060%); 13.1 MeV | ok |
| PDG 2026 average M_H = 125.13 +- 0.11 | PDG 2026 summary table, S = 1.5 | ok |
| CMS result of 2 November 2026: 125.065 +- 0.088 GeV | CMS news item of 2 November 2026: 125.065 GeV with 88 MeV from gamma gamma and four leptons at 7, 8 and 13 TeV (HIG-26-010); the first pass missed it | ok (second pass) |
| Z Breit-Wigner mass 34 MeV above the pole mass | Gamma_Z^2/(2 M_Z) = 34.1 MeV | ok |
| Q(232Th -> 132Sn + 100Zr) = 188.8 MeV; M_H + M_Z,pole - M(232Th) = 187.1 MeV | 188.82 and 187.1 MeV with M_H = 125.13; 257.1 MeV with M_H = 125.20 | ok, depends on M_H |
| McDonnell, Nazarewicz, Sheikh identify a 132Sn + 100Zr dimolecule in 232Th | the abstract of PRC 87, 054327 associates the reflection-asymmetric configurations around the third minimum with dimolecular states of 132Sn and a deformed Zr or Mo fragment, and predicts very shallow or no third minima in 232Th | ok (second pass) |
| Algora et al. identify 100Zr + 132Sn with a maximum of the 232Th fission mass distribution | Rev. Mex. Fis. S 52(1), 12 (2006) states it without citation (agent); the evaluated post-neutron mean masses of 232Th(0.5 MeV) fission are 91.1 and 139.7, so the split 100 + 132 lies 8.9 u above the light centroid and 7.7 u below the heavy one | qualified |
| Hyde table: heavy peaks 139, 138, 139, 139, 138, 136, 139 and light peaks 92 ... 108 | first five pairs within 1 u of ENDF/B-VIII.0 post-neutron means (91.1/139.7, 93.4/138.2, 94.9/138.7, 97.4/138.8, 99.0/138.1); 252Cf(sf): 106.1/142.0 (ENDF), 106.6/141.8 post and 108.55/143.5 pre (EXFOR); the pair (108, 139) mixes a pre-neutron light value with a heavy value 2.5 to 4.5 u low; the 242Cm pair (103, 136) is probably low by 2.3 to 2.7 u | corrected for Cf; probable for Cm (second pass parse) |
| conversion at 0.9306 GeV/u makes the heavy peak about 130 GeV, above M_H | 138.1 to 139.8 u post-neutron (Th to Pu) gives 128.5 to 130.1 GeV; Cf 131.7 GeV | ok |
| Standard II near 144 | survey range 138.0 to 143.3 | ok |
| McGlynn and Simenel: S1 and S2 can share one effective potential well | PRC 111, 034619 (2025), arXiv:2410.02187; scission-point model with an anharmonic potential (agent) | ok |
| heavy charge centroids near 52.5 (S1) and 55 (S2) across parents | Table 1: 52.73 +- 0.58 and 55.18 +- 0.57 | ok |
| Z-vector energy about 0.9 eV per nucleon, Higgs energy about 5e-5 eV per nucleon | reproduced: 0.889 eV and 5.3e-5 eV (5.4e-5 with M_H = 125.13) with rho = 0.16 fm^-3 | ok |
| M_W^2 + M_Z^2 + M_H^2 close to v^2/2 (viXra:1709.0386) | 30450 GeV^2 against 30312 GeV^2 with PDG 2025 (+0.45%) | ok |
| nothing in viXra or arXiv states M_Z + M_H = 29/33 v | search result of the other agent, not repeated | unverified |
| ATLAS H+- -> cb excess near 130 GeV (3.0 sigma local, 2.5 global); the July 2025 talk; the 2026 Z3 two-doublet paper | JHEP 09 (2023) 004: local about 3 sigma, global about 2.5 sigma at 130 GeV (second pass); talk and 2026 paper not checked | ok for the excess, unverified for the rest |
| the "132Sb + 100Zr" numbers | correct arithmetic for 232Pa (Z = 91); the physical thorium partition is 132Sn + 100Zr, which the same exchange later adopts | qualified |

## 4. Open items

1. The 2 November 2026 CMS value and the PDG 2026 Higgs entry were confirmed in the second pass (CMS news item; PDG 2026 summary table).
2. The charm remainder is 23 standard deviations of the D0 mass; the relation is a coincidence at 0.06% and the audit treats it as such.
3. The mass-resolved yields (A and Z of the heavy fragment) are needed for the mass-against-charge test of `02_checks.md`, E7 and E7b.
