# Nuclear and particle mass scales: tin sums, the charm threshold and fission modes

Started on 12 November 2026. The standing question comes from the brief: what could relate v / Lambda_QCD, the Higgs self-coupling lambda and the charm Yukawa coupling to nuclear landmarks, and which further check would dissolve the pattern. Two replies from other agents are archived next to the brief and audited here. A second pass on the same day re-checked every alleged error and wrote the review of the relations and of the suggested explanations. **`unified_discussion.md` is the single entry point**: it unifies the whole discussion, writes out the mathematics of each point, and works under the hypothesis that the relations are physical.

The relations under discussion:

* **R1** v = 2 M(132Sn), +0.19% with atomic masses.
* **R2** M_Z + M_H = M(100Sn) + M(132Sn), +0.13% to +0.19% depending on the Higgs-mass value; equivalently (M_Z + M_H)/v = 232/264 = 29/33.
* **R3** 2 m(D0) = M(alpha), a remainder of 2.30 MeV (0.06%).

## Contents

| Path | Content |
| --- | --- |
| `unified_discussion.md` | the unified account: relations, mathematics, constraints, links between Higgs-originated and QCD-originated masses (Standard Model, routes to a pure number, Seiberg duality and Seiberg-Witten theory), fission hypotheses, catalogue of 28 explanations, programme |
| `sources/00_author_brief.md` | the brief: observations, dated claims, items already examined, the question |
| `sources/01_feedback_A_*.md`, `sources/02_feedback_B_*.md` | the two supplied replies, verbatim |
| `notes/01_audit_and_errata.md` | every number and citation of the brief and of both replies, with labels |
| `notes/02_checks.md` | executed checks (E1 to E12) and proposed checks |
| `notes/03_mechanisms.md` | requirements set by the audit and four mechanism classes |
| `notes/04_error_check.md` | second pass: each alleged error re-checked against a primary source |
| `notes/05_review.md` | review: inventory of the coincidences, the fusion side, the fission side, the 21 suggested explanations, tests in order |
| `alpha.md` | side note, kept apart for its numerological character: the Nambu and Barut rules, the number 27/2, the electroweak value 1/alpha = 132, half-integers of m_e/alpha^2; numbers from `calculations/alpha_note.py` |
| `calculations/audit.py`, `audit_output.txt` | the reproducible audit (15 sections) |
| `calculations/scale_links.py`, `scale_links_output.txt` | numbers of the unified document: common unit, running coupling, infrared fixed points, Casimir scaling, unification relations, duality bookkeeping, fermium half-lives |
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
10. The unified document (13 November) sets the chance reading aside and catalogues 28 explanations. New entries: a second condensation channel of QCD (Casimir scaling), an infrared fixed point above the weak scale, Seiberg duality (confinement as a dual Higgs phase), and Seiberg-Witten vacuum selection with masses as central charges, the one structure that produces integers and exact sum rules across sectors. The three relations share a unit of 932.1 to 932.7 MeV; the unit form predicts M_H = 116 m(D0) - M_Z = 125.133 +- 0.006 GeV. In the central-charge reading the bound M >= A m_0 limits the unit to 930.4 MeV (iron), which places the electroweak quantities and the D0 about 0.2% above their integers.
11. A final review and an independent second reading (13 November) corrected 22 points of the unified document, among them the bound just mentioned, the label of the vacuum-stability formula, the holomorphic-matching exponent 1/(3 N_c), and the weak-charge factor in the Z contact energy.
12. Correction to the brief found on 13 November: the nuclear spin-orbit splitting has the sign of the Thomas term of the net potential and exceeds it 15 to 40 times; the opposite sign holds relative to the atomic formula.
13. Weighting (13 November): precisions are recorded and carry little weight, following the cases of the Koide relation (exact to 1e-5, no host) and the Gell-Mann-Okubo relations (percent level, explained by SU(3)). The weight rests on the integers and landmarks, a hosting structure, and a second consequence. The bottom thresholds (Upsilon states and 2 m(B), 10.2 to 11.5 mass units) fall among the alpha-cluster nuclei between 10B and 12C and are left open; the top has no landmark.
14. Aside on time scales (unified document, 11.5): W, Z and top decay in 0.08 to 0.14 fm/c, a few hundred times faster than the rupture of the neck; the Higgs lifetime (48 to 66 fm/c) matches the nucleon crossing time and the neck rupture, and its width of 3 to 4 MeV, set mostly by the bottom Yukawa coupling, is a nuclear energy.

## Reproduce

```
python -I calculations/audit.py > calculations/audit_output.txt
python -I calculations/fission_yields_check.py NFY_DIR SFY_DIR > calculations/fission_yields_output.txt
```

The audit reads `data/ame2020_mass_table.csv` (built from `mass_1.mas20.txt` with `make_ame_csv.py`; the checksum is in `data/README.md`). The yield check needs the two unpacked ENDF/B-VIII.0 sublibraries named in `data/README.md`.
