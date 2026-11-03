"""Flexibility (GIGO) analysis of the lepton and proton relations in Kritov v13.

For each target ratio, enumerate the formulas obtainable by changing the discrete
choices of the construction, count how many match the data, and estimate how often
the same family would match a random target with the same uncertainty."""
from fractions import Fraction as Fr
from itertools import product
import random
import mpmath as mp

mp.mp.dps = 30
ainv = mp.mpf('137.035999177'); u_ainv = mp.mpf('2.1e-8')
a = 1 / ainv
me = mp.mpf('0.51099895069')
RMU, U_MU = mp.mpf('206.7682827'), mp.mpf('0.0000046')
RTAU, U_TAU = mp.mpf('1776.93') / me, mp.mpf('0.09') / me           # PDG 2026
RP, U_PREF = mp.mpf('1836.152673426'), mp.mpf('0.000000032')
U_P = mp.sqrt(U_PREF**2 + (mp.mpf(27) / 2 * u_ainv)**2)          # with alpha uncertainty


def coverage(values, lo, hi, half):
    """Fraction of [lo, hi] lying within +-half of some value (union of windows)."""
    iv = sorted((max(lo, v - half), min(hi, v + half)) for v in values if hi > v - half and v + half > lo)
    tot, cur_s, cur_e = mp.mpf(0), None, None
    for s, e in iv:
        if cur_e is None or s > cur_e:
            if cur_e is not None:
                tot += cur_e - cur_s
            cur_s, cur_e = s, e
        else:
            cur_e = max(cur_e, e)
    if cur_e is not None:
        tot += cur_e - cur_s
    return tot / (hi - lo)


print("=" * 78)
print("LEPTONS")
print("=" * 78)
kappa = mp.mpf(3) / 2 * ainv

# ---- 1. leading-term choices ------------------------------------------------
print("\n1. Leading coefficient c/alpha (sphere level x radius), muon target needs c =",
      mp.nstr(RMU * a, 6))
for c in [Fr(1, 2), Fr(1), Fr(3, 2), Fr(2), Fr(5, 2), Fr(3)]:
    print(f"   c = {str(c):>4}: c/alpha = {mp.nstr(c.numerator / mp.mpf(c.denominator) * ainv, 8):>12}  "
          f"offset needed = {mp.nstr(RMU - c.numerator / mp.mpf(c.denominator) * ainv, 6)}")
print("\n   tau weight needed rho_tau/kappa =", mp.nstr(RTAU / kappa, 6))
for n in [2, 4, 8]:
    for name, g in [("unnormalized trace, 1+n^2", 1 + n * n), ("trace/n, 1+n", 1 + n), ("trace/n^2, 2", 2)]:
        print(f"   dim S = {n}, {name:<26}: g_tau = {g:>3}  offset needed = {mp.nstr(RTAU - g * kappa, 6)}")

# ---- 2. offset rules for the muon given c = 3/2, g_tau = 17 --------------------
ints = [1, 2, 3, 4, 5, 6, 14, 15, 16, 17, 31]          # integers the carrier supplies
etas = [Fr(1, 2), Fr(1), Fr(2)]
mu_offsets = {}
for N, D, eta in product(ints, ints, etas):
    v = eta * Fr(N, D)
    if 0 < v <= 3:
        mu_offsets.setdefault(v, (N, D, eta))
vals = [kappa + mp.mpf(v.numerator) / v.denominator for v in mu_offsets]
hits = [(v, mu_offsets[v]) for v in mu_offsets
        if abs(kappa + mp.mpf(v.numerator) / v.denominator - RMU) <= 2 * U_MU]
cov1 = coverage(vals, kappa, kappa + 3, U_MU)
cov2 = coverage(vals, kappa, kappa + 3, 2 * U_MU)
print(f"\n2. Muon offset family eta*N/D, N,D in {ints}, eta in {{1/2,1,2}}, value in (0,3]:")
print(f"   distinct offsets: {len(mu_offsets)};   within 2 sigma of data: {[(str(v), m) for v, m in hits]}")
print(f"   chance a random offset in (0,3] is matched within 1 sigma: {mp.nstr(cov1, 3)}; within 2 sigma: {mp.nstr(cov2, 3)}")

