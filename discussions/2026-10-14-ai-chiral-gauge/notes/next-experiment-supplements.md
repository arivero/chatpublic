# A feasible next experiment using Craig's actual reconstruction

Prepared 2026-10-14. This proposes a finite 4D implementation; no job was launched. Source citations are to the uploaded mathematical companion (printed pages) and 2D supplement.

## Recommendation and limits

The next meaningful target is the **actual first comparison current B0 on a one-site four-dimensional torus refined to 3^4 sites**, with generic noncommuting SU(5) links, a full inherited-frame derivative, and independent finite endpoint checks. This tests an ingredient absent from the completed homogeneous-background campaign. It should use the correct left-handed `10 + 5bar` matter and matched vectorlike controls.

Five more hours can potentially buy a finite-current measurement and controls after implementation and a timing pilot. It cannot establish the infinite refinement, general locality bounds or all-loop theorem. Do not promise a particular number of quadrature nodes before timing the actual matrices. The dense B1 calculation is already outside ordinary resources: its wedge-representation matrix has dimension 262,440 and occupies about 1.10 TB **per complex matrix**.

One-site links can be generic full SU(5) matrices. Avoid an SU(2), SU(3), or automatically real/vectorlike subgroup fixture as the sole chiral test: representation restrictions can make the physical response cancel for reasons unrelated to the proposed general construction. Use all four spacetime directions and matrices without a common invariant color subspace. A moderately nonflat fixture with measured spectral/branch margins is a finite diagnostic; the 4D paper does not supply a numerical universal admissibility threshold that certifies such a fixture automatically.

## Explicit reconstruction algorithm supplied by the PDF

The companion Appendix A, pp. 36–43, is algorithmic enough to implement independently:

1. **Weights, A.1–A.7.** Define the normalized smooth bump beta supported in (-1/8,1/8), convolve it with three unit boxes to obtain kappa, and use `phi_i(y)=product_mu sqrt(kappa(y_mu-i_mu))`. At most 4^4=256 lifted vertices are active. Tabulate the one-dimensional weights with controlled interpolation/quadrature accuracy and check sum_i phi_i^2=1. Do not substitute a different convenient spline and call it the same construction.
2. **Short transport words, A.8.** For every needed lifted pair i,j, average all 24 coordinate-order paths, normalize the 5×5 matrix by its positive polar factor, then remove its determinant phase with the near-one fifth-root branch. Retain lifts separately even on a one-site torus; periodicity looks up input links but does not shorten paths.
3. **Rank-five fiber, A.10–A.13.** Assemble `K_ij=phi_i u_ij phi_j`. Select its five eigenvalues near one, obtaining projector Pi. For an anchor k define `W_k,i=phi_i u_ik` and `w_k=Pi W_k (W_k† Pi W_k)^(-1/2)`.
4. **Determinant-corrected frames, A.14.** Compute `t_ij=w_i†w_j`, `r_i=sum_j phi_j^2 det(t_ij)`, `d_i=r_i/|r_i|`, and `C_i=w_i exp(Log(d_i)/5)`. The positive sign in this final correction matters; the earlier polar transport normalization uses a negative sign.
5. **Spatial connection, A.15–A.16.** In frame C_i its coefficient is `A_i=C_i† d_y C_i - tr(C_i† d_y C_i)/5`. This defines the precise SU(5) connection whose transports are required below.
6. **Inherited frames, A.25 and A.28.** Start with `f_1(i)=C_i(i)`. For each child y, set `f_(1/3)(y)=tau(y<-parent(y)) f_1(parent(y))`. Sample `V(y,mu)=f(y)† tau(y<-y+mu/3) f(y+mu/3)`. Both endpoint frames and the edge depend on the original links. The comparison's coarse endpoint remains the literal original U, **not** F1(U).

There are two useful implementation reductions that preserve these definitions in a controlled numerical limit:

- K is up to 1280×1280 but only a five-dimensional invariant subspace is wanted. Iterate a five-column subspace starting from W_k, orthogonalize, and stop using the invariant-subspace residual and separation from the unwanted cluster. Audit selected points with a full Hermitian eigensolve. If X is an orthonormal selected basis, `w_i=X polar(X†W_i)`; the remaining Gram/frame work is only 5×5. Cache short transport words across all spatial points at fixed U.
- Avoid coding spatial derivatives of Pi initially. On a path, multiply the polar factors of successive frame overlaps `C(y_next)† C(y_prev)`, removing their determinant phases. This converges to parallel transport for the traceless frame connection above. Use a fixed anchor over each chart segment, preserve ambient lifted-row labels in overlaps, and insert chart transitions where necessary. Demonstrate path-step convergence and branch margins. This is a numerical approximation to the prescribed connection, not an exact equality at finite path subdivision.

## Original-link derivatives without omitting the ancestors

