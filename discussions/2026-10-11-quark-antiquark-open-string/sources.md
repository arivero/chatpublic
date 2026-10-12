# Sources and evidence

The two uploaded transcripts are the immediate source material. They are conversations containing claims, calculations, and historical requests, not independently refereed evidence. Their references to generated PDFs, ZIP files, scripts, and images do not include those artifacts in this directory.

Both originals were preserved byte-for-byte under `references/`. The assessment links to them through [README.md](README.md).

## Primary literature reading trail

The following are primary references for the established frameworks discussed in the assessment. PDF retrieval from `https://arxiv.org/pdf/...` was attempted for all eight papers during this task and returned `Tunnel connection failed: 403 Forbidden`. No text of these papers was retrieved in this run. The source links should therefore be used to check the literature claims independently; none is presented as a new search result or a verified recent experimental limit.

| ID | Reference | Relevance and scope |
| --- | --- | --- |
| S1 | Cullen, Perelstein, Peskin, [hep-ph/0001166](https://arxiv.org/abs/hep-ph/0001166), *TeV Strings and Collider Probes of Large Extra Dimensions* | The string-QED embedding underlying the simple charged-fermion benchmark; the amplitude is established prior work |
| S2 | Antoniadis, Benakli, Laugier, [hep-th/0011281](https://arxiv.org/abs/hep-th/0011281), *Contact interactions in D-brane models* | Why dimension-eight oscillator corrections are not universal to all open-string matter; other realizations permit dimension-six terms |
| S3 | Polchinski, Strassler, [hep-th/0109174](https://arxiv.org/abs/hep-th/0109174), *Hard Scattering and Gauge/String Duality* | Warping can convert flat-string softness into hard exclusive power behavior; it does not identify an ordinary QCD meson with an elementary lepton |
| S4 | Polchinski, Strassler, [hep-th/0209211](https://arxiv.org/abs/hep-th/0209211), *Deep Inelastic Scattering and Gauge/String Duality* | Inclusive scattering and the qualifications needed when comparing holographic hard scattering with partonic behavior |
| S5 | Sonnenschein, Weissman, [arXiv:1402.5603](https://arxiv.org/abs/1402.5603), *Rotating strings confronting PDG mesons* | Phenomenological endpoint masses and Regge spectra; a rotating-string fit does not establish the pion's chiral dynamics or a fermionic partner |
| S6 | Dosch, de Téramond, Brodsky, [arXiv:1501.00959](https://arxiv.org/abs/1501.00959) | Superconformal hadronic spectroscopy; the unpaired pion does not imply a physical negative-orbital-angular-momentum partner |
| S7 | Seiberg, [hep-th/9411149](https://arxiv.org/abs/hep-th/9411149), *Electric-magnetic duality in supersymmetric non-Abelian gauge theories* | A concrete precedent for changing elementary/composite descriptions across regimes, with different field content and dynamical assumptions |
| S8 | Bourilkov, [hep-ph/0002172](https://arxiv.org/abs/hep-ph/0002172), *Search for TeV strings and new phenomena in Bhabha scattering at CERN LEP2* | The uploads cite a historical 95% CL bound of \(M_s>0.631\) TeV in the CPP-based benchmark. This number was not rechecked here and is not treated as a universal string-scale bound |

The reported 2025–2026 collider, magnetic-moment, and baryon-junction claims in the uploaded conversations were not needed for the central result and were not independently validated. No claim of a current strongest compositeness bound is made.

## Independently checked in this task

- The fermion parity of a quark–antiquark Wilson-line operator and the color representation products.
- The low-energy gamma-function expansion and its same-sign channel interpretation.
- Exact gamma-function values and cross-section ratios at a specified hadronic slope.
- The proposed hard-wall radial average as a mathematical ansatz, including its Mellin and disk-modulus integrals for the numerical example.
- The necessary bound on hadronic amplitude weight within a positive radial-average ansatz.

The included script reproduces the numerical checks. It does not derive a worldsheet theory, quantize a QCD flux tube with new fermions, establish a string compactification, or perform a likelihood fit to data.

## Historical target clarified on 12 October 2026

The user identified J. H. Schwarz's 1971 *Dual quark-gluon model of hadrons* as the intended historical anchor, and recalled related early work with Joel Scherk. This supersedes treating “quark gluon dual theories” as an unspecified phrase. The exact Scherk papers still need identification. Quark–gluon, quark–diquark, and lepton–meson correspondences should be compared separately, with explicit gauge representations and observables.

A request to the INSPIRE literature API for the exact Schwarz title returned `Tunnel connection failed: 403 Forbidden`. No primary text or bibliographic metadata was obtained. The manuscript records the user-supplied title/year and deliberately leaves journal/pages unfilled rather than guessing them.

Related reading leads, also not retrieved here:

- P. Ramond, *Dual Theory for Free Fermions*, Phys. Rev. D 3, 2415 (1971), [DOI](https://doi.org/10.1103/PhysRevD.3.2415).
- I. Bars and A. J. Hanson, *Quarks at the ends of the string*, Phys. Rev. D 13, 1744 (1976), [DOI](https://doi.org/10.1103/PhysRevD.13.1744).
- The Aharonov–Casher–Susskind dual-parton work discussed in the uploads; exact bibliography and model content should be checked before using it as evidence for the new correspondence.

The preprint drafts referenced by the uploads remain absent. The [new manuscript](manuscript/README.md) is an independent reconstruction created before reading them. The [workplan](notes/workplan.md) includes a source-by-source comparison when they become available.
