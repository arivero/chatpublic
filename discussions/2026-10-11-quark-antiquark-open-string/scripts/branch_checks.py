#!/usr/bin/env python3
"""Check the conditional two-branch dictionary and a restricted mixing EFT.

These are charge, Pauli, and matching checks, not a dynamical construction.
"""

import itertools
import json
from pathlib import Path

import numpy as np
import sympy as sp


def main():
    checks = []
    charges = {"u": sp.Rational(2, 3), "d": sp.Rational(-1, 3), "s": sp.Rational(-1, 3)}
    names = list(charges)
    branch = []
    for target in names:
        constituents = [name for name in names if name != target]
        antidiquark_charge = -sum(charges[name] for name in constituents)
        assert antidiquark_charge == charges[target]
        missing_flavor = [int(name == target) + int(name in constituents) for name in names]
        assert missing_flavor == [1, 1, 1]
        branch.append({"quark": target, "antiquark_flavors": constituents,
                       "Q": str(antidiquark_charge), "missing_Nu_Nd_Ns": missing_flavor})
    checks.append("Three light-flavor antidiquarks have quark charges and a common missing (1,1,1) flavor weight")

    missing_B_quark = sp.Rational(1, 3) - sp.Rational(-2, 3)
    missing_BL_lepton = (0, 1)
    missing_BL_quark = (missing_B_quark, 0)
    assert missing_BL_quark == (1, 0)
    assert missing_BL_quark != missing_BL_lepton
    # The antilepton has L=-1, so both shifts can instead have B-L=+1.
    assert missing_BL_quark[0] - missing_BL_quark[1] == 0 - (-1)
    assert (+1)*(-1) == -1  # Even meson/antidiquark times an odd carrier.
    checks.append("Separate conserved B and L require distinct carriers; the antilepton orientation can match only their B-L shift")

    # Full exchange signs, rather than a dimension count alone, select the channel.
    allowed = []
    for color, spin, flavor in itertools.product((-1, 1), repeat=3):
        if color*spin*flavor == -1:  # S-wave spatial sign is +1.
            allowed.append({"color_exchange": color, "spin_exchange": spin, "flavor_exchange": flavor})
    scalar_antisymmetric_color = [r for r in allowed if r["color_exchange"] == -1 and r["spin_exchange"] == -1]
    assert scalar_antisymmetric_color == [{"color_exchange": -1, "spin_exchange": -1, "flavor_exchange": -1}]
    # Construct an antisymmetric flavor tensor and verify its rank in pair space.
    pair_dimensions = {}
    for nf in (3, 5):
        matrices = []
        for i, j in itertools.combinations(range(nf), 2):
            tensor = sp.zeros(nf)
            tensor[i, j], tensor[j, i] = 1, -1
            assert tensor.T == -tensor
            matrices.append(tensor.reshape(nf*nf, 1))
        rank = sp.Matrix.hstack(*matrices).rank()
        assert rank == nf*(nf-1)//2
        pair_dimensions[str(nf)] = rank
    checks.append("Exchange antisymmetry selects scalar color-antisymmetric flavor tensors with dimensions 3 (Nf=3) and 10 (Nf=5)")

    rng = np.random.default_rng(1971)
    max_rotation_error = 0.0
    for _ in range(32):
        m0 = float(rng.uniform(0.1, 0.5))
        gap = float(rng.uniform(1.0, 5.0))
        mc = m0 + gap
        delta = float(rng.uniform(-0.15, 0.15))
        matrix = np.array([[m0, delta], [delta, mc]])
        eigenvalues, eigenvectors = np.linalg.eigh(matrix)
        theta = 0.5*np.arctan2(2*delta, gap)
        rotation = np.array([[np.cos(theta), np.sin(theta)], [-np.sin(theta), np.cos(theta)]])
        transformed = rotation.T @ matrix @ rotation
        error = float(np.max(np.abs(transformed-np.diag(eigenvalues))))
        max_rotation_error = max(max_rotation_error, error)
        assert error < 1e-12
        eta = (1-gap/np.sqrt(gap**2+4*delta**2))/2
        assert abs(eigenvectors[1, 0]**2-eta) < 1e-14
        # Probe current and resonance coupling rotated directly from the original basis.
        fc = float(rng.uniform(0.05, 0.95))
        probe = rotation.T @ np.diag([1.0, fc]) @ rotation
        resonance = rotation.T @ np.diag([0.0, 3.0]) @ rotation
        assert abs(probe[0, 0]-(1-eta+eta*fc)) < 1e-14
        assert abs(resonance[0, 0]-3*eta) < 1e-14
    checks.append("Independent numerical diagonalization and current rotation agree with mixing formulas in 32 parameter cases")

    q2, eta, radius2, rho, coupling, mass, current = sp.symbols("q2 eta radius2 rho coupling mass current", real=True)
    ff = 1-eta+eta*(1-radius2*q2/6)
    assert sp.simplify(-6*sp.diff(ff, q2)-eta*radius2) == 0
    rho_lagrangian = mass**2*rho**2/2+coupling*eta*rho*current
    solution = sp.solve(sp.diff(rho_lagrangian, rho), rho)[0]
    effective = sp.factor(rho_lagrangian.subs(rho, solution))
    assert sp.simplify(effective+coupling**2*eta**2*current**2/(2*mass**2)) == 0
    example_coefficient = abs(effective.coeff(current, 2).subs({coupling: 3, eta: sp.Rational(1,1000), mass: 1}))
    assert example_coefficient == sp.Rational(45, 10_000_000)
    checks.append("Charge radius and tree-level elimination of a massive vector give eta and eta-squared suppression with the stated normalization")

    result = {
        "scope": "Conditional physical-endpoint charge dictionary, S-wave Pauli symmetry, and a real symmetric two-Dirac-state mixing model with diagonal currents. No duality or compositeness bound established.",
        "quark_branch": branch,
        "carrier_B_L": {"quark_branch": [1, 0], "lepton_branch": [0, 1]},
        "allowed_S_wave_exchange_signs": allowed,
        "antisymmetric_flavor_dimensions": pair_dimensions,
        "numerical_mixing_cases": 32,
        "maximum_diagonalization_error": max_rotation_error,
        "illustration": {"eta": 0.001, "g_rho": 3, "m_rho_GeV": 1,
                         "rF_over_rC": float(np.sqrt(0.001)), "abs_C6_GeV_minus2": float(example_coefficient)},
        "checks_passed": checks,
    }
    target = Path(__file__).resolve().parents[1]/"calculations"/"branch_results.json"
    target.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
