# Living research paper

**Cycle-closure snapshot, 13 October 2026:** version 0.5 was committed and pushed in `210d0b4`. The user has closed this research cycle pending new models. The source and built PDF remain the final physics result of this run; linking the shared conversations requires no rebuild.

Version 0.5, 13 October 2026: *Retained adjoint-fermion binding with explicit $\hbar$*. The user selects the retained adjoint as the most interesting concrete object: it binds both fermionic endpoints through regulated contact interactions, without a direct endpoint force. The broader four-string and whole-state scattering goals remain open.

- [Built PDF](quark_diquark_lepton_meson.pdf) and [main source](quark_diquark_lepton_meson.tex).
- [Focused calculation](retained_adjoint_hbar.tex), [new radius derivation](../blackboard/009_anharmonic_radius.md), and [conditional supersymmetry dictionary](supersymmetry_dictionary.tex).
- [Workplan](../notes/workplan.md) and [validation record](../notes/validation.md).

Version 0.2, with the warped-current comparison and scalar-completion appendix, is preserved at Git commit `6b73d29`; version 0.1 at `333e537`. Earlier `pointlike_current.tex`, `current_results.tex`, and `fermionic_binding.tex` remain as historical comparison sources and are not included in the version 0.5 build. The [supplied preprints](../references/received-2026-10-12/README.md) are archived unchanged. Earlier natural-unit formulas should not be mechanically converted into current instructions.

The new calculation keeps physical $\hbar$ explicit, uses $c_{\rm light}$ where relevant, distinguishes physical momentum transfer $Q$ from wave number $Q/\hbar$, and assigns the contact coupling $G$ units of energy × length³. It gives a sufficient binding condition, attractive recoil starting at order $(\mu/M)^2$, and deep Gaussian energy and whole-state charge radius through $\hbar^2$. The leading anharmonic radius correction is positive: $r_E^2=r_{E,\mathrm{harm}}^2[1+5S_\eta\varepsilon/8]+O(R^2\varepsilon^3)$. The next quantitative calculation is the anharmonic shape of the finite-$Q$ current. The formal $\pi/K$ scalar assignment passes the charged Dirac multiplet count; exact physical $B-L$ adds a separate conditional constraint. A general $U(6)$ basis can mix the six charged mesons but leaves their zero $B-L$ unchanged. The [1983 source assessment](../references/greenberg_mohapatra_yasue.md) identifies a distinct quasi-Nambu–Goldstone mass-protection mechanism, not a Goldstino or a whole-state form factor. No anharmonic finite-$Q$ current was calculated in this revision.

Build from this directory with `latexmk -pdf -interaction=nonstopmode -halt-on-error quark_diquark_lepton_meson.tex`. The PDF is tracked so it can be read without TeX; auxiliary files are ignored.
