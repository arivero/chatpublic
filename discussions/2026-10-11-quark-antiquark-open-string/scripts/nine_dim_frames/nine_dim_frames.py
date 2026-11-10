#!/usr/bin/env python3
"""Nine dimensions: SO(32) labels, winding and the exceptional groups.

Blackboard 015.  Exact arithmetic (fractions); no floating point.

The charge lattice of the heterotic string on a circle is the even self-dual
lattice of signature (17,1).  In SO(32) variables a vector is (pi; n, w) with
pi in Gamma16 (the sixteen label charges), n the momentum and w the winding
number on the circle, and (pi; n, w)^2 = pi^2 + 2 n w.  A vacuum is a timelike
direction t = (-A; -E, 1), with A the Wilson line and R^2 = 2E - A^2 the squared
radius in units alpha' = 2 (so R^2/alpha' = R^2/2).  Massless charged gauge
bosons are the lattice vectors of norm 2 orthogonal to t.

A. The nineteen simple roots in SO(32) labels; their diagram; null vectors.
B. The E8 x E8 cusp: z has winding 2 and z-perp/z is Gamma8 + Gamma8.
C. Exceptional groups from m labels and the circle: E_(m+1) x SO(32-2m).
D. E8 at the E8 x SO(18) point: winding grading, label content, the SU(9)
   dictionary, the centralizers used in the colour lemma, and the colour
   singlets of E8 under the SO(32) colour (they form G2 x SU(3)).
E. All maximal enhancements from the diagram, cross-checked by enumerating the
   roots at each point; which ones keep the SO(32) colour at zero winding, and
   which have a Wilson line that depends only on electric charge.
F. The SU(18) point: sixteen labels and two winding labels; the classes of
   SU(18) present in the lattice; the lightest massive charged states.
G. Other duality frames: images of the SO(32) cusp under reflections, and how
   each of them grades the E8 of part D.
Output: calculations/nine_dim_frames/nine_dim_frames.txt
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
# ------------------------------------------------------------------ lattice
def vec(pi, n=0, w=0):
    return tuple(F(x) for x in pi) + (F(n), F(w))
def ip(u, v):
    return sum(a * b for a, b in zip(u[:16], v[:16])) + u[16] * v[17] + u[17] * v[16]
def add(u, v, c=1):
    return tuple(a + c * b for a, b in zip(u, v))
def lin(pairs):
    r = (F(0),) * 18
    for c, v in pairs:
        r = add(r, v, c)
    return r
def in_lattice(v):
    pi = v[:16]
    if v[16].denominator != 1 or v[17].denominator != 1: return False
    dens = {x.denominator for x in pi}
    if dens not in ({1}, {2}): return False
    return sum(pi) % 2 == 0
def unit(i, s=1):
    return [s if a == i else 0 for a in range(16)]
def plus(p, q):
    return [a + b for a, b in zip(p, q)]

def rank(vectors):
    M = [[F(x) for x in v] for v in vectors]
    r = 0
    ncol = len(M[0]) if M else 0
    for c in range(ncol):
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
def det(M):
    M = [list(row) for row in M]
    n = len(M); d = F(1)
    for c in range(n):
        piv = next((i for i in range(c, n) if M[i][c] != 0), None)
        if piv is None: return F(0)
        if piv != c:
            M[c], M[piv] = M[piv], M[c]; d = -d
        d *= M[c][c]
        for i in range(c + 1, n):
            if M[i][c] != 0:
                f = M[i][c] / M[c][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[c])]
    return d
def nullspace(rows, ncol):
    M = [list(r) for r in rows]
    pivots = []; r = 0
    for c in range(ncol):
        piv = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        M[r] = [a / M[r][c] for a in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        pivots.append(c); r += 1
        if r == len(M): break
    free = [c for c in range(ncol) if c not in pivots]
    basis = []
    for fcol in free:
        x = [F(0)] * ncol; x[fcol] = F(1)
        for i, pc in enumerate(pivots):
            x[pc] = -M[i][fcol]
        basis.append(x)
    return basis

# ------------------------------------------------------------------ root systems
def components(roots, ipf=None):
    ipf = ipf or ip
    parent = list(range(len(roots)))
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]; a = parent[a]
        return a
    for i in range(len(roots)):
        for j in range(i + 1, len(roots)):
            if ipf(roots[i], roots[j]) != 0:
                a, b = find(i), find(j)
                if a != b: parent[a] = b
    comp = {}
    for i in range(len(roots)):
        comp.setdefault(find(i), []).append(roots[i])
    return list(comp.values())
def type_of(r, N):
    if r == 6 and N == 72: return 'E6'
    if r == 7 and N == 126: return 'E7'
    if r == 8 and N == 240: return 'E8'
    if N == r * (r + 1): return f'A{r}'
    if r >= 4 and N == 2 * r * (r - 1): return f'D{r}'
    return f'?(rank {r}, {N} roots)'
def group_name(t):
    if t.startswith('A'): return f'SU({int(t[1:]) + 1})'
    if t.startswith('D'): return f'SO({2 * int(t[1:])})'
    return t
def order_key(t):
    return ('EDA'.index(t[0]), -int(t[1:])) if t[0] in 'EDA' else (9, 0)
def root_system(roots, ipf=None, null=None):
    types = []
    for c in components(roots, ipf):
        r = rank(c + [null]) - 1 if null is not None else rank(c)
        types.append(type_of(r, len(c)))
    return sorted(types, key=order_key)
def show(types):
    return ' x '.join(group_name(t) for t in types) if types else '(none)'

def roots_at(A, R2, s=F(0)):
    """all lattice vectors v of norm 2 with v.t = s, t = (-A; -E, 1), E = (A^2 + R^2)/2.
    s = 0 gives the massless charged gauge bosons; p_R^2 = s^2/R^2 in general."""
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
                o = []
                k0 = floor(-c)
                for k in range(k0 - 2, k0 + 4):
                    x = F(k) + F(half, 2)
                    if (x + c) ** 2 <= target: o.append(x)
                opts.append(o)
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
                        if n.denominator == 1:
                            v = acc + (n, F(w))
                            assert ip(v, v) == 2 and in_lattice(v)
                            res.append(v)
                    continue
                for x in opts[i]:
                    stack.append((i + 1, acc + (x,), norm + (x + centre[i]) ** 2))
    return res

# ------------------------------------------------------------------ A
out('A. the nineteen simple roots in SO(32) labels, vectors (pi; n, w), norm pi^2 + 2nw')
alpha = {0: vec(plus(unit(0, -1), unit(1, -1)), 1, 0)}
for i in range(1, 16):
    alpha[i] = vec(plus(unit(i - 1), unit(i, -1)))
alpha[16] = vec(plus(unit(14), unit(15)))
g1 = vec([0] * 16, -1, -1)
g2 = vec([-H] * 16, 1, -1)
chain = [g1, alpha[0]] + [alpha[i] for i in range(2, 15)] + [alpha[16], g2]
chain_names = ['g1', 'a0'] + [f'a{i}' for i in range(2, 15)] + ['a16', 'g2']
nodes = chain + [alpha[1], alpha[15]]
names = chain_names + ['a1', 'a15']
out('   g1 = (0; -1, -1)   a0 = (-e1-e2; 1, 0)   a_i = (e_i - e_(i+1); 0, 0), i = 1..15')
out('   a16 = (e15+e16; 0, 0)   g2 = ((-1/2)^16; 1, -1)')
edges = {(i, i + 1) for i in range(16)} | {(2, 17), (14, 18)}
okG = True
for i in range(19):
    for j in range(19):
        want = 2 if i == j else (-1 if (min(i, j), max(i, j)) in edges else 0)
        if ip(nodes[i], nodes[j]) != want: okG = False
out('   all nineteen in the lattice:', all(in_lattice(v) for v in nodes), '; all of norm 2:', all(ip(v, v) == 2 for v in nodes))
out('   Gram matrix is the diagram: chain of 17 (g1-a0-a2-a3-...-a14-a16-g2), a1 attached to a2, a15 attached to a14:', okG)
out('   rank of the nineteen vectors:', rank(nodes), '(the lattice has rank 18)')
unimod = []
for drop in range(19):
    rest = [nodes[i] for i in range(19) if i != drop]
    d = det([[ip(a, b) for b in rest] for a in rest])
    if abs(d) == 1: unimod.append(names[drop])
out('   dropping one node leaves a basis of the whole lattice (Gram determinant -1 or +1) for:', ', '.join(unimod))
marks_left = [(2, chain[0]), (4, chain[1]), (6, chain[2]), (5, chain[3]), (4, chain[4]), (3, chain[5]), (2, chain[6]), (1, chain[7]), (3, alpha[1])]
marks_right = [(2, chain[16]), (4, chain[15]), (6, chain[14]), (5, chain[13]), (4, chain[12]), (3, chain[11]), (2, chain[10]), (1, chain[9]), (3, alpha[15])]
zL, zR = lin(marks_left), lin(marks_right)
kD = lin([(1, alpha[0]), (1, alpha[1]), (1, alpha[15]), (1, alpha[16])] + [(2, alpha[i]) for i in range(2, 15)])
def brief(v):
    c = Counter(v[:16])
    return '(' + ' '.join(f'{x}^{m}' for x, m in sorted(c.items())) + f'; n={v[16]}, w={v[17]})'
out('   affine E8 on the left (g1,a0,a2..a7 with a1): null vector z =', brief(zL), 'norm', ip(zL, zL))
out('   affine E8 on the right (a9..a14,a16,g2 with a15): null vector', brief(zR), '; equal to the left one:', zL == zR)
out('   affine D16 (a0..a16): null vector k =', brief(kD), 'norm', ip(kD, kD), '-> pure momentum')
out('   z has winding', zL[17], 'and k.z =', ip(kD, zL))

# ------------------------------------------------------------------ B
out('')
out('B. the E8 x E8 cusp: z-perp / z')
z = zL
D16 = []
for i, j in itertools.combinations(range(16), 2):
    for si in (1, -1):
        for sj in (1, -1):
            D16.append(plus(unit(i, si), unit(j, sj)))
classes = []
for p in D16:                      # w = 0
    s8 = sum(p[:8])
    if s8 % 2 == 0:
        v = vec(p, -F(s8, 2), 0)
        assert ip(v, z) == 0 and ip(v, v) == 2
        classes.append(v)
n_w0 = len(classes)
for bits in itertools.product((0, 1), repeat=8):       # w = 1, integer class
    if sum(bits) % 2 == 0:
        v = vec(list(bits) + [0] * 8, 1 - F(sum(bits), 2), 1)
        assert ip(v, z) == 0 and ip(v, v) == 2 and in_lattice(v)
        classes.append(v)
for signs in itertools.product((1, -1), repeat=8):     # w = 1, half-integer class
    if signs.count(-1) % 2 == 0:
        p = [H] * 8 + [F(s, 2) for s in signs]
        v = vec(p, 1 - F(sum(p[:8])) / 2, 1)
        assert ip(v, z) == 0 and ip(v, v) == 2 and in_lattice(v)
        classes.append(v)
out(f'   classes of norm 2: {n_w0} with w = 0 (two copies of the SO(16) roots), {len(classes) - n_w0} with w = 1 mod 2')
out('   root system of z-perp/z:', show(root_system(classes, null=z)), f'({len(classes)} roots)')
out('   so the SO(32) frame sees the E8 x E8 decompactification limit as a state of winding 2,')
out('   and the spinor roots of each E8 as states of odd winding')

# ------------------------------------------------------------------ C
out('')
out('C. exceptional groups from m labels and the circle: A = ((-1/2)^m, 0^(16-m)), R^2 = 2 - m/4 (alpha\' = 2)')
out('    m  R^2/alpha\'  gauge group                 zero winding            roots by |w| = 0,1,2')
series = {}
for m in range(0, 8):
    A = [-H] * m + [F(0)] * (16 - m)
    R2 = 2 - F(m, 4)
    rts = roots_at(A, R2)
    series[m] = rts
    byw = Counter(abs(v[17]) for v in rts)
    full = root_system(rts)
    zero = root_system([v for v in rts if v[17] == 0])
    out(f'    {m}  {str(R2 / 2):9s}  {show(full):26s}  {show(zero):22s}  {byw[0]}, {byw[1]}, {byw[2]}')
out('   (E_1 = SU(2), E_2 = SU(2) x U(1), E_3 = SU(3) x SU(2), E_4 = SU(5), E_5 = SO(10))')
out('   m = 8 is the cusp of B (R -> 0); m = 9 is m = 7 with the two blocks exchanged, by the lattice shift (1/2)^16')

# ------------------------------------------------------------------ D
out('')
out('D. E8 at the E8 x SO(18) point: A = ((-1/2)^7, 0^9), R^2/alpha\' = 1/8')
rts = series[7]
comps = components(rts)
E8 = next(c for c in comps if len(c) == 240)
SO18 = next(c for c in comps if len(c) == 144)
out('   components:', sorted(len(c) for c in comps), '; the 144 roots all have w = 0 and labels 8..16 only:',
    all(v[17] == 0 and all(x == 0 for x in v[:7]) for v in SO18))
byw = Counter(v[17] for v in E8)
out('   E8 by winding number:', {str(k): byw[k] for k in sorted(byw)}, '-> 14 + 64 + (84 roots + 8 Cartan) + 64 + 14')
w0 = [v for v in E8 if v[17] == 0]
out('   zero winding:', show(root_system(w0)), 'on labels 1..7:', all(all(x == 0 for x in v[7:16]) for v in w0))
w1 = [v for v in E8 if v[17] == 1]
ok01 = all(all(x in (0, 1) for x in v[:7]) and all(x == 0 for x in v[7:16]) for v in w1)
sizes = Counter(int(sum(v[:7])) for v in w1)
out('   winding 1: pi is a subset of the seven labels:', ok01, '; subset sizes:', dict(sorted(sizes.items())),
    '; momentum n = 1 - |S|/2:', all(v[16] == 1 - F(sum(v[:7]), 2) for v in w1))
out('   physical label charges p_L = pi + w A of the winding-1 states are (+-1/2)^7:',
    all(all(abs(v[a] - H) == H for a in range(7)) for v in w1), '(the spinor of SO(14))')
w2 = [v for v in E8 if v[17] == 2]
out('   winding 2: p_L = pi + 2A is plus or minus a single label:',
    sorted(Counter(tuple(sorted(Counter(v[a] - 1 for a in range(7)).items())) for v in w2).values()), '(the vector of SO(14))')

# colour content with seven labels = (u,c) x 3 colours + n
def singlet_number(M):
    """number of SU(3) singlets in a multiset M of weights (Dynkin labels): sum over the Weyl group of sgn * M(rho - w rho)."""
    rho = (1, 0, -1); tot = 0
    for perm, sgn in (((0, 1, 2), 1), ((1, 0, 2), -1), ((0, 2, 1), -1), ((2, 1, 0), -1), ((1, 2, 0), 1), ((2, 0, 1), 1)):
        d = tuple(rho[i] - rho[perm[i]] for i in range(3))
        tot += sgn * M.get((d[0] - d[1], d[1] - d[2]), 0)
    return tot
def colour_weight(v, colour_of):
    n = [0, 0, 0]
    for a, x in enumerate(v):
        c = colour_of(a)
        if c is not None: n[c] += x
    return (n[0] - n[1], n[1] - n[2])
def colour_singlets(vectors, colour_of, cartan=0):
    M = Counter(colour_weight(v, colour_of) for v in vectors)
    M[(0, 0)] += cartan
    return singlet_number(M)
col7 = lambda a: (a - 1) % 3 if 1 <= a < 7 else None  # label 1 = n, labels 2..7 = (u,c) x colour
stat = {}
for v in w1:
    key = (int(sum(v[1:7])), int(v[0]))
    stat.setdefault(key, []).append(tuple(int(x) for x in v[:7]))
out('   with label 1 = n and labels 2..7 = (u,c) x colour, the winding-1 states are:')
for (k, wn), vs in sorted(stat.items()):
    out(f'      {k} coloured labels{" + n" if wn else "    "}: {len(vs):2d} states, colour singlets: {colour_singlets(vs, col7)}')
out('      so three coloured labels come with n, and the colour singlets are 1 + 4 + 1')

def singlets_by_winding(rts, colour_of, rk):
    res = {}
    for w in sorted({v[17] for v in rts}):
        res[str(w)] = colour_singlets([v[:16] for v in rts if v[17] == w], colour_of, cartan=rk if w == 0 else 0)
    return res
sb8 = singlets_by_winding(E8, col7, 8)
out('   colour singlets in the 248 of E8 by winding (colour = the SO(32) colour on labels 2..7):', sb8, 'total', sum(sb8.values()))
E7 = next(c for c in components(series[6]) if len(c) == 126)
col6 = lambda a: a % 3 if a < 6 else None
sb7 = singlets_by_winding(E7, col6, 7)
out('   same for the 133 of E7 at the E7 x SO(20) point (labels 1..6 = (u,c) x colour):', sb7, 'total', sum(sb7.values()))

# lightest massive states at this point: norm 2, v.t = +-1/4 (the two signs are conjugate; -1/4 has winding +1)
A7 = [-H] * 7 + [F(0)] * 9
R7 = F(1, 4)
for sv in (F(-1, 4), F(1, 2)):
    vs = roots_at(A7, R7, sv)
    e8neutral = all(ip(v, r) == 0 for v in vs[:40] for r in E8[::16])
    out(f"   norm-2 vectors with v.t = {sv} (p_R^2 = {sv * sv / R7}, alpha' M^2 = {2 * sv * sv / R7}): {len(vs)}",
        '; windings', sorted({str(v[17]) for v in vs}), '; neutral under E8 (sample):', e8neutral)
    if sv == F(-1, 4):
        spin = all(all(abs(v[a]) == H for a in range(7, 16)) for v in vs)
        ks = Counter(sum(1 for a in range(7, 16) if v[a] > 0) for v in vs)
        out('      label charges on labels 8..16 are (+-1/2)^9, the spinor of SO(18):', spin,
            '; number of + signs:', dict(sorted(ks.items())))
        col9 = lambda a: a % 3
        for k in sorted(ks):
            sub = [tuple(1 if v[a] > 0 else 0 for a in range(7, 16)) for v in vs if sum(1 for a in range(7, 16) if v[a] > 0) == k]
            cs = colour_singlets(sub, col9)
            if cs: out(f'      {k} of the nine labels (d,s,b) x colour: {len(sub)} states, colour singlets: {cs}')

# the SU(9) inside E8: seven labels and two winding labels
minus_theta = add(alpha[7], zL, -1)
a8 = [g1, alpha[0], alpha[2], alpha[3], alpha[4], alpha[5], alpha[6], minus_theta]
E8set = set(E8)
okA8 = all(c in E8set for c in a8) and all(
    ip(a8[i], a8[j]) == (2 if i == j else -1 if abs(i - j) == 1 else 0) for i in range(8) for j in range(8))
out('   SU(9) chain g1, a0, a2..a6, -theta with -theta =', brief(minus_theta), ': roots of E8 forming A8:', okA8)
wchain = [c[17] for c in a8]
lab = [F(0)]
for x in wchain: lab.append(lab[-1] - x)
shift = sum(lab) / 9
lab = [x - shift for x in lab]
out('   winding carried by the nine labels of this SU(9) (traceless):', [str(x) for x in lab])
cls = {0: [], 3: [], 6: []}
for v in E8:
    d = [ip(v, c) for c in a8]
    cls[int(sum((i + 1) * d[i] for i in range(8)) % 9)].append(v)
out('   E8 roots by SU(9) class: adjoint', len(cls[0]), ', three-label', len(cls[3]), ', anti-three-label', len(cls[6]))
for name, key in (('adjoint (72 roots)', 0), ('84', 3), ('84bar', 6)):
    c = Counter(v[17] for v in cls[key])
    out(f'      {name}: by winding', {str(k): c[k] for k in sorted(c)})
z84 = [v for v in cls[3] if v[17] == 0]
shape = Counter()
for v in z84:
    if v[0] == 0: shape['e_i + e_j, both coloured' if sum(v[1:7]) == 2 else 'other'] += 1
    else: shape['e_i - e_n, i coloured' if (v[0] == -1 and sum(v[1:7]) == 1) else 'other'] += 1
out('      zero-winding part of the 84 in SO(32) labels:', dict(shape))
p84 = [v for v in cls[3] if v[17] == 1]
out('      winding-1 part of the 84, subset sizes (coloured labels, n):',
    dict(sorted(Counter((int(sum(v[1:7])), int(v[0])) for v in p84).items())))

# E8 in nine-label coordinates: positions of the winding functional relative to SU(9); centralizers
third = F(1, 3)
R9 = [tuple((1 if a == i else -1 if a == j else 0) for a in range(9)) for i in range(9) for j in range(9) if i != j]
L3 = [tuple((1 if a in s else 0) - third for a in range(9)) for s in itertools.combinations(range(9), 3)]
R9 = R9 + L3 + [tuple(-x for x in v) for v in L3]
dot9 = lambda x, y: sum(a * b for a, b in zip(x, y))
norm4 = set()
for r in R9:
    for s in R9:
        if dot9(r, s) == 0:
            norm4.add(tuple(a + b for a, b in zip(r, s)))
pat = Counter(tuple(sorted(Counter(v).values(), reverse=True)) for v in norm4)
out('   vectors of norm 4 in E8, written in nine labels:', len(norm4), '; by multiplicities of equal entries:', dict(pat))
out('   so the nine labels split by winding as 7+1+1, 4+4+1 or 5+2+2, and never in triples')
for rep, name in (((1, 1, 1, 1, 1, 1, 1, -2, -5), '7+1+1'), ((2, 2, 2, 2, -1, -1, -1, -1, -4), '4+4+1'), ((3, 3, -3, -3, 0, 0, 0, 0, 0), '5+2+2')):
    c = tuple(F(x, 3) for x in rep)
    assert c in norm4 or tuple(-x for x in c) in norm4
    hist = Counter(sum(c[a] for a in s) for s in itertools.combinations(range(9), 3))
    cent = [r for r in R9 if dot9(r, c) == 0]
    out(f'      pattern {name}: three-label states by winding', {str(k): hist[k] for k in sorted(hist)},
        '; E8 roots at zero winding:', len(cent))
seen = Counter()
for a in range(-6, 7):
    for b in range(-6, 7):
        d = -a - b
        if (a, b, d) == (0, 0, 0): continue
        c = (a,) * 3 + (b,) * 3 + (d,) * 3
        cent = [r for r in R9 if dot9(r, c) == 0]
        seen[show(root_system(cent, ipf=dot9))] += 1
out('   E8 roots orthogonal to a colour-blind direction (a,a,a,b,b,b,d,d,d), a+b+d = 0, all integers up to 6:', dict(seen))
# the SO(32) colour inside E8 in nine labels: labels 0-2 and 3-5 are two coloured flavours, 6,7,8 colourless
def proj9(r):
    a = sum(F(x) for x in r[0:3]) / 3; b = sum(F(x) for x in r[3:6]) / 3
    return (a,) * 3 + (b,) * 3 + tuple(F(x) for x in r[6:9])
groups = {}
for r in R9:
    groups.setdefault(proj9(r), Counter())[colour_weight(r, lambda a: a % 3 if a < 6 else None)] += 1
groups.setdefault((F(0),) * 9, Counter())[(0, 0)] += 8
sing = {mu: singlet_number(M) for mu, M in groups.items()}
sing = {mu: m for mu, m in sing.items() if m}
zero9 = (F(0),) * 9
nz = [mu for mu in sing if mu != zero9]
out('   E8 in nine labels with the SO(32) colour (two coloured flavours, three colourless labels):')
out('      colour singlets in the 248:', sum(sing.values()), '; with zero weight:', sing.get(zero9, 0),
    '; non-zero weights:', len(nz), 'each once:', all(sing[mu] == 1 for mu in nz))
for comp in components(nz, dot9):
    norms = Counter(str(dot9(mu, mu)) for mu in comp)
    kind = {(12, 2): 'G2', (6, 2): 'A2'}.get((len(comp), rank(comp)), '?')
    out(f'      component with {len(comp)} weights of rank {rank(comp)}, squared lengths {dict(norms)} -> {kind}')
long_g2 = [mu for mu in nz if dot9(mu, mu) == 2 and len({mu[0], mu[3], mu[6]}) > 1 and mu[6] == mu[7] == mu[8]]
out('      long roots of the G2: three-label states of one flavour or of the three colourless labels, and conjugates:', len(long_g2))
out('   colour lemma: roots of an E8 at zero winding embed in the roots of Gamma16, which are those of D16;')
out('   D16 has no subsystem of type E, so the winding functional on E8 is never colour-blind in 9 = 3 x 3')

# ------------------------------------------------------------------ E
out('')
out('E. maximal enhancements: delete two nodes, keep finite type; cross-check by enumerating roots at the point')
adj = {i: set() for i in range(19)}
for a, b in edges:
    adj[a].add(b); adj[b].add(a)
def dynkin_types(keep):
    keep = set(keep); seen = set(); types = []
    for s in sorted(keep):
        if s in seen: continue
        comp = []; stack = [s]; seen.add(s)
        while stack:
            x = stack.pop(); comp.append(x)
            for y in adj[x] & keep:
                if y not in seen: seen.add(y); stack.append(y)
        cs = set(comp)
        deg = {x: len(adj[x] & cs) for x in comp}
        br = [x for x in comp if deg[x] == 3]
        if max(deg.values()) > 3 or len(br) > 1: return None
        n = len(comp)
        if not br:
            types.append(f'A{n}'); continue
        arms = []
        for y in adj[br[0]] & cs:
            length = 1; prev, cur = br[0], y
            while True:
                nxt = [x for x in adj[cur] & cs if x != prev]
                if not nxt: break
                prev, cur = cur, nxt[0]; length += 1
            arms.append(length)
        arms.sort()
        if arms[0] == 1 and arms[1] == 1: types.append(f'D{n}')
        elif arms == [1, 2, 2]: types.append('E6')
        elif arms == [1, 2, 3]: types.append('E7')
        elif arms == [1, 2, 4]: types.append('E8')
        else: return None
    return sorted(types, key=order_key)
def fold(x):
    x = x - floor(x)
    return min(x, 1 - x)
def mirror(x):
    return 16 - x if x <= 16 else (18 if x == 17 else 17)
maximal = []
for i, j in itertools.combinations(range(19), 2):
    keep = [x for x in range(19) if x not in (i, j)]
    types = dynkin_types(keep)
    if types is None: continue
    rows = []
    for x in keep:
        r = nodes[x]
        rows.append(list(r[:16]) + [r[17], r[16]])       # v.t = pi.t_pi + n t_w + w t_n ; unknowns (t_pi, t_n, t_w)
    ns = nullspace(rows, 18)
    assert len(ns) == 1
    t = ns[0]
    assert t[17] != 0
    t = [x / t[17] for x in t]
    A = [-x for x in t[:16]]; E = -t[16]
    R2 = 2 * E - sum(a * a for a in A)
    assert R2 > 0
    rts = roots_at(A, R2)
    found = root_system(rts)
    zero = root_system([v for v in rts if v[17] == 0])
    wmax = max(abs(v[17]) for v in rts)
    folded = Counter(fold(a) for a in A)
    triples = sum(m // 3 for m in folded.values())
    mult = sorted(folded.values(), reverse=True)
    charge = mult[0] >= 15 or (len(mult) >= 2 and mult[0] >= 9 and mult[1] >= 6)
    pos = lambda x: x if x <= 16 else (2 if x == 17 else 14)
    maximal.append(dict(deleted=(names[i], names[j]), types=types, found=found, A=A, R2=R2, zero=zero,
                        wmax=wmax, folded=folded, colour=triples >= 5, nroots=len(rts), charge=charge,
                        left=min(pos(i), pos(j)),
                        key=min(tuple(sorted((i, j))), tuple(sorted((mirror(i), mirror(j)))))))
bykey = {}
for m in maximal:
    bykey.setdefault(m['key'], []).append(m)
out('   pairs of deleted nodes with finite type:', len(maximal), '; diagram and enumeration agree at every one:',
    all(m['types'] == m['found'] for m in maximal))
out('   the diagram has a left-right symmetry; up to it the number of maximal enhancements is', len(bykey),
    '(', sum(len(v) == 1 for v in bykey.values()), 'symmetric )')
out('   mirror partners have the same group, radius, zero-winding roots and colour test:',
    all(len({(tuple(m['types']), m['R2'], tuple(m['zero']), m['colour']) for m in v}) == 1 for v in bykey.values()))
out('   colour test: the sixteen Wilson-line values, folded to [0, 1/2], contain five disjoint triples of equal values')
out('   deleted    R^2/alpha\'  gauge group                      zero-winding roots              max|w|  folded Wilson line        colour')
def showfold(c):
    return ' '.join(f'{x}^{m}' for x, m in sorted(c.items()))
reps = sorted((max(v, key=lambda m: m['left']) for v in bykey.values()), key=lambda m: [order_key(t) for t in m['types']])
for m in reps:
    out(f"   {'/'.join(m['deleted']):9s}  {str(m['R2'] / 2):10s}  {show(m['types']):31s}  {show(m['zero']):30s}  {str(m['wmax']):6s}  {showfold(m['folded']):24s}  {'yes' if m['colour'] else 'no'}")
out('   colour-compatible points:', sum(m['colour'] for m in reps), 'of', len(reps))
out('   charge test: the Wilson line is constant on six labels (u,c) and on nine labels (d,s,b); n is free')
out('   points passing the charge test:', sum(m['charge'] for m in reps), '; all of them pass the colour test:',
    all(m['colour'] for m in reps if m['charge']))
for m in reps:
    if m['charge']:
        out(f"      {show(m['types']):26s} R^2/alpha' = {str(m['R2'] / 2):6s} labels by folded Wilson line: {showfold(m['folded'])}")
out('   colour-compatible points with an exceptional factor (Wilson line unfolded):')
for m in reps:
    if m['colour'] and any(t[0] == 'E' for t in m['types']):
        out(f"      {show(m['types']):28s} R^2/alpha' = {str(m['R2'] / 2):5s} A = {showfold(Counter(m['A']))}")

# ------------------------------------------------------------------ F
out('')
out('F. the SU(18) point')
su18 = next(m for m in maximal if m['types'] == ['A17'])
out('   deleted nodes:', su18['deleted'], '; Wilson line:', showfold(Counter(su18['A'])), '; R^2/alpha\' =', su18['R2'] / 2)
rts = roots_at(su18['A'], su18['R2'])
byw = Counter(v[17] for v in rts)
out('   roots by winding:', {str(k): byw[k] for k in sorted(byw)}, '; zero winding:', show(su18['zero']))
wch = [c[17] for c in chain]
lab = [F(0)]
for x in wch: lab.append(lab[-1] - x)
shift = sum(lab) / 18
out('   winding carried by the eighteen labels of SU(18) (traceless):', dict(Counter(str(x - shift) for x in lab)))
w1 = [v for v in rts if v[17] == 1]
shapes = Counter(tuple(sorted(Counter(a + b for a, b in zip(v[:16], su18['A'])).items())) for v in w1)
out('   winding-1 states, physical label charges p_L = pi + A:')
for s, c in sorted(shapes.items(), key=lambda kv: str(kv)):
    out(f'      {c} states with p_L entries ' + ' '.join(f'{x}^{m}' for x, m in s))
def cls18(v):
    return int(sum((i + 1) * ip(v, chain[i]) for i in range(17)) % 18)
out('   SU(18) class (label number mod 18) of the two deleted simple roots a1, a15:', cls18(alpha[1]), cls18(alpha[15]),
    '; of the seventeen chain roots:', sorted({cls18(c) for c in chain}))
out('   the nineteen roots span the lattice, so every state has label number divisible by 3: the group is SU(18)/Z3')
A18, R18 = su18['A'], su18['R2']
for sv in (F(1, 4), F(1, 2), F(3, 4)):
    vs = roots_at(A18, R18, sv)
    byc = Counter(cls18(v) for v in vs)
    out(f"   norm-2 vectors with v.t = {sv} (p_R^2 = {sv * sv / R18} in units alpha' = 2): {len(vs)}", '; by SU(18) class:', dict(sorted(byc.items())))
vs = [v for v in roots_at(A18, R18, F(1, 2)) if cls18(v) == 3]
byw = Counter(v[17] for v in vs)
out('   the three-label class at v.t = 1/2:', len(vs), 'states (Lambda^3 of 18 has 816); by winding:', {str(k): byw[k] for k in sorted(byw)})
z3 = [v for v in vs if v[17] == 0]
kinds = Counter(' '.join(f'{x}^{m}' for x, m in sorted(Counter(abs(x) for x in v[:16]).items())) for v in z3)
signs = Counter('same sign in the frame of the unbroken U(16)' if
                len({(x if 1 <= a <= 14 else -x) for a, x in enumerate(v[:16]) if x != 0}) == 1 else 'other' for v in z3)
out('   its zero-winding members are SO(32) two-label states: |pi| entries', dict(kinds), ';', dict(signs))
so34 = next(m for m in maximal if m['types'] == ['D17'])
out('   for comparison SO(34): deleted', so34['deleted'], ', Wilson line', showfold(Counter(so34['A'])), ', R^2/alpha\' =', so34['R2'] / 2,
    ', zero winding', show(so34['zero']))

# ------------------------------------------------------------------ G
out('')
out('G. other duality frames: null vectors k\' obtained from k = (0; 1, 0) by reflections in the nineteen roots')
def refl(v, r):
    c = ip(v, r)
    return tuple(a - c * b for a, b in zip(v, r))
NCUSP = 6000
seen = [kD]; seen_set = {kD}; head = 0
while head < len(seen) and len(seen) < NCUSP:
    v = seen[head]; head += 1
    for r in nodes:
        u = refl(v, r)
        if u not in seen_set:
            seen_set.add(u); seen.append(u)
            if len(seen) >= NCUSP: break
pats = Counter(); example = {}
for v in seen:
    c = Counter(abs(ip(v, r)) for r in E8)
    key = tuple(sorted((int(a), b) for a, b in c.items()))
    pats[key] += 1
    example.setdefault(key, v)
out(f'   {len(seen)} frames examined; each is of SO(32) type; "winding" in the frame k\' is v.k\'')
out('   frames   zero-winding part of E8    E8 roots by |winding|')
for key, m in sorted(pats.items(), key=lambda kv: -kv[1]):
    v = example[key]
    zero = root_system([r for r in E8 if ip(v, r) == 0])
    out(f'   {m:6d}   {show(zero):24s}   {dict(key)}')
out('   SO(14) is the frame of parts C and D; with SU(8) eight of the nine labels of an SU(9) in E8 are')
out('   SO(32) labels of that frame and the ninth differs from them by three units of winding')
out('   no frame has all of E8 at zero winding, and none has a zero-winding part of type E (colour lemma)')

with open(os.path.join(OUTDIR, 'nine_dim_frames.txt'), 'w') as f:
    f.write('\n'.join(LINES) + '\n')
print('\n'.join(LINES))
