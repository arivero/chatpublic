# Review of the uploaded ancillary documents

Reviewed on 2026-10-14 from the user's uploaded `arXiv-2610.09093v1.tar.gz`, extracted under `submission-v1/`. Citations below use the documents' **printed page numbers**, which differ from PDF page ordinals in the two long supplements. This is a reading and scope audit, not a verification of the mathematical theorem or the reported certificates.

## What is actually included

The `anc/` directory contains `README.txt` and three PDFs: the Lean verification report (7 PDF pages), mathematical companion (65 PDF pages), and two-dimensional supplement (106 PDF pages). `pdfdetach -list` reports **zero embedded files in each PDF**. There is no Lean project or numerical calculation archive in this ancillary directory.

The README explicitly sends readers to two external repositories:

- Mathematical companion/formalization: `https://doi.org/10.5281/zenodo.23196062`.
- Two-dimensional calculations: `https://doi.org/10.5281/zenodo.23196101`.

It says `calculation_archive_2026_10_05.tar.gz` must be downloaded separately and extracted beside the 2D PDF so its relative evidence links resolve. Thus the uploaded submission supplies substantially more mathematics and fixture definitions, but **does not supply the missing implementation or verification records**. These documents establish that the author cites those repositories; they do not establish whether the repositories exist or ever existed.

Extracted reading copies are in `/workspace/work/craig/submission-reading/`.

## Formalization: strong reported claims, absent replayable source

The Lean report says `Companion.measure_exists` assembles companion theorem 4.1, with an explicitly defined refinement current (`comparisonCurrent`) rather than an arbitrary current assumed to have the desired properties. The report describes preceding theorems supplying reconstruction estimates, comparison gaps, locality, infinitesimal identities and global phase control. This is a claim of formalizing the central analytic construction, not merely checking the last algebraic inference (report §§1–2, pp. 1–4).

The reported verification used Lean 4.35.0-rc2 on ARM64 Linux. It records all 16 modules compiling without errors or warnings, 95,810 exported declarations accepted by kernel replay, and only `propext`, `Classical.choice`, and `Quot.sound` in the accepted axiom set, with no `sorryAx`. It also reports Codex correspondence review of 2,488 source items and 39 assumption contexts, plus agreement of 673 configured declaration types and 39 supporting types (§5, p. 6). These are **reported results**, not checks we can replay from the uploaded files.

The same table records a failed original Comparator reference comparison. The explanation is differing compiler-generated proof names and a reference that required one supporting proof body to equal a `sorry` placeholder despite the delivered completed proof. The report distinguishes that failure from its separately successful compile, axiom and kernel runs (§5, pp. 6–7). Without the source, reference configuration and receipts, we cannot independently assess that diagnosis; it neither demonstrates a false theorem nor warrants concealing the failed check.

The missing `paper-supplement.zip` reportedly contains `Formalization.lean`, `Formalization/C01.lean` through `C15.lean`, pinned dependencies, coverage/assumption ledgers and verification receipts. A second missing `verification-records.tar.gz` reportedly retains history, failed attempts and diagnostics (§6, p. 7).

The formalization used a September 8 companion and was delivered September 25. The uploaded companion is an October 5 revision. Three changes were reportedly compared against the existing Lean evidence: treatment of piecewise-smooth joins; smoothing continuous loop homotopies while retaining admissibility; and the real scalar commutant of the SU(5) adjoint action. The full correspondence ledger concerns the September version; only a targeted comparison is claimed for the revised passages (report §4, pp. 5–6; companion §1, pp. 1–2). This is a precise source-version caveat, not evidence of a demonstrated mismatch.

## What the 4D theorem does and does not claim

Companion theorem 4.1 (§4.5) claims a smooth, exponentially local gauge-covariant measure current for the Wilson-mass-one overlap operator in left-handed SU(5) `10 + 5bar`, on every nonempty component satisfying a sufficiently small strict fundamental plaquette bound. The threshold and positive locality rate are independent of volume, component and derivative order. Boundary conditions may independently be periodic or antiperiodic in each direction. One constant phase per admissible component remains unspecified.

The significant obligations are simultaneous: a uniform gap **through the whole coarse/fine interpolation**; convergence in original-link derivative/locality norms; the anomalous Ward equation; and the full determinant-phase identity for all closed histories, including noncontractible ones. Vanishing curvature alone does not provide the last condition. The global argument reduces a rank-five history bundle over `T^4 × S^1` to rank three, uses antiunitary pairing at that endpoint, then controls the deformation back (companion §§5–9; 2D supplement §S10.2, pp. 81–82).

