# Next experiment: literal reconstruction and one finite current comparison

14 October 2026. Based on the uploaded `submission-v1/lcf_v2.tex` and the completed five-hour run. No new jobs were launched in preparing this note.

## Completed run and what it leaves unresolved

The terminal supervisor status records `budget_exhausted`, 18,000 seconds, 42 completed seeds and two timed-out partial cases. The previously generated completed-case audit contains 42 complete N=3,9,27 cases; its narrative was written just before the final deadline, so its sentence saying the campaign was still running is now stale. Its complete-case figures remain useful: N=27 chiral-curvature residuals 1.52e-12 to 7.86e-11, component curvatures up to approximately 0.003, vectorlike sums below 2.46e-17, and Dirac/Weyl determinant assembly agreement around double-precision per block. These are diagnostics of fixed homogeneous backgrounds. They do not evaluate the original-link current or inherited-frame derivatives.

Another five hours of the same homogeneous momentum code has low marginal value compared with an implementation of one literal finite comparison. A full implementation of the *infinite* current, uniform locality proof, and all-loop phase test cannot be promised from a second short CPU campaign.

## Reconstruction is computationally specified

Contrary to an assumption that the archive is essential for the definitions, Appendix A supplies concrete formulas. The missing archive prevents reproduction of the author's implementation but does not prevent an independent one.

1. **Weights:** lines 3605–3640, equation `app:g:partition`. With `delta_b=1/8`, normalize the even bump `beta(t)=C exp[-1/(delta_b^2-t^2)]` on `|t|<delta_b`. Let `kappa=b*b*b*beta`, `b=1_[−1/2,1/2]`; `phi_i(y)=product_mu sqrt(kappa(y_mu-i_mu))`; `rho_i=phi_i^2`. Support radius is 13/8; at most 4^4=256 vertices are active. Numerically normalize the bump after subtracting its maximal exponent to avoid underflow. The triple-box convolution is the standard piecewise quadratic function and can be integrated against the bump by one-dimensional quadrature.
2. **Short transports:** lines 3685–3746, `app:g:polar`. For each nearby vertex pair with coordinate differences at most three, average all 24 coordinate-run orderings of original-link paths. Apply the positive polar factor and remove one fifth of the determinant logarithm near one. Cache these `u_ij` for every required local box and original-field evaluation. They are U-dependent, not y-dependent.
3. **Color fiber:** lines 3749–3810, `app:g:gram` and `app:g:projection-formula`. Build the block matrix `K_ij=phi_i u_ij phi_j`; retain its five eigenvalues near one. `Pi` is their orthogonal projector. Verify the separation from the remaining eigenvalues at all sampled geometry nodes. A rank-five iterative eigensolver with residual checks can save enormous work compared with full dense diagonalization of the up-to-1280-dimensional ambient color matrix.
4. **Canonical corrected frames:** lines 3811–3867, `app:g:safe-frame` and `app:g:determinant`. For a valid anchor i, set `W_i,j=phi_j u_ji`; `w_i=Pi W_i (W_i†Pi W_i)^−1/2`. Form `r_i=sum_j rho_j det(w_i†w_j)`, `d_i=r_i/|r_i|`, and `C_i=w_i exp(Log(d_i)/5)`. Check all Gram matrices and determinant-log branches. Active-coordinate changes must preserve the ambient vertex identities; periodic lattice vertices must not be incorrectly merged inside this cover-space construction.
5. **Connection and transport:** lines 3869–3900 and 4081–4110, `app:g:connection` and `app:g:transport`. `nabla^0=Pi d−theta/5`, `theta=(sigma,d sigma)`; the ambient transport generator is `[partial_v Pi,Pi]+theta(v)Pi/5`. This is a fully specified ODE. An implementable alternative is a mesh of corrected local frames along the path, polar-decomposing their successive overlap matrices and removing the determinant phase. As mesh size tends to zero, this approximates transport for `C†dC−tr(C†dC)/5`. It must be checked by mesh refinement and reversal/composition controls; it is not exact at finite mesh. Keep the same local anchor on a segment when possible, or explicitly apply chart transitions.
6. **Inherited frames and fine links:** lines 4047–4080 and 4131–4168. Initialize `f_1(i)=C_i(i,U)`. Each fine site is the centered child of a unique parent: `3x+k`, k_mu in {−1,0,1}. Transport the parent frame along the straight segment to its child, recursively. Fine link `F_hU(x,mu)=f_h(y)† tau(y<-y+h mu) f_h(y+h mu)`. Cover-space translations at periodic boundaries and fermion boundary signs are different operations and must each be counted once.

There is no explicit optimal numerical universal 4D admissibility threshold in the theorem. Small chosen input plaquettes plus observed geometric and Wilson gaps are numerical diagnostics, not proof of membership in every universal hypothesis. All branch/gap failures should terminate a case, never be silently clipped.

## The smallest genuinely closer calculation

Implement **B_0**, from actual original U to its literal reconstructed `F_(1/3)[U]`. Do not substitute `F_1[U]` for U (lines 1346–1357). Start with a 1x1x1x1 original torus and generic small SU(5) links; the reconstructed fine field lives on 3^4 sites and need not be spatially constant inside the original cell. All four spacetime directions and the full chiral SU(5) representation are retained. The one-site original volume means this is still a limited fixture; it cannot probe spatial locality on the original lattice.

