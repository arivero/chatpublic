# Final results: reconstructed 4D first comparison B0

The run ended at **17:24:50 Europe/Madrid on 15 October 2026**, reaching its
18,000-second wall-time budget. **16 cases completed** (32 representation
quadratures, 520 nodes); case 16 was interrupted at the deadline. No execution
errors, source-hash changes or nonempty worker stderr logs were found. The worker
exited; the supervisor was an exited zombie awaiting OS reaping at the final
inspection. No calculation was restarted or extended.

The [final archive](../results/b0-final/README.md) contains the raw cases,
reconstructed fields and derivative inputs, quadrature nodes, manifest, source
hashes and actual timestamped reports. The [machine-readable summary](../results/b0-final/summary.json)
records the final process checks and all derived comparisons.

## Completed base response

The finest complete base case is **case 7**: transport mesh 16, 32 Gauss-Legendre
nodes and original-link source steps 0.01 and 0.005. These are numerical finite-B0
coefficients, not infinite-current values. Both representations complete before
their chiral sum is reported.

| Quantity | Value |
|---|---:|
| Chiral Bx, source step 0.005 | 1.1146396307264954e-8 |
| Chiral By, source step 0.005 | -1.631924032966742e-8 |
| Bx with inherited-coordinate derivative frozen | 7.136417545019296e-9 |
| Relative change from freezing that contribution | 35.9756% |
| Vectorlike response | Numerically zero in the shared-band control |
| Chiral finite Ward residual | 6.234731316767379e-14 |
| Anti5 finite Ward residual | 2.1588833134790443e-14 |
| 10 finite Ward residual | 4.075848003288335e-14 |

The frozen control omits the variation of parent-transport coordinates in varying
canonical local frames; it does not hold changing ambient fibers fixed. Its
effect is large compared with the measured refinement changes. The vectorlike
zero follows from complementary spectral-band identities using shared data and
serves as an algebraic implementation control.

## Separate convergence checks

| Refinement | Absolute change in chiral Bx | Relative change |
|---|---:|---:|
| Source step 0.01 to 0.005, mesh16/q32 | 1.01131e-11 | 0.09073% |
| Transport mesh 2 to 4, q16 | 1.65275e-11 | 0.14834% |
| Transport mesh 4 to 8, q16 | 4.07323e-12 | 0.03655% |
| Transport mesh 8 to 16, q32 | 1.01507e-12 | 0.009107% |
| Quadrature 16 to 32, mesh8 | 9.47953e-17 | 8.50534e-7% |

The successive transport differences fall by about four on mesh doubling,
consistent with the expected overlap-transport discretization trend on this
fixture. The quadrature comparison is much smaller than the source-step and
transport changes. These are observed differences, **not certified total error
bounds**. In particular, quadrature stability does not establish comparable
accuracy of the full reconstructed current.

At mesh2, the chiral Ward residual improves from about -1.06e-9 with four
quadrature nodes to 3.65e-12 with eight and 8.20e-14 with sixteen. This tests the
integrated finite current against separately computed endpoint moments. The
one-site original torus permits only a common original-site gauge action, not a
test of spatially varying original gauge transformations.

## Nongauge curl

Both sets of four shifted cases completed, with identical mesh8/q16 and inner
source step 0.005. Their matching complete base is case 5. The convention is
`curl = partial_a B_b - partial_b B_a`, compared with
`Omega_original - F_(1/3)^*Omega_fine`.

The matching endpoint curvature difference is **-9.023302647588216e-7**.

| Outer parameter step | Complete cases | Chiral curl | Residual against endpoint | Relative discrepancy |
|---|---|---:|---:|---:|
| 0.01 | 8,9,10,11 | -9.028318443978945e-7 | -5.0157963907296e-10 | 0.05559% |
| 0.005 | 12,13,14,15 | -9.024663843535586e-7 | -1.3611959473704062e-10 | 0.01509% |

The curl residual shrinks by **3.68485** when the outer step is halved. This is
consistent with decreasing finite-difference error in the tested identity; two
steps do not certify an asymptotic order or an exact equality. Per-representation
curl values and matching targets are retained in the summary, so cancellation
cannot hide their individual discrepancies.

## Interrupted case and remaining limits

Case **16**, mesh16/q32 with finer source steps 0.005 and 0.0025, saved **40/64
nodes**. Anti5 completed but 10 did not. Its return code -9 records the deliberate
deadline stop. It contributes no full chiral B0 current, no convergence comparison
and no curl. Consequently the finer source-step check remains unfinished. Three
later queued cases never started.

The minimum sampled comparison gap, including saved nodes of the interrupted
case, was 0.9874946778662416; the maximum sampled eigenpair residual was about
2.34e-14. These floating-point observations do not prove a gap for every s or
provide interval certificates. They are separate from complete-current results.

This experiment advances beyond the original homogeneous momentum calculation:
it numerically implements the specified reconstruction and inherited-frame
dependence and directly tests a nongauge finite current, finite Ward identity,
and finite curl on one 4D fixture. It supplies no infinite-refinement tail bound,
uniform locality estimates, arbitrary global-loop test, larger-volume local
gauge test, dynamical gauge ensemble or interacting continuum limit. The finite
identities alone also do not uniquely identify a current, so their agreement is
meaningful alongside the explicit reconstruction, not a substitute for it.
These results support the tested finite construction; they do not prove Craig's
full theorem.
