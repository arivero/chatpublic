# Second pass: the alleged errors, re-checked

Second pass of 12 November 2026. Every allegation made in `01_audit_and_errata.md`, in feedback A about the brief, and in the first pass about feedback B was checked again against a source read in this pass. Sources read directly: the AME2020 and NUBASE2020 files; the PDG summary tables of 2014 to 2026; the text of arXiv:nucl-th/0312003v1 and the abstract of hep-ph/0405076; the texts of Boeckstiegel et al. (arXiv:0712.3808), McDonnell et al. (1302.1165), Algora et al. (Rev. Mex. Fis. S 52 (2006) 12), Dubray et al. (0712.0252), McGlynn and Simenel (2410.02187), Bernard et al. (2409.02818) and Chen et al. (2605.30828); the ATLAS charged-Higgs paper (2302.11739, JHEP 09 (2023) 004); the CMS news item of 2 November 2026; the ENSDF level lists of 131Sn and 133Sb; the ENDF/B-VIII.0 fission yields, parsed with `../calculations/fission_yields_check.py` (output in `../calculations/fission_yields_output.txt`).

Verdicts: **stands**, **revised**, **withdrawn**.

## 1. Allegations about the brief

| # | Allegation | Made by | Check in this pass | Verdict |
| --- | --- | --- | --- | --- |
| 1 | The 0.19% offsets hold for atomic masses, the Breit-Wigner Z mass and PDG 2025; the other conventions give 0.11% to 0.22% | first pass | audit section 3 recomputed; nuclear masses give +0.207% and +0.216% | stands |
| 2 | The pair sum sits at 89% of the 0.5 u granularity limit, so the sharp content lies in the ratio form and in the charm relation | first pass | audit section 2b | revised. The bookkeeping holds, and its force depends on how the pair was chosen. For a pair picked to fit, a sum within 0.5 u comes for free. The pair of the brief was named in 2003 (Z with the 100Sn square, H with the 132Sn rectangle) before the Higgs mass was known, so the target was fixed in advance and the 0.19% is the distance to a preset number. Read that way the sentence of the brief is correct |
| 3 | By the 2003 bracketing criterion the measured Higgs mass (134.41 u) lies 2.4 u beyond the 132Sn corner | first pass | v1 text: the abstract states the bracketing; section 5 gives two orderings of the neutron subshells. Klinkenberg ordering (6h11/2 below 3s1/2 and 4d3/2): N = 65 to 76, interval [106, 126]. HFB ordering, called "the best approach" in the text: N = 71 to 82, interval [112, 132]. The LEP value (123.46 u) cuts a corner in both, as the text says | stands, for either ordering (2.4 u and 8.4 u beyond the upper edge) |
| 4 | 257Fm decays 99.79% by alpha; the SF partial half-life is 131 y; the step to 258Fm is a factor 1.1e13 | feedback A, first pass | NUBASE2020 lines in `../data/nubase2020_fm_excerpt.txt` | stands |
| 5 | "The measured quantity [of the heavy ridge] is the charge" | first pass | scope check | revised: this holds for the GSI secondary-beam data, which record element yields. For U, Pu and Cf the fragment masses are measured directly (double energy and velocity, radiochemistry), and the Standard I and II decompositions are fitted in mass |
| 6 | Mass numbers near 134 refer to post-neutron yields; the heavy group of 235U thermal fission peaks at A = 134 | first pass (agent) | own ENDF parse: Y(134) = 7.85%, the largest single-mass yield of the heavy group; centroid 138.68 | stands |
| 7 | 264Fm equals two 132Sn only in proton and neutron numbers | feedback A | counting | stands |
| 8 | The A = 133 to 136 ridge is the Standard I component; Standard II lies near 140 | feedback A | ENDF heavy centroids 138.1 to 139.7 for Th to Pu, single-mass maxima at 134 for 235U, 238U and 239Pu | stands |
| 9 | 0.5 u is the rounding scale of a single match | feedback A | definition | stands |
| 10 | The abstract of hep-ph/0405076 lists 246 GeV among the drip-line masses | first pass | abstract read: "45, 68, 92, 115, 175 and 246 GeV" | stands |