For each representation independently, assemble the full position-space Wilson matrix and

`H_s=(1-s)H_f+s[I H_c I†+gamma5(1-II†)]`,

with the paper's centered copying matrix `I psi(child)=psi(parent)/9` and boundary signs. For an original-link tangent `delta U_e=T U_e`, recompute **the entire reconstruction, transports, and inherited frames** at `exp(±epsilon T)U_e`; repeat at epsilon/2. A centered difference of these complete sampled maps includes the frame derivatives that the existing campaign lacks. Cache H_f and its derivative before s quadrature; only the linear comparison coefficients vary with s.

At each quadrature node diagonalize H_s. For a positive eigenvalue lambda_i and negative lambda_j, the projector divided difference is `1/(lambda_i-lambda_j)`. The real current integrand is

`-2 Im sum_(i+,j-) <i|partial_s H|j> conjugate(<i|delta H|j>)/(lambda_i-lambda_j)^2`.

Sum the 10 and 5bar contributions before assessing anomaly cancellation. The matched right-handed calculation uses the negative band on the same H_s; the equal-coupling vectorlike sum should cancel. This tests an actual finite current coefficient rather than only fine-endpoint curvature.

## Controls required for scientific value

- Check reconstructed SU(5) links, frame orthonormality, spectral projector rank/gap, I†I=1, gamma5-Hermiticity, and comparison gaps.
- Recompute after original gauge transformations and verify the inherited fine gauge action is copied from the original ancestor (lines 4158–4168). On a one-site original lattice this only tests the common original-site gauge action. Do not call it a spatial gauge test.
- Show transport-mesh convergence, finite-difference convergence, and s-quadrature convergence separately. A tiny chiral sum is meaningful only relative to these measured errors.
- Evaluate the finite Ward identity `B_(0,-nabla omega)=m_0-m_1`, where `m_n=i Tr[(P_n-P_+)R(omega_n)]` and `omega_n` is copied from the original ancestor (lines 2210–2289). Calculate the B integral, not just its endpoint right-hand side.
- If cost permits, compare the integrated current around one small two-parameter closed loop with independently transported endpoint determinant phases. This checks `exp(i integral B_0)=T_0/T_1` and quadrature/phase conventions. The finite transgression identity holds for any smooth gapped interpolation; it alone is not evidence for the infinite-refinement theorem.
- Deliberately omit frame derivatives in a diagnostic variant and measure whether the result changes. The fixture should be chosen so this control is nontrivial; a commuting/pure-gauge special case can hide the omission.

## Cost and alternatives

The full position-space matrix dimension is `4 * number_of_fine_sites * color_dimension`:

| Original torus / comparison | fine sites | 5bar dimension | 10 dimension |
|---|---:|---:|---:|
| 1^4, B0: 1^4 -> 3^4 |81|1620|3240|
| 2x1x1x1, B0 -> 6x3x3x3 |162|3240|6480|
| 1^4, B1: 3^4 -> 9^4 |6561|131220|262440|

One complex dense 3240-square matrix is about 168 MB; the eigensolver and transformed derivatives require several such arrays. A 6480-square matrix is about 672 MB. At B1 one 10-representation dense matrix alone is about 1.1 TB. A refinement multiplies dimension by 81 and naive dense cubic cost by 531441. Thus B1 and a convergence curve for the full current are not credible with this direct method on the present cloud budget.

Even B0 runtime needs a pilot on this machine: geometry reconstruction, eigensolver choice, BLAS threading, and quadrature nodes dominate. Do not announce a reliable five-hour science run until a complete minimal coefficient and its controls work. A useful five-hour allocation can then buy increased transport/s quadrature and source variations, rather than more random backgrounds. A bounded runner should save each converged finite coefficient and error estimates.

If literal generic-SU(5) B0 is too expensive, a principled restricted fixture is the subgroup with fundamental `3_a + 1_b + 1_c`, `3a+b+c=0`, allowing noncommuting SU(3) transport and distinct U(1) charges. The 10 splits into `3bar_(2a)+3_(a+b)+3_(a+c)+1_(b+c)` and 5bar into `3bar_(-a)+1_(-b)+1_(-c)`. With generic charges this remains chiral under the subgroup; it is not the conjugate-paired SU(3)-only auxiliary fixture. Literal reconstruction and transport preserve this block structure. Fermion eigensystems then have color dimension at most three (972 for one-site B0;1944 for a two-site original torus), allowing a spatially varying two-site original field and nonconstant gauge transformations at lower cost. It must be reported as a restricted subgroup background, not generic SU(5). A claim of this speed-up should be verified by a block-vs-full small-matrix control.

**Recommendation:** implement and benchmark the literal finite B0 fixture first, with measured reconstruction/frame-derivative errors and a finite Ward or loop identity. A second 5–6 hour run can then materially advance the evidence. Do not promise a result that establishes Craig's entire construction, and do not use the existing homogeneous code under that description. Sparse rational-sign/trace methods could eventually make B1 feasible, but developing and validating that separate numerical method is a larger project, with stochastic/error-control issues not solved by extending wall time.
