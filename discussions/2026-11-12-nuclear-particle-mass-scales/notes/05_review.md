# Review: the coincidences and the suggested explanations

State of 12 November 2026 (second pass). Superseded by `../unified_discussion.md`, which sets the chance reading aside and extends the catalogue of explanations. Higgs-mass inputs: PDG 2025 (125.20 +- 0.11), PDG 2026 (125.13 +- 0.11), ATLAS+CMS preliminary combination of LHCP 2026 (125.09 +- 0.07), CMS of 2 November 2026 (125.065 +- 0.088). Masses are AME2020 atomic values unless marked. Section numbers refer to `../calculations/audit_output.txt`. Attribution: brief, A and B (the two supplied replies), first pass and this pass (this folder).

## 1. Inventory

### I. Independent core: one Standard Model parameter each

| Label | Statement | Offset | Uncertainty of the offset | Pins | Dated |
| --- | --- | --- | --- | --- | --- |
| R1 | v = 2 M(132Sn) | +0.186% (nuclear masses +0.207%) | ppm | v / Lambda_QCD, equivalently alpha_s(M_Z) to 3.9e-5 | brief, 2026; 246 GeV already in the 2004 drip-line list |
| R2 | M_Z + M_H = M(100Sn) + M(132Sn) | +0.192% (PDG 2025), +0.160% (PDG 2026), +0.141% (LHCP), +0.130% (CMS) | +-0.05% from M_H | lambda, given g and g' | brief; pair named in 2003, sum after 2012 |
| R3 | 2 m(D0) = M(alpha) | +2.301 MeV, 0.0617% | +-0.10 MeV (PDG 2025), +-0.08 MeV (PDG 2026) | y_c v / Lambda_QCD | brief, 2026 |

### II. Algebraic consequences of the core

| Statement | Value now | Pulls of PDG 2026 / LHCP / CMS | Source |
| --- | --- | --- | --- |
| (M_Z + M_H)/v = 29/33 (R2 over R1) | deviation +5.3e-5 (2025), -2.3e-4, -3.9e-4, -5.0e-4 | -0.52 / -1.38 / -1.39 sigma for M_H = 125.187 (Breit-Wigner M_Z); -0.83 / -1.87 / -1.77 for 125.221 (pole) | B |
| M_H = v - M_Z + M(100Sn) - M(132Sn) = 125.243 GeV (R2 minus R1) | | -1.03 / -2.19 / -2.03 sigma | A |
| v / m(D0) = 132.03 (R1 with R3) | 0.025% from 132 | | first pass |
| M_Z + M_H = M(232Th) + 246 MeV (R2 with the Q-value of 232Th into the two tins) | +0.114% | | first pass |

### III. Post hoc or convention-selected

| Statement | Value | Remark | Source |
| --- | --- | --- | --- |
| M_H + M_Z(pole) - M(232Th) = Q(232Th -> 132Sn + 100Zr) | 187.1 against 188.8 MeV with M_H = 125.13; 257 MeV with 125.20. As a prediction M_H = 125.132 GeV: pulls -0.02 / -0.60 / -0.76 | built with the PDG 2026 value and the pole mass | B |
| lobes 134Te + 98Sr and 134Sn + 98Zr within 0.5 GeV of H and Z | offsets +0.46 / -0.03 and +0.45 / -0.02 GeV | the nearest integers to M_H/u = 134.4 and M_Z/u = 97.9 | A |
| 2 m(D0) - M(alpha) = B(d), so 2 m(D0) + M(d) = M(alpha) + m_p + m_n | +0.076 +- 0.10 MeV (0.8 sigma) | one of 19 light-nucleus energies compared (section 14); exact form predicts m(D0) = 1864.802 MeV | this pass |
| midpoint of the symmetric-to-asymmetric transition A50 against (M_H + (M_W + M_Z)/2)/u | 226.93 against 226.49 | GSI data at about 11 MeV excitation (section 15) | this pass |

### IV. Approximate fission associations

