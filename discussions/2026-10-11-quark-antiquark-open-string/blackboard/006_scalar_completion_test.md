# Supporting experiment: can scalar matching supply the contact trimer?

12 October 2026. Full derivation is in the living paper's supporting appendices, [fermionic_binding.tex](../manuscript/fermionic_binding.tex), sections “First completion test” and “Seiberg variables.” This is an analytic model test. The user's later four-sector correction makes whole-string pointlike scattering the main goal; the active mechanism test is [007](007_pointlike_current_mechanism.md).

**Specified test.** One chiral fundamental scalar per flavor, a massive vectorlike Dirac endpoint, and a Majorana adjoint; Yukawa `−y φ† Tᵃ ψ λᵃ + h.c.`. Use normalized NR fields with a factor 1/√2 per massive Weyl particle component. A global-color Yukawa model contains a bosonic scalar; a full SQCD interpretation additionally contains gauge bosons. Neither is an exclusively fermionic UV theory.

The threshold denominators are D_s=m_φ²−(m+M)² and D_u=m_φ²−(m−M)². In the endpoint–carrier color triplet, the s and u tensors have eigenvalues 4/3 and −1/6. Including the Majorana crossed graph gives

\[
V=-[g_0P_0+g_1P_1]f_R,\qquad
g_0=\frac{2|y|^2}{3D_s}-\frac{|y|^2}{24D_u},\quad
g_1=\frac{|y|^2}{24D_u}.
\]

For positive detuning both channels attract but g₀≥15g₁. The Gaussian is a regulator, not a derived scalar-exchange range. Additional chiral scalars require their own matching.

**First finding: the spin-independent proof does not transfer.** The eigenvalues of P⁰_qλ+P⁰_qbarλ are 1/2, 3/2 and 0 in endpoint-spin/total-spin sectors (0,1/2), (1,1/2), (1,3/2). With equal orbital overlaps, the strongest channel has endpoint spin one. Its product trial gives E₃≤2ε₂((3g₀+g₁)/4), whereas breakup is ε₂(g₀). Both pairs cannot simultaneously realize the full spin-singlet attraction. The original proof remains valid for its different, spin-independent Hamiltonian.

**Second finding: a restricted no-binding result.** Bargmann's bound and T_rel≥(p_x²+p_y²)/(2m) yield

\[
\frac{m g_0}{\pi^{3/2}R}<1\quad\Rightarrow\quad H_{\rm rel}\ge0.
\]

This excludes even a trimer without bound dimers in the regulated model. It holds parametrically for perturbative y, m_φ≫m,M and cutoff R⁻¹≪min(m,M). The argument uses a genuine lower bound, not failure of a sufficient variational binding criterion. It does not exclude all scalar completions.

**Remaining candidate.** Near δ=m_φ−m−M>0, the contact grows, but E≪δ and p≪√(2μδ) are needed to integrate out the scalar. Scalar dressing and conversion channels must be retained in a resonant treatment. At negative detuning a scalar-plus-endpoint threshold is lower. Flavor-diagonal endpoints may also annihilate into carriers; distinct exactly conserved endpoint flavors forbid that particular channel, giving a specific reason to introduce a second flavor.

**Optional continuation:** a spin-resolved resonant three-body calculation could determine whether a more complete binding regime survives. It is not the next main milestone and no unattended calculation was scheduled successfully. The immediate task is to derive the UV mode and common string/dual profiles identified in [007](007_pointlike_current_mechanism.md). If the contact problem is revisited, new numerical work needs a quantitative target, declared approximation and independent convergence criterion, using a smaller model and disk outputs as requested.

Checks: the tree/color/spin matching and bounds were independently derived/reviewed by another agent. No new numerical physics script. The paper's version 0.2 incorporates the result; version 0.1 remains at `333e537`. Bargmann citation metadata was verified through Crossref: PNAS 38 (1952), 961–966, DOI [10.1073/pnas.38.11.961](https://doi.org/10.1073/pnas.38.11.961). The standard bound is applied analytically here; primary-paper proof verification is not claimed.
