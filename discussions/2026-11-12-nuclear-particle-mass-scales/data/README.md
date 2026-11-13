# Data provenance

| File | Content | Source |
| --- | --- | --- |
| `ame2020_mass_table.csv` | All 3558 entries of the AME2020 atomic-mass table, from the neutron upward: Z, N, A, symbol, mass excess (keV), uncertainty, estimate flag, atomic mass (micro-u) | `mass_1.mas20.txt` from https://www-nds.iaea.org/amdc/ame2020/ , sha256 `e8599c6d7f724fac91934e59f1b9de8fb8f63e820f4b39456b790665ed2a3307`; converted by `../calculations/make_ame_csv.py`. Reference: Huang et al., Chin. Phys. C 45, 030002 (2021); Wang et al., Chin. Phys. C 45, 030003 (2021). Entries with `estimated = 1` carry the `#` flag of the evaluation (extrapolated from systematics). |
| `nubase2020_fm_excerpt.txt` | NUBASE2020 lines for 256-260Fm (half-lives, decay branches) | `nubase_4.mas20.txt` from the same site, sha256 `1585a5eea86c5e17e90307c7e6e786d060049c4039e392a261ff6db977df9859`. Reference: Kondev et al., Chin. Phys. C 45, 030001 (2021). |

## Constants and particle data used by `../calculations/audit.py`

CODATA 2018: u = 931.49410242 MeV, m_e = 0.51099895 MeV, m_p = 938.27208816 MeV, m_n = 939.56542052 MeV, alpha-particle mass 3727.3794066 MeV, deuteron mass 1875.61294257 MeV.
PDG: G_F = 1.1663788e-5 GeV^-2 (giving v = 246.2196 GeV), Gamma_Z = 2.4955 GeV, MSbar m_c = 1.2730 GeV (2025 edition).

PDG summary tables read in this session (files `rppYYYY-sum-*.pdf` from https://pdg.lbl.gov/YYYY/tables/ ):

| Edition | M_Z (GeV) | M_W (GeV) | M_H (GeV) | m_top direct (GeV) | D0 (MeV) | D+- (MeV) |
| --- | --- | --- | --- | --- | --- | --- |
| 2014 | 91.1876 +- 0.0021 | | 125.7 +- 0.4 | | | |
| 2016 | 91.1876 +- 0.0021 | | 125.09 +- 0.24 | | | |
| 2018 | 91.1876 +- 0.0021 | | 125.18 +- 0.16 | | | |
| 2020 | 91.1876 +- 0.0021 | | 125.10 +- 0.14 | | | |
| 2022 | 91.1876 +- 0.0021 | | 125.25 +- 0.17 (S = 1.5) | | | |
| 2024 | 91.1880 +- 0.0020 | | 125.20 +- 0.11 (S = 1.4) | | | |
| 2025 | 91.1880 +- 0.0020 | 80.3692 +- 0.0133 | 125.20 +- 0.11 (S = 1.4) | 172.56 +- 0.31 (S = 1.6) | 1864.84 +- 0.05 | 1869.66 +- 0.05 |
| 2026 | 91.1879 +- 0.0020 | 80.3625 +- 0.0077 | 125.13 +- 0.11 (S = 1.5) | 172.60 +- 0.27 (S = 1.5) | 1864.84 +- 0.04 | 1869.66 +- 0.05 |

The PDG tables list the Z mass as a Breit-Wigner mass parameter. The propagator pole mass is lower by about Gamma_Z^2 / (2 M_Z) = 34 MeV.

Other Higgs-mass results used as context (not PDG averages):

* ATLAS+CMS preliminary combination of the four most precise Run 1 and Run 2 measurements: 125.09 +- 0.07 GeV, shown at LHCP 2026 (CERN Courier, 17 September 2026, https://cerncourier.com/a/precision-holds-court-in-paris/ ).
* CMS H -> gamma gamma, Run 2 re-measurement combined with 7 and 8 TeV data: 125.06 +- 0.14 GeV (CMS-HIG-24-007, CERN-EP-2026-195, July 2026).
* CMS, 2 November 2026: 125.065 GeV with 88 MeV, from H -> gamma gamma and H -> ZZ -> 4 leptons at 7, 8 and 13 TeV, physics analysis summary HIG-26-010 (news item https://cms.cern/news/how-much-does-higgs-boson-weigh-cms-gives-its-most-precise-answer-yet/ ). Quoted correctly in feedback B; the first pass of this audit had missed it.

PDG 2025 meson masses used in audit section 14 (MeV, from `rpp2025-sum-mesons.pdf`): K+- 493.677, K0 497.611, eta 547.862, omega 782.66, eta' 957.78, phi 1019.460, D0 1864.84, D+- 1869.66, Ds+- 1968.35, D*0 2006.85, D*+- 2010.26, eta_c 2984.1, J/psi 3096.900, chi_c1(3872) 3871.64, B+- 5279.41, B0 5279.72, Bs 5366.93, Upsilon(1S) 9460.40, Upsilon(4S) 10579.4.

`../calculations/scale_links.py` produces the remaining numbers of `../unified_discussion.md` (sections 1.3, 3.4, 7 to 10) from the same constants, with alpha_s(M_Z) = 0.1180, alpha_em^-1(M_Z) = 127.95, sin^2 theta_W = 0.23122, f_pi = 92.3 MeV and the four-loop MS-bar beta function.

## Fission yields

`../calculations/fission_yields_check.py` reads the ENDF/B-VIII.0 neutron-induced (nfy) and spontaneous (sfy) fission-yield sublibraries, archives `ENDF-B-VIII.0_nfy.zip` (sha256 `92c5371fdb21eecf4989f48828671b904186abc6386b3d7510c8fcee2ee5ffcf`) and `ENDF-B-VIII.0_sfy.zip` (sha256 `7a13c998eb8aecf50399301eb70f33efb87b1f4bb22dc3fad81c35288f7972b4`) from https://www.nndc.bnl.gov/endf-b8.0/zips/ . The archives are left out of the repository; the output is `../calculations/fission_yields_output.txt`. The heavy-fragment charge positions of Boeckstiegel et al. (Nucl. Phys. A 802 (2008) 12, arXiv:0712.3808, Table 1) are typed into `../calculations/audit.py`.