| Statement | Data | Remark | Source |
| --- | --- | --- | --- |
| H (134.4 u) on the Standard I heavy fragment | GSI: Z_H = 52.73 +- 0.58, mass by charge density 132.6 +- 1.4 (15 systems); ENDF post-neutron single-mass maxima at 134 for 235U, 238U, 239Pu, heavy centroids 138.1 to 139.7 | holds at +-2 u; the measured variable in the GSI data is the charge | brief |
| Z (97.9 u) on the light peak of 238U and 239Pu | light centroids 97.4 and 99.0 | the light peak moves with the parent, A_L = A - A_H | brief |
| light peaks of Th to U between W (86.3) and Z (97.9) | 91.1, 93.4, 94.9, 97.4; Pu 99.0 and Cf 106.1 lie above | same mechanism of the moving light peak | B |
| v / u = 264.3 and 264Fm; onset of fast spontaneous fission at 258Fm | SF partial half-life 131 y (257Fm) to 0.37 ms (258Fm) | the onset lies 6 u before 264; symmetric fragments of 258Fm are 129Sn | brief |
| 226Th Standard I mass 134.6 against 134.4 | one of five systems within 1 u among 15 | | A |
| Standard II (139 to 143 u, 130 to 133 GeV) against the ATLAS H+- excess at 130 GeV | ATLAS JHEP 09 (2023) 004: local 3 sigma, global 2.5 sigma | Standard I and II can belong to one valley (McGlynn and Simenel 2025) | exchange with B |

### V. Failing or unmatched

| Statement | Value | Source |
| --- | --- | --- |
| 2003 bracketing for the Higgs | measured mass 2.4 u beyond the 132Sn corner (8.4 u in the Klinkenberg ordering) | first pass, this pass |
| top against 208Pb | -10.9% (inside the 2003 rectangle, 1.3 u from its lower edge) | brief |
| 2 m(B) | 10.56 GeV; nearest light nucleus 11B at +3.0% | brief, this pass |

### VI. Relations of the same size inside the electroweak sector (context)

M_H / (v/2) - 1 = +1.7% (lambda = 0.1293 against 1/8); (M_W^2 + M_Z^2 + M_H^2) / (v^2/2) - 1 = +0.45%; (2 M_W + M_Z)/v - 1 = +2.3%; (M_W / M_Z) / (29/33) - 1 = +0.29%. They show how densely the electroweak masses alone populate the 0.3% to 2% range.

## 2. What the inventory says

1. The independent content is three numbers, R1, R2 and R3, which pin v / Lambda_QCD, lambda and y_c. The rest follows from them, was selected after the fact, or holds at the +-2 u level of fission phenomenology.
2. The sharpest statements are R3 (0.06%) and the ratio form of R2 over R1. The ratio sat 5e-5 from 29/33 with PDG 2025 and has moved to -2.3e-4 to -5.0e-4 with the three newest Higgs-mass values (0.5 to 1.4 sigma). The exact completion of A (125.243 GeV) is now 2.0 to 2.2 sigma from the two most precise measurements. R2 itself stays at 0.13% to 0.16%.
3. The completion of B (125.132 GeV) agrees best with the newest values, and it was constructed from the PDG 2026 value with the pole Z mass.
4. The 2003 association survives for W, Z and the top by its own bracketing criterion, and the measured Higgs mass falls outside it. The later tin relations are a second, nearest-nucleus statement.

## 3. The fusion side (charm and light nuclei)

The first pass covered R3, the D0 against the deuteron, the charged threshold, the charm-mass sensitivity (0.09% of m_c moves the remainder by 2.3 MeV) and the one-parameter family (R3 becomes exact 0.11% below the observed v for K_D = 0.85). This pass adds two systematic comparisons (section 14).

