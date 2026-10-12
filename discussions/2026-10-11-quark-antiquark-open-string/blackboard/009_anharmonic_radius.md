# Leading anharmonic correction to the retained-adjoint charge radius

13 October 2026, Europe/Madrid. Assigned analytic continuation of [008](008_retained_adjoint_hbar.md), using the focused manuscript and task contract at baseline `7d718ab`. The user explicitly brought the start forward from 01:40 to approximately 01:15. The assigned input files had no uncommitted changes when read. This note establishes one new coefficient within the existing fixed-number contact model; it does not supply a string or relativistic completion. No numerical calculation was needed. The parent independently checked the quadratic-source differentiation and its sign; unchanged earlier results were not re-reviewed.

## Question, inherited assumptions and units

What is the first correction to the **whole-state** mean-square charge radius when the correlated harmonic ground state is perturbed by the Gaussian contact's quartic term?

Keep the manuscript's distinguishable, equal-mass endpoints of mass $m$, a retained neutral adjoint fermion of mass $M$, global color, and no direct endpoint potential. The internal Hamiltonian is

\[
H=\frac{p_x^2+p_y^2}{2\mu}
 +\frac{\mathbf p_x\cdot\mathbf p_y}{M}
 -V_0\left(e^{-x^2/R^2}+e^{-y^2/R^2}\right),
\qquad \mathbf p=-i\hbar\nabla,
\]

\[
\mu=\frac{mM}{m+M},\qquad
\eta=\frac{\mu}{M}=\frac{m}{m+M},\qquad
V_0=\frac{3G}{2\pi^{3/2}R^3},\qquad [G]={\rm energy}\,{\rm length}^3.
\]

Define

\[
\omega^2=\frac{2V_0}{\mu R^2},\qquad
\ell^2=\frac{\hbar}{\mu\omega},\qquad
\varepsilon=\frac{\hbar}{\mu\omega R^2}=\frac{\ell^2}{R^2}\ll1,
\]

\[
S_\eta=\sqrt{1+\eta}+\sqrt{1-\eta},\qquad
D_\eta=\sqrt{1+\eta}-\sqrt{1-\eta}.
\]

The expansion holds at fixed $V_0,R,\mu$ and fixed $0\leq\eta<1$. Equivalently, hold the physical contact coupling, range and constituent masses fixed while counting powers of $\hbar$. The result is not a recoil expansion and is not asserted uniform as $\eta\to1$.

Use the leading nonrelativistic one-body electric density, pointlike constituents, endpoint charges $e_1,e_2$, and $e_1+e_2\ne0$. Exchange symmetry of the orbital dynamics makes the endpoint form factors equal, regardless of their individual charges. With a neutral adjoint, the normalized current therefore measures

\[
\mathbf a=\mathbf r_q-\mathbf R_{\rm cm}
 =\frac{\mathbf x-\eta\mathbf y}{1+\eta},\qquad
F(\mathbf Q)=\left\langle e^{i\mathbf Q\cdot\mathbf a/\hbar}\right\rangle,
\qquad r_E^2=\langle a^2\rangle.
\]

Here $\mathbf Q$ is physical momentum and $\mathbf Q/\hbar$ is wave number. Constituent radii, relativistic current corrections, and additional two-body currents are outside this specified observable. Spin is inert in this spin-independent orbital calculation.

## Quadratic sources include the changed state

Set $\mathbf u_\pm=(\mathbf x\pm\mathbf y)/\sqrt2$. Introduce independent auxiliary quadratic sources into the original Hamiltonian,

\[
H(j_+,j_-)=H+\frac{j_+u_+^2+j_-u_-^2}{2},\qquad
k_\pm=\mu\omega^2+j_\pm.
\]

The sources have units of energy/length squared. Hold $V_0,R,\mu,\eta$, including the quartic interaction's coefficient, fixed under these derivatives. Nonnegative sources suffice; derivatives at zero can be taken from the positive side, avoiding an unbounded negative quadratic potential outside the finite well.

The source-dependent harmonic frequencies and Cartesian variances are

\[
\Omega_\pm=\sqrt{\frac{(1\pm\eta)k_\pm}{\mu}},\qquad
v_\pm=\langle u_{\pm i}^2\rangle_0
 =\frac{\hbar\sqrt{1\pm\eta}}{2\sqrt{\mu k_\pm}},\qquad
s=\langle x_i^2\rangle_0=\langle y_i^2\rangle_0
 =\frac{v_++v_-}{2}.
\]

