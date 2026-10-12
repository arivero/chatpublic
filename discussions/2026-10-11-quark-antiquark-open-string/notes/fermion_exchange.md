# Fermionic coherence, exchange range, and contact interactions

The user's motivating conjecture is that a bosonic field can build a coherent binding field, whereas fermionic statistics obstruct this buildup and may confine a fermionic interaction to contact. This note records what survives and what needs an additional mechanism. Natural units are used throughout.

**12 October correction:** the intended construction changes the binding carrier itself. The [new three-fermion model](../blackboard/005_fermionic_binding_and_seiberg.md) proves binding with an active adjoint fermion in a finite-range contact theory. The exchange selection rule below does not forbid that retained-constituent mechanism, whose vertices have two carrier fields.

## The distinction in classical fields is real

Let \(P=(-1)^F\) and let a physical density operator respect fermion parity, \([\rho,P]=0\). Since \(P\chi P=-\chi\),

\[
\langle\chi\rangle=\operatorname{Tr}(\rho\chi)
=-\operatorname{Tr}(\rho\chi)=0.
\]

A fermionic field therefore cannot have the same ordinary c-number classical expectation value as a bosonic field. Formal Grassmann coherent states do not overturn this physical statement. Pauli exclusion also prevents macroscopic occupation of a single one-particle fermion state.

But the two-point function \(\langle T\chi(x)\bar\chi(y)\rangle\) is even under parity and need not vanish or be local. Fermions have quantum coherence, and even operators such as fermion bilinears or Cooper-pair operators can support collective order. The absence of an odd one-point function is not the absence of a propagator or interaction.

A force also need not be established by a macroscopic coherent population of mediators. Exchange amplitudes and source-dependent energy shifts can be calculated without that population. For QCD confinement, a gauge-invariant diagnostic is the energy inferred from a Wilson loop; the flux tube is not established merely by saying that gluons can occupy one state.

## Allowed fermion exchange conserves angular momentum

For scalar fields \(\phi_i\), spinors \(\psi_i\), and a mediator \(\chi\),

\[
\mathcal L_{\rm int}
=-\sum_i\bigl(g_i\phi_i^\dagger\bar\chi\psi_i+\mathrm{h.c.}\bigr)
\]

is Lorentz invariant and contains an even number of fermionic fields at each vertex. It allows a process such as

\[
F_1+B_2\longrightarrow B_1+F_2.
\]

The source changes between a bosonic and a fermionic state while spin is carried by the exchanged spinor. Angular momentum is conserved. The interaction is off-diagonal in source species; it is not a temporary exception to a conservation law.

A single fermion cannot instead provide the ordinary one-particle exchange between two unchanged fermionic sources: each cubic vertex would contain three fermions. That is a selection rule on the channel, not a rule that any allowed fermion exchange must be contact. Elastic effects from multiple fermion exchanges are also possible.

After choosing allowed spin/orbital channels, an interaction between \(|FB\rangle\) and \(|BF\rangle\) can have the matrix form

\[
H(r)=\begin{pmatrix}E_1&K(r)\\K(r)^*&E_2\end{pmatrix}.
\]

Both basis states have the same total fermion parity, so their coherent mixing is allowed. If \(E_1=E_2=E_0\), the energies are \(E_0\pm|K(r)|\). A spatially varying exchange kernel can therefore produce attractive and repulsive energy branches without any nonzero classical fermionic field.

## Its range follows from propagation and thresholds

For a free relativistic fermion,

\[
S_F(q)=\frac{i(\not q+m_\chi)}{q^2-m_\chi^2+i0}.
\]

The numerator carries spin information. The denominator has the same mass shell as a scalar propagator. At zero energy transfer, its spatial transform is built from

\[
G_m(r)=\int\frac{d^3\mathbf q}{(2\pi)^3}
\frac{e^{i\mathbf q\cdot\mathbf r}}{\mathbf q^2+m^2}
=\frac{e^{-mr}}{4\pi r}.
\]

Up to vertex factors and overall conventions, the spinor kernel contains \((m+i\boldsymbol\gamma\cdot\nabla)G_m(r)\). In particular,

