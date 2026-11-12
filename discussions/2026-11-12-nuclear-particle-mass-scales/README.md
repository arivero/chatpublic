# Nuclear and particle mass scales: tin sums, the charm threshold and fission modes

Started on 12 November 2026. The standing question comes from the author's brief: what could relate v / Lambda_QCD, the Higgs self-coupling lambda and the charm Yukawa coupling to nuclear landmarks, and which further check would dissolve the pattern. Two replies from other agents are archived next to the brief and audited here. A second pass on the same day re-checked every alleged error and wrote the review of the coincidences and of the suggested explanations.

The relations under discussion:

* **R1** v = 2 M(132Sn), +0.19% with atomic masses.
* **R2** M_Z + M_H = M(100Sn) + M(132Sn), +0.13% to +0.19% depending on the Higgs-mass value; equivalently (M_Z + M_H)/v = 232/264 = 29/33.
* **R3** 2 m(D0) = M(alpha), a remainder of 2.30 MeV (0.06%).

## Contents

| Path | Content |
| --- | --- |
| `sources/00_author_brief.md` | the author's brief: observations, dated claims, items already examined, the question |
| `sources/01_feedback_A_*.md`, `sources/02_feedback_B_*.md` | the two supplied replies, verbatim |
| `notes/01_audit_and_errata.md` | every number and citation of the brief and of both replies, with labels |
| `notes/02_checks.md` | executed checks (E1 to E12) and proposed checks |
| `notes/03_mechanisms.md` | requirements set by the audit and four mechanism classes |
| `notes/04_error_check.md` | second pass: each alleged error re-checked against a primary source |
| `notes/05_review.md` | review: inventory of the coincidences, the fusion side, the fission side, the 21 suggested explanations, tests in order |
| `calculations/audit.py`, `audit_output.txt` | the reproducible audit (15 sections) |
| `calculations/fission_yields_check.py`, `fission_yields_output.txt` | ENDF/B-VIII.0 post-neutron mass-yield centroids and maxima |
| `calculations/make_ame_csv.py` | converts the AME2020 table to `data/ame2020_mass_table.csv` |
| `data/README.md` | provenance of every input, PDG values by edition |

## Findings after the second pass

1. The numbers of the brief reproduce. The 0.19% offsets belong to atomic masses, the Breit-Wigner Z mass and PDG 2025; the legitimate conventions give +0.11% to +0.22% for R2 and +0.19% to +0.21% for R1.
2. The independent content is three numbers (R1, R2, R3), pinning v / Lambda_QCD, lambda and y_c. R1 corresponds to alpha_s(M_Z) at 3.9e-5.
3. The ratio (M_Z + M_H)/v sat 5e-5 from 29/33 with PDG 2025. With PDG 2026 (125.13 +- 0.11), the LHCP 2026 combination (125.09 +- 0.07) and CMS of 2 November 2026 (125.065 +- 0.088) it sits 0.5 to 1.4 sigma below. The four exact completions predict M_H = 125.132 (feedback B), 125.187 and 125.221 (29/33 with the two Z-mass conventions) and 125.243 GeV (feedback A); the last is now 2.0 to 2.2 sigma from the newest measurements.
4. The November 2003 text brackets the boson masses by subshell intervals that end at the doubly magic corners. W, Z and the top fall inside; the measured Higgs mass lies 2.4 u beyond the 132Sn corner in either subshell ordering.
5. Fusion side: among 19 mesons, as single masses and as pair thresholds, against 14 light nuclei, the entries below 1% are all charmed (D0 D0-bar against 4He at +0.06%). The charm remainder 2.30 MeV equals the deuteron binding energy within 0.08 +- 0.10 MeV, a post hoc match among 19 energies compared; its exact form predicts m(D0) = 1864.802 MeV.
6. Fission side: the GSI data fix the Standard I charge at Z_H = 52.7 +- 0.6; the ENDF yields of U and Pu put the heavy single-mass maximum at A = 134 and the hump centroid at 138 to 140. The asymmetric share in the GSI data behaves as a function of parent mass, with its midpoint at A = 226.9 against a band centre (M_H + (M_W + M_Z)/2)/u = 226.5; the shell picture predicts the same A dependence, and the excitation-energy dependence discriminates.
7. The 257Fm spontaneous-fission partial half-life is 131 y; 258Fm lives 0.37 ms, a factor 1.1e13 lower.
8. Second-pass corrections: the CMS value quoted in feedback B, the reading of McDonnell et al. and the ATLAS 130 GeV excess are confirmed (three first-pass verdicts reversed); the charge statement is limited to the GSI data; the granularity remark applies to a pair chosen to fit, while the brief's pair was fixed in 2003.
9. Confirmed corrections to the replies: the 252Cf entry (and probably the 242Cm entry) of the peak table in feedback B; the uncited claim of Algora et al. on the 232Th mass distribution.
10. Of the 21 suggested explanations, the parameter relation, the baryon-number branch and the sharp-feature selection remain open without a candidate; the lobe-mass preference and the octupole softening near M_H + M_Z are testable with data in hand; coincidence remains the default reading.

## Reproduce

```
python -I calculations/audit.py > calculations/audit_output.txt
python -I calculations/fission_yields_check.py NFY_DIR SFY_DIR > calculations/fission_yields_output.txt
```

The audit reads `data/ame2020_mass_table.csv` (built from `mass_1.mas20.txt` with `make_ame_csv.py`; the checksum is in `data/README.md`). The yield check needs the two unpacked ENDF/B-VIII.0 sublibraries named in `data/README.md`.