# ---- 3. joint rule family: same rule for mu and tau ---------------------------
print("\n3. Joint rules (c, dim S, trace normalization, redistribution space d, calibration eta, rule):")
rules = {
    "R1 paper: (+eta g/d, -eta g)": lambda g, d, e: (e * Fr(g, d), -e * g),
    "R2 Barut: (+eta, +eta)": lambda g, d, e: (e, e),
    "R3 no offset": lambda g, d, e: (Fr(0), Fr(0)),
    "R4 (+eta g/d, -eta g + eta g/d)": lambda g, d, e: (e * Fr(g, d), -e * g + e * Fr(g, d)),
    "R5 (+eta (g-1)/d, -eta (g-1))": lambda g, d, e: (e * Fr(g - 1, d), -e * (g - 1)),
}
fam, fits = [], []
for c, n, tn, dsel, eta, (rname, rule) in product(
        [Fr(1, 2), Fr(1), Fr(3, 2), Fr(2), Fr(5, 2), Fr(3)], [2, 4, 8], ["1+n^2", "1+n", "2"],
        ["n^2-2", "n^2-1", "n^2", "3"], etas, rules.items()):
    g = {"1+n^2": 1 + n * n, "1+n": 1 + n, "2": 2}[tn]
    d = {"n^2-2": n * n - 2, "n^2-1": n * n - 1, "n^2": n * n, "3": 3}[dsel]
    om, ot = rule(g, d, eta)
    k = mp.mpf(c.numerator) / c.denominator * ainv
    rm = k + mp.mpf(om.numerator) / om.denominator
    rt = g * k + mp.mpf(ot.numerator) / ot.denominator
    fam.append((rm, rt))
    zm, zt = (rm - RMU) / U_MU, (rt - RTAU) / U_TAU
    if abs(zm) <= 2 and abs(zt) <= 2:
        fits.append((str(c), n, tn, dsel, str(eta), rname, float(zm), float(zt)))
print(f"   family size: {len(fam)} formulas;   fitting both within 2 sigma: {len(fits)}")
for f in fits:
    print("     ", f)
# random-target null: lepton ratios drawn uniformly, same absolute uncertainties
random.seed(1)
famset = sorted(set((round(float(m), 9), round(float(t), 6)) for m, t in fam))
ntrial, nhit_mu, nhit_both = 200000, 0, 0
import bisect
mus = sorted(m for m, t in famset)
for _ in range(ntrial):
    tm = random.uniform(150, 300); tt = random.uniform(2000, 5000)
    i = bisect.bisect_left(mus, tm - 2 * float(U_MU))
    ok_mu = False
    while i < len(mus) and mus[i] <= tm + 2 * float(U_MU):
        ok_mu = True; break
    if ok_mu:
        nhit_mu += 1
        if any(abs(m - tm) <= 2 * float(U_MU) and abs(t - tt) <= 2 * float(U_TAU) for m, t in famset):
            nhit_both += 1
print(f"   random targets (rho_mu in [150,300], rho_tau in [2000,5000]), {ntrial} draws:"
      f" muon matched {nhit_mu}, both matched {nhit_both}")
print(f"   analytic estimate, muon: {len(set(m for m, t in famset))} distinct values x 4 sigma / 150 ="
      f" {len(set(m for m, t in famset)) * 4 * float(U_MU) / 150:.2e}")

# ---- 4. continuous knobs of Sec. 11.1 -----------------------------------------
print("\n4. Continuous knobs (lambda, g, eta) of Eq. (11.1), derivatives at (1,1,1):")
print("   d rho_mu/d lambda =", mp.nstr(-kappa, 6), " d rho_mu/d g =", mp.nstr(mp.mpf(16) / 14, 4),
      " d rho_mu/d eta =", mp.nstr(mp.mpf(17) / 14, 6))
print("   d rho_tau/d lambda =", mp.nstr(-17 * kappa, 6), " d rho_tau/d g =", mp.nstr(16 * (kappa - 1), 6),
      " d rho_tau/d eta =", -17)
print("   1-sigma window in each knob alone (muon):  lambda +-", mp.nstr(U_MU / kappa, 3),
      " g +-", mp.nstr(U_MU / (mp.mpf(16) / 14), 3), " eta +-", mp.nstr(U_MU / (mp.mpf(17) / 14), 3))
print("   1-sigma window in each knob alone (tau):   lambda +-", mp.nstr(U_TAU / (17 * kappa), 3),
      " g +-", mp.nstr(U_TAU / (16 * (kappa - 1)), 3), " eta +-", mp.nstr(U_TAU / 17, 3))

# ---- 5. alpha scale and mass scheme --------------------------------------------
dal_mu = a / (3 * mp.pi) * (mp.log(RMU**2) - mp.mpf(5) / 3)
dal_tau = a / (3 * mp.pi) * (mp.log(RTAU**2) - mp.mpf(5) / 3) + a / (3 * mp.pi) * (mp.log((RTAU / RMU)**2) - mp.mpf(5) / 3)
print("\n5. alpha(0) -> alpha(m_mu): rho_mu shift", mp.nstr(-kappa * dal_mu, 4),
      "; alpha(0) -> alpha(m_tau) (e+mu loops): rho_tau shift", mp.nstr(-17 * kappa * dal_tau, 4))
