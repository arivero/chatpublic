#!/usr/bin/env python3
"""Strings that are points in the noncompact directions: stretched and wound strings.

Blackboard 016.  Exact arithmetic.  Same lattice and conventions as
nine_dim_frames.py (blackboard 015): vectors (pi; n, w), norm pi^2 + 2nw,
vacuum t = (-A; -E, 1) with E = (A^2 + R^2)/2 in units alpha' = 2, so that a
vector of norm 2 has alpha' M^2 = (v.t)^2 / r with r = R^2/alpha' = R^2/2.

A. Wilson line proportional to electric charge, A = (3/2) Q.  Gauge group, and
   which two-label states it lifts.
B. Single-label states with winding: the SU(18) point (massless) and the
   E7 x SO(20) point (massive).
Output: calculations/nine_dim_frames/charge_wilson_line.txt
"""
import itertools, os
from collections import Counter
from fractions import Fraction as F
from math import floor

OUTDIR = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                       '..', '..', 'calculations', 'nine_dim_frames'))
os.makedirs(OUTDIR, exist_ok=True)
LINES = []
def out(*a):
    LINES.append(' '.join(str(x) for x in a))
H = F(1, 2)

def ip(u, v):
    return sum(a * b for a, b in zip(u[:16], v[:16])) + u[16] * v[17] + u[17] * v[16]
def rank(vectors):
    M = [[F(x) for x in v] for v in vectors]
    r = 0
    for c in range(len(M[0]) if M else 0):
        piv = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c] / M[r][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        r += 1
        if r == len(M): break
    return r
def components(roots):
    parent = list(range(len(roots)))
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]; a = parent[a]
        return a
    for i in range(len(roots)):
        for j in range(i + 1, len(roots)):
            if ip(roots[i], roots[j]) != 0:
                a, b = find(i), find(j)
                if a != b: parent[a] = b
    comp = {}
    for i in range(len(roots)):
        comp.setdefault(find(i), []).append(roots[i])
    return list(comp.values())
def type_of(r, N):
    if (r, N) == (6, 72): return 'E6'
    if (r, N) == (7, 126): return 'E7'
    if (r, N) == (8, 240): return 'E8'
    if N == r * (r + 1): return f'SU({r + 1})'
    if r >= 4 and N == 2 * r * (r - 1): return f'SO({2 * r})'
    return f'?(rank {r}, {N} roots)'
def root_system(roots):
    return ' x '.join(sorted((type_of(rank(c), len(c)) for c in components(roots)), reverse=True)) or '(none)'
def vectors_at(A, R2, s=F(0)):
    """lattice vectors of norm 2 with v.t = s."""
    A = [F(a) for a in A]
    E = (sum(a * a for a in A) + R2) / 2
    res = []
    for w in range(-60, 61):
        target = 2 - 2 * w * s - w * w * R2
        if target < 0: continue
        centre = [w * a for a in A]
        for half in (0, 1):
            opts = []
            for c in centre:
                k0 = floor(-c)
                opts.append([F(k) + F(half, 2) for k in range(k0 - 2, k0 + 4) if (F(k) + F(half, 2) + c) ** 2 <= target])
            if any(not o for o in opts): continue
            minrest = [F(0)] * 17
            for i in range(15, -1, -1):
                minrest[i] = minrest[i + 1] + min((x + centre[i]) ** 2 for x in opts[i])
            stack = [(0, (), F(0))]
            while stack:
                i, acc, norm = stack.pop()
                if norm + minrest[i] > target: continue
                if i == 16:
                    if norm == target and sum(acc) % 2 == 0:
                        n = s + sum(p * a for p, a in zip(acc, A)) + w * E
                        if n.denominator == 1: res.append(acc + (n, F(w)))
                    continue
                for x in opts[i]:
                    stack.append((i + 1, acc + (x,), norm + (x + centre[i]) ** 2))
    return res
def fold(x):
    x = x - floor(x)
    return min(x, 1 - x)
def showc(c):
    return ' '.join(f'{x}^{m}' for x, m in sorted(c.items()))

# labels: 0..5 = (u,c) x colour, 6..14 = (d,s,b) x colour, 15 = n
def charges(qn):
    return [F(2, 3)] * 6 + [F(-1, 3)] * 9 + [F(qn)]

# ------------------------------------------------------------------ A
out('A. Wilson line proportional to electric charge: A = (3/2) Q')
for qn, R2 in ((-1, H), (0, F(1, 4))):
    q = charges(qn)
    A = [F(3, 2) * x for x in q]
    out(f'   q_n = {qn}: A = (3/2)q = {showc(Counter(A))}; folded: {showc(Counter(fold(a) for a in A))}')
    rts = vectors_at(A, R2)
    out(f"      at R^2/alpha' = {R2 / 2}: gauge group {root_system(rts)} ({len(rts)} roots);",
        'at zero winding:', root_system([v for v in rts if v[17] == 0]))
q = charges(-1)
A = [F(3, 2) * x for x in q]
out('   holonomy on a state of charge Q is exp(3 pi i Q) = (-1)^(3Q); two-label states (the 480 roots of SO(32)), q_n = -1:')
table = Counter()
for i, j in itertools.combinations(range(16), 2):
    for si in (1, -1):
        for sj in (1, -1):
            Q = si * q[i] + sj * q[j]
            d = fold(F(3, 2) * Q)
            table[(abs(Q), 'lifted' if d != 0 else 'massless', str(d * d))] += 1
