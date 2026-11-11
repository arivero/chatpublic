#!/usr/bin/env python3
"""Readable massless chiral spectrum of selected prime-order models, grouped by
sector (U = untwisted = internal components of the 10D gauge field, Tk = twisted)."""
from fractions import Fraction as F
from math import comb
from collections import Counter, defaultdict
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from full_spectrum import spectrum, blocks, anomalies, frac1, OUTDIR

def describe(V, chir):
    bl = blocks(V)
    groups = defaultdict(int)
    for P, mult, sec in chir:
        labs, dim = [], 1
        for val in sorted(bl):
            mem = bl[val]
            ent = [s * P[a] for a, s in mem]
            n = len(ent)
            if val == 0 or val == F(1, 2):
                name = f'SO({2*n})'
                nz = [x for x in ent if x != 0]
                if not nz:
                    lab = '1'
                elif len(nz) == 1 and abs(nz[0]) == 1:
                    lab, dim = 'vector', dim * 2 * n
                elif all(abs(x) == F(1, 2) for x in ent):
                    if n == 1:
                        lab = f'charge {ent[0]}'
                    else:
                        lab, dim = 'spinor', dim * 2 ** (n - 1)
                else:
                    lab = 'other' + str(sorted(set(ent)))
                if n == 1 and lab == 'vector':
                    lab, dim = f'charge {nz[0]}', dim // 2
            else:
                name = f'U({n})'
                base = Counter(ent).most_common(1)[0][0]
                up = sum(1 for x in ent if x == base + 1)
                dn = sum(1 for x in ent if x == base - 1)
                if up + dn + sum(1 for x in ent if x == base) != n:
                    lab = 'other'
                else:
                    q = sum(ent)
                    if up == 0 and dn == 0:
                        lab = f'1(q={q})'
                    else:
                        parts = []
                        if up:
                            parts.append(f'antisym^{up}' if up > 1 else 'fund')
                        if dn:
                            parts.append(f'conj antisym^{dn}' if dn > 1 else 'antifund')
                        lab = ' x '.join(parts) + f'(q={q})'
                        dim *= comb(n, up) * comb(n - up, dn)
            labs.append(f'{name}:{lab}')
        groups[(sec, ' | '.join(labs), dim)] += mult
    rows = []
    for (sec, lab, dim), tot in sorted(groups.items()):
        rows.append((sec, lab, dim, F(tot, dim)))
    return rows

MODELS = {
    'Z3, V=(1^15,3)/3  [equivalent to (1^14,2,0)/3], gauge U(15) x SO(2)':
        (3, (1, 1, -2), [F(1, 3)] * 15 + [F(1)]),
    'Z7, V=(1^6,2^9,0)/7, gauge U(6) x U(9) x SO(2)':
        (7, (1, 2, -3), [F(1, 7)] * 6 + [F(2, 7)] * 9 + [F(0)]),
}

if __name__ == '__main__':
    out = {}
    lines = []
    for name, (N, v, V) in MODELS.items():
        V2 = sum(x * x for x in V); v2 = sum(F(a, N) ** 2 for a in v)
        chir = spectrum(V, N, v, +1)
        lines.append(f'== {name}')
        an = {k: str(val) for k, val in anomalies(V, chir).items()}
        lines.append(f'   level matching N(V^2-v^2) = {N*(V2-v2)} ; cubic anomalies: {an}')
        rows = describe(V, chir)
        out[name] = [(s, l, d, str(c)) for s, l, d, c in rows]
        for sec, lab, dim, copies in rows:
            lines.append(f'   {sec:3s} copies={str(copies):>4s} dim={dim:<5d} {lab}')
    json.dump(out, open(os.path.join(OUTDIR, 'selected_spectra.json'), 'w'), indent=1)
    path = os.path.join(OUTDIR, 'selected_spectra.txt')
    open(path, 'w').write('\n'.join(lines) + '\n')
    print('wrote', path)