print("   pole -> MSbar common-scale ratio: mu/e", mp.nstr(RMU * 3 * a / (2 * mp.pi) * mp.log(RMU), 4),
      "; tau/e", mp.nstr(RTAU * 3 * a / (2 * mp.pi) * mp.log(RTAU), 4))

print("\n" + "=" * 78)
print("PROTON")
print("=" * 78)
print("   u(rho_p) combined with alpha:", mp.nstr(U_P, 3), "(reference only:", mp.nstr(U_PREF, 2), ")")
print("   weight needed rho_p/kappa =", mp.nstr(RP / kappa, 6))
X = mp.mpf(27) / 2 * ainv - RP
print("   offset to explain after 27/(2 alpha):  -", mp.nstr(X, 10))
print("   after the Compton subtraction -27/2:  ", mp.nstr(-X + mp.mpf(27) / 2, 10), "(paper: -1/3 + O(alpha^2))")
print("   residual after -83/6:", mp.nstr(RP - (mp.mpf(27) / 2 * ainv - mp.mpf(83) / 6), 6),
      " = coefficient", mp.nstr((RP - (mp.mpf(27) / 2 * ainv - mp.mpf(83) / 6)) / a**2, 6), "x alpha^2,",
      " 1-sigma on coefficient:", mp.nstr(U_P / a**2, 3))

# screening forms with m = 1/3
print("\n6. Screening forms f(alpha) in delta_c = -f/3:")
forms = {
    "1 (no screening)": 1,
    "1 - alpha^2/(1-alpha)  [paper]": 1 - a**2 / (1 - a),
    "1 - alpha^2": 1 - a**2,
    "1 - alpha^2/(1+alpha)": 1 - a**2 / (1 + a),
    "1/(1+alpha^2)": 1 / (1 + a**2),
    "sqrt(1-2 alpha^2)": mp.sqrt(1 - 2 * a**2),
    "1 - alpha": 1 - a,
    "1 - alpha^2/2": 1 - a**2 / 2,
    "1 - 2 alpha^2": 1 - 2 * a**2,
}
base = mp.mpf(27) / 2 * ainv - mp.mpf(27) / 2
for name, f in forms.items():
    rp = base - f / 3
    print(f"   {name:<32} rho_p = {mp.nstr(rp, 14)}   z(ref only) = {mp.nstr((rp - RP) / U_PREF, 4):>9}"
          f"   z(with alpha) = {mp.nstr((rp - RP) / U_P, 3):>7}")

# proton family
print("\n7. Proton family rho_p = W (3/2)(1/alpha - s) - m f(alpha):")
Ws = [Fr(k, 2) for k in range(14, 23)]                     # 7 ... 11
ss = {"0": 0, "1 (Compton)": 1, "1/2": mp.mpf(1) / 2, "alpha (Bohr)": a, "2": 2}
ms = sorted({Fr(p, q) for p in range(1, 10) for q in range(1, 10)})
fvals = {k: v for k, v in forms.items() if k != "1 - alpha"}
pfam, phits = [], []
for W, (sn, s), m, sgn, (fn, f) in product(Ws, ss.items(), ms, [1, -1], fvals.items()):
    rp = W.numerator / mp.mpf(W.denominator) * mp.mpf(3) / 2 * (ainv - s) - sgn * m.numerator / mp.mpf(m.denominator) * f
    pfam.append(rp)
    if abs(rp - RP) <= 2 * U_P:
        phits.append((str(W), sn, ("-" if sgn > 0 else "+") + str(m), fn, float((rp - RP) / U_P)))
print(f"   family size {len(pfam)}; matching within 2 sigma (alpha included): {len(phits)}")
for h in phits:
    print("     ", h)
lo, hi = mp.mpf(1830), mp.mpf(1842)
print("   fraction of random targets in [1830,1842] matched within 1 sigma:", mp.nstr(coverage(pfam, lo, hi, U_P), 3),
      "; within 2 sigma:", mp.nstr(coverage(pfam, lo, hi, 2 * U_P), 3))
# same with the reference-only uncertainty the paper uses
print("   same with the reference-only uncertainty 3.2e-8, 1 sigma:", mp.nstr(coverage(pfam, lo, hi, U_PREF), 3))
# leading-order coincidence only: -83/6-type constants
consts = sorted({Fr(p, q) for q in range(1, 7) for p in range(0, 6 * 20)})
cv = [mp.mpf(c.numerator) / c.denominator for c in consts]
Xs = -X + 0
print("   chance that 27/(2a) - rho_p lies within |residual| = 1.79e-5 of a fraction with q<=6:",
      mp.nstr(coverage(cv, mp.mpf(13), mp.mpf(15), abs(RP - (mp.mpf(27) / 2 * ainv - mp.mpf(83) / 6))), 3))