## 2. Allegations about feedback B

| # | Allegation of the first pass | Check | Verdict |
| --- | --- | --- | --- |
| 1 | The CMS value 125.065 +- 0.088 GeV of 2 November 2026 could not be located | CMS news item of 2 November 2026: H -> gamma gamma and H -> ZZ -> 4 leptons at 7, 8 and 13 TeV, 125.065 GeV with 88 MeV, physics analysis summary HIG-26-010, described as the most precise single-experiment value | withdrawn: feedback B quoted it correctly |
| 2 | Feedback B overstates McDonnell et al. | abstract: "very shallow or no third minima" in 232Th and 232U; the reflection-asymmetric configurations around the third minimum "can be associated with dimolecular states involving the spherical doubly magic 132Sn and a lighter deformed Zr or Mo fragment" | withdrawn: the sentence of feedback B matches the abstract; the shallow minimum of 232Th stays as context |
| 3 | Algora et al. state without citation that 100Zr + 132Sn sits at the maximum of the 232Th fission mass distribution, and the evaluated yields disagree | section 3.3 of the paper: the sentence carries no reference (the next sentence cites [18] for the third minimum); the paper's own selection rule forbids this clusterization for ground-state shapes. ENDF/B-VIII.0, 232Th at 0.5 MeV: centroids 91.1 and 139.7, single-mass maxima at A = 90 and 140, Y(98) = 3.6%, Y(134) = 5.2% | stands |
| 4 | Peak table: 252Cf (108, 139) and 242Cm (103, 136) are off | own ENDF parse: 252Cf(sf) post-neutron centroids 106.1 / 142.0, maxima 107 / 143; pre-neutron 108.55 / 143.5 (EXFOR 21851, Schmidt and Henschel, read by the agent). No evaluation exists for 242Cm(sf); the neighbours give 100.7 / 138.7 (n + 242Cm at 0.5 MeV) and 103.1 / 138.8 (244Cm(sf)) | stands for 252Cf (heavy value 3 to 4.5 u low); probable for 242Cm (heavy value about 2.7 u low by systematics) |
| 5 | The ATLAS H+- -> cb excess near 130 GeV was unverified | JHEP 09 (2023) 004: largest excess at m(H+-) = 130 GeV, local significance about 3 sigma, global about 2.5 sigma | withdrawn: confirmed |
| 6 | The "132Sb + 100Zr" numbers describe 232Pa | arithmetic | stands (qualified, as before) |

## 3. Errors of the first pass, now corrected

1. Items 2.1, 2.2 and 2.5 above (two verdicts on feedback B reversed, one confirmed).
2. Item 1.5 above (scope of the charge statement).
3. `02_checks.md`, E2: the resolution of the ratio is 8.4 times the 2025 deviation (the first pass wrote nine).
4. The AME2020 CSV omitted the first three entries (n, 1H, 2H) through a header skip of three lines too many. `make_ame_csv.py` now tries every line; the table has 3558 entries, and sections 1 to 13 of the audit are identical before and after the fix.
5. The ENDF file for neutrons on 242Cm holds only 0.5 MeV yields; the label in `fission_yields_check.py` now says so.
6. `02_checks.md`, E7b and proposal 2: the mass-resolved data sets include Lohengrin (thermal fission), VAMOS (transfer-induced fission) and SOFIA (inverse kinematics).

## 4. Still unverified

Feedback A: the Kaiser-Weise cancellation and the agreement of the free spin-orbit contact strength with spectra. Feedback B: the January 2025 study of 235U fragment charges, the 2026 Z3-flavoured two-doublet paper, the July 2025 talk title, and the viXra search.
