# Clifford geometry and mass relations — critical review

Research discussion, 3 November 2026, examining Alexander Kritov, *Clifford Geometry and Mass Relations: From Charged Leptons to the Proton*, English manuscript v13 (31 pages).

The original third-party manuscript is **not** redistributed in this public-ready directory. This folder contains independent analysis, generated plots, reports and reproducible calculations.

## Contents

- [Notes: mathematical audit and GIGO input/output ledger](notes/audit.md)
- [Notes: parameter identifiability, integer constraints and Koide](notes/parameter-koide.md)
- [Notes: RG analysis and historical radiative mass literature](notes/rg-history.md)
- [Reports](reports/): integer-constrained scan (8-page PDF and LaTeX), RG supplement (4-page PDF and LaTeX)
- [Calculations](calculations/): Python scripts used for the numerical scans
- [Figures](figures/): seven parameter/Koide figures, three RG figures, two conceptual infographics

## Manuscript equations

At the measured Thomson-limit fine-structure constant and measured electron mass, the postulated lepton relation is:

\[
 m_\mu/m_e=3/(2\alpha)+17/14,\qquad m_\tau/m_e=51/(2\alpha)-17.
\]

The baryonic extension independently assumes additional geometric and screening rules to obtain:

\[
 m_p/m_e=27/(2\alpha)-83/6+\alpha^2/[3(1-\alpha)].
\]

These are *not* successive alpha and alpha-squared loop suppression relations. The leading electron-to-muon and electron-to-tau ratios both scale as alpha; the muon-to-tau ratio tends to 1/17.

## Overall assessment

Much of the finite-dimensional algebra is correct once the response operator and mass-matching postulates are chosen. The precision of the numerical comparisons is notable, especially the proton, but it does not establish the uniqueness or physical necessity of the chosen response, radius and baryonic screening prescriptions. The predictions are expressed in pole masses and Thomson alpha; naive replacement by running alpha does not preserve the fit.

**Publication status:** these are discussion notes, not a peer-reviewed endorsement or published correction of the manuscript.