The normal modes are independent in this Gaussian state. The quartic term is a perturbation, not a stand-alone potential at large distance:

\[
V_4=-\frac{V_0}{2R^4}(x^4+y^4),\qquad
\langle x^4\rangle_0=\langle y^4\rangle_0=15s^2,
\]

\[
E(j_+,j_-)=-2V_0+\frac{3\hbar}{2}(\Omega_++\Omega_-)
 -\frac{15V_0}{R^4}s^2+O(V_0\varepsilon^3).
\]

Only the source dependence of the first quartic expectation is needed; no further energy coefficient is evaluated. Hellmann–Feynman gives

\[
\langle u_\pm^2\rangle=2\frac{\partial E}{\partial j_\pm},\qquad
\frac{\partial s}{\partial j_\pm}=-\frac{v_\pm}{4k_\pm},
\]

and hence, evaluated at zero source,

\[
\langle u_\pm^2\rangle
 =3v_\pm+\frac{15V_0s v_\pm}{k_\pm R^4}
 +O(R^2\varepsilon^3)
 =\frac{3\hbar\sqrt{1\pm\eta}}{2\mu\omega}
  \left(1+\frac58 S_\eta\varepsilon\right)
 +O(R^2\varepsilon^3).
\]

This differentiates the energy of the perturbed state. It includes the first-order wavefunction response and is not the expectation of the radius in the unchanged harmonic state. Explicitly, for any source-independent quadratic observable $A$, the same correction is

\[
\delta\langle A\rangle
 =2\operatorname{Re}\sum_{n\ne0}
 \frac{\langle0|A|n\rangle\langle n|V_4|0\rangle}
 {E_{0,{\rm harm}}-E_{n,{\rm harm}}},
\]

where the harmonic excitation gaps contain $\hbar\Omega_\pm$. The source differentiation performs this response sum analytically. Differentiating only the source-free energy coefficient with respect to $\omega$, while allowing the quartic coefficient to vary with it, would measure a different operator and would miss this result.

Endpoint exchange sends $\mathbf u_-\mapsto-\mathbf u_-$, so $\langle\mathbf u_+\cdot\mathbf u_-\rangle=0$ in the symmetric ground state. Transforming back gives both required moments:

\[
\boxed{
\langle x^2\rangle=\langle y^2\rangle
 =\frac{3\hbar S_\eta}{4\mu\omega}
 +\frac{15\hbar^2S_\eta^2}{32\mu^2\omega^2R^2}
 +O(R^2\varepsilon^3),}
\]

\[
\boxed{
\langle\mathbf x\cdot\mathbf y\rangle
 =\frac{3\hbar D_\eta}{4\mu\omega}
 +\frac{15\hbar^2S_\eta D_\eta}{32\mu^2\omega^2R^2}
 +O(R^2\varepsilon^3).}
\]

For $\eta>0$, anharmonicity increases the positive recoil correlation as well as the marginal endpoint variance. Both receive the common fractional correction $5S_\eta\varepsilon/8$ at this order. Their ratio therefore has no correction linear in $\varepsilon$.

## Paper-ready radius coefficient

Define

\[
N_\eta=(1+\eta^2)S_\eta-2\eta D_\eta
 =(1-\eta)^2\sqrt{1+\eta}+(1+\eta)^2\sqrt{1-\eta}>0.
\]

Using the full center-of-mass weights and the corrected correlation,

\[
r_E^2=\frac{(1+\eta^2)\langle x^2\rangle
                   -2\eta\langle\mathbf x\cdot\mathbf y\rangle}
                  {(1+\eta)^2},
\]

\[
\boxed{
r_E^2=\frac{3\hbar N_\eta}{4\mu\omega(1+\eta)^2}
 +\frac{15\hbar^2S_\eta N_\eta}
 {32\mu^2\omega^2R^2(1+\eta)^2}
 +O(R^2\varepsilon^3)
 =r_{E,{\rm harm}}^2\left(1+\frac58S_\eta\varepsilon\right)
 +O(R^2\varepsilon^3).}
\]

