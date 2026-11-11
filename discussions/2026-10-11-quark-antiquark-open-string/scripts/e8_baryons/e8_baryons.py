#!/usr/bin/env python3
"""Three-label states: baryon labels in E8 and in the spinor class of SO(32).

Blackboard 014.  Exact arithmetic (fractions); no floating point.

A. E8 in its SU(9) form.  Roots: e_i - e_j (72) and +-(e_i+e_j+e_k - (1/3) sum e) (84+84)
   in R^9.  With the nine labels read as (flavour, colour), decompose the 84 and
   the 80 under SU(3)_f x SU(3)_c by comparing weight multisets.
B. Spinor class of Spin(32)/Z2: subsets of the sixteen labels (5 flavours x 3
   colours, plus n).  Colour singlets by number of coloured labels, and the
   charge offset for q_n = 0 and q_n = -1.
C. The Z3 orbifold of the E8 x E8 heterotic string with gauge group
   SU(9) x SO(14) x U(1): untwisted and twisted massless states and the SU(9)
   cubic anomaly as an independent check.
Output: calculations/e8_baryons/e8_baryons.txt
"""
import itertools, os
from collections import Counter
from fractions import Fraction as F
from math import comb

OUTDIR = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                       '..', '..', 'calculations', 'e8_baryons'))
os.makedirs(OUTDIR, exist_ok=True)
LINES = []
def out(*a):
    LINES.append(' '.join(str(x) for x in a))

# ------------------------------------------------------------------ A
out('A. E8 in SU(9) form')
third = F(1, 3)
A8 = [tuple((1 if a == i else -1 if a == j else 0) for a in range(9))
      for i in range(9) for j in range(9) if i != j]
L3 = [tuple((1 if a in s else 0) - third for a in range(9)) for s in itertools.combinations(range(9), 3)]
L3b = [tuple(-x for x in v) for v in L3]
roots = A8 + L3 + L3b
dot = lambda x, y: sum(a * b for a, b in zip(x, y))
ok_norm = all(dot(r, r) == 2 for r in roots)
ips = Counter(dot(r, s) for r in roots[:40] for s in roots)
closed = all((tuple(a - b * dot(r, s) for a, b in zip(r, s)) in set(roots)) for r in roots[::7] for s in roots[::5])
out(f'   roots: {len(A8)} + {len(L3)} + {len(L3b)} = {len(roots)}; all norm 2: {ok_norm}; '
    f'inner products all integers: {all(k.denominator == 1 for k in ips)}; closed under reflections (sample): {closed}')

# labels a = 3*f + c ; SU(3)_f x SU(3)_c weights of a 9-vector: flavour sums and colour sums, mod trace
def fc_weight(v):
    fl = [sum(v[3 * f + c] for c in range(3)) for f in range(3)]
    co = [sum(v[3 * f + c] for f in range(3)) for c in range(3)]
    return (fl[0] - fl[1], fl[1] - fl[2], co[0] - co[1], co[1] - co[2])

def su3_weights(kind):
    e = [(1, 0), (-1, 1), (0, -1)]                       # weights of the 3 in Dynkin labels
    add = lambda *ws: tuple(sum(x) for x in zip(*ws))
    if kind == '1':  return [(0, 0)]
    if kind == '3':  return list(e)
    if kind == '8':  return [add(e[i], tuple(-x for x in e[j])) for i in range(3) for j in range(3) if i != j] + [(0, 0), (0, 0)]
    if kind == '10': return [add(e[i], e[j], e[k]) for i, j, k in itertools.combinations_with_replacement(range(3), 3)]
    if kind == '6':  return [add(e[i], e[j]) for i, j in itertools.combinations_with_replacement(range(3), 2)]
    raise ValueError(kind)
def product_weights(a, b):
    return Counter((x[0], x[1], y[0], y[1]) for x in su3_weights(a) for y in su3_weights(b))

w84 = Counter(fc_weight(v) for v in L3)
target84 = product_weights('10', '1') + product_weights('8', '8') + product_weights('1', '10')
out('   84 = Lambda^3(3_f x 3_c) equals (10,1)+(8,8)+(1,10) as weight multisets:', w84 == target84)
w80 = Counter(fc_weight(v) for v in A8) + Counter({(0, 0, 0, 0): 8})
target80 = product_weights('8', '1') + product_weights('1', '8') + product_weights('8', '8')
out('   80 = adjoint of SU(9) equals (8,1)+(1,8)+(8,8):', w80 == target80)