\[
\nabla G_m(r)
=-\hat{\mathbf r}\frac{e^{-mr}}{4\pi}
\left(\frac m r+\frac1{r^2}\right).
\]

It has a finite range set by \(1/m\). In the massless limit the derivative kernel has a power-law tail, not delta-function support. Projection onto a particular source/spin channel can make contributions vanish; there is no assertion that every channel produces a nonzero static force.

For source conversions with energy transfer \(\omega\), the exponential scale below threshold is instead \(\sqrt{m_\chi^2-\omega^2}\). The simple static formula assumes negligible energy transfer, which can be arranged with degenerate local source states. Above threshold, real propagation and inelastic effects can invalidate an instantaneous-potential interpretation.

## Contact is a low-transfer limit or an auxiliary-field choice

Introduce the odd current \(J=\sum_i g_i\phi_i^\dagger\psi_i\) and write

\[
\mathcal L=\bar\chi(i\!\not\partial-m_\chi)\chi
-\bar\chi J-\bar J\chi.
\]

Integrating out the quadratic mediator gives

\[
\mathcal L_{\rm eff}
=-\bar J(i\!\not\partial-m_\chi)^{-1}J
=\frac{\bar J J}{m_\chi}
+\frac{\bar J i\!\not\partial J}{m_\chi^2}+\cdots.
\]

The derivative expansion requires the transferred energies and momenta to be small relative to the mediator mass. Chiral projectors can remove the displayed leading term in particular models. None of this eliminates the underlying pole or changes statistics into a zero-range theorem. Heavy boson exchange has an analogous local expansion.

An auxiliary fermion with no kinetic term gives an exactly local interaction algebraically. Such a field has no propagating particle pole; this is not a construction of a physical Ramond string or an observed fermion.

Energy–time uncertainty does not authorize temporary energy nonconservation. In a stationary, translation-invariant theory, energy and momentum are conserved at vertices. Virtual lines need not satisfy the on-shell mass relation; that is different from violating conservation. The familiar inverse-mass length arises from the propagator. Angular momentum is likewise conserved throughout.

## Even a contact binding force does not imply a pointlike bound state

This is a second, independent issue. A renormalized zero-range two-body interaction can have a shallow bound state with positive scattering length \(a\), reduced mass \(\mu\), and

\[
E_B=\frac1{2\mu a^2},\qquad
\langle r_{\rm separation}^2\rangle=\frac{a^2}{2}.
\]

Its radius grows as the binding becomes shallow, despite the interaction being contact. For equal masses and one charged constituent, the leading zero-range form factor is

\[
F(Q)=\frac4{aQ}\arctan\frac{aQ}{4}
=1-\frac{a^2Q^2}{48}+\cdots,
\qquad \langle r_{\rm charge}^2\rangle=\frac{a^2}{8}.
\]

This example is valid within the zero-range EFT's momentum domain. It demonstrates that exchange range and the size inferred from whole-bound-state scattering are separate quantities.

## Consequence for the string proposal

A fermionic object can be extended and held together by a bosonic field; ordinary baryons illustrate this. A Ramond string also retains the bosonic embedding coordinates and string tension. Calling the state fermionic does not mean its binding field has been replaced by a classical fermionic field.

Moreover, the simple four-Ramond disk amplitude factorizes through NS states. Lack of a classical fermionic mediator field does not remove that bosonic exchange tower or its string corrections.

The clarified constructive question is: **can a fermionic carrier bind the two fermionic endpoints, with a completion that gives the desired whole-state scattering?** Endpoint-conversion models and a retained adjoint constituent are different mechanisms. The new contact construction advances the latter; its completion and current remain to be derived. Neither a preformed meson nor an inert spectator should be silently substituted for the binding channel.

The working formulation and explicit tests are in [blackboard entry 001](../blackboard/001_fermionic_coherence_and_range.md). [The calculation script](../scripts/fermion_exchange_checks.py) verifies the propagator algebra, spatial kernel, local expansion, coupled-channel eigenvalues, and zero-range dimer example. These are diagnostic examples, not a completed string model.