Use a smooth original-link family U(a), reconstruct everything at each a, and obtain the derivative of the final sampled link matrices from central differences/Richardson checks. This automatically differentiates the short words, Pi, the original C_i, both parent-child transports, and the fine edge. It avoids a large first implementation of mixed Fréchet derivatives while providing a measurable discretization error.

At B0 the complete derivative is schematically

`delta V = (delta f_y†) tau f_z + f_y† (delta tau) f_z + f_y† tau (delta f_z)`.

Companion A.26–A.27 also gives an eventual exact tangent implementation: evolve the ambient propagator with `G=[partial_y Pi,Pi]+theta_y Pi/5`, and evolve its tangent by `delta Tdot=G delta T+(delta G)T`. This is more work but removes the source finite-difference error.

A deliberate wrong control should freeze both inherited endpoint frames while retaining the varied edge transport. Another should retain only the fine-edge segment, omitting parent paths. Compare the current itself, not merely its curl: the 2D supplement B.4, pp. 95–96, shows some symmetric derivative omissions are invisible to curls, and its frame component can be larger than its local component.

## The actual 4D current calculation

Companion §6.2–6.3, equations (6.3), (6.4), (6.8), pp. 11–13:

```
I psi(3*x+k) = psi(x)/9,                 k in {-1,0,1}^4
H_s = (1-s) H(V) + s [ I H(U) I† + gamma5 (1-I I†) ]
P_s = (1+sign(H_s))/2
B0(eta) = integral_0^1 i Tr P_s [d_s P_s, d_eta P_s] ds
```

Impose fermion boundary signs independently of the gauge representation, including the cover-based inclusion. In inherited coordinates I has zero source derivative. Every original-link derivative instead enters U and V. Check I†I=1, endpoint identification, Hermiticity, rank and the entire sampled s-path gap.

For a Hermitian eigendecomposition `H_s=Q diag(lambda) Q†`, define `A=Q†(d_s H_s)Q` and `B=Q†(d_eta H_s)Q`. The real curvature integrand can be evaluated without explicitly forming projector derivatives:

`-2 Im sum_(i positive,j negative) A_ij conj(B_ij)/(lambda_i-lambda_j)^2`.

Sum the two left-handed representation currents. The matched right-handed projector gives the negative curvature, supplying a vectorlike cancellation control. Independent Dirac determinant checks can still be retained, but they do not replace the direct B0 test.

Fermion matrix dimensions are **1620 for 5bar** and **3240 for 10**. The latter matrix alone is about 168 MB; eigensolver workspace, vectors and derivative transforms bring a complete calculation into the gigabyte range. Each dense diagonalization and basis transform scales cubically. The former homogeneous 4d/representation block timing is not a prediction of this cost.

## Prioritized tests for a bounded five-hour campaign

1. **Geometry and implementation gates:** exact flat-field reproduction; unitary/determinant errors; spectral cluster and branch margins; periodic cover consistency; covariance under a known original gauge transformation; path-step and original-source difference convergence. The positive cluster dimension must remain five. Do not proceed with an uncertified implementation bug just to occupy the allotted time.
2. **Direct B0 for one nongauge source**, with successive s-quadrature rules and geometry/source step refinements. Cache reconstructed fields because they do not depend on s. Report individual representation values before the anomaly-free sum, avoiding cancellation-hidden errors.
3. **Finite Ward control:** directly integrate B0 on an original gauge variation and separately evaluate the original and sampled endpoint gauge moments, retaining the terminal contribution. This checks the actual current integral against a simpler independent target. On a one-site torus this gauge transformation is global conjugation; it does not test large-volume local covariance.
4. **Nongauge curl if pilot timing allows:** use a two-parameter original family U(a,b). Compute `partial_a B_b-partial_b B_a` and compare against the original minus pulled-back fine endpoint projector curvature. Use coordinate derivatives of this same family, so the commutator bookkeeping is automatic. A central-difference curl needs four nearby current evaluations and roughly nine reconstructed fields, reusable across s nodes. Repeat at smaller source steps before interpreting tiny differences. This is more demanding and more informative than another gauge-direction-only test.
5. Run the frame-frozen and vectorlike controls using identical numerical settings. They must be visible in the saved comparison; a zero control caused by symmetry is not a discriminating success.

Eight and sixteen Gauss nodes for a single current already require 24 eigendecompositions in each representation; a finite-difference curl multiplies this by four before source-step repetition. Benchmark one 3240×3240 eigensolve, transforms, and one geometry build; use those observed costs to set the work queue. Save each completed node and every operator/geometry residual. Stop new tasks before the wall-clock limit, preserving partial quadrature sums without presenting them as complete results.

The scientific gain is a genuine finite-level application of Craig's specified reconstruction and inherited current in 4D. It still would not supply a converged infinite current. The supplement itself warns that even Ward, curvature and every loop period cannot identify the whole prescribed current against addition of an exact gauge-invariant local one-form (B.9, pp. 101–102). Direct nongauge current values and explicit implementation correspondence remain important.
