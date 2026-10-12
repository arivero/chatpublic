# 002 — Two branches, conserved charges, and a mixing diagnostic

12 October 2026. Status: checked algebra and a conditional EFT example. **No complete dual construction.** This entry supports the [independent manuscript](../manuscript/README.md), written before receipt of the missing preprints.

## What is being tested

The strong target is a theory in which the whole fermion and extended bosonic hadron are related by a derived operator/spectral dictionary, while the fermion has approximately elementary hard scattering. A weaker, useful target permits an elementary fermion with hadronic dressing. These must not be counted as the same achievement.

The user has identified Schwarz's 1971 *Dual quark-gluon model of hadrons* as the historical anchor, and recalls related early work with Joel Scherk. This is more specific than our initial Ramond/dual-parton/endpoint-string reading trail. The precise identification and historical claims await primary-text review. An INSPIRE metadata request returned proxy 403 on 12 October; no publication details have been invented to fill the gap.

## Charge and statistics ledger

Assume actual vectorlike Dirac endpoint quarks, conventional separately conserved baryon and lepton numbers, and a color-singlet odd carrier. Let `D` be a color-3 scalar antidiquark, and `M` a color-singlet meson component.

| Object | Color | Fermion parity | B | L |
| --- | --- | --- | --- | --- |
| M = q qbar | 1 | even | 0 | 0 |
| D = qbar qbar | 3 | even | −2/3 | 0 |
| χQ | 1 | odd | 1 | 0 |
| χL | 1 | odd | 0 | 1 |
| D χQ | 3 | odd | 1/3 | 0 |
| M χL | 1 | odd | 0 | 1 |

Both carriers may have electric charge zero. A charged meson times χL can then interpolate a charged lepton, but this says nothing yet about its mass, family, or scattering. χQ and χL may denote elementary trial fields, composite operators, or specified topological sectors; their existence and dynamics have to be supplied.

One carrier with a fixed `(B,L)` cannot do both jobs under these assumptions. If only `B−L` is conserved, using an antilepton in the second branch makes both required shifts `B−L = +1`. That relaxes the bookkeeping, but does not retain separate B and L or explain the dynamics. A charge-conjugate carrier is also a distinct charge sector; it must be included explicitly.

For `u ↔ [dbar sbar] χQ`, `d ↔ [sbar ubar] χQ`, and `s ↔ [ubar dbar] χQ`, electric charges match. The common missing flavor-number vector is `(Nu,Nd,Ns)=(1,1,1)`, so χQ has B=1, Q=0, strangeness −1. This identifies a weight, not a unique SU(3) flavor representation. A nonet or baryon-octet choice needs its full tensor contraction and dynamics. Replacing χQ by an existing baryon can reduce the operator to an ordinary quark with additional even dressing; pole/current calculations decide whether anything stronger has occurred.

## Pauli check before representation counting

For two identical antiquark species treated in a flavor multiplet, the total exchange sign must be negative. In an S wave the spatial sign is positive. The color-3 channel is antisymmetric and spin zero is antisymmetric, so flavor must be antisymmetric too. Thus the scalar color-3 flavor multiplicity is `Nf(Nf−1)/2`: 3 for three flavors, 10 for five. A five-flavor symmetric 15 does not belong to this same scalar channel. Spin one or another color representation changes the count.

## A calculable weak correspondence

Let an elementary fermion F0 and a composite resonance C have identical unbroken charges. A real symmetric Dirac mass matrix is a restricted but sufficient example:

```math
\mathsf M=\begin{pmatrix}m_0&\delta\\\delta&M_C\end{pmatrix},\qquad M_C>m_0.
```

For the light eigenvector `F = cos θ F0 − sin θ C`,

```math
\tan2\theta=\frac{2\delta}{M_C-m_0},\qquad
\eta=\sin^2\theta=\frac12\left[1-\frac{M_C-m_0}{\sqrt{(M_C-m_0)^2+4\delta^2}}\right].
```

If a normalized probe current is diagonal in this basis, has no transition form factor, and the elementary component has form factor one,

```math
F_F(Q^2)=1-\eta+\eta F_C(Q^2),\qquad r_F^2=\eta r_C^2.
```

This is a conditional current model, not a general probability formula for hadronic overlap. Off-diagonal currents invalidate this simple expression. For quarks, use a specified gauge/factorization prescription and physical jet observables rather than treating the color-charged form factor as an isolated observable.

A massive vector with interaction `gρ ρμ Cbar γμ C` couples to the light state with `gρ η`. At momenta small relative to its mass, integrating it out gives

```math
\Delta\mathcal L=-\frac{g_\rho^2\eta^2}{2m_\rho^2}
(\bar F\gamma_\mu F)(\bar F\gamma^\mu F)+\cdots.
```

The sign follows from the displayed mass/interaction convention in the manuscript. There are also transitions to the heavy state. The expansion is not valid at or above the vector resonance; a small low-energy coefficient cannot hide that regime without examining production, poles, and widths.

This construction suppresses visible compositeness by making the state mostly elementary. It does **not** derive an entirely composite pointlike fermion. A strong duality would have to generate the elementary variable, its small overlap, and the bosonic/fermionic spectrum. It would also need to protect the light mass against mixing corrections.

## Why fermion parity is not the missing protection

Even if an odd field cannot acquire a conventional one-point function, `Fbar γμ F`, `Fbar F`, and permitted bosonic couplings remain even. The vector-current four-fermion operator is also compatible with massless chiral symmetry. Neither the absence of a classical odd field nor small Dirac mass explains a small coefficient. Useful candidates are a calculated wavefunction overlap, weak inter-sector mixing, or a genuinely dual weak variable; their stability and scale range must be established.

## Checks and next discriminator

[branch_checks.py](../scripts/branch_checks.py) verifies the three-flavor charge differences, the Pauli tensor dimensions, the mass/current rotations in 32 numerical cases, the radius relation, and tree-level elimination of the massive vector. Results: [branch_results.json](../calculations/branch_results.json).

The next substantive calculation is a renormalized spectral matrix and probe-current three-point function for an actual candidate realization of both branches, followed by a four-point amplitude. A formal dictionary or a two-state mixing ansatz alone does not supply this calculation. The [workplan](../notes/workplan.md) defines the decision points.
