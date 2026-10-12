"""Finite-Q hard-wall current averages for two assumed radial profiles.

Run from any directory. The JSON output is written beside this script's
parent directory in calculations/. All momenta are in units of Lambda_had.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import mpmath as mp
from scipy import integrate, optimize, special


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "calculations" / "warped_current_experiment.json"
R_VALUES = (100, 1000, 3000, 10000, 100000)
T_VALUES = (1, 3, 10, 30, 100)


def current(z: float, t: float, r: float) -> float:
    eps = 1.0 / r
    b = special.k0(t) / special.i0(t)
    x = t * z
    x0 = t * eps
    return x * (special.k1(x) + b * special.i1(x)) / (
        x0 * (special.k1(x0) + b * special.i1(x0))
    )


def average(t: float, r: float, profile: str, tolerance: float = 2e-12) -> tuple[float, float]:
    eps = 1.0 / r
    if profile == "R":
        # P_R(z)=eps/[ (1-eps) z^2 ]; multiply by dz/d(log z)=z.
        def density(logz: float) -> float:
            z = math.exp(logz)
            return eps / ((1 - eps) * z) * current(z, t, r)
    elif profile == "B":
        # P_B(z)=2z/(1-eps^2).
        def density(logz: float) -> float:
            z = math.exp(logz)
            return 2 * z * z / (1 - eps * eps) * current(z, t, r)
    else:
        raise ValueError(profile)
    return integrate.quad(
        density, math.log(eps), 0.0, epsabs=tolerance,
        epsrel=tolerance, limit=300,
    )


def mp_average(t: float, r: float, profile: str, dps: int, order: int) -> float:
    with mp.workdps(dps):
        tt, rr = mp.mpf(str(t)), mp.mpf(str(r))
        eps = 1 / rr
        b = mp.besselk(0, tt) / mp.besseli(0, tt)
        x0 = tt * eps
        den = x0 * (mp.besselk(1, x0) + b * mp.besseli(1, x0))

        def f(y: mp.mpf) -> mp.mpf:
            z = mp.exp(y)
            x = tt * z
            v = x * (mp.besselk(1, x) + b * mp.besseli(1, x)) / den
            if profile == "R":
                return eps / ((1 - eps) * z) * v
            return 2 * z * z / (1 - eps * eps) * v

        # Independent fixed-order Gauss quadrature on short log intervals.
        a = mp.log(eps)
        n = max(8, math.ceil(float(-a)))
        nodes = [a * (1 - mp.mpf(i) / n) for i in range(n + 1)]
        gauss_x, gauss_w = special.roots_legendre(order)
        total = mp.mpf(0)
        for i in range(n):
            mid = (nodes[i] + nodes[i + 1]) / 2
            half = (nodes[i + 1] - nodes[i]) / 2
            total += half * mp.fsum(
                mp.mpf(str(w)) * f(mid + half * mp.mpf(str(x)))
                for x, w in zip(gauss_x, gauss_w)
            )
        return float(total)


def marginal_exact(t: float, r: float) -> float:
    x = t / r
    b = special.k0(t) / special.i0(t)
    return (special.k0(x) - b * special.i0(x)) / (
        math.log(r) * x * (special.k1(x) + b * special.i1(x))
    )


def main() -> None:
    scan = []
    for r in R_VALUES:
        for t in T_VALUES:
            if t / r > 0.1:
                continue
            fr, er = average(t, r, "R")
            fb, eb = average(t, r, "B")
            deficit = ((math.pi / 2) * (t / r) - 1 / r) / (1 - 1 / r)
            scan.append({
                "r": r, "t": t, "t_over_r": t / r,
                "F_R": fr, "F_B": fb, "F_R_squared": fr * fr,
                "asymptotic_1_minus_F_R": deficit,
                "actual_1_minus_F_R": 1 - fr,
                "quadrature_error_estimates": {"R": er, "B": eb},
            })

    threshold = optimize.brentq(
        lambda r: average(10, r, "R")[0] ** 2 - 0.99,
        100, 100000, xtol=1e-8,
    )
    precision_checks = []
    for t, r in ((10, threshold), (100, 10000)):
        for profile in ("R", "B"):
            scipy_value, scipy_error = average(t, r, profile)
            mp40 = mp_average(t, r, profile, 40, 24)
            mp60 = mp_average(t, r, profile, 60, 36)
            precision_checks.append({
                "t": t, "r": r, "profile": profile,
                "scipy": scipy_value, "scipy_error_estimate": scipy_error,
                "mpmath_bessels_40dps_gauss24_float": mp40,
                "mpmath_bessels_60dps_gauss36_float": mp60,
                "scipy_minus_fixed_gauss36": scipy_value - mp60,
                "fixed_gauss24_minus_gauss36": mp40 - mp60,
            })

    marginal_r, marginal_t = 3000, 10
    # Independent log-coordinate integral for nu=0: P(z) dz = dy/log(r).
    marginal_quad, marginal_error = integrate.quad(
        lambda y: current(math.exp(y), marginal_t, marginal_r) / math.log(marginal_r),
        -math.log(marginal_r), 0, epsabs=2e-12, epsrel=2e-12,
    )
    marginal = marginal_exact(marginal_t, marginal_r)
    result = {
        "description": "Finite-Q hard-wall current average for assumed radial profiles; conditional toy-model calculation.",
        "conventions": {
            "z_IR": 1, "z_UV": "epsilon=1/r", "t": "Q/Lambda_had",
            "b": "K_0(t)/I_0(t)",
            "V": "tz[K_1(tz)+b I_1(tz)]/{t epsilon[K_1(t epsilon)+b I_1(t epsilon)]}",
            "P_R": "nu epsilon^nu z^(-nu-1)/(1-epsilon^nu), nu=1 (c=1)",
            "P_B": "2z/(1-epsilon^2)",
            "F": "integral_epsilon^1 dz P(z)V(Q,z)",
            "marginal": "nu=0 (c=1/2), P=1/[z log(r)]",
            "squared_quantity": "F_R^2, interpreted only as the square of this real toy current average",
        },
        "scan_constraint": "t/r <= 0.1",
        "scan": scan,
        "threshold": {
            "t": 10, "target_F_R_squared": 0.99,
            "r": threshold, "F_R": average(10, threshold, "R")[0],
            "F_B": average(10, threshold, "B")[0],
            "t_over_r": 10 / threshold,
        },
        "independent_precision_checks": precision_checks,
        "marginal_localization_discriminator": {
            "t": marginal_t, "r": marginal_r,
            "F_exact": marginal, "F_log_quadrature": marginal_quad,
            "difference": marginal_quad - marginal,
            "quadrature_error_estimate": marginal_error,
            "F_R_nu_1": average(marginal_t, marginal_r, "R")[0],
            "exact_formula": "[K_0(x)-b I_0(x)]/[log(r) x(K_1(x)+b I_1(x))], x=t/r",
        },
        "methods": {
            "scipy": "adaptive Gauss-Kronrod integration in log(z), absolute/relative tolerance 2e-12; Brent root",
            "cross_check": "mpmath Bessel evaluation at 40/60 decimal digits with fixed Gauss-Legendre orders 24/36 on short log(z) subintervals; nodes and weights originate in double-precision scipy.roots_legendre; returned results are floats. Agreement checks the two quadrature methods near double precision and does not certify 40/60-digit integral accuracy.",
            "asymptotic": "[(pi/2)(t/r)-1/r]/(1-1/r); comparison only, not substituted for finite-Q integral",
        },
        "scope": "Assumed radial profiles and hard-wall probe only; no string amplitudes, dynamical localization mechanism, or experimental limits established.",
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({
        "output": str(OUTPUT), "scan_points": len(scan),
        "threshold_r": threshold,
        "marginal_F": marginal,
        "max_abs_scipy_fixed_gauss_difference": max(abs(c["scipy_minus_fixed_gauss36"]) for c in precision_checks),
    }, indent=2))


if __name__ == "__main__":
    main()