out("      |Q|     states  status     (v.t)^2 = r alpha' M^2")
for (Q, st, d2), m in sorted(table.items()):
    out(f'      {str(Q):6s}  {m:5d}  {st:9s}  {d2}')
out('      lifted exactly when 3Q is odd:',
    all((st == 'lifted') == ((3 * Q) % 2 == 1) for (Q, st, d2) in table))
neutral = sum(1 for f in range(5) for g in range(5) if (f < 2) == (g < 2)) - 1
charged = sum(1 for f in range(5) for g in range(5) if (f < 2) != (g < 2))
out(f'   colour-singlet meson-like labels of five flavours, the (24,1): {neutral} neutral (massless) + {charged} of charge +-1 (lifted)')
out("   common mass of the lifted two-label states: alpha' M^2 = 1/(4r), equal to 1 at the E7 x SO(20) point r = 1/4")

# ------------------------------------------------------------------ B
out('')
out('B. single-label states with winding')
A18 = [F(-3, 4)] + [F(-1, 4)] * 14 + [F(1, 4)]
R18 = H
rts = vectors_at(A18, R18)
out('   SU(18) point: A =', showc(Counter(A18)), ", R^2/alpha' = 1/4; gauge group", root_system(rts))
# simple roots of the SU(18) chain in the conventions of 015
def vec(pi, n=0, w=0):
    return tuple(F(x) for x in pi) + (F(n), F(w))
def unit(i, s=1):
    return [s if a == i else 0 for a in range(16)]
def plus(p, r):
    return [a + b for a, b in zip(p, r)]
chain = [vec([0] * 16, -1, -1), vec(plus(unit(0, -1), unit(1, -1)), 1, 0)]
chain += [vec(plus(unit(i - 1), unit(i, -1))) for i in range(2, 15)]
chain += [vec(plus(unit(14), unit(15))), vec([-H] * 16, 1, -1)]
okc = all(ip(chain[i], chain[j]) == (2 if i == j else -1 if abs(i - j) == 1 else 0) for i in range(17) for j in range(17))
out('   chain of seventeen simple roots reproduces the A17 Cartan matrix:', okc, '; all are roots at this point:', all(c in set(rts) for c in chain))
# the eighteen labels l_0 .. l_17 with l_(i-1) - l_i = chain[i-1]; l_0 and l_17 are the winding labels.
# charge = diag(0, q_1..q_16, 0), traceless when the sixteen label charges sum to zero (q_n = -1).
x = [F(0)] + charges(-1) + [F(0)]
out('   charge generator diag(0; sixteen label charges; 0) is traceless:', sum(x) == 0)
colour = [None] + [a % 3 for a in range(15)] + [None, None]
# every root is l_a - l_b; identify (a, b) from the Dynkin labels d_i = v.chain_i
def labels_of(v):
    d = [ip(v, c) for c in chain]
    # weights of l_a - l_b in the basis of fundamental weights: d_i = delta(i, a+1) - delta(i, a) - delta(i, b+1) + delta(i, b)
    for a in range(18):
        for b in range(18):
            if a == b: continue
            e = [0] * 18
            e[a] += 1; e[b] -= 1
            if all(d[i] == e[i] - e[i + 1] for i in range(17)): return a, b
    raise ValueError
stat = Counter()
for v in rts:
    a, b = labels_of(v)
    if v[17] != 1: continue
    lab = a if b in (0, 17) else b
    sign = 'label' if b in (0, 17) else 'anti-label'
    kind = 'colourless (n)' if lab == 16 else 'coloured'
    stat[(sign, kind, str(x[a] - x[b]))] += 1
out('   massless states of winding +1 at the SU(18) point (32 in all):')
for (sign, kind, Q), m in sorted(stat.items()):
    out(f'      {m:2d} states: one {sign}, {kind}, charge {Q}')
out('   every one of them is a root l_a - l_b with exactly one of a, b a winding label')

A7 = [-H] * 6 + [F(0)] * 10
out('   E7 x SO(20) point: A =', showc(Counter(A7)), ", R^2/alpha' = 1/4")
e7 = [c for c in components(vectors_at(A7, H)) if len(c) == 126][0]
for sv in (F(1, 4), F(-1, 2)):
    vs = vectors_at(A7, H, sv)
    out(f"   norm-2 vectors with v.t = {sv} (alpha' M^2 = {sv * sv / F(1, 4)}): {len(vs)}")
    if not vs: continue
    neutral7 = [v for v in vs if all(ip(v, r) == 0 for r in e7[::9])]
    spin = [v for v in neutral7 if all(abs(v[a]) == H for a in range(6, 16))]
    byw = Counter(str(v[17]) for v in spin)
    plusses = Counter(sum(1 for a in range(6, 16) if v[a] > 0) for v in spin)
    out(f'      neutral under E7 with label charges (+-1/2)^10 on the ten labels (the spinor of SO(20)): {len(spin)};',
        'windings', dict(byw), '; number of + signs', dict(sorted(plusses.items())))
    two = [v for v in vs if v[17] == 0]
    out(f'      two-label states of zero winding among them: {len(two)} (one label in each block: {all(sum(1 for a in range(6) if v[a] != 0) == 1 for v in two)})')

with open(os.path.join(OUTDIR, 'charge_wilson_line.txt'), 'w') as f:
    f.write('\n'.join(LINES) + '\n')
print('\n'.join(LINES))
