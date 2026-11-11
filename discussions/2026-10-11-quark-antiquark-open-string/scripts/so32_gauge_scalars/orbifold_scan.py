#!/usr/bin/env python3
"""Untwisted spectrum of abelian Z_N orbifolds of the 10D SO(32) vector multiplet
(heterotic Spin(32)/Z2 consistency conditions), for colour-blind gauge shifts.

Labels: the 16 Cartan directions are 15 = 5 flavours x 3 colours plus one
colourless label n.  A colour-blind shift is V = (w_1^3, ..., w_5^3, w_n).

Open-string-like sectors of the 480 roots (flavour level):
  M(i,j)  = +e_(i,c) - e_(j,d), i != j : 9 roots = colour 1+8   phase w_i - w_j
  M(i,i)  : colour-octet roots of flavour i                     phase 0
  D(i,j)  = +e_(i,c) + e_(j,d), i<j    : 9 roots = colour 3bar+6 phase w_i + w_j
  D(i,i)  : 3 roots = colour 3bar                               phase 2 w_i
  Q(i,-/+) = e_(i,c) -/+ e_n            : 3 roots = colour 3     phase w_i -/+ w_n
and conjugates.  A root p gives a 4D gauge boson if p.V is an integer and a
chiral multiplet from the internal gauge-field component A_{z_k} if
p.V = t_k mod 1, with t = (t_1,t_2,t_3) the orbifold twist.

Consistency (no Wilson lines): N V in Gamma_16, N (V^2 - t^2) = 0 mod 2.
Output: JSON with every admissible colour-blind shift and a text summary.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement, combinations
import json, sys
import os
OUTDIR = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                       '..', '..', 'calculations', 'so32_gauge_scalars'))
os.makedirs(OUTDIR, exist_ok=True)

TWISTS = {
    'Z3':     (3,  (1, 1, -2)),
    'Z4':     (4,  (1, 1, -2)),
    'Z6-I':   (6,  (1, 1, -2)),
    'Z6-II':  (6,  (1, 2, -3)),
    'Z7':     (7,  (1, 2, -3)),
    'Z8-I':   (8,  (1, 2, -3)),
    'Z8-II':  (8,  (1, 3, -4)),
    'Z12-I':  (12, (1, 4, -5)),
    'Z12-II': (12, (1, 5, -6)),
}

def frac1(x):            # reduce mod 1 into [0,1)
    return x - (x.numerator // x.denominator)

def admissible(N, t, w, wn):
    """w: 5 flavour entries (each repeated 3 times), wn: colourless entry."""
    ent = [N * x for x in w for _ in range(3)] + [N * wn]
    ints = all(e.denominator == 1 for e in ent)
    halves = all(e.denominator == 2 for e in ent)
    if not (ints or halves):
        return False
    if sum(ent) % 2 != 0:
        return False
    V2 = 3 * sum(x * x for x in w) + wn * wn
    t2 = sum(F(a, N) ** 2 for a in t)
    return (N * (V2 - t2)) % 2 == 0

def spectrum(N, t, w, wn):
    tw = [frac1(F(a, N)) for a in t]
    def cls(phase):
        ph = frac1(phase)
        if ph == 0:
            return 'V'                       # gauge boson (vector multiplet)
        m = sum(1 for x in tw if x == ph)    # chiral multiplets from A_{z_k}
        mb = sum(1 for x in tw if x == frac1(-ph))   # their conjugates sit on -p
        return (m, mb)
    out = {'M': {}, 'D': {}, 'Q': {}}
    for i in range(5):
        for j in range(5):
            if i != j:
                out['M'][f'{i}{j}'] = cls(w[i] - w[j])
        for j in range(i, 5):
            out['D'][f'{i}{j}'] = cls(w[i] + w[j])
        out['Q'][f'{i}-'] = cls(w[i] - wn)
        out['Q'][f'{i}+'] = cls(w[i] + wn)
    return out

def gauge_group(w, wn):
    """Unbroken group from colour-blind shift: reflect labels so w in [0,1/2]."""
    def canon(x):
        x = frac1(x)
        return min(x, 1 - x)
    groups = {}
    for x in w:
        groups.setdefault(canon(x), [0, 0])[0] += 3
    groups.setdefault(canon(wn), [0, 0])[1] += 1
    parts = []
    for val in sorted(groups):
        n = groups[val][0] + groups[val][1]
        if val == 0 or val == F(1, 2):
            parts.append(f'SO({2*n})')
        else:
            parts.append(f'U({n})')
    return ' x '.join(parts)

def scan(name):
    N, t = TWISTS[name]
    res = []
    for half in (0, 1):
        base = [F(2 * k + half, 2 * N) for k in range(N)]
        basen = [F(2 * k + half, 2 * N) for k in range(2 * N)]
        for w in combinations_with_replacement(base, 5):
            for wn in basen:
                if admissible(N, t, w, wn):
                    res.append((w, wn))
    return N, t, res

def summarise(name, fh):
    N, t, res = scan(name)
    rows = []
    for w, wn in res:
        sp = spectrum(N, t, w, wn)
        D = sp['D']
        # diquark sector: all 15 symmetric flavour pairs
        kinds = set(D.values())
        all_matter_same = (len(kinds) == 1 and 'V' not in kinds)
        rows.append({
            'w': [str(x) for x in w], 'wn': str(wn),
            'gauge': gauge_group(w, wn),
            'D': {k: v for k, v in D.items()},
            'M': sp['M'], 'Q': sp['Q'],
            'diquark_uniform': all_matter_same,
            'diquark_mult': (list(kinds)[0] if all_matter_same else None),
        })
    if '--json' in sys.argv:          # full per-shift dump (large); off by default
        json.dump({'orbifold': name, 'N': N, 'twist': t, 'models': rows},
                  open(os.path.join(OUTDIR, f'scan_{name}.json'), 'w'), indent=1, default=str)
    groups = {}
    for r in rows:
        groups.setdefault(r['gauge'], 0)
        groups[r['gauge']] += 1
    print(f'== {name}: twist {t}/{N}; admissible colour-blind shifts: {len(rows)}', file=fh)
    for g, c in sorted(groups.items(), key=lambda kv: -kv[1]):
        print(f'   {c:5d}  {g}', file=fh)
    uni = [r for r in rows if r['diquark_uniform']]
    print(f'   shifts where all 15 diquark labels are chiral matter with one multiplicity: {len(uni)}', file=fh)
    seen = set()
    for r in uni:
        key = (r['gauge'], str(r['diquark_mult']))
        if key in seen:
            continue
        seen.add(key)
        print(f"     gauge {r['gauge']}; (copies on D, copies on Dbar) = {r['diquark_mult']}; "
              f"example w={r['w']} wn={r['wn']}", file=fh)
    return rows

if __name__ == '__main__':
    path = os.path.join(OUTDIR, 'scan_summary.txt')
    with open(path, 'w') as fh:
        for name in TWISTS:
            summarise(name, fh)
    print('wrote', path)
