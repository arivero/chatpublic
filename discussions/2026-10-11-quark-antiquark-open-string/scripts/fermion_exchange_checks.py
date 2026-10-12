#!/usr/bin/env python3
"""Check the exchange/contact/dimer examples in the public research notebook.

Uses natural units. These are QFT/EFT examples, not a model of the proposed string.
"""

import json
from pathlib import Path

import mpmath as mp
import sympy as sp
from sympy.physics.matrices import mgamma


def main():
    checks = []
    energy, momentum = sp.symbols("energy momentum", real=True)
    mass = sp.symbols("mass", positive=True)
    slash_p = energy*mgamma(0)-momentum*mgamma(1)
    identity = sp.eye(4)
    inverse_check = (slash_p-mass*identity)*(slash_p+mass*identity)
    assert sp.simplify(inverse_check-(energy**2-momentum**2-mass**2)*identity) == sp.zeros(4)
    checks.append("Dirac inverse has the scalar mass-shell denominator")

    r = sp.symbols("r", positive=True)
    green = sp.exp(-mass*r)/(4*sp.pi*r)
    assert sp.simplify(sp.diff(green,r,2)+2*sp.diff(green,r)/r-mass**2*green) == 0
    massless_gradient = sp.limit(sp.diff(green,r), mass, 0, dir="+")
    assert sp.simplify(massless_gradient+1/(4*sp.pi*r**2)) == 0
    checks.append("Off-source Helmholtz equation and nonzero massless spatial derivative")

    mp.mp.dps = 45
    numerical_green = []
    for m0, r0 in [("0","1"),("0.3","2"),("2","0.5"),("2","2")]:
        mm, rr = mp.mpf(m0), mp.mpf(r0)
        # Positive proper-time representation of the three-dimensional Fourier transform.
        integral = mp.quad(lambda tau: tau**(-mp.mpf("1.5"))*mp.exp(-mm**2*tau-rr**2/(4*tau)),
                           [0, mp.mpf("0.1"), 1, 10, mp.inf])/(4*mp.pi)**mp.mpf("1.5")
        exact = mp.exp(-mm*rr)/(4*mp.pi*rr)
        assert mp.almosteq(integral, exact, rel_eps=mp.mpf("1e-18")), (integral, exact)
        numerical_green.append({"mass": m0, "r": r0, "G": mp.nstr(exact, 18)})
    checks.append("Yukawa/Coulomb spatial Green function from an independent proper-time integral")

    series = sp.series(mass/(mass**2+momentum**2), momentum, 0, 6).removeO()
    assert sp.simplify(series-(1/mass-momentum**2/mass**3+momentum**4/mass**5)) == 0
    checks.append("Low-transfer expansion gives a contact term and derivative corrections")

    delta, coupling, eigenvalue = sp.symbols("delta coupling eigenvalue", real=True)
    hamiltonian = sp.Matrix([[delta/2, coupling],[coupling,-delta/2]])
    assert sp.expand((eigenvalue*sp.eye(2)-hamiltonian).det()) == eigenvalue**2-delta**2/4-coupling**2
    checks.append("Eigenvalues of a Hamiltonian in a fixed total-parity two-channel basis")

    a, Q = sp.symbols("a Q", positive=True)
    radial_probability = 2*sp.exp(-2*r/a)/a
    assert sp.integrate(radial_probability, (r,0,sp.oo)) == 1
    mean_separation_squared = sp.integrate(r**2*radial_probability,(r,0,sp.oo))
    assert mean_separation_squared == a**2/2
    form_factor = 4*sp.atan(a*Q/4)/(a*Q)
    ff_series = sp.series(form_factor,Q,0,6).removeO()
    charge_radius_squared = sp.simplify(-6*ff_series.coeff(Q,2))
    assert charge_radius_squared == a**2/8
    dimer_values=[]
    for aa, qq in [(mp.mpf(2),mp.mpf("0.1")),(mp.mpf(2),mp.mpf(1)),(mp.mpf(2),mp.mpf(4))]:
        beta=aa*qq/4
        direct=mp.quad(lambda t: mp.exp(-t)*(mp.sin(beta*t)/(beta*t) if t else 1),
                       [0,1,5,10,25,50,mp.inf])
        exact=mp.atan(beta)/beta
        assert mp.almosteq(direct,exact,rel_eps=mp.mpf("1e-25"))
        dimer_values.append({"a":str(aa),"Q":str(qq),"F":mp.nstr(exact,18)})
    checks.append("Renormalized zero-range dimer has finite, tunable radius and nontrivial form factor")

    results={
        "scope":"Free fermion exchange, a coupled-channel Hamiltonian, and a leading zero-range dimer EFT. Not a string construction or experimental fit.",
        "checks_passed":checks,
        "green_function_values":numerical_green,
        "static_scalar_green_function":"exp(-m*r)/(4*pi*r)",
        "massless_radial_derivative":"-1/(4*pi*r^2)",
        "coupled_channel_eigenvalues":"+/- sqrt(delta^2/4 + |K|^2), relative to the mean channel energy",
        "dimer_separation_squared":str(mean_separation_squared),
        "dimer_charge_radius_squared":str(charge_radius_squared),
        "dimer_form_factor":"4*atan(a*Q/4)/(a*Q), equal masses and one charged constituent",
        "dimer_sample_values":dimer_values}
    target=Path(__file__).resolve().parents[1]/"calculations"/"fermion_exchange_results.json"
    target.write_text(json.dumps(results,indent=2)+"\n")
    print(json.dumps(results,indent=2))


if __name__=="__main__":
    main()
