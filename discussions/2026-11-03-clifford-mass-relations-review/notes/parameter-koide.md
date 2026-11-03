# Parameter scans with integer structure preserved; Koide geometry

## What may be varied?

In original H1 the complex mode-space dimension 4, matrix dimension 16, sector ranks `(1,14,1)` and response eigenvalues `(0,1,17)` are **exact integer consequences of definitions**. They are not continuous error bars. An integer change such as response weight `n=16` or `18` means a distinct theory; do not include it as a continuous uncertainty around 17.

Real radius multiplier `lambda` and complete-response correction coefficient `eta` are explicitly labelled *deformations* of physical postulates. The original paper sets `lambda=eta=1`. With `n=17` fixed and `k=3/(2alpha)`, the deformed masses are

`rho_mu=k/lambda+(17/14)*eta`, `rho_tau=17*(k/lambda-eta)`.

The two observed ratios yield a unique solution for these two continuous parameters: `x=(14*rmu+rtau)/31`, `lambda=k/x`, `eta=(14/17)*(rmu-x)`. With the discussion's CODATA muon and PDG tau central values, `lambda≈1.000008277`, `eta≈1.001399651`. The original integer model is therefore numerically close to this fit. When lambda and eta are fixed by H1/H2, there are zero tunable mass parameters.

## Koide as a cone

For `v=(sqrt(m_e),sqrt(m_mu),sqrt(m_tau))`, let `n=(1,1,1)/sqrt(3)`. Then `Q=(Σm_i)/(Σsqrt(m_i))²=||v||²/[3(v.n)²]`. Exact Koide `Q=2/3` is the **45° cone** `||v_parallel||²=||v_perp||²`. A parametrization on this cone is `sqrt(m_k)=a[1+sqrt(2)*cos(delta+2*pi*k/3)]`, with the components restricted to be nonnegative. The 45° condition is not derived by the Clifford carrier.

In the manuscript `Q≈0.66666598341546`, equivalent to `Q/(2/3)-1≈-1.0248768 ppm`. For the comparison masses chosen in the discussion, the central experimental Koide is about `0.666664463406`. Along any *exact* fit to all three masses, Koide is trivially constant and adds no independent constraint.

The actual model is **not** a successive alpha-alpha² lepton hierarchy. Its two heavy lepton masses both have leading terms `O(1/alpha)` relative to electron. In a hypothetical radiative hierarchy `m_tau=M`, `m_mu=A alpha M`, `m_e=B alpha² M`, `Q=2/3` becomes a quartic in `t=sqrt(alpha)`; it may have isolated positive roots, but cannot hold as an identity for all alpha when A,B are finite positive constants, since `Q->1` as alpha->0.

## Proton parameter identifiability

With the integer SU(3) representation dimensions fixed, a *continuous* positive response matrix `M_{u,v}=[[1,-u alpha],[-u alpha,1-v alpha]]` has determinant `1-v alpha-u² alpha²>0` and the same colour-singlet structure. Its prediction depends on `u²/(1-v alpha)`, leading to a flat fit direction in `(u,v)`. This is an explicit extension beyond the original `u=v=1` choice, not an assertion that the manuscript has free coefficients internally.

See the 8-page PDF in `../reports/` for plots of discrete weight alternatives, constrained continuous scans and Koide variation.