The leading radius is order $\hbar$ and its first anharmonic correction is order $\hbar^2$, with the potential and masses held fixed. The correction is positive for every fixed $0\leq\eta<1$: the finite Gaussian well softens away from its minimum and makes this charge distribution larger. Dropping the correction to $\langle\mathbf x\cdot\mathbf y\rangle$ would give the wrong coefficient at nonzero recoil.

## Analytic limit, dimensions and error order

At $\eta=0$, $S_0=2$, $D_0=0$, and the two dimer coordinates decouple. The result reduces to

\[
\langle\mathbf x\cdot\mathbf y\rangle=0,\qquad
r_E^2=\langle x^2\rangle
 =\frac{3\hbar}{2\mu\omega}
 +\frac{15\hbar^2}{8\mu^2\omega^2R^2}
 +O(R^2\varepsilon^3)
 =\frac{3\hbar}{2\mu\omega}
  \left(1+\frac54\varepsilon\right)+O(R^2\varepsilon^3).
\]

For an independent one-dimer check, keep $-V_0r^4/(2R^4)$ fixed and add $jr^2/2$ to its harmonic Hamiltonian. With $k=\mu\omega^2+j$,

\[
E_{4,{\rm dimer}}(j)=-\frac{15V_0\hbar^2}{8\mu R^4k},\qquad
2\left.\frac{\partial E_{4,{\rm dimer}}}{\partial j}\right|_{j=0}
 =\frac{15\hbar^2}{8\mu^2\omega^2R^2},
\]

which is exactly the displayed radius correction. A physical heavy-carrier limit at fixed $m$ also sends $\mu\to m$; no fixed-$\mu$ heavy-mass series is implied.

The factors $\hbar/(\mu\omega)$ and $\hbar^2/(\mu^2\omega^2R^2)$ both have units of length squared; $S_\eta,D_\eta,N_\eta,\varepsilon$ are dimensionless. First-order sextic and second-order quartic effects, including the associated state normalization, first contribute to this quadratic observable at $O(R^2\varepsilon^3)$, or order $\hbar^3$ at fixed physical parameters. No numerical evidence is claimed.

## Physical momentum window and remaining scope

Rotational invariance gives

\[
F(Q)=1-\frac{Q^2r_E^2}{6\hbar^2}
 +O\!\left(\frac{Q^4\langle a^4\rangle}{\hbar^4}\right),
\qquad \langle a^4\rangle=O(R^4\varepsilon^2)
\]

at fixed $\eta$. The radius controls the current when $Q\sqrt{r_E^2}/\hbar\ll1$. The natural localization momentum is

\[
Q_{\rm loc}=\frac{\hbar}{\ell}=\sqrt{\hbar\mu\omega}.
\]

For fixed $\eta$, small $Q/Q_{\rm loc}$ is a sufficient low-resolution window. A perturbative form factor at fixed $Q\ell/\hbar=O(1)$ would require its full non-Gaussian state correction; the radius alone does not determine it. In particular, inserting the corrected radius into a Gaussian exponential does not establish the anharmonic form factor or a uniform large-$Q$ tail.

If the same single-current Born-rate assumptions as the manuscript apply, then near $Q=0$

\[
|F(Q)|^2=1-\frac{Q^2r_E^2}{3\hbar^2}+O(Q^4\ell^4/\hbar^4).
\]

The positive radius correction increases the leading rate deficit at a given physical $Q$. A radius scaling as $\hbar$ still does not imply pointlike scattering at fixed physical $Q$ when the resolution length is $\hbar/Q$; the fixed-$Q$ limit leaves the controlled small-$Q/Q_{\rm loc}$ window.

Separately require nonrelativistic internal momenta and probe momenta small compared with the relevant $mc_{\rm light}$ and $Mc_{\rm light}$ scales, and binding energies small compared with the constituent rest energies. Choosing $V_0\ll\min(m,M)c_{\rm light}^2$ and a sufficiently large $R$ can accommodate the deep-well and nonrelativistic conditions together. The $\varepsilon$ expansion by itself does not bound omitted relativistic current effects; those require a separate accuracy estimate if compared to the displayed correction.

This completes the assigned radius coefficient. One subsequent calculation, if chosen, is the leading full elastic-form-factor correction at fixed $Q\ell/\hbar$, including its non-Gaussian shape. It has not been performed here.
