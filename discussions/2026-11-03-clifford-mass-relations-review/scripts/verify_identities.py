"""Independent numerical check of the identities in
'Clifford Geometry and Mass Relations' (v13)."""
import itertools
import numpy as np
from scipy.linalg import expm, sqrtm
import mpmath as mp

np.set_printoptions(precision=6, suppress=True)
ok = lambda name, cond: print(f"[{'OK ' if cond else 'BAD'}] {name}")
cl = lambda a, b, tol=1e-10: np.allclose(a, b, atol=tol)

# ---------------- Appendix B gamma matrices ----------------
s1 = np.array([[0, 1], [1, 0]], complex)
s2 = np.array([[0, -1j], [1j, 0]], complex)
s3 = np.array([[1, 0], [0, -1]], complex)
I2 = np.eye(2)
g = [np.kron(s1, I2), np.kron(s2, I2), np.kron(s3, s1), np.kron(s3, s2)]
I4 = np.eye(4)
ok("(3.1) Clifford relations", all(cl(g[a] @ g[b] + g[b] @ g[a], 2 * (a == b) * I4)
                                    for a in range(4) for b in range(4)))
Sig = g[0] @ g[1] @ g[2] @ g[3]
ok("(3.1) Sigma Hermitian, square 1, traceless",
   cl(Sig, Sig.conj().T) and cl(Sig @ Sig, I4) and abs(np.trace(Sig)) < 1e-12)

