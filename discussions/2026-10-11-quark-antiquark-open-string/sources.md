# Sources and evidence

The two uploaded transcripts were the initial source material. They are conversations containing claims, calculations, and historical requests, not independently refereed evidence. The previous PRL/PRD/addendum PDFs were supplied later on 12 October and are now [preserved with hashes and text extractions](references/received-2026-10-12/README.md). Other mentioned ZIPs/scripts/images have not been supplied as original artifacts.

Both originals were preserved byte-for-byte under `references/`. The assessment links to them through [README.md](README.md).

## Primary literature reading trail

The following are primary references for the established frameworks discussed in the assessment. At the initial checkpoint all eight PDF requests returned proxy 403 failures. **Access was restored on 12 October:** S7 was retrieved and its relevant sections read; the other seven have not been reread in this update. The [new reading record](references/literature_2026-10-12.md) also covers Schwarz metadata and recent AI-assisted mathematics/physics sources. No current experimental limit is inferred from this access change.

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

The first INSPIRE request was blocked; the successful follow-up verified **Phys. Lett. B 37 (1971), 315–319, DOI [10.1016/0370-2693(71)90028-1](https://doi.org/10.1016/0370-2693(71)90028-1)**, [INSPIRE 75918](https://inspirehep.net/literature/75918). Its abstract describes mathematical quarks/gluons and a quark-emission vertex. The full paper remains unread. The historical pre-PDF manuscript is preserved in Git; the current manuscript is version 0.2.

Related reading leads, also not retrieved here:

- P. Ramond, *Dual Theory for Free Fermions*, Phys. Rev. D 3, 2415 (1971), [DOI](https://doi.org/10.1103/PhysRevD.3.2415).
- I. Bars and A. J. Hanson, *Quarks at the ends of the string*, Phys. Rev. D 13, 1744 (1976), [DOI](https://doi.org/10.1103/PhysRevD.13.1744).
- The Aharonov–Casher–Susskind dual-parton work discussed in the uploads; exact bibliography and model content should be checked before using it as evidence for the new correspondence.

The [independent manuscript](manuscript/README.md) was created before the previous PDFs arrived and is preserved at `333e537`. Those PDFs have now been received and [compared](notes/draft_comparison.md). The reconstruction had already used detailed conversation fragments and should not be described as a blind discovery or evidence of independent priority.

## AI-assisted research and source-verification scope

The user explicitly wants to situate the project in model-assisted mathematical and physical research. The [annotated AI bibliography](notes/ai_research_bibliography.md) separates research advances, benchmark performance, rediscovery, and numerical methods. It now includes retrieved October 2026 sources with explicit reading and verification scope.

Earlier requests to Nature, DeepMind and OpenAI failed with proxy 403 responses. After the network change, FunSearch, OpenAI's current mathematics release and its pinned README, and two recent AI-assisted physics papers were retrieved. Those authors' results were not independently proved or reproduced here; other bibliography entries and the supplied drafts' citations retain their stated verification limits. See the [reading record](references/literature_2026-10-12.md).

The [research protocol](notes/research_protocol.md) records the user's instructions to avoid routine scripted rechecks of known results, use smaller models for justified computation/extraction, save outputs to disk, and distinguish reproducibility from discovery.

## Current-profile and scalar-completion revision, 12 October

- T. Gherghetta and A. Pomarol, *Bulk Fields and Supersymmetry in a Slice of AdS*, [hep-ph/0003129](https://arxiv.org/abs/hep-ph/0003129). Standard background for warped bulk fermions and supersymmetry constraints.
- H. R. Grigoryan and A. V. Radyushkin, *Form Factors and Wave Functions of Vector Mesons in Holographic QCD*, [hep-ph/0703069](https://arxiv.org/abs/hep-ph/0703069). Background for holographic current overlaps; it does not establish our chosen pair of profiles as string sectors.
- V. Bargmann, *On the Number of Bound States in a Central Field of Force*, PNAS **38**, 961–966 (1952), [DOI 10.1073/pnas.38.11.961](https://doi.org/10.1073/pnas.38.11.961). Used for the scoped no-binding bound in the supporting scalar completion.

The first two arXiv metadata pages and abstracts were retrieved on 12 October; their full texts have not been reviewed in this step. Bargmann's publication metadata was checked previously. The finite-cutoff current formulas and bounds are derived explicitly in the paper rather than attributed as new literature results. See [007](blackboard/007_pointlike_current_mechanism.md) for the calculation's scope.
