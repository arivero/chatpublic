#!/usr/bin/env python3
"""'t Hooft twists and magnetic flux for the label space C^15 = C^5 (x) C^3.

Question (blackboard 013): can a flux background of the U(15) inside SO(32)
single out SU(3) colour, and what does it do to the multiplicities that the
sBootstrap reads as flavour?

Parts
  A. sanity checks of the construction (commutants of twist eaters, the
     noncommutative-torus relation); standard facts, not results;
  B. fractional-momentum classes of the meson-like (adjoint) fields;
  C. zero-mode counts on one two-torus from first Chern classes;
  D. a bounded scan of factorized fluxes on T^6 for three stacks
     (u: N=3, wrapping 2; d: N=3, wrapping 3; neutral: N=1).
Output: calculations/so32_gauge_scalars/flux_twist.txt
"""
import itertools, math, os
from fractions import Fraction as F
import numpy as np

OUTDIR = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                       '..', '..', 'calculations', 'so32_gauge_scalars'))
os.makedirs(OUTDIR, exist_ok=True)
L = []
def out(*a):
    L.append(' '.join(str(x) for x in a))

def clock_shift(n):
    w = np.exp(2j * np.pi / n)
    U = np.diag([w ** k for k in range(n)])
    V = np.roll(np.eye(n), 1, axis=0)
    return U, V                      # U V = w V U

def commutant_dim(mats, N):
    I = np.eye(N)
    A = np.vstack([np.kron(I, M) - np.kron(M.T, I) for M in mats])
    s = np.linalg.svd(A, compute_uv=False)
    return int(np.sum(s < 1e-9))