The construction's h^4 current bound comes from ordered color cancellation producing h^8 before the h^-4 trace-site density. The terminal curvature has h^6 times h^-4 = h^2. The initial comparison B0 separately retains the original links, which need not equal the spacing-one reconstructed sample. All later levels sample **one** reconstructed connection; reconstructing afresh at each level or freezing inherited frames defines another calculation (companion §§6–7; 2D §§S3, S10.1).

The companion explicitly leaves **reflection positivity, efficient evaluation of the complete current, and an interacting continuum limit open** (§13, printed p. 36). Its classical continuum estimates concern fixed compact smooth background families at each fixed derivative order. Its fixed-cutoff normalized amplitude comparison additionally requires a nonzero limiting partition function. It asserts no practical complexity bound for evaluating the polynomial coefficients (§10.4, p. 28). These limitations preclude identifying a finite numerical success with a full constructive Standard Model or phenomenological prediction.

## What the 2D numerical supplement adds

The 2D anomaly-free matter is `3 × 5bar_L + 10_R + 5 × 1_R`, **not** the 4D chiral multiplet. Its common certified plaquette cap is `epsilon_* = 1/83886080` (about 1.19e-8); larger exploratory fields do not automatically lie in that theorem's domain (§S7, pp. 62–68). The universal bounds are explicit but vastly too conservative for a practical stopping rule. The author expressly rejects using a small next term or exponential fit as a substitute for a tail bound (§S7.3, p. 68).

Useful reported benchmarks are:

- A free 18×18 comparison gap of at least **11/25**, supported by 1,193,334 boxes. The replay shares matrix assembly and residual code with the producer, so it is an independent execution, not an independently implemented verifier (§S7.1, pp. 63–64).
- A direct cubic current coefficient on a 4×4 AP/AP fixture of **0.012136272892297925 ± 9.104279e-13**, with separately evaluated endpoint curl coefficients. These are Taylor coefficients, not complete finite-amplitude currents (§S9.2, pp. 70–72).
- An enclosed infinite point current **1.16912079572e-9 ± 1.13540e-11** in a specified small-amplitude 2×2 family, including prefix, nonlinear and all-level tail errors (§S9.3, pp. 72–74).
- An infinite loop-current integral **1.1277977410453992 ± 3.590e-7**, consistent with a separately evaluated phase near **1.127797741044919**. The nonflat perturbation is only **2^-64**; this is primarily a controlled transfer from a flat family, not a large-amplitude non-Abelian matrix computation (§S9.3, pp. 74–76).
- A selected nonlinear Ward coefficient from **244×244 momentum points × 220 Gauss nodes = 13,097,920 points**, enclosed at **|J−E| < 7.484e-24** for a response about 6.82e-12. This is a continuous momentum integral for one local coefficient. The full original-frame matching and frame correction are explicitly not evaluated, so the impressive enclosure is not an enclosure of the native full current (§S9.4, pp. 76–80).

The missing archive is required to replay the asserted rational spectral covering, interval arithmetic, stored fixture arrays, and detailed calculation certificates. Many formulas and some fixture families are available in the PDFs and can support an independent implementation, but reproducing that implementation is still work.

## Controls and limitations relevant to our campaign

Inherited-frame contributions can be numerically substantial. In the reported B2 cubic coefficient, the local part is approximately 1.2266e-9 and the frame part 2.9757e-9, summing to 4.2023e-9. Omitting an ancestor contribution changes one midpoint response by 14.768%. Fourth/fifth-order tests detect geometry omissions invisible to leading coefficients (Appendix B.4, pp. 95–96). A calculation lacking these terms cannot be relabelled as Craig's current solely because it has the right anomaly cancellation.

The supplement carefully records cancellation of shared endpoint errors: individual phase-leg residuals around ±3.91e-16 sum to 3.34e-19, which **is not** the accuracy of either leg or a certified total error (B.5, p. 96). It also reports controls insensitive by symmetry, unresolved higher-order responses, and some integration refinements without sustained convergence (B.9, pp. 101–102).

There is a deeper diagnostic limitation: adding an exact gauge-invariant local one-form `dW` can preserve Ward, curvature and all loop-phase tests while changing a transverse response. The supplement constructs such an example. Thus those identities alone do not identify the prescribed current; direct nongauge evaluation or derivation remains necessary (B.9, pp. 101–102).

Finally, §S9.5 (p. 80) explicitly says that a practical independently enclosed evaluator of the complete infinite current on a generic finite-amplitude non-Abelian field is **not supplied**. It states that none of the numerical checks establishes reflection positivity, the interacting continuum limit, or the 4D measure theorem. Section S10.2 (pp. 81–82) stresses that the 2D free gap, geometry bounds and phase cancellation do not establish their distinct 4D counterparts. Our finite 4D background/Dirac controls can test real mechanisms, but cannot close these obligations by running longer alone.
