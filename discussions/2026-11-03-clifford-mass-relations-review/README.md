# Review of Kritov, *Clifford Geometry and Mass Relations*, v13

Started 3 November 2026. This directory records a review of A. Kritov's manuscript *Clifford Geometry and Mass Relations: From Charged Leptons to the Proton*, version 13, supplied by the user as a PDF. The manuscript derives

$$\frac{m_\mu}{m_e} = \frac{3}{2\alpha}+\frac{17}{14},\qquad \frac{m_\tau}{m_e} = \frac{51}{2\alpha}-17,\qquad \frac{m_p}{m_e} = \frac{27}{2\alpha}-\frac{83}{6}+\frac{\alpha^2}{3(1-\alpha)}$$

from a Clifford carrier on a round three-sphere of radius $r_e$ and two postulates.

- [Review report (PDF, 23 pages)](review/clifford_mass_relations_review.pdf), with all figures and table views. Figures G1 and G2 draw the construction: the round S³ and its lowest Dirac level, the 16-dimensional carrier and the operator C, the response weights and their minimum, the resulting masses, and the proton's two radii and colour singlet. Figure G3 shows how the weights 0, 1, 17 arise and compares other splits of the 16 directions.
- [Review page source (HTML)](review/clifford_mass_relations_review.html). It loads MathJax and fonts from public CDNs and embeds its plot data; open it in a browser. GitHub shows only the source.
- [Chronological recap](notes/conversation_recap.md) of the user's requests and outcomes.
- [Koide's ratio for masses linear in 1/α](notes/koide_linear_alpha.md): the expansion in √α behind the user's last remark.
- [Supplied manuscript and transcription](references/README.md): kept local, not redistributed.

## Main results

1. **Mathematics.** The derivations are internally consistent. 57 identities (Clifford completeness, response operator, flows, Kraus maps and dilation, colour sector, Casimirs) agree numerically, and every number in Tables 1 and 3 reproduces. Five findings, none changing a result: the proton comparison omits the uncertainty carried by α, nine times the reference uncertainty used for its *z*; the $m_pc^2$ row is not an independent test; the return map of Sec. 6.2 is fixed only on active inputs; Sec. 8.2 should read 8.30×10⁻⁷; some symbols are reused.
2. **History.** The relations belong to the excitation line of Nambu and Barut ($m_\mu/m_e$ as a leading $1/\alpha$ term). The radiative line of Weinberg, Georgi–Glashow and Barr–Zee reads the same leading relation as $m_e = O(\alpha)\,m_\mu$; in that form the manuscript fixes $m_e/m_\mu = \tfrac23\alpha - \tfrac{34}{63}\alpha^2+\dots$.
3. **Flexibility.** With the manuscript's integers and ratios kept on simple-ratio grids, every discrete choice is fixed by the data; the nearest grid neighbour misses by at least $1.8\times10^4\sigma$. On a grid of 1443 possible muon offsets, 17/14 is the only match, with a chance probability of about $4\times10^{-3}$ at 1σ. The proton relation has more freedom, and its agreement depends on the α determination used: it passes with CODATA 2022 and the electron $g-2$ value, and fails at −4.8σ with the Cs recoil value and +2.7σ with the Rb value.
4. **Running.** No energy scale suits the relations better than the infrared. In an on-shell scheme the needed offsets equal the manuscript's values only below about 6 keV (muon), 300 keV (τ) and 0.5 keV (proton). In MS-bar the lepton mass ratios freeze above the τ while α keeps running, and the needed offsets never approach 17/14 or −17.
5. **Koide.** At the manuscript's point Koide holds to $10^{-6}$ because the formulas reproduce the measured masses. Exact Koide inside the model needs a τ weight of 17.000115, not a simple ratio. For masses linear in 1/α relative to a fixed electron, the electron term enters at order √α and prevents Koide from holding for all α; a Z₃-circulant square-root mass operator gives it identically.

## Companion analysis

The user also supplied a second, independent analysis of the same manuscript, prepared in a separate conversation, as `chatpublic_clifford_bundle.zip` (SHA-256 `07579b4ba62f81f716628d2ef84b96657b48c846f3f3a7cc2772654d6d2fdfd3`). Its files are added here unchanged; only its README was renamed, to avoid replacing this one.

- [Overview](companion_analysis.md) (the bundle's README).
- Notes: [mathematical audit and GIGO ledger](notes/audit.md), [what the geometric drawing shows](notes/geometry.md), [parameters, integer constraints and Koide](notes/parameter-koide.md), [RG and radiative-mass history](notes/rg-history.md).
- Reports: [integer-constrained scan, 8 pages](reports/clifford_integer_constrained_scan_report.pdf) ([LaTeX](reports/clifford_integer_scan_report.tex)); [RG supplement, 4 pages](reports/clifford_rg_supplement.pdf) ([LaTeX](reports/clifford_rg_supplement.tex)).
- [Figures](figures/): seven parameter and Koide plots, three RG plots, two infographics.
- Scripts: [clifford_integer_scan_figures.py](calculations/clifford_integer_scan_figures.py), [clifford_rg_scan.py](calculations/clifford_rg_scan.py).

**Agreement with this review.** Both analyses find the finite algebra correct given the postulates, 17 = 1 + 16 from the unnormalized trace, a Spin(4) commutant of dimension 10, the same domain qualification for the return map, and a proton uncertainty from α of 2.8×10⁻⁷ against the 3.2×10⁻⁸ quoted. The running results match: MS-bar ratios 210.657 and 3578.2 above the τ, Koide shifted by +1.74×10⁻³, and on-shell central-value scales of 0.10 keV (proton), 3.8 keV (muon) and 160 keV (τ), consistent with the 1σ upper scales found here.

**Content not in this review.** The two-parameter exact fit $(\lambda,\eta) = (1.000008277, 1.001399651)$; integer τ weights with λ fitted to the muon, where 16 and 18 miss the τ by −104 and +104 MeV; the Koide-exact point $(\lambda,\eta) = (0.999996, 0.999371)$ with $m_\tau = 1776.969$ MeV; a counterfactual integer lattice $(u,q)$ and a real scale β for the proton's return matrix; the observation that the same finite spectrum follows on an abstract $\mathbb C^{16}$ without Clifford multiplication; and radiative-mass references not cited here (Barr–Zee 1977, Phys. Rev. D 15, 2652; Barr 1980, Phys. Rev. D 21, 1424; Ma 1989, Phys. Rev. Lett. 62, 1228), checked against INSPIRE.

**Read with care.**

- The two PNG infographics draw the sphere of radius $\ell_e$ smaller than the sphere of radius $r_e$. In fact $r_e = \alpha\ell_e$ is 137 times smaller. The companion's [geometry note](notes/geometry.md) says the drawings are not to scale.
- `clifford_rg_scan.py` writes its outputs to `/mnt/data`, the path of the environment where it ran; set `OUT` before running it elsewhere. The integer-scan report names its script `scan_figures.py`; the file here is `clifford_integer_scan_figures.py`, which writes next to itself.
- The reports' LaTeX includes figures by bare file name; the figures are in `figures/`.

## Reproduction

The scripts use `numpy`, `scipy` and `mpmath`; the PDF renderer uses Node with Playwright and Chromium. From this directory:

```bash
python scripts/verify_identities.py
```

```bash
python scripts/gigo_flexibility.py
```

```bash
cd calculations && python ../scripts/plotdata_koide.py && python ../scripts/rg_scan.py
```

```bash
python scripts/rg_scales.py
```

```bash
node scripts/render_pdf.js review/clifford_mass_relations_review.html review/clifford_mass_relations_review.pdf
```

`geometry_figures.py` and `geometry_figure_g3.py` write the inline SVG of Figures G1–G3. `plotdata_koide.py` and `rg_scan.py` write [plotdata.json](calculations/plotdata.json) and [rgdata.json](calculations/rgdata.json); the HTML page embeds the merged contents. `verify_identities.py` checks the manuscript's identities with its own matrices; `gigo_flexibility.py` prints the formula-family counts; `rg_scales.py` gives the infrared validity scales quoted above.

## Scope

- The running is a leading-order estimate. Leptonic vacuum polarization is exact at one loop; the hadronic part is a dispersive model with narrow resonances and perturbative continua calibrated to $\Delta\alpha_{\rm had}^{(5)}(M_Z^2) = 0.02783$; MS-bar uses two-loop leptonic running and one-loop Standard Model running above $M_Z$. The conclusions do not depend on the hadronic details at the stated precision.
- Chance probabilities for the flexibility analysis depend on the grid or rule set chosen, which was written after the target values were known. The review states them for the grids used.
- The review was prepared with Claude Code. Citations were checked against INSPIRE records and abstracts, PDG material and the cited arXiv texts where stated in the review; the Barr–Zee and Barut papers themselves were not opened.
