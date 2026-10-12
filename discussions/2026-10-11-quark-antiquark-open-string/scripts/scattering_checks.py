#!/usr/bin/env python3
"""Reproduce the conditional string-scattering calculations in assessment.md.

Run from any working directory with Python, mpmath, numpy, scipy, matplotlib.
The positive radial average is a toy ansatz, not a derived QCD string model.
No experimental fit or quantum loop corrections are implemented here.
"""

from pathlib import Path
import csv
import json
import os
import tempfile

import mpmath as mp
import numpy as np
from scipy.integrate import quad
from scipy.special import gammaln

# Keep plotting caches writable in this cloud workspace.
os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "chatpublic-string-matplotlib"))
os.environ.setdefault("XDG_CACHE_HOME", str(Path(tempfile.gettempdir()) / "chatpublic-string-cache"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "calculations"
OUT.mkdir(exist_ok=True)
mp.mp.dps = 60


def veneziano(z, x=mp.mpf("0.5")):
    """V(t,u), z=alpha_prime*s, t=-x*s, u=-(1-x)*s."""
    z, x = mp.mpf(z), mp.mpf(x)
    return mp.exp(mp.loggamma(1 + z*x) + mp.loggamma(1 + z*(1-x))
                  - mp.loggamma(1 + z))


def radial_average(z, nu=2, x=mp.mpf("0.5")):
    """nu * integral_0^1 du u^(nu-1) V(z*u,x); nu must be positive."""
    z, nu = mp.mpf(z), mp.mpf(nu)
    if nu <= 0 or z < 0:
        raise ValueError("Need nu>0 and z>=0")
    if z == 0:
        return mp.mpf(1)
    breaks = [mp.mpf(0)] + [mp.mpf(b) for b in (1, 10, 100) if b < z] + [z]
    return nu*z**(-nu)*mp.quad(lambda w: w**(nu-1)*veneziano(w, x), breaks)


def close(a, b, relative=mp.mpf("1e-35")):
    assert mp.almosteq(a, b, rel_eps=relative), (a, b)


def main():
    checks = []
    close(veneziano(0), 1)
    close(veneziano(1), mp.pi/4)
    close(veneziano(2), mp.mpf("0.5"))
    checks.append("Normalization and exact values V(1)=pi/4, V(2)=1/2")

    small = mp.mpf("1e-7")
    coefficient = (1-veneziano(small))/small**2
    close(coefficient, mp.pi**2/24, mp.mpf("1e-6"))
    checks.append("Low-energy flat amplitude coefficient pi^2/24")

    direct = 2*mp.quad(lambda u: u*veneziano(9*u), [0, 1])
    close(direct, radial_average(9))
    radial_coefficient = (1-radial_average(small))/small**2
    close(radial_coefficient, mp.pi**2/48, mp.mpf("1e-6"))
    checks.append("Radial change of variables and nu=2 low-energy coefficient")

    mellin = mp.quad(lambda w: w*veneziano(w), [0, 1, 10, 100, mp.inf])
    # At x=1/2, xi = 1/(1+exp(-v)) converts the disk-modulus integral
    # into an integral with ell(v)=log(2*cosh(v/2)), avoiding endpoint loss.
    mellin_modulus = mp.quad(lambda v: mp.log(2*mp.cosh(v/2))**(-3),
                            [0, 1, 10, mp.inf])
    close(mellin, mellin_modulus)
    close(radial_average(90), 2*mellin/90**2, mp.mpf("1e-20"))
    checks.append("Mellin integral, independent disk-modulus form, high-energy power")

    f_ir = mp.mpf("0.2")
    mixture = 1-f_ir+f_ir*veneziano(90)
    bound = (1-mp.sqrt(mixture**2))/(1-veneziano(90))
    close(bound, f_ir)
    checks.append("Hadronic overlap bound saturated by pointlike UV component")

    for z in (mp.mpf("0.01"), mp.mpf(1), mp.mpf(90)):
        assert 0 < veneziano(z) <= radial_average(z) <= 1
    checks.append("Flat and radially averaged ratios have the expected ordering")

    slope = mp.mpf("0.9")  # GeV^-2; illustrative hadronic Regge slope
    rows = []
    for energy in ("0.1", "0.3", "1", "3", "10"):
        z = slope*mp.mpf(energy)**2
        rows.append({"energy_GeV": energy, "z": str(z),
                     "flat_cross_section_ratio": mp.nstr(veneziano(z)**2, 18),
                     "radial_nu2_cross_section_ratio": mp.nstr(radial_average(z)**2, 18)})
    with (OUT / "hadronic_scale.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    sensitivity = []
    for epsilon in ("0.01", "0.001"):
        eps = mp.mpf(epsilon)
        root = mp.findroot(lambda z: veneziano(z)**2-(1-eps), (mp.mpf("0.01"), mp.mpf("0.2")))
        sensitivity.append({"fractional_cross_section_tolerance": epsilon,
                            "minimum_Ms_over_E_exact": mp.nstr(1/mp.sqrt(root), 16),
                            "minimum_Ms_over_E_leading_order": mp.nstr((mp.pi**2/(12*eps))**mp.mpf("0.25"), 16),
                            "maximum_hadronic_amplitude_weight_at_10GeV": mp.nstr((1-mp.sqrt(1-eps))/(1-veneziano(90)), 16)})
    results = {"assumptions": "Tree-level same-sign 90-degree scattering. Positive radial toy average, nu=2. No data fit.",
               "alpha_prime_had_GeV_minus2": str(slope),
               "Ms_had_GeV": mp.nstr(1/mp.sqrt(slope), 16),
               "mellin_nu2_x_half": mp.nstr(mellin, 18),
               "flat_ratio_10GeV": mp.nstr(veneziano(90)**2, 18),
               "radial_ratio_10GeV": mp.nstr(radial_average(90)**2, 18),
               "radial_ratio_1TeV_asymptotic": mp.nstr((2*mellin/mp.mpf(900000)**2)**2, 18),
               "sensitivity": sensitivity,
               "numerical_checks_passed": checks}
    (OUT / "results.json").write_text(json.dumps(results, indent=2)+"\n")

    energy_over_ms = np.geomspace(0.03, 10, 240)
    zs = energy_over_ms**2
    flat = np.exp(2*(2*gammaln(1+zs/2)-gammaln(1+zs)))

    def radial_float(z):
        integrand = lambda u: 2*u*np.exp(2*gammaln(1+z*u/2)-gammaln(1+z*u))
        value, error = quad(integrand, 0, 1, epsabs=1e-12, epsrel=1e-10)
        assert error < 1e-9
        return value**2

    warped = np.array([radial_float(z) for z in zs])
    fig, ax = plt.subplots(figsize=(8.4, 5.3), layout="constrained")
    ax.loglog(energy_over_ms, np.ones_like(zs), color="#334155", ls="--", lw=1.6,
              label="Point-particle benchmark")
    ax.loglog(energy_over_ms, flat, color="#b45309", lw=2.3,
              label="Flat open-string disk amplitude")
    ax.loglog(energy_over_ms, warped, color="#1d4ed8", lw=2.3,
              label="Positive radial average, ν = 2 (toy ansatz)")
    ax.set_ylim(1e-8, 1.3)
    ax.set_xlim(0.03, 10)
    ax.set_xlabel(r"Collision energy $E_{\rm cm}/M_s$ (IR scale for radial average)")
    ax.set_ylabel(r"$(d\sigma/d\Omega)/(d\sigma/d\Omega)_{\rm point}$ at $90^\circ$")
    ax.set_title("A power-law tail still differs from point-particle scattering", loc="left", pad=14)
    ax.grid(which="major", alpha=0.2)
    ax.legend(loc="lower left", fontsize=9, frameon=False)
    fig.savefig(OUT / "scattering_comparison.png", dpi=180)
    fig.savefig(OUT / "scattering_comparison.svg")
    plt.close(fig)
    print(json.dumps(results, indent=2))
    print(f"Wrote numerical results and figure to {OUT}")


if __name__ == "__main__":
    main()