# (B.2) Hermitian words
words = []
for r in range(5):
    for I in itertools.combinations(range(4), r):
        M = I4.copy()
        for a in I:
            M = M @ g[a]
        words.append((1j) ** (r * (r - 1) // 2) * M)
ok("(B.2) 16 words Hermitian, square to I4",
   len(words) == 16 and all(cl(W, W.conj().T) and cl(W @ W, I4) for W in words))
G = np.array([[np.trace(A @ B) for B in words] for A in words])
ok("(5.2) tr(Gamma_A Gamma_B) = 4 delta", cl(G, 4 * np.eye(16)))
Y = np.random.randn(4, 4) + 1j * np.random.randn(4, 4)
ok("(5.2) sum Gamma Y Gamma = 4 tr(Y) I4", cl(sum(W @ Y @ W for W in words), 4 * np.trace(Y) * I4))

# ---------------- W = End(S) as C^16 with orthonormal basis E_A = Gamma_A/2 ----------
E = [W / 2 for W in words]
def vec(X):   # coordinates in orthonormal basis
    return np.array([np.trace(B.conj().T @ X) for B in E])
def mat(v):
    return sum(c * B for c, B in zip(v, E))
def superop(f):
    return np.column_stack([vec(f(B)) for B in E])

Iw = np.eye(16)
Pe = superop(lambda X: np.trace(X) * I4 / 4)
Pt = superop(lambda X: np.trace(Sig @ X) * Sig / 4)
Pm = Iw - Pe - Pt
ok("(3.3) projectors", cl(Pe @ Pe, Pe) and cl(Pt @ Pt, Pt) and cl(Pe @ Pt, 0 * Iw)
   and np.isclose(np.trace(Pm).real, 14))
C = superop(lambda X: np.trace(Sig @ X) * I4)
Cd = C.conj().T
ok("(3.4) C^dag X = tr(X) Sigma", cl(Cd, superop(lambda X: np.trace(X) * Sig)))
ok("(3.4) C^2 = 0", cl(C @ C, 0 * Iw))
ok("(3.5) C^dag C = 16 P_tau, C C^dag = 16 P_e", cl(Cd @ C, 16 * Pt) and cl(C @ Cd, 16 * Pe))
s = vec(I4 / 2); p = vec(Sig / 2)
ok("(5.1) C p = 4 s", cl(C @ p, 4 * s))
Iact = Iw - Pe
dc = superop(lambda X: sum(W @ (W @ X - X @ W) - (W @ X - X @ W) @ W for W in words) / 32)
ok("(5.3) (1/32) sum [G,[G,X]] = I_act", cl(dc, Iact))
T = superop(lambda X: sum(W @ X @ Sig @ W @ Sig for W in words))
ok("(5.4) T = 16 P_tau", cl(T, 16 * Pt))
A = Iact + T
ok("(5.5) A = P_mu + 17 P_tau, Tr A = 31", cl(A, Pm + 17 * Pt) and np.isclose(np.trace(A).real, 31))
ok("(5.1) A = I_act (I + Delta) I_act", cl(A, Iact @ (Iw + Cd @ C + C @ Cd) @ Iact))
ev = np.round(np.linalg.eigvalsh(A), 8)
ok("(5.6) spec A = {0,1,17} mult (1,14,1)",
   sorted(set(ev)) == [0, 1, 17] and list(ev).count(1) == 14)

# ---------------- Appendix A ----------------
J = [-0.5j * g[a] @ g[b] for a in range(4) for b in range(a + 1, 4)]
ok("(A.1) J_ab^2 = I/4", all(cl(j @ j, I4 / 4) for j in J))
ok("(A.2) sum J^2 = 3/2 I4", cl(sum(j @ j for j in J), 1.5 * I4))
cas = superop(lambda X: sum(j @ (j @ X - X @ j) - (j @ X - X @ j) @ j for j in J))
evc = np.round(np.linalg.eigvalsh(cas), 8)
ok("App. A adjoint Casimir eigenvalues 0^2,3^8,4^6",
   list(evc).count(0) == 2 and list(evc).count(3) == 8 and list(evc).count(4) == 6)
# Spin(4) commutant dimension on W
gens = [superop(lambda X, j=j: j @ X - X @ j) for j in J]
Mbig = np.vstack([np.kron(Iw, gm) - np.kron(gm.T, Iw) for gm in gens])
null = 256 - np.linalg.matrix_rank(Mbig, tol=1e-8)
ok(f"App. A Spin(4) commutant dim = 10 (found {null})", null == 10)

# ---------------- Section 6: flows ----------------
D = Cd @ C
def Jret(Z):
    return np.trace(D @ Z) * Pm / 14
def Lgen(Z):
    return Jret(Z) - 0.5 * (D @ Z + Z @ D)
# superoperator of L on 16x16 matrices (column-major vec)
Lsup = np.zeros((256, 256), complex)
for k in range(256):
    Z = np.zeros(256, complex); Z[k] = 1
    Lsup[:, k] = Lgen(Z.reshape(16, 16, order='F')).reshape(-1, order='F')
for zeta in [0.01, 0.07, 0.3]:
    u = np.exp(-16 * zeta)
    Zu = (expm(zeta * Lsup) @ A.reshape(-1, order='F')).reshape(16, 16, order='F')
    ok(f"(6.8) Z_u at zeta={zeta}", cl(Zu, (1 + 17 / 14 * (1 - u)) * Pm + 17 * u * Pt))
    # Kraus (9.4) vs exp(zeta L) on a random Z
    hs = np.linalg.eigh(Pm)[1][:, -14:]          # orthonormal basis of harmonic sector
    K0 = Pe + Pm + np.sqrt(u) * Pt
    Ka = [np.sqrt((1 - u) / 14) * np.outer(hs[:, a], p.conj()) for a in range(14)]
    ok(f"(9.4) Kraus completeness zeta={zeta}",
       cl(K0.conj().T @ K0 + sum(k.conj().T @ k for k in Ka), Iw))
    Zr = np.random.randn(16, 16) + 1j * np.random.randn(16, 16)
    Tz = K0 @ Zr @ K0.conj().T + sum(k @ Zr @ k.conj().T for k in Ka)
    ok(f"(9.4) Kraus map = exp(zeta L) on random Z, zeta={zeta}",
       cl(Tz, (expm(zeta * Lsup) @ Zr.reshape(-1, order='F')).reshape(16, 16, order='F')))
    Zt = expm(-zeta * D / 2) @ A @ expm(-zeta * D / 2)
    ok(f"(6.9) tilde Z_c, zeta={zeta}", cl(Zt, Pm + 17 * u * Pt))
    Zc = 31 * Zt / np.trace(Zt)
    # derivative check of (6.10)
    h = 1e-6
    Ztp = expm(-(zeta + h) * D / 2) @ A @ expm(-(zeta + h) * D / 2); Zcp = 31 * Ztp / np.trace(Ztp)
    Ztm = expm(-(zeta - h) * D / 2) @ A @ expm(-(zeta - h) * D / 2); Zcm = 31 * Ztm / np.trace(Ztm)
    lhs = (Zcp - Zcm) / (2 * h)
    rhs = -0.5 * (D @ Zc + Zc @ D) + np.trace(D @ Zc) / 31 * Zc
    ok(f"(6.10) normalized flow ODE, zeta={zeta}", cl(lhs, rhs, 1e-5))
    # (9.9) variational amplitude
    Y0 = Pm + np.sqrt(17) * Pt
    Yz = np.sqrt(31) * expm(-zeta * A / 2) @ Y0 / np.linalg.norm(expm(-zeta * A / 2) @ Y0)
    ok(f"(9.9) Y Y^dag = Z_c, zeta={zeta}", cl(Yz @ Yz.conj().T, Zc))
    abar = np.trace(Yz.conj().T @ A @ Yz) / np.trace(Yz.conj().T @ Yz)
    Yp = np.sqrt(31) * expm(-(zeta + h) * A / 2) @ Y0 / np.linalg.norm(expm(-(zeta + h) * A / 2) @ Y0)
    Ym = np.sqrt(31) * expm(-(zeta - h) * A / 2) @ Y0 / np.linalg.norm(expm(-(zeta - h) * A / 2) @ Y0)
    ok(f"(9.11) Ydot = -(1/2)(A - abar I_act)Y, zeta={zeta}",
       cl((Yp - Ym) / (2 * h), -0.5 * (A - abar * Iact) @ Yz, 1e-5))
ok("(6.5) sum L_a^dag L_a = D",
   cl(sum((4 / np.sqrt(14) * np.outer(hs[:, a], p.conj())).conj().T @
          (4 / np.sqrt(14) * np.outer(hs[:, a], p.conj())) for a in range(14)), D))
Zs = 31 / 14 * Pm
B = Zs - A
ok("(6.11)-(6.13) B = 17(P_mu/14 - P_tau), Tr B = 0",
   cl(B, 17 * (Pm / 14 - Pt)) and abs(np.trace(B)) < 1e-10 and cl((A + B) @ Pt, 0 * Iw))

# covariance (9.5) with random U in G
from scipy.stats import unitary_group
Umu = unitary_group.rvs(14)
th_e, th_t = 0.37, 1.11
Ufull = np.exp(1j * th_e) * Pe + np.exp(1j * th_t) * Pt + hs @ Umu @ hs.conj().T
Un = np.zeros((15, 15), complex); Un[0, 0] = 1; Un[1:, 1:] = np.exp(1j * th_t) * Umu.conj()
zeta = 0.2; u = np.exp(-16 * zeta)
K0 = Pe + Pm + np.sqrt(u) * Pt
Ka = [np.sqrt((1 - u) / 14) * np.outer(hs[:, a], p.conj()) for a in range(14)]
V = np.vstack([np.kron(K, np.eye(1)) for K in [K0] + Ka])          # (15*16) x 16, record index outer
Vfull = np.zeros((16 * 15, 16), complex)
for r, K in enumerate([K0] + Ka):
    Vfull[r::15, :] = K        # ordering: W (x) E_n with E_n index fastest
ok("(9.5) V^dag V = I", cl(Vfull.conj().T @ Vfull, Iw))
ok("(9.5) V U = (U x U_n) V", cl(Vfull @ Ufull, np.kron(Ufull, Un) @ Vfull))

# ---------------- Section 9.1 collective profiles ----------------
Fe, Fm, Ft = Pe, Pm / np.sqrt(14), Pt
F = [Fe, Fm, Ft]
gram = np.array([[np.trace(a.conj().T @ b) for b in F] for a in F])
ok("(4.3) profiles orthonormal", cl(gram, np.eye(3)))
rho = np.random.randn(3, 3) + 1j * np.random.randn(3, 3); rho = rho @ rho.conj().T
Gam = lambda r: sum(r[i, j] * F[i] @ F[j].conj().T for i in range(3) for j in range(3))
Lc = np.zeros((3, 3)); Lc[1, 2] = 4
Dk = Lc.T @ Lc
LK = lambda r: Lc @ r @ Lc.T - 0.5 * (Dk @ r + r @ Dk)
ok("(9.6) Gamma(rho0) = A", cl(Gam(np.diag([0, 14, 17])), A))
ok("(9.7) Gamma(L_K rho) = L(Gamma rho)", cl(Gam(LK(rho)), Lgen(Gam(rho))))

# (9.8) collision step
th = 0.3
Hex = np.kron(np.outer([0, 1, 0], [0, 0, 1]), np.outer([0, 1], [1, 0]))
Hex = Hex + Hex.T
U = expm(-1j * th * Hex)
st = np.kron([0, 0, 1], [1, 0])
out = U @ st
ok("(9.8) survival cos^2", np.isclose(abs(out[np.argmax(st)]) ** 2, np.cos(th) ** 2))

# ---------------- Section 10 colour ----------------
lam = np.zeros((8, 3, 3), complex)
lam[0] = [[0, 1, 0], [1, 0, 0], [0, 0, 0]]
lam[1] = [[0, -1j, 0], [1j, 0, 0], [0, 0, 0]]
lam[2] = [[1, 0, 0], [0, -1, 0], [0, 0, 0]]
lam[3] = [[0, 0, 1], [0, 0, 0], [1, 0, 0]]
lam[4] = [[0, 0, -1j], [0, 0, 0], [1j, 0, 0]]
lam[5] = [[0, 0, 0], [0, 0, 1], [0, 1, 0]]
lam[6] = [[0, 0, 0], [0, 0, -1j], [0, 1j, 0]]
lam[7] = np.diag([1, 1, -2]) / np.sqrt(3)
t = lam / 2
CF = 4 / 3
I3 = np.eye(3); Ic = np.eye(27)
ok("(10.1) tr(t t)=delta/2, sum t t = CF I", cl(np.array([[np.trace(a @ b) for b in t] for a in t]), np.eye(8) / 2)
   and cl(sum(a @ a for a in t), CF * I3))
def Ti(a, i):
    ops = [I3, I3, I3]; ops[i] = t[a]
    return np.kron(np.kron(ops[0], ops[1]), ops[2])
q = [(Ti(a, 0) + Ti(a, 1) + Ti(a, 2)) / (3 * np.sqrt(CF)) for a in range(8)]
Lcol = sum(x @ x for x in q)
Kcol = sum((Ti(a, i) - Ti(a, j)) @ (Ti(a, i) - Ti(a, j)) for a in range(8)
           for i in range(3) for j in range(i + 1, 3)) / CF
ok("(10.3) K_c = 9(I - L_c)", cl(Kcol, 9 * (Ic - Lcol)))
sc = np.zeros(27)
for a, b, c in itertools.permutations(range(3)):
    sgn = np.linalg.det(np.eye(3)[[a, b, c]])
    sc[9 * a + 3 * b + c] = sgn
sc /= np.sqrt(6)
evL = np.linalg.eigvalsh(Lcol)
ok("(10.4) ker L_c one-dimensional, L_c s=0, K_c s=9s",
   np.sum(abs(evL) < 1e-10) == 1 and cl(Lcol @ sc, 0 * sc) and cl(Kcol @ sc, 9 * sc))
ok("(10.5) Tr(L_c sigma0) = 1/3", np.isclose(np.trace(Lcol).real / 27, 1 / 3))
print("     spectrum of L_c:", sorted(set(np.round(evL, 8))))
al = 1 / 137.035999177
fa = 1 - al ** 2 / (1 - al)
Mmat = np.array([[1, -al], [-al, 1 - al]])
ok("(10.8) minors 1, 1-a-a^2", np.isclose(np.linalg.det(Mmat), 1 - al - al ** 2))
Yr = [np.random.randn(27, 27) + 1j * np.random.randn(27, 27) for _ in range(8)]
R1 = sum(x @ x + (1 - al) * y.conj().T @ y - al * (x @ y + y.conj().T @ x) for x, y in zip(q, Yr))
R2 = fa * Lcol + (1 - al) * sum((y - al / (1 - al) * x).conj().T @ (y - al / (1 - al) * x) for x, y in zip(q, Yr))
ok("(10.9) completing the square", cl(R1, R2, 1e-8))
sigs = np.outer(sc, sc)
ok("(10.10) delta_c = -f_a/3", np.isclose(np.trace(fa * Lcol @ (sigs - Ic / 27)).real, -fa / 3))
# (10.14)
Ur = unitary_group.rvs(3)
ok("(10.14) U^{x3} s = det(U) s", cl(np.kron(np.kron(Ur, Ur), Ur) @ sc, np.linalg.det(Ur) * sc))

# ---------------- Numerics (high precision) ----------------
mp.mp.dps = 40
ainv = mp.mpf('137.035999177'); sa = mp.mpf('0.000000021')
me = mp.mpf('0.51099895069'); sme = mp.mpf('0.00000000016')
a = 1 / ainv
rmu = mp.mpf(3) / 2 * ainv + mp.mpf(17) / 14
rtau = mp.mpf(51) / 2 * ainv - 17
mtau = me * rtau
print("rho_mu      =", mp.nstr(rmu, 16), " z =", mp.nstr((rmu - mp.mpf('206.7682827')) / mp.mpf('0.0000046'), 6))
print("m_tau c^2   =", mp.nstr(mtau, 17), " zCOD =", mp.nstr((mtau - mp.mpf('1776.86')) / mp.mpf('0.12'), 6),
      " zPDG =", mp.nstr((mtau - mp.mpf('1776.93')) / mp.mpf('0.09'), 6))
print("m_mu c^2    =", mp.nstr(me * rmu, 16), " rho_tau =", mp.nstr(rtau, 17))
print("d rho_mu    =", mp.nstr(mp.mpf(3) / 2 * sa, 6))
print("d m_tau     = (alpha part)", mp.nstr(mp.mpf(51) / 2 * me * sa, 6), "+ (me part)", mp.nstr(rtau * sme, 6),
      "=", mp.nstr(mp.mpf(51) / 2 * me * sa + rtau * sme, 6))
QK = (1 + rmu + rtau) / (1 + mp.sqrt(rmu) + mp.sqrt(rtau)) ** 2
print("Q_K         =", mp.nstr(QK, 16), " Q/(2/3)-1 =", mp.nstr(QK / (mp.mpf(2) / 3) - 1, 12))
rp = mp.mpf(27) / 2 * ainv - mp.mpf(83) / 6 + a ** 2 / (3 * (1 - a))
print("rho_p       =", mp.nstr(rp, 17), " z =", mp.nstr((rp - mp.mpf('1836.152673426')) / mp.mpf('0.000000032'), 6))
print("m_p c^2     =", mp.nstr(rp * me, 16), " z =", mp.nstr((rp * me - mp.mpf('938.27208943')) / mp.mpf('0.00000029'), 6))
print("CODATA rho_p*me =", mp.nstr(mp.mpf('1836.152673426') * me, 16))
print("model d rho_p from alpha:", mp.nstr(mp.mpf(27) / 2 * sa, 6), " (CODATA u(rho_p) = 3.2e-8)")
print("model d m_p c^2 from me :", mp.nstr(rp * sme, 6), " from alpha:", mp.nstr(mp.mpf(27) / 2 * sa * me, 6),
      " (CODATA u = 2.9e-7)")
print("alpha^2/(3(1-alpha))    =", mp.nstr(a ** 2 / (3 * (1 - a)), 10))
eta_lo = 14 * (mp.mpf('206.7682827') - mp.mpf('0.0000046') - mp.mpf(3) / 2 * ainv) / 17
eta_hi = 14 * (mp.mpf('206.7682827') + mp.mpf('0.0000046') - mp.mpf(3) / 2 * ainv) / 17
print("eta interval:", mp.nstr(eta_lo, 10), mp.nstr(eta_hi, 10))
print("n-p threshold:", mp.mpf('1.29333251') - me, mp.mpf('1.29333251') + me)
print("14 m_mu + m_tau (in me):", mp.nstr(14 * rmu + rtau, 15), " 93/(2a):", mp.nstr(mp.mpf(93) / 2 * ainv, 15))
# inverse: alpha^-1 implied by the proton relation and the tau relation
f = lambda x: mp.mpf(27) / 2 * x - mp.mpf(83) / 6 + (1 / x) ** 2 / (3 * (1 - 1 / x)) - mp.mpf('1836.152673426')
xp = mp.findroot(f, ainv)
print("alpha^-1 implied by rho_p(CODATA):", mp.nstr(xp, 15), "+/-", mp.nstr(mp.mpf('0.000000032') / mp.mpf(13.5), 3),
      " CODATA:", ainv, "+/-", sa)