# electric charge for flavours (u,d,s): Q = diag(2/3,-1/3,-1/3) x 1_3, traceless on the nine labels
q9 = [F(2, 3)] * 3 + [F(-1, 3)] * 6
out('   charge generator traceless on the nine labels (lies in SU(9)):', sum(q9) == 0)
def colour_singlet_count(vectors, colour_of):
    """number of colour singlets in a weight multiset: sum over the Weyl group of sgn * M(rho - w rho)."""
    M = Counter()
    for v, extra in vectors:
        n = [0, 0, 0]
        for a, x in enumerate(v):
            c = colour_of(a)
            if c is not None: n[c] += x
        M[(n[0] - n[1], n[1] - n[2], extra)] += 1
    extras = {k[2] for k in M}
    rho = (1, 0, -1); res = Counter()
    for ex in extras:
        tot = 0
        for perm, sgn in (((0, 1, 2), 1), ((1, 0, 2), -1), ((0, 2, 1), -1), ((2, 1, 0), -1), ((1, 2, 0), 1), ((2, 0, 1), 1)):
            d = tuple(rho[i] - rho[perm[i]] for i in range(3))
            tot += sgn * M.get((d[0] - d[1], d[1] - d[2], ex), 0)
        res[ex] = tot
    return res
dec = colour_singlet_count([(v, dot(v, q9)) for v in L3], lambda a: a % 3)
out('   colour singlets in the 84 by electric charge (u,d,s):', {str(k): v for k, v in sorted(dec.items())},
    '-> the decuplet: 1, 2, 3, 4 states at charges 2, 1, 0, -1:', dict(dec) == {F(2): 1, F(1): 2, F(0): 3, F(-1): 4})
mes = colour_singlet_count([(v, dot(v, q9)) for v in A8] + [((0,) * 9, F(0))] * 8, lambda a: a % 3)
out('   colour singlets in the 80 by charge:', {str(k): v for k, v in sorted(mes.items())}, '(octet: 2,4,2 at -1,0,+1; the count includes no SU(9) singlet)')
# the Z3 grading and the epsilon tensor: [84,84] lands in 84bar
s84, s84b = set(L3), set(L3b)
br = Counter()
for x in L3[:30]:
    for y in L3:
        z = tuple(a + b for a, b in zip(x, y))
        if z in s84b: br['84bar'] += 1
        elif z in s84: br['84'] += 1
        elif z in set(A8): br['80'] += 1
out('   sums of two 84-roots that are roots (sample of 30 x 84):', dict(br), '-> label number is conserved mod 9')
for name, nf in (('(u,c): 2 flavours', 2), ('five flavours', 5)):
    N = 3 * nf
    vecs = [(tuple(1 if a in s else 0 for a in range(N)), 0) for s in itertools.combinations(range(N), 3)]
    out(f'   Lambda^3 for {name}: {comb(N, 3)} states, colour singlets:', colour_singlet_count(vecs, lambda a: a % 3)[0])

