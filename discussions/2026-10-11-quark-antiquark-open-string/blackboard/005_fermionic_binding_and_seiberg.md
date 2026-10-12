# Two fermionic endpoints bound through an adjoint fermion

12 October 2026. The user corrected the active target: replace the binding carrier, rather than bind a preformed meson to an inert neutral spectator. They also proposed Seiberg duality if the string belongs to super-QCD. This entry constructs a limited binding example, then tests what ordinary SQCD can supply. No numerical scripts were needed. The few-body variational method and SQCD results are established tools; their application here is not a claim of literature novelty.

## 1. Separate exchange from a retained carrier

Take “the same colours as the gluon” to mean an adjoint carrier, λ in the 8 of SU(3). This is an explicit working interpretation. A propagating fermion exchanged virtually and a fermion retained in a bound-state sector are different possibilities:

- A local vertex λ qbar q contains three Grassmann-odd fields and is not an ordinary Lorentz-scalar interaction. SQCD instead permits a quark–squark–gluino vertex. Single-gluino exchange connects endpoint **conversion** channels. Eliminating a higher two-squark channel can induce attraction in a two-quark channel, but that state remains even under fermion parity.
- A retained q qbar λ sector has odd parity. Its q qbar pair need not be a meson constituent: to make a singlet with an adjoint, the pair must be a color octet. Interactions containing two λ fields can bind the endpoints without converting them into scalars.

The second possibility admits the following explicit toy solution. It has an active fermionic binding constituent, not an inert spectator attached to an independently bound meson.

## 2. A finite-range fermion-only binding model

Assume nonrelativistic q, qbar and λ fields, with masses m, m and M. Color is a **global** SU(3) symmetry here; select its singlet sector. Constituent numbers are separately conserved, so annihilation is absent by definition. These are limitations of the model, not properties already established for relativistic QCD. One endpoint flavor suffices for binding. Additional flavors may give a charged state; neither pion dynamics nor generations are required for this test.

Use units ℏ=c=1 and Tr(TᵃTᵇ)=δᵃᵇ/2. There is one singlet in 3⊗3bar⊗8. In it,

\[
T_q\!\cdot T_{\bar q}=\frac16,\qquad
T_q\!\cdot T_\lambda=T_{\bar q}\!\cdot T_\lambda=-\frac32.
\]

These follow from C_F=4/3 and C_A=3: q qbar is an octet, while qλ is a triplet and qbar λ an antitriplet. The positive q qbar factor would be repulsive for a vector Coulomb kernel, but **we do not introduce such a kernel or gluon exchange**.

Instead define a spin-independent regulated density interaction,

\[
V=G\,[T_q\!\cdot T_\lambda f_R(x)
       +T_{\bar q}\!\cdot T_\lambda f_R(y)],\quad
f_R(r)=\frac{e^{-r^2/R^2}}{\pi^{3/2}R^3},\quad G>0,
\]

where x=r_q−r_λ and y=r_qbar−r_λ. There is **no direct q qbar potential**. G has mass dimension −2. This is a finite-range regulated four-fermion contact interaction: schematically a color density of each endpoint times the color density of λ. Each vertex has even fermion parity. No propagating bosonic field is part of this Hamiltonian. We assume its coupling; we have not derived it from SQCD, a string, or a UV completion. A bosonic auxiliary-field rewriting would not by itself add a propagating boson, but a UV completion might do so.

After removing the center of mass, μ=mM/(m+M) and

\[
H_{\rm rel}=-\frac{\nabla_x^2+\nabla_y^2}{2\mu}
             -\frac{\nabla_x\!\cdot\nabla_y}{M}
             -\frac{3G}{2}\,[f_R(x)+f_R(y)].
\]

The cross term accounts for recoil of the shared fermionic carrier. Dropping it as an operator would be unjustified.

### Binding, including the breakup threshold

First consider the endpoint–carrier dimer,

\[
h=-\frac{\nabla^2}{2\mu}-\frac{3G}{2}f_R(r).
\]

For the normalized orbital u_a(r)=(πa²)^(-3/4) exp[−r²/(2a²)],

\[
\langle h\rangle_a=\frac{3}{4\mu a^2}
       -\frac{3G}{2\pi^{3/2}(R^2+a^2)^{3/2}}.
\]

Minimizing the sufficient condition for this expression to be negative gives a²=2R² and

\[
\boxed{G>\frac{3\sqrt3\,\pi^{3/2}}{4}\frac{R}{\mu}.}
\]

This is a sufficient bound, not the exact critical coupling. It guarantees an exact dimer ground energy ε₂<0. Let u be its real normalized S-wave orbital. The three-body trial state u(x)u(y), multiplied by the singlet color wavefunction, has

