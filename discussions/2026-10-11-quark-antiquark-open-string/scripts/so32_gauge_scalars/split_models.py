#!/usr/bin/env python3
"""Detail for the (u,c | d,s,b) flavour split: shifts w = (a,a,b,b,b; wn).
For each admissible shift list what each open-string-like sector becomes:
V = 4D gauge boson, (m, mbar) = number of chiral multiplets on the sector
and on its conjugate, '-' = projected out.  Deduplicated by spectrum."""
from fractions import Fraction as F
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from orbifold_scan import TWISTS, admissible, frac1, OUTDIR

def cls(N, t, phase):
    tw = [frac1(F(a, N)) for a in t]
    ph = frac1(phase)
    if ph == 0:
        return 'V'
    m = [k + 1 for k, x in enumerate(tw) if x == ph]
    mb = [k + 1 for k, x in enumerate(tw) if x == frac1(-ph)]
    if not m and not mb:
        return '-'
    s = ''
    if m:
        s += 'chiral[plane ' + ','.join(map(str, m)) + ']'
    if mb:
        s += ('+' if s else '') + 'conj[plane ' + ','.join(map(str, mb)) + ']'
    return s

out = []
for name, (N, t) in TWISTS.items():
    seen = {}
    for half in (0, 1):
        base = [F(2 * k + half, 2 * N) for k in range(N)]
        basen = [F(2 * k + half, 2 * N) for k in range(2 * N)]
        for a in base:
            for b in base:
                if a == b:
                    continue
                for wn in basen:
                    w = (a, a, b, b, b)
                    if not admissible(N, t, w, wn):
                        continue
                    row = {
                        'uu': cls(N, t, 2 * a), 'ud': cls(N, t, a + b), 'dd': cls(N, t, 2 * b),
                        'u dbar': cls(N, t, a - b), 'd ubar': cls(N, t, b - a),
                        'u n': cls(N, t, a + wn), 'u nbar': cls(N, t, a - wn),
                        'd n': cls(N, t, b + wn), 'd nbar': cls(N, t, b - wn),
                    }
                    key = json.dumps(row, sort_keys=True)
                    seen.setdefault(key, []).append((str(a), str(b), str(wn)))
    for key, shifts in seen.items():
        row = json.loads(key)
        out.append({'orbifold': name, 'twist': f'{t}/{N}', 'n_shifts': len(shifts),
                    'example (w_u, w_d, w_n)': shifts[0], **row})
json.dump(out, open(os.path.join(OUTDIR, 'split_models.json'), 'w'), indent=1)

def matter(x):
    return x not in ('V', '-')

path = os.path.join(OUTDIR, 'split_models.txt')
with open(path, 'w') as fh:
    print('models (deduplicated) per orbifold:',
          {n: sum(1 for r in out if r['orbifold'] == n) for n in TWISTS}, file=fh)
    print(file=fh)
    print('A. all three diquark types uu, ud, dd are chiral matter (no diquark vectors):', file=fh)
    for r in out:
        if matter(r['uu']) and matter(r['ud']) and matter(r['dd']):
            print(f"  {r['orbifold']:7s} {r['example (w_u, w_d, w_n)']}  uu:{r['uu']}  ud:{r['ud']}  dd:{r['dd']}"
                  f"  | u dbar:{r['u dbar']}  d ubar:{r['d ubar']}  | un:{r['u n']} unbar:{r['u nbar']}"
                  f" dn:{r['d n']} dnbar:{r['d nbar']}", file=fh)
    print(file=fh)
    print('B. charged mesons (u dbar) are chiral matter:', file=fh)
    for r in out:
        if matter(r['u dbar']) or matter(r['d ubar']):
            print(f"  {r['orbifold']:7s} {r['example (w_u, w_d, w_n)']}  u dbar:{r['u dbar']}  d ubar:{r['d ubar']}"
                  f"  | uu:{r['uu']}  ud:{r['ud']}  dd:{r['dd']}", file=fh)
print('wrote', path)
