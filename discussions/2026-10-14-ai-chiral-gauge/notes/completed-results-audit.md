# Completed-case numerical audit

Observed **2026-10-14T07:26:16.681676+00:00**. The campaign status then was `running`; this is not a claim that the five-hour campaign has ended.

The snapshot contains **42 completed seeds**, each completing N=3,9,27 and all 531,441 N=27 momenta. There are 0 finite/hash/seed/completion consistency errors and 0 nonempty completed-case stderr logs. Active partial cases are excluded.

| Observable | N=3 | N=9 | N=27 |
|---|---:|---:|---:|
| Absolute chiral residual range | 3.92e-07–0.000202 | 1.72e-07–1.7e-05 | 1.52e-12–7.86e-11 |
| Absolute anti5 component range | 6.5e-06–0.00025 | 9.64e-06–0.00281 | 5.56e-07–0.00295 |
| Absolute 10 component range | 3.3e-05–0.000451 | 2.96e-06–0.00282 | 5.56e-07–0.00295 |

For every completed seed, the absolute residual decreases from N=9 to27. Ratios |Omega27/Omega9| span **6.69e-07–1.87e-05**, median 4.73e-06. Coarse N=3 to9 non-monotone cases: [].

Across all levels, maximum absolute vectorlike sum is 2.46e-17; per-momentum Dirac/Weyl log and phase discrepancies are at most 3.55e-14 and 2.42e-13 radians. The maximum accumulated log discrepancy is 2.1e-09. Minimum sampled Wilson gap is 0.998838807.

At N=27, |residual|/(sum arithmetic proxy) ranges from 63.7 to 3.18e+03; 0 seeds lie within 10 times that proxy, 2 within100 times. The proxy is expressly **not an error bound or validated noise floor**. More precision and independent error analysis are needed to interpret the smallest residuals.

The campaign supports smooth-background cancellation and its implementation controls. Homogeneous backgrounds can exhibit special suppression; the dramatic decrease cannot be promoted to a universal power law. It does not calculate Craig's original-link comparison current, prove infinite refinement/locality, establish all-loop integrability, or certify that Craig solved the full chiral-gauge problem.

Full per-case numbers, hashes, outliers, calibration checks and scope caveats are in `completed-results-audit.json`.
