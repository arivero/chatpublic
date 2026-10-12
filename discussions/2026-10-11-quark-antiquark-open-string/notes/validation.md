# Validation of the independent reconstruction

12 October 2026, manuscript version 0.1. These checks support the displayed calculations and reproducibility; they do not establish a complete physical model.

**Later clarification from the user:** the 24 check groups below are not 24 scientific results. Several reproduce known algebra. They are retained as a historical validation record; future work should follow [research_protocol.md](research_protocol.md), avoid automatic reruns, and use scripts only for a concrete quantitative need. The previous drafts arrived after this validation; see [their comparison](draft_comparison.md).

| Check | Result |
| --- | --- |
| Original uploaded conversation SHA-256 checks | Both match the preserved originals |
| Flat-string and positive radial calculations | 6 check groups passed |
| CP² geometry, charge assignments, and scale examples | 7 check groups passed |
| Fermion propagation, contact expansion, and zero-range bound-state example | 6 check groups passed |
| Two-branch charges, Pauli tensors, and mixing EFT | 5 check groups passed, including 32 independent numerical diagonalizations/current rotations |
| Manuscript compilation | 13-page PDF; no LaTeX warnings, overflowing boxes, or unresolved references |
| PDF inspection | Title/abstract, scattering figure, and final page inspected; text extraction has no unresolved-reference markers |
| Local Markdown links and Git whitespace checks | Passed |

From the notebook directory, the calculation commands are:

```bash
python scripts/scattering_checks.py
python scripts/geometry_checks.py
python scripts/fermion_exchange_checks.py
python scripts/branch_checks.py
```

Run `sha256sum -c SHA256SUMS` **inside `references/`**, because the manifest uses basenames. Build the paper inside `manuscript/` with:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error quark_diquark_lepton_meson.tex
```

Python packages `numpy`, `scipy`, `mpmath`, `sympy`, and `matplotlib` and the required LaTeX packages were already available. The preprint uses the standard `article` class, Latin Modern fonts, and the `slashed` package; REVTeX is unavailable. No service startup or dependency installation was necessary for the current-instance research workflow, so no environment configuration change was required. A new cloud instance has not been independently tested.

The scattering script regenerates figures; SVG timestamps and internal identifiers can change without a mathematical or visual change. The validation run's incidental SVG rewrite was discarded after inspection. The numerical outputs and PNG remained unchanged.

Primary-literature retrieval remains incomplete: arXiv attempts in the earlier assessment and the latest INSPIRE metadata request were blocked by the network proxy. No experimental fit was run, and the missing preprint drafts were not inspected.

## Version 0.2 checkpoint — 12 October 2026

The preceding record describes version 0.1. The drafts have since arrived and network access recovered. The living paper now incorporates the four-sector goal, finite-momentum current calculation and analytic localization discriminator; contact studies are supporting appendices.

- `latexmk -pdf -interaction=nonstopmode -halt-on-error quark_diquark_lepton_meson.tex` completed: 20-page PDF, no final-log warnings, unresolved references or overfull boxes. Rendered pages 3–4 were inspected for the new equations and result table.
- Both reference checksum manifests passed: all six original uploads remain unchanged.
- The new `warped_current_experiment.py` was run by a `gpt-6-sol` agent. Its 23-point scan and threshold are saved in JSON. Adaptive and fixed-rule quadrature agree within 4×10⁻¹⁶ at the selected comparison points. Higher precision Bessel arithmetic does not remove the double-precision node/output limitation.
- Additional agents reviewed the analytic profile formulas and scientific framing. Model agreement does not establish physical correctness, a common string construction or agreement with experiment.

The older four physics scripts were not rerun: no new changes required their execution. No additional package installation, service startup or environment configuration change was needed. The recovered current instance supports the workflow; the cloud interruption's root cause is unknown.