# ------------------------------------------------------------------ B
out('')
out('B. spinor class of Spin(32)/Z2: subsets S of the sixteen labels with |S| even')
qf = [F(2, 3), F(2, 3), F(-1, 3), F(-1, 3), F(-1, 3)]
for qn in (F(0), F(-1)):
    q16 = [qf[a // 3] for a in range(15)] + [qn]
    offset = -sum(q16) / 2
    stats = Counter(); charges = {}
    groups = {}
    for k in range(0, 16):                                   # coloured labels in S
        for with_n in (0, 1):
            if (k + with_n) % 2: continue
            vecs = []
            for s in itertools.combinations(range(15), k):
                Q = sum(q16[a] for a in s) + (qn if with_n else 0) + offset
                v = tuple(1 if a in s else 0 for a in range(15))
                vecs.append((v, Q))
            cs = colour_singlet_count(vecs, lambda a: a % 3)
            tot = sum(cs.values())
            if tot:
                groups[(k, with_n)] = (tot, sorted({str(c) for c, m in cs.items() if m}))
    out(f'   q_n = {qn}: charge offset of the class = {offset}')
    for (k, wn), (tot, chs) in sorted(groups.items()):
        out(f'      {k:2d} coloured labels{" + n" if wn else "    "}: {tot:4d} colour singlets, B = {k // 3}, charges {chs}')
    out('      total colour singlets:', sum(t for t, _ in groups.values()),
        '; all charges integers:', all('/' not in c for _, chs in groups.values() for c in chs))

# ------------------------------------------------------------------ C
out('')
out('C. Z3 orbifold of E8 x E8, V = (1,1,1,1,2,0,0,0 ; 2,0,0,0,0,0,0,0)/3')
def frac1(x): return x - (x.numerator // x.denominator)
V = [F(1, 3)] * 4 + [F(2, 3)] + [F(0)] * 3 + [F(2, 3)] + [F(0)] * 7
def e8_roots(off):
    R = []
    for i, j in itertools.combinations(range(8), 2):
        for si in (1, -1):
            for sj in (1, -1):
                p = [F(0)] * 16; p[off + i], p[off + j] = F(si), F(sj); R.append(tuple(p))
    for signs in itertools.product((1, -1), repeat=8):
        if signs.count(-1) % 2 == 0:
            p = [F(0)] * 16
            for i, s in enumerate(signs): p[off + i] = F(s, 2)
            R.append(tuple(p))
    return R
R1, R2 = e8_roots(0), e8_roots(8)
V2 = sum(x * x for x in V)
out('   3(V^2 - 2/3) =', 3 * (V2 - F(2, 3)), '(must be even)')
ph = lambda p: frac1(sum(a * b for a, b in zip(p, V)))
g1 = [p for p in R1 if ph(p) == 0]; m1 = [p for p in R1 if ph(p) == third]
g2 = [p for p in R2 if ph(p) == 0]; m2 = [p for p in R2 if ph(p) == third]
out(f'   first E8: {len(g1)} unbroken roots (SU(9) has 72), {len(m1)} roots with phase 1/3 (the 84)')
out(f'   second E8: {len(g2)} unbroken roots (SO(14) has 84), {len(m2)} roots with phase 1/3 (14 + 64 = 78)')

def osc(etas, emax):
    energies = []
    for e in etas:
        for base in (e, 1 - e):
            m = 0
            while base + m <= emax:
                energies.append(base + m); m += 1
    deg = {F(0): 1}
    for e in energies:
        new = dict(deg); mult = 1
        while e * mult <= emax:
            for E, c in deg.items():
                if E + e * mult <= emax: new[E + e * mult] = new.get(E + e * mult, 0) + c
            mult += 1
        deg = new
    return deg
etas = [third, third, third]
emax = 1 - sum(e * (1 - e) for e in etas) / 2
targets = {2 * (emax - E): c for E, c in osc(etas, emax).items()}
bound = max(targets)
tw = {}
for eps1 in (F(0), F(1, 2)):
    for eps2 in (F(0), F(1, 2)):
        eps = [eps1] * 8 + [eps2] * 8
        opts = [[frac1(V[a] + eps[a]) + n for n in (-2, -1, 0, 1) if (frac1(V[a] + eps[a]) + n) ** 2 <= bound] for a in range(16)]
        minrest = [F(0)] * 17
        for i in range(15, -1, -1):
            minrest[i] = minrest[i + 1] + min(x * x for x in opts[i])
        def rec(i, acc, norm):
            if norm + minrest[i] > bound: return
            if i == 16:
                if norm in targets:
                    n1 = sum(acc[a] - V[a] - eps[a] for a in range(8))
                    n2 = sum(acc[a] - V[a] - eps[a] for a in range(8, 16))
                    if n1 % 2 == 0 and n2 % 2 == 0: tw[tuple(acc)] = targets[norm]
                return
            for x in opts[i]: rec(i + 1, acc + [x], norm + x * x)
        rec(0, [], F(0))
# classify twisted states by their weights under the unbroken roots of each factor
def proj_norm(P, gens):
    # sum over the unbroken roots of (P.alpha)^2 = 2 h |P_proj|^2 for a simply-laced factor with Coxeter number h
    return sum(dot(P, g) ** 2 for g in gens)
cl = Counter()
for P, d in tw.items():
    cl[(str(proj_norm(P, g1) / 18), str(proj_norm(P, g2) / 24), d)] += 1   # h = 9 for SU(9), 12 for SO(14)
out('   twisted massless left-moving states (before the factor 27 of fixed points):')
for (a, b, d), c in sorted(cl.items()):
    out(f'      {c:3d} weights, squared weight length in SU(9): {a} (a fundamental weight has 8/9), in SO(14): {b}, oscillator degeneracy {d}')
# SU(9) cubic anomaly: sum of (c.P)^3 over chiral states, for Cartan directions c in the span of the unbroken roots
import random
random.seed(1)
res = []
for _ in range(3):
    cvec = [F(0)] * 16
    for g in random.sample(g1, 5):
        cvec = [a + random.randint(-2, 2) * b for a, b in zip(cvec, g)]
    U = 3 * sum(dot(cvec, p) ** 3 for p in m1)
    T = 27 * sum(d * dot(cvec, P) ** 3 for P, d in tw.items())
    res.append((str(U), str(T), U + T == 0))
out('   SU(9) cubic sums (untwisted, twisted, cancel):', res)
path = os.path.join(OUTDIR, 'e8_baryons.txt')
open(path, 'w').write('\n'.join(LINES) + '\n')
print('wrote', path)
