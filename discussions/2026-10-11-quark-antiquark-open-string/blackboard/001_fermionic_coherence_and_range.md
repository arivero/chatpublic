# 001 — Does absent fermionic field buildup hide the string?

Working entry, 2026-10-11. Status: the motivating hypothesis is being refined; a statistical argument alone does not establish contact range or pointlike scattering.

## User motivation

The user proposes that bosonic symmetry permits many quanta in one state and therefore a coherent binding field. A corresponding fermionic field cannot build up in the same way, and spin exchange seems problematic; perhaps its effective reach is only contact. The user relates this intuition to inverse-energy or inverse-momentum uncertainty scales.

The intended endpoint quarks remain vectorlike Dirac quarks, as clarified in the preceding exchange. This entry does not revert to the earlier “non-Dirac” typo.

## Separate four observables

| Question | Object to calculate |
| --- | --- |
| Can there be a classical field expectation? | One-point function and its parity/gauge properties |
| How far does a particular exchange act? | Propagator/current kernel, poles, thresholds, energy transfer |
| Is the composite pointlike under a hard probe? | Current form factors and complete scattering amplitudes |
| Is there a confining mesonic string? | Flux-tube energy, Wilson-loop behavior, spectrum, chiral dynamics |

These quantities need not share one scale or one yes/no answer.

## A. A valid selection rule, but no locality consequence

For \(P\rho P=\rho\) and \(P\chi P=-\chi\),

\[
\operatorname{Tr}(\rho\chi)=-\operatorname{Tr}(\rho\chi)=0.
\]

The pair \(\chi(x)\bar\chi(y)\) is parity even, so this argument gives no restriction on its separation. A normalized fermion one-particle wave packet also has coherent propagation despite the absence of a classical odd field expectation.

**Recorded conclusion:** absent fermionic one-point coherence does not imply absent two-point propagation. This implication is rejected. The selection rule itself is retained.

## B. Explicit spatial kernel

The free Dirac inverse satisfies

\[
(\not q-m)(\not q+m)=(q^2-m^2)\mathbf1.
\]

At zero frequency, the scalar part of the spatial kernel is the Yukawa Green function. An independent representation useful for numerical checking is

\[
G_m(r)=\frac1{(4\pi)^{3/2}}\int_0^\infty
\frac{d\tau}{\tau^{3/2}}
\exp\!\left[-m^2\tau-\frac{r^2}{4\tau}\right].
\]

It equals \(e^{-mr}/(4\pi r)\). The spinor numerator produces mass and gradient terms. At \(m=0\), \(\partial_rG_0=-1/(4\pi r^2)\), explicitly nonzero away from the source. Source projection may kill a particular term; that requires a specified coupling.

For a conversion frequency \(\omega\), use the denominator \(\mathbf q^2+m^2-\omega^2-i0\). The subthreshold decay constant is \(\kappa=\sqrt{m^2-\omega^2}\). Thus even “range equals inverse mass” has an energy-transfer qualification. It is not a universal spin-dependent statement.

## C. A force without a classical odd field

After selecting allowed angular-momentum channels, take a two-state sector with total odd parity:

\[
|1\rangle=|FB\rangle,\qquad |2\rangle=|BF\rangle.
\]

Relative to the mean energy, a Hermitian interaction has

\[
H=\begin{pmatrix}\Delta/2&K(r)\\K(r)^*&-\Delta/2\end{pmatrix},
\qquad
E_\pm=\pm\sqrt{\Delta^2/4+|K(r)|^2}.
\]

At degeneracy this is \(\pm|K(r)|\). With large channel splitting it gives a perturbative energy shift proportional to \(|K(r)|^2/\Delta\). Neither requires a nonzero fermion expectation value. The Yukawa vertex \(\phi^\dagger\bar\chi\psi\) carries the necessary angular momentum and preserves total parity.

Qualification: degeneracy of the two *total* channel energies does not by itself make each local transition frequency zero. The static exchange example also assumes negligible local transition frequency. Otherwise use the frequency-dependent kernel above.

A large splitting may suppress a coupling-induced energy shift without making it exactly local: light exchanged modes can still generate long-distance tails. Therefore a large source splitting is not by itself the required spectral gap.

## D. Independent counterexample: zero-range binding with a large radius

Use a renormalized nonrelativistic zero-range EFT, not an unregulated bare delta potential in three dimensions. For positive scattering length \(a\), a shallow S-wave bound state has the leading wavefunction

\[
\psi(\mathbf r)=\frac1{\sqrt{2\pi a}}\frac{e^{-r/a}}r,
\qquad E_B=\frac1{2\mu a^2}.
\]

The radial probability measure is \((2/a)e^{-2r/a}dr\). It integrates to one and gives \(\langle r^2\rangle=a^2/2\).

For equal masses and one charged constituent, its position relative to the center of mass is \(\mathbf r/2\), so

\[
F(Q)=\frac2a\int_0^\infty dr\,e^{-2r/a}
\frac{\sin(Qr/2)}{Qr/2}
=\frac4{aQ}\arctan\frac{aQ}{4}.
\]

This yields \(\langle r_{\rm charge}^2\rangle=a^2/8\). The state can be much larger than the underlying interaction range. The EFT permits a window \(1/a\ll Q\ll\Lambda_{\rm UV}\) in which the contact approximation to the force is good but the bound state's structure is resolved.

**Recorded conclusion:** even granting a contact interaction does not establish a pointlike state. This is a separate missing implication in the original motivation.

## E. Revised research conjecture

Investigate whether the dual/geometric theory supplies a low-energy hierarchy in which:

1. The even sector has the interactions required for confinement and pion/chiral dynamics.
2. The candidate odd sector couples weakly, or only through suitably gapped channels, to the *additional hadronic structure* that would otherwise affect its hard scattering.
3. Its ordinary electromagnetic/color couplings remain those required by the intended point-particle limit.

This is a hypothesis about dynamics and spectral couplings. It does not follow solely from the statistics of a mediator. It also does not require every interaction to be contact: a point charged fermion still has long-range electromagnetic interactions.

An appropriate spectral gap in the relevant transfer channel permits a derivative expansion; low-mass states with nonzero residue can obstruct it. Suppression of residues may be as important as their masses. The precise statement must use the channel actually probed, not a universal “fermionic force” label.

## F. Concrete next tests

- Specify what changes between the bosonic and fermionic string states: only overall statistics, the endpoint states, a defect sector, or the binding channel itself. In ordinary RNS theory the bosonic embedding coordinates and tension remain.
- Write the allowed couplings. An unchanged-source single-fermion exchange is forbidden, but a scalar or vector coupling to two fermions is allowed and can still communicate hadronic structure.
- Compute both the bosonic binding observable and the candidate fermion's current matrix element in the same theory. A transition potential alone is insufficient.
- Distinguish a high-mass propagating mediator from a strictly auxiliary Grassmann field. The latter cannot itself be the observed fermion.
- If duality is invoked, identify the odd operator/defect and map the probe current. Exact duality preserves physical observables and parity.

No completed model or new experimental limit is claimed. The six groups of checks in [fermion_exchange_checks.py](../scripts/fermion_exchange_checks.py) substantiate the diagnostic examples above; outputs are in [fermion_exchange_results.json](../calculations/fermion_exchange_results.json).