\[
\langle\nabla_x\!\cdot\nabla_y\rangle
   =\Big(\int u\nabla u\,d^3x\Big)^2=0,
\qquad \langle H_{\rm rel}\rangle=2\epsilon_2.
\]

Both possible dimer-plus-spectator thresholds are ε₂, and the three-free-particle threshold is zero. Thus

\[
\boxed{E_3\leq 2\epsilon_2<\epsilon_2<0.}
\]

The Hamiltonian is bounded below and has bounded short-range potentials, so it has a genuine three-body bound state below breakup, not merely an energy below the three-free-particle threshold. The shared λ binds both endpoints; removing it leaves q and qbar unbound. With the two spin-1/2 endpoint spins coupled to zero and λ spin 1/2, the S-wave state is fermionic. The three species are distinct, so there is no additional identical-species exclusion obstruction.

Choose mR, MR≫1 and energies small compared with m,M to use this nonrelativistic model consistently. This proves binding in its fixed-number sector. It does not prove stability against relativistic annihilation, a gauged-color completion, a confining flux tube, a light lepton mass, or pion dynamics. The known gluino R-hadron field content is a useful comparison; ordinary R-hadron binding still uses QCD gauge interactions, which have not been imported into this proof.

### What this does and does not buy for scattering

Binding by a fermionic constituent does not automatically hide spatial size. For equal endpoint masses, a state symmetric under x↔y, neutral λ, and a leading constituent probe current, the two endpoint form factors coincide. If their charges are Q_i and −Q_j, the whole-state form factor is (Q_i−Q_j)f(k), with f(0)=1. For a charged state its normalized charge radius is the positive endpoint mean-square displacement from the center of mass.

For the Gaussian product trial state specifically,

\[
\langle r_{\rm ch}^2\rangle_{\rm trial}
=\frac{(m+M)^2+m^2}{(2m+M)^2}\frac{3a^2}{2}.
\]

This follows from r_q−R_cm=[(m+M)x−my]/(2m+M); it is not an exact form factor of the interacting ground state or a high-energy scattering calculation. The binding milestone is crossed for this toy model; pointlike whole-state scattering remains a separate unsolved target.

## 3. What Seiberg duality supplies

Consider N=1 electric SU(N_c) SQCD with N_f pairs Q_i, Qtilde_j and no tree superpotential. Each superfield contains a scalar φ and a Weyl fermion ψ; pairing the fundamental and antifundamental Weyl fields gives vectorlike Dirac quarks. The vector multiplet contains **both** the gauge boson and the adjoint gluino. The component coupling has the form

\[
\mathcal L_Y=-\sqrt2g\,
 [\phi_i^\dagger T^a\psi_i\lambda^a
 +\widetilde\phi_j^\dagger T_{\bar F}^a\widetilde\psi_j\lambda^a]
 +\mathrm{h.c.}
\]

Spinor contractions are understood. This realizes fermionic exchange with scalar endpoint conversion. Gauge invariance still requires the bosonic connection, and supersymmetry fixes related interactions. Ordinary SQCD consequently provides a controlled laboratory, not an automatic replacement of all bosonic glue.

The magnetic description has SU(N_f−N_c), dual quarks q_m,qtilde_m, a gauge-singlet meson superfield M_c, and W=h qtilde_m M_c q_m. The electric operator M_e=Qtilde Q maps, up to normalization, to μ_match M_c. Its components are

\[
(M_e)|=\widetilde\phi\phi,\qquad
\psi_{M_e}=\widetilde\phi\psi+\widetilde\psi\phi,
\]
\[
F_{M_e}=\widetilde\phi F_Q+F_{\widetilde Q}\phi
        -\widetilde\psi\psi.
\]

Thus the usual SQCD mesino is a scalar–fermion operator, not by definition two physical fermions held by a gluino. The two-fermion bilinear occurs in the top component. Calling all components simply “the meson” would conceal the distinction the user raised.

### A candidate dictionary that retains the intended endpoints

An appropriate local odd interpolator is

\[
\mathcal H_{ji,\alpha}
  =(\widetilde\psi_j T^a\psi_i)\lambda^a_\alpha.
\]

The endpoint spinors in parentheses are contracted. H is a color singlet of three fermions, with an octet endpoint pair; it is not a color-singlet meson times a neutral spectator. For anomaly-free R(Q)=R(Qtilde)=r=1−N_c/N_f,

\[
R(\mathcal H)=2(r-1)+1=2r-1=R(\psi_{M_e}).
\]