* **All heavy-meson masses and pair thresholds against light nuclei.** Nineteen mesons from the kaons to the Upsilon(4S), each as a single mass and as a pair threshold, compared with fourteen nuclei from the deuteron to 16O. Below 1% there are four entries, all charmed: 2 m(D0) against 4He (+0.06%), m(D+-) against d (-0.32%), 2 m(D+-) against 4He (+0.32%) and m(D0) against d (-0.57%). The next are Upsilon(1S) against 10B (+1.46%), 2 m(eta') against d (+2.13%) and 2 m(B) against 11B (+2.99%). The charm cluster reflects m(D) close to 2 m_N; the alpha binding per nucleon pair (14.15 MeV) is close to the shortfall of m(D0) below 2 m_N (13.0 MeV).
* **The charm remainder against light-nucleus and fusion energies.** The remainder 2.301 +- 0.10 MeV was compared with 19 energies: the binding energies of d, t, 3He and 4He, m_n - m_p, m_e, 2 m_e, m(D+) - m(D0), and the Q-values of d+d (both branches), d+t, d+3He, t+t, 3He+3He, d+d -> 4He, p+11B -> 3 alpha, 8Be -> 2 alpha, 3 alpha -> 12C and 12C + alpha -> 16O. One lies within 1 sigma: B(d) = 2.2246 MeV, leaving +0.076 MeV. The next is Q(d+d -> 3He+n) = 3.269 MeV, 9.7 sigma away. The exact form 2 m(D0) = M(alpha) + B(d) predicts m(D0) = 1864.802 MeV, against 1864.84 +- 0.04 in PDG 2026 (0.95 sigma). A D0 mass measured to +-0.01 MeV would test it at the 4 sigma level if the central value stays. This match was found after the fact among 19 candidates and is labelled post hoc in the inventory.

## 4. The fission side

* **Mass against charge.** The GSI data fix the charge of the Standard I fragment (Z_H = 52.7 +- 0.6) over 15 neutron-deficient parents; their masses carry the charge-density model. The ENDF yields of U and Pu, which measure the mass after neutron emission, place the single-mass maximum at A = 134 and the hump centroid at 138 to 140. A fixed-mass heavy fragment at 134.4 for every parent and a fixed-charge fragment at Z = 52.7 differ by up to 5 u among neutron-deficient thorium isotopes (`02_checks.md`, E7). The decisive data are mass- and charge-resolved yields along isotopic chains.
* **Asymmetric share against parent mass (section 15).** In Table 1 of Boeckstiegel et al. the share of asymmetric fission changes little between isobars (A = 232: 82.1 and 81.9%; A = 228: 62.5 and 64.5%; A = 223: 16.0 and 11.6%) and much more between isotones (N = 134: 24.2 and 11.6%; N = 138: 62.5 and 74.6%). In this set the share behaves as a function of the parent mass number. A logistic fit gives the midpoint A50 = 226.93 and width 2.65 u (rms residual 3.9 points). The midpoint lies 0.4 u above (M_H + (M_W + M_Z)/2)/u = 226.49, the centre of the proposed band. Three remarks limit the weight of this match. The data come from fission at about 11 MeV of excitation, and the competition between the channels moves with excitation energy as shell effects fade. The shares saturate near 89% at 234U, so the edges of the transition depend on the fit shape. The shell picture also predicts a dependence on A: the heavy fragment is pinned near Z = 52.7, and the competition is set mostly by the size of the light partner A - A_H. The discriminator is the movement of A50 with excitation energy and proton number. A fixed electroweak band keeps A50 in place; shell-driven competition moves it.

## 5. Suggested explanations

| # | Explanation | Proposed in | Respects the constraints of the brief | What it predicts | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | Standard Model bosons enter the effective meson exchange, enhanced when the mass of the whole nucleus equals a boson mass | 2003 text, section 6 | conflicts with the momentum-transfer argument and with the 1e-8 to 1e-13 strengths | | excluded (accepted in the brief) |
| 2 | Direct mixing or resonance of a boson with a nucleus | standard objection | baryon number forbids it | | excluded |
| 3 | Coherent Higgs coupling through the trace anomaly | brief, B | yes | smooth response, K_A = 0.3 | real, carries no sharp feature |
| 4 | Coherent Z coupling to the weak charge (about N) | B | yes | 0.9 eV per nucleon, shape-independent at leading order | real (coherent neutrino scattering), negligible for structure |
| 5 | Combined Higgs-Z terms through the hZZ vertex; two-neutrino exchange | B | yes | further suppressed | negligible |
| 6 | Enhanced parity violation in octupole-deformed nuclei | B | yes | larger parity-odd observables | leaves masses and yields untouched |
| 7 | Scalar coupled to the full trace of the energy-momentum tensor (dilaton, f = v) | B, first pass | yes | coupling M_A/v = 0.50 for 132Sn; contact 3e-12 of sigma exchange | negligible for structure |
| 8 | A relation among parameters, v / Lambda_QCD = F(g, g', lambda, m_q / Lambda_QCD) | A | yes | alpha_s(M_Z) fixed to 3.9e-5 and a reason for the integer 132 | open; no candidate formula |
| 9 | Heavy-quark decoupling, Lambda_3 proportional to Lambda_4^(25/27) m_c^(2/27) | A | yes | smooth dependence of nuclear masses on m_c | real; supplies no sharp feature |
| 10 | A competing branch with the baryon number of the nucleus and a crossing | brief, A | yes, if such a state exists | splitting 0.33 (K_X - K_A) GeV at the observed v | no candidate state |
| 11 | lambda close to 1/8, so M_H close to v/2 = 1.0019 M(132Sn) | brief, first pass | yes | the 2003 Higgs slot as R1 plus lambda; the 1.7% displacement needs an account | reformulation |
| 12 | Trace (Schur-Horn) reading of R2: Z and H as level-repelled tins | first pass | requires mixing of B = 0 and B = 100, 132 states | | formal |
| 13 | Selection with a sharp feature (relaxion-type scan, landscape with a nuclear criterion) | brief, first pass | yes | a feature at most 0.3% wide in v; the only nuclear thresholds that sharp in AME2020 are the 187Re and 163Ho weak-decay Q-values | open; no feature tied to tin or charm |
| 14 | Anthropic windows | brief | yes | windows of 1.5% to 17% in v | too wide |
| 15 | Trace-anomaly self-consistency, Higgs criticality or asymptotic safety, scale-invariant origin of v | brief | yes | leave alpha_s free | insufficient alone |
| 16 | Neutron-specific spin-orbit term delta E(q) = F(M_parent) I_n(q) on the fission path | A | yes, as phenomenology | barrier and yield shifts; must vanish after scission | ad hoc; the charge constancy of the heavy fragment points to protons |
| 17 | Lobe-mass preference: the forming drops favour masses M_H and M_Z | exchange with A | yes (baryon number stays in the drops) | heavy fragment fixed at 134.4 u for every parent; at A = 240 two channels, 134 + 106 and 142 + 98 | testable with mass-resolved yields; the GSI charge data and the ENDF centroids (138 to 140) argue against a fixed heavy hump at 134.4, the Standard I component alone remains open |
| 18 | Octupole softening for parents near M_H + M_Z, enhancing asymmetric fission | exchange with B | yes | asymmetric share rising across the band 220.7 to 232.3 u | the transition midpoint lies at 226.9 against a band centre of 226.5; the shell picture predicts the same A dependence; the excitation-energy dependence of A50 discriminates |
| 19 | Standard II tied to a charged Higgs at 130 GeV | exchange with B | a charged scalar has no diagonal coherent coupling to a nucleus | | speculative; the excess is 2.5 sigma global |
| 20 | Retired drip-line version (2004) | 2004 preprint | | | retired |
| 21 | Coincidence | standard reply | | no correlated signals; deviations stay where precision puts them | the default reading; probability arguments are out of scope |

## 6. Tests in order of decisiveness

1. **Higgs mass at 0.02 to 0.03 GeV.** It separates the four exact completions: 125.132 (B), 125.187 (29/33, Breit-Wigner M_Z), 125.221 (29/33, pole) and 125.243 GeV (A). The newest measurements already sit 2 sigma below the last.
2. **D0 mass at 0.01 to 0.02 MeV.** It tests the post hoc completion 2 m(D0) = M(alpha) + B(d) (m(D0) = 1864.802 MeV).
3. **Mass- and charge-resolved Standard I yields along isotopic chains** (Lohengrin, VAMOS, SOFIA). A fixed mass of 134.4 u against a fixed charge of 52.7.
4. **The midpoint of the symmetric-to-asymmetric transition against excitation energy and proton number.** A fixed electroweak band keeps it at 226.5; a shell-driven competition moves it.
5. **A state with the baryon number of the nucleus near 123 GeV**, or a parameter relation with infrared matching at the 3.9e-5 level in alpha_s. Both are theory items.

Explanations 8, 10 and 13 remain open without a candidate. Explanations 17 and 18 are testable phenomenology with data already in hand. Explanation 21 stays the default reading.