# ---------------------------------------------------------------- A
out('A. sanity checks')
dims = []
for m in range(15):
    g = math.gcd(m, 15); n = 15 // g
    if n == 1:
        dims.append((m, 225)); continue
    U, V = clock_shift(n)
    mats = [np.kron(U, np.eye(g)), np.kron(np.linalg.matrix_power(V, (m // g) % n), np.eye(g))]
    dims.append((m, commutant_dim(mats, 15)))
out('   U(15) twist eaters with flux m: (m, dim of commutant) =', dims)
out('   all equal gcd(m,15)^2:', all(d == math.gcd(m, 15) ** 2 for m, d in dims))
Q = np.diag([2 / 3] * 6 + [-1 / 3] * 9).astype(complex)
U5, V5 = clock_shift(5)
T = [np.kron(U5, np.eye(3)), np.kron(V5, np.eye(3))]
out('   irreducible five-fold twist: commutant dim', commutant_dim(T, 15),
    '; charge generator commutes:', all(np.allclose(Q @ t, t @ Q) for t in T))
U2, V2 = clock_shift(2); U3, V3 = clock_shift(3)
def block(A, B):
    Z = np.zeros((15, 15), dtype=complex); Z[:6, :6] = A; Z[6:, 6:] = B; return Z
B2 = [block(np.kron(U2, np.eye(3)), np.kron(U3, np.eye(3))),
      block(np.kron(V2, np.eye(3)), np.kron(V3, np.eye(3)))]
out('   block twist (2 | 3): commutant dim', commutant_dim(B2, 15),
    '; charge generator commutes:', all(np.allclose(Q @ t, t @ Q) for t in B2))
for n in (2, 3, 5):
    U, V = clock_shift(n); w = np.exp(2j * np.pi / n)
    for mp in range(1, n):
        if math.gcd(mp, n) != 1: continue
        s = pow(mp, -1, n)
        Z1, Z2 = V, np.linalg.matrix_power(U, (-s) % n)
        ok = (np.allclose(U @ Z1 @ U.conj().T, w * Z1)                       # x1 -> x1 + L1
              and np.allclose(np.linalg.matrix_power(V, mp) @ Z2 @ np.linalg.matrix_power(V, mp).conj().T, w * Z2)
              and np.allclose(Z1 @ Z2, w ** s * Z2 @ Z1))
        out(f'   n={n}, m\'={mp}: theta = {s}/{n}; generators Z1 ~ V, Z2 ~ U^-{s} consistent:', ok)

# ---------------------------------------------------------------- B
out('')
out('B. meson-like classes: lowest n^2 |p|^2 in units (2 pi hbar / (L c))^2, square torus')
def classes(n, mp):
    d = {}
    for a in range(n):
        for b in range(n):
            if (a, b) == (0, 0): continue
            p1 = min(abs(F(b, n) + k) for k in (-1, 0, 1))
            p2 = min(abs(F(-mp * a, n) + k) for k in range(-mp - 1, mp + 2))
            v = (p1 * p1 + p2 * p2) * n * n
            d[v] = d.get(v, 0) + 1
    return {str(k): v for k, v in sorted(d.items())}
for n, mp in ((5, 1), (5, 2), (2, 1), (3, 1), (3, 2)):
    out(f'   n={n}, m\'={mp}: {classes(n, mp)}')

# ---------------------------------------------------------------- C
out('')
out('C. zero modes on one two-torus (first Chern numbers)')
out('   one coloured stack, wrapping n, flux m\': antitriplets (n+1) m\', sextets (n-1) m\'')
for n in (2, 3, 5):
    for mp in (1, 2):
        if math.gcd(n, mp) == 1:
            out(f'      n={n} m\'={mp}: 3bar x {(n + 1) * mp}, 6 x {(n - 1) * mp}')
out('   two stacks u (n=2, m_u odd) and d (n=3, m_d not divisible by 3):')
out('      m_u m_d | uu 3bar, uu 6 | dd 3bar, dd 6 | ud diquark | u dbar meson')
hits = []
for mu in (1, -1, 3, -3, 5):
    for md in (1, -1, 2, -2, 4, -4, 5):
        row = (3 * mu, mu, 4 * md, 2 * md, 3 * mu + 2 * md, 3 * mu - 2 * md)
        if abs(mu) == 1 and abs(md) <= 2:
            out(f'      {mu:3d} {md:3d} | {row[0]:3d} {row[1]:3d} | {row[2]:3d} {row[3]:3d} | {row[4]:3d} | {row[5]:3d}')
        if (abs(row[0]), abs(row[4]), abs(row[2])) == (3, 6, 6):
            hits.append((mu, md))
out('   assignments with (uu, ud, dd) antitriplet counts (3, 6, 6):', hits, '-> would need m_d = 3/2')

# ---------------------------------------------------------------- D
out('')
out('D. factorized fluxes on T^6, |m| <= 4; stacks u: N=3, n=(2,1,1); d: N=3, n=(3,1,1) or (1,3,1); neutral: N=1')
R = range(-4, 5)
nu = (2, 1, 1)
cnt = tad = 0; ratio = []; both = []
for nd in ((3, 1, 1), (1, 3, 1)):
    for mu in itertools.product(R, repeat=3):
        if math.gcd(nu[0], mu[0]) != 1: continue
        for md in itertools.product(R, repeat=3):
            if any(n > 1 and math.gcd(n, m) != 1 for n, m in zip(nd, md)): continue
            Au = 12 * math.prod(mu); Ad = 16 * math.prod(md)
            Iud = math.prod(nu[i] * md[i] + mu[i] * nd[i] for i in range(3))
            if 0 in (Au, Ad, Iud): continue
            cnt += 1
            r = (Iud == 2 * Au and Ad == 2 * Au)
            if r: ratio.append((nd, mu, md))
            for mc in itertools.product(R, repeat=3):
                if all(3 * nu[i] * mu[j] * mu[k] + 3 * nd[i] * md[j] * md[k] + mc[j] * mc[k] == 0
                       for i, j, k in ((0, 1, 2), (1, 0, 2), (2, 0, 1))):
                    tad += 1
                    if r: both.append((nd, mu, md, mc))
out('   assignments with uu, ud, dd indices all non-zero:', cnt)
out('   of these, with (uu : ud : dd) = 1 : 2 : 2:', len(ratio))
out('   of these, tadpole-free for some neutral-brane flux in range:', tad)
out('   both:', len(both))

path = os.path.join(OUTDIR, 'flux_twist.txt')
open(path, 'w').write('\n'.join(L) + '\n')
print('wrote', path)
