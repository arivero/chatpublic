# Mathematical audit and GIGO ledger

## Inputs fixed by the manuscript

1. The round spin-frame manifold is SU(2) ≅ S³, with radius **the classical electron radius** `r_e=alpha*hbar/(m_e*c)`, rather than the reduced Compton wavelength `ell_e=hbar/(m_e*c)`.
2. Keep both signs of the lowest Dirac modes, giving a complex 4-dimensional spinor carrier `S`; take `W=End(S)`, complex dimension 16.
3. Distinguish the scalar `I` and grading/pseudoscalar `Sigma`, with `P_e`, `P_tau` rank-one and complementary `P_mu` rank 14.
4. Choose the **unnormalized** matrix trace `C(X)=tr(Sigma X) I` and graph response `A=(I-P_e)+C†C` with the two terms equally weighted.
5. Invariance under the full `U(1) x U(14) x U(1)` stabilizer; this is stronger than Spin(4) rotational symmetry.
6. H2: minimize mean response at fixed active auxiliary trace, and transfer the *complete* stationary displacement `B=Z*-A` into rest energy with coefficient `m_e*c²`, rather than the geometric coefficient `E*=3*m_e*c²/(2*alpha)`.
7. Physical identification of the three invariant profiles with electron, muon and tau, and a common charged Dirac field.

## Consequences of these axioms

`dim(W)=1+14+1`, `C²=0`, `C†C=16 P_tau`, `A=P_mu+17P_tau`, and `spec(A)={0,1,17}`. The mean-energy minimizer is `Z*=(31/14)P_mu`, and `B=(17/14)P_mu-17P_tau`. The mass operator prescribed by H1/H2 is `H/(m_e*c²)=P_e+[3/(2alpha)]A+B`. The lepton mass formulas follow exactly.

These are primarily correct finite-algebra calculations, but their derivation is **conditional** on the response and physical-calibration axioms. The integer 17 is not a three-sphere Dirac eigenvalue: it is `1+16`, with 16 coming from the squared norm of the prescribed trace map.

## Explicit countermodels and caveats

- No Clifford multiplication is required for the *same finite response spectrum*: on abstract complex `C^16`, take orthogonal unit `s,p`, `C=4|s><p|`, `P_e=|s><s|`, `P_tau=|p><p|`, and `P_mu=I-P_e-P_tau`. Then `C†C=16P_tau` and precisely the same spectra and stationary correction follow. This does not refute H1; it refutes necessity of Clifford multiplication for these finite coefficients.
- Spin(4) rotations alone do not give only three profiles. With `S=(2,1)⊕(1,2)`, `End(S)=2(1,1)⊕(3,1)⊕(1,3)⊕2(2,2)` and the rotational commutant has dimension `2²+1+1+2²=10`. The reduction to three uses the larger stabilizer by assumption.
- Replacing the unnormalized trace by `C'(X)=tr(Sigma X) I/4` changes `C'†C'` to `P_tau`, so `A'=P_mu+2P_tau`, while retaining the same block dimensions and positivity. Again, this changes H1 rather than contradicting it.
- The claimed full-space uniqueness of the return map needs a domain qualification. If trace balance is demanded only for positive active inputs, `J_c(Z)=[Tr(DZ)+c Tr(P_e Z)]P_mu/14`, `c≥0`, obeys the active conditions, whereas the maps differ on nonactive inputs. Global trace balance and preservation of the electron line remove this freedom.

## Proton extension: independent additional prescriptions

Colour algebra gives `3⊗3⊗3=1⊕8⊕8⊕10`, a unique colour singlet, and an identity `K_c=9(I-L_c)`. The chosen uncorrelated colour reference is `sigma_0=I_27/27`, giving `Tr(L_c sigma_0)=1/3`. These group-theoretic facts do *not* determine a proton mass.

Two extra physical prescriptions enter: geometric formation energy is set to **nine times the Dirac-level difference between radii** `ell_e` and `r_e`; and the response matrix is selected as `[[1,-alpha],[-alpha,1-alpha]]`. Its Schur complement `1-alpha²/(1-alpha)` produces the additive mass correction. Other positive colour-covariant response matrices `[[1,-u alpha],[-u alpha,1-v alpha]]` lead to `rho_p(u,v)=27/(2alpha)-83/6+u² alpha²/[3(1-v alpha)]` and the *same* colour singlet. This explicitly shows the non-uniqueness of the chosen continuous coefficients.

For the proton prediction, varying the measured `alpha^-1` by its input standard uncertainty `2.1e-8` propagates to about `2.835e-7` in the proton/electron ratio, versus quoted reference uncertainty of `3.2e-8`. The paper's small reference-only z residual should not be mistaken for a combined significance. CODATA correlations matter too.

## Physical interpretation

The fields in the paper are assigned an electron, muon, tau mass matrix and common electromagnetic charge; this demonstrates compatible field kinematics, not chirality-changing radiative generation. No QCD confinement scale or flavour-specific baryon binding calculation is derived. A colour singlet is shared by many baryons.
