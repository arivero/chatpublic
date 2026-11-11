#!/usr/bin/env python3
"""Complete massless charged spectrum (untwisted + twisted) for prime-order
orbifolds Z3 and Z7 of the Spin(32)/Z2 heterotic string, for a given shift V,
and the cubic non-abelian anomaly as an independent consistency test.

Twisted sector k:  P = p + k V, p in Gamma_16,
    P^2/2 + N_osc - 1 + dc_k = 0,  dc_k = (1/2) sum_i eta_i (1 - eta_i),
    eta_i = frac(k v_i).
For prime N every level-matched state survives, with one chiral multiplet per
fixed point (27 for Z3, 7 for Z7).  Left-chiral sectors are those with
sum_i eta_i = 1; the others are their CPT conjugates.
Untwisted chiral multiplets sit on roots p with p.V = s * v_i mod 1; the sign
s is fixed by requiring anomaly cancellation (both signs are evaluated).
"""
from fractions import Fraction as F
from itertools import combinations
import sys, json, os
OUTDIR = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                       '..', '..', 'calculations', 'so32_gauge_scalars'))
os.makedirs(OUTDIR, exist_ok=True)

def frac1(x):
    return x - (x.numerator // x.denominator)

def roots16():
    out = []
    for a, b in combinations(range(16), 2):
        for sa in (1, -1):
            for sb in (1, -1):
                p = [0] * 16
                p[a], p[b] = sa, sb
                out.append(tuple(p))
    return out

def osc_degeneracies(etas, emax):
    """number of oscillator monomials of total energy E <= emax (E as Fraction)."""
    energies = []
    for e in etas:
        for base in (e, 1 - e):
            m = 0
            while base + m <= emax:
                if base + m > 0:
                    energies.append(base + m)
                m += 1
    deg = {F(0): 1}
    for e in energies:                 # unrestricted multiplicity of each mode
        new = dict(deg)
        mult = 1
        while e * mult <= emax:
            for E, c in deg.items():
                if E + e * mult <= emax:
                    new[E + e * mult] = new.get(E + e * mult, 0) + c
            mult += 1
        deg = new
    return deg

def twisted(V, k, N, v):
    etas = [frac1(F(k * a, N)) for a in v]
    dc = sum(e * (1 - e) for e in etas) / 2
    emax = 1 - dc
    deg = osc_degeneracies(etas, emax)
    targets = {2 * (emax - E): c for E, c in deg.items()}   # P^2 -> degeneracy
    bound = max(targets)
    states = {}
    for eps in (F(0), F(1, 2)):
        shifts = [frac1(k * x + eps) for x in V]            # entry = shift + integer
        opts = []
        for s in shifts:
            o = [(s + n) for n in (-2, -1, 0, 1) if (s + n) ** 2 <= bound]
            opts.append(o)
        minrest = [F(0)] * 17
        for i in range(15, -1, -1):
            minrest[i] = minrest[i + 1] + min((x * x for x in opts[i]), default=bound + 1)
        def rec(i, acc, norm):
            if norm + minrest[i] > bound:
                return
            if i == 16:
                if norm in targets:
                    # lattice parity: sum of the integer parts n_a must be even
                    nsum = sum(acc[a] - k * V[a] - eps for a in range(16))
                    if nsum.denominator == 1 and nsum % 2 == 0:
                        states[tuple(acc)] = targets[norm]
                return
            for x in opts[i]:
                rec(i + 1, acc + [x], norm + x * x)
        rec(0, [], F(0))
    return etas, states

def spectrum(V, N, v, sign):
    nfix = {3: 27, 7: 7}[N]
    tw = [frac1(F(sign * a, N)) for a in v]
    chir = []                                   # (weight, multiplicity)
    for p in roots16():
        ph = frac1(sum(F(pi) * Vi for pi, Vi in zip(p, V)))
        m = sum(1 for x in tw if x == ph)
        if ph != 0 and m:
            chir.append((tuple(F(x) for x in p), m, 'U'))
    for k in range(1, N):
        etas, st = twisted(V, k, N, v)
        if sum(etas) != 1:
            continue                            # CPT conjugate sector
        for P, d in st.items():
            chir.append((P, d * nfix, f'T{k}'))
    return chir

def blocks(V):
    """group the 16 directions by |shift| (after reflecting labels)."""
    def canon(x):
        x = frac1(x)
        return min(x, 1 - x)
    b = {}
    for a, x in enumerate(V):
        b.setdefault(canon(x), []).append((a, 1 if frac1(x) == canon(x) else -1))
    return b

def anomalies(V, chir):
    res = {}
    for val, members in blocks(V).items():
        if val == 0 or val == F(1, 2) or len(members) < 3:
            continue                            # SO(2n) or too small: no cubic anomaly
        (a1, s1), (a2, s2), (a3, s3) = members[:3]
        tot = F(0)
        for P, mult, _ in chir:
            c = s1 * P[a1] + s2 * P[a2] - 2 * s3 * P[a3]
            tot += mult * c ** 3
        res[f'SU({len(members)}) [shift {val}]'] = tot / (-6)   # in units of a fundamental
    return res

MODELS = {
    'Z3 U(15)xSO(2), V=(1^15,3)/3':  (3, (1, 1, -2), [F(1, 3)] * 15 + [F(1)]),
    'Z3 U(12)xSO(8)':  (3, (1, 1, -2), [F(1, 3)] * 12 + [F(0)] * 4),
    'Z3 U(9)xSO(14), V=(1^8,2,0^7)/3':  (3, (1, 1, -2), [F(1, 3)] * 8 + [F(2, 3)] + [F(0)] * 7),
    'Z3 U(6)xSO(20)':  (3, (1, 1, -2), [F(1, 3)] * 6 + [F(0)] * 10),
    'Z3 std embedding U(3)xSO(26)': (3, (1, 1, -2), [F(1, 3), F(1, 3), F(-2, 3)] + [F(0)] * 13),
    'Z7 U(6)xU(9)xSO(2), V=(1^6,2^9,0)/7': (7, (1, 2, -3), [F(1, 7)] * 6 + [F(2, 7)] * 9 + [F(0)]),
}

if __name__ == '__main__':
    report = {}
    lines = []
    for name, (N, v, V) in MODELS.items():
        V2 = sum(x * x for x in V); v2 = sum(F(a, N) ** 2 for a in v)
        ok = (N * (V2 - v2)) % 2 == 0
        lines.append(f'== {name}: level matching {"ok" if ok else "FAILS"}')
        for sign in (+1, -1):
            chir = spectrum(V, N, v, sign)
            an = anomalies(V, chir)
            nU = sum(m for _, m, s in chir if s == 'U')
            nT = sum(m for _, m, s in chir if s != 'U')
            lines.append(f'   untwisted sign {sign:+d}: untwisted weights x mult = {nU}, twisted = {nT}; cubic anomalies: '
                         + ', '.join(f'{k}: {val}' for k, val in an.items()))
            report[f'{name} | sign {sign:+d}'] = {k: str(val) for k, val in an.items()}
    json.dump(report, open(os.path.join(OUTDIR, 'anomaly_check.json'), 'w'), indent=1)
    path = os.path.join(OUTDIR, 'anomaly_check.txt')
    open(path, 'w').write('\n'.join(lines) + '\n')
    print('wrote', path)