Flavor representation, baryon number zero, and vector flavor charges also agree. For an electromagnetic flavor embedding, its charge is Q_i−Q_j. This does not assign it a lepton number or establish a physical lepton.

These symmetries **allow**, but do not prove, an infrared overlap

\[
\mathcal H\ \longrightarrow\ c_H\Lambda^3\psi_{M_c}+\cdots
\quad (\mu_{\rm match}\sim\Lambda).
\]

Equivalently the coefficient of the unnormalized ψ_Me has dimension two. If c_H is nonzero in a specified source/renormalization prescription, a free infrared mesino contributes a pole proportional to |c_H|²Λ⁶ p·σ/(p²+i0) to the H two-point function. The coefficient is not a constituent probability: finite operator redefinitions can change overlaps with lower-dimension operators. A current or scattering matrix element is needed for an observable statement.

Nor is H a new protected chiral primary simply because Qtilde W_α Q is chiral. That superfield is trivial in the fundamental-matter SQCD chiral ring; its top component contains H **and other component terms**. The descendant relation does not give an isolated exact H↔ψ_M map. We have not calculated c_H.

### Choose the number of flavors for a reason

At the massless origin, the SU(3) cases give a sharp choice:

| N_f | Standard SQCD behavior | Consequence for this test |
| --- | --- | --- |
| 2 | ADS runaway without further terms | A two-flavor QCD-like starting point is not automatically a vacuum at the SQCD origin. |
| 3 | Quantum-deformed moduli space | The classical origin is removed; no free magnetic SU(0) description. |
| 4 | Smooth confinement with mesons and baryons (s-confinement) | A controlled infrared composite-fermion laboratory, but no non-Abelian magnetic gauge group. |
| 5 | Magnetic SU(2) in the interacting conformal window | Not a free magnetic fermion: Δ(M)=6/5 and Δ(ψ_M)=17/10 at the fixed point. |

For N_c=3,N_f=4 the exact holomorphic superpotential, in unnormalized electric composite variables, is

\[
W=\frac{\widetilde B M_e B-\det M_e}{\Lambda^5}.
\]

Writing M_e∼ΛM_c and B_e∼Λ²B_c gives a marginal cubic interaction plus an irrelevant det(M_c)/Λ term; numerical Kähler normalizations are not fixed by holomorphy. Mesons and baryons become free asymptotically in the infrared. The massless origin has unbroken chiral symmetry, so its massless scalar mesons are not already QCD Goldstone pions. Four flavors are being added to obtain this controlled phase, not to infer weak generations. Decoupling them back to two changes the phase and needs a new analysis.

The **strict** non-Abelian free-magnetic window is N_c+1<N_f<3N_c/2. Its smallest integer example is electric SU(5), N_f=7, magnetic SU(2), with b_m=2N_f−3N_c=−1. SU(4),N_f=6 is the marginal boundary, treated in the usual phase diagram separately from this strict inequality. SU(3) has no non-Abelian example in the free-magnetic range. A change to SU(5) changes the color model and cannot be silently identified with physical QCD.

These weak descriptions concern momenta below their matching scale Λ. They do not prove pointlike scattering above Λ. A possible target is a derived hierarchy Λ_had≪Q_probe≪Λ, with a specified deformation producing the lower binding/string scale. Exact supersymmetry links scalar and fermion dynamics; assigning different radii or couplings to partners is not itself such a derivation. At a conformal origin, a mesonic Regge spectrum and string tension are also not supplied automatically.

## 4. What changed, and the next discriminating step

**Achieved here:** an explicit interaction, a sufficient binding condition, and a three-fermion singlet below breakup in a stated contact model. Its fermionic constituent is necessary for binding. Seiberg duality supplies a separately controlled composite-fermion phase and a candidate symmetry-compatible operator bridge, not a proved identification with that trimer.

**Next:** test a deformation that could connect these descriptions. Start by matching the low-energy qλ interaction obtained on integrating out a specified massive squark, recording its spin/color projection, sign, cutoff, and annihilation channels. Ask whether the attractive coefficient and nonrelativistic range used above are attainable without losing control. If they are, compute a current of that same state; if they are not, retain the contact model as an existence example and change the completion. Do not infer the required coefficient, c_H, or a string from symmetry alone. The s-confining holomorphic superpotential by itself does not fix the needed nonholomorphic scattering data.

Primary source: Seiberg, [hep-th/9411149](https://arxiv.org/abs/hep-th/9411149), §§2–4, especially Eq. (3.3) and Eq. (4.14), retrieved and read on 12 October. See the [source reading record](../references/literature_2026-10-12.md).
