"""Numbers quoted in ../unified_discussion.md that the audit does not already contain.

usage: python -I scale_links.py > scale_links_output.txt

Sections: common unit; shell-model magic numbers; trace-anomaly fraction; QCD share of the
W mass; running of alpha_s; infrared fixed points; Casimir scaling; unification relations;
Seiberg duality bookkeeping; Seiberg-Witten check; Higgs-mass frameworks; fermium half-lives.
"""
import math
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import audit as A  # noqa: E402  (constants, AME2020 masses)

V, U = A.V, A.U_MEV
MZ, MW, MT = 91.1880, 80.3692, 172.56
MH = [("PDG 2025", 125.20, 0.11), ("PDG 2026", 125.13, 0.11), ("LHCP 2026", 125.09, 0.07), ("CMS Nov 2026", 125.065, 0.088)]
D0 = 1864.84
ZETA3 = 1.2020569031595943
ALPHA_S_MZ = 0.1180


def head(t):
    print("\n" + "=" * 96 + "\n" + t + "\n" + "=" * 96)


# ---------------------------------------------------------------- running coupling
def beta_coeffs(n):
    b0 = 11 - 2 * n / 3
    b1 = 102 - 38 * n / 3
    b2 = 2857 / 2 - 5033 * n / 18 + 325 * n * n / 54
    b3 = (149753 / 6 + 3564 * ZETA3) - (1078361 / 162 + 6508 * ZETA3 / 27) * n \
        + (50065 / 162 + 6472 * ZETA3 / 81) * n * n + 1093 * n ** 3 / 729
    return b0, b1, b2, b3


def nf_at(mu):
    return 3 + (mu > 1.273) + (mu > 4.183) + (mu > MT)


def dalpha_dt(alpha, mu):
    a = alpha / (4 * math.pi)
    b0, b1, b2, b3 = beta_coeffs(nf_at(mu))
    return -2 * 4 * math.pi * (b0 * a ** 2 + b1 * a ** 3 + b2 * a ** 4 + b3 * a ** 5)


def alpha_s(mu, steps=4000):
    t0, t1 = math.log(MZ), math.log(mu)
    h = (t1 - t0) / steps
    al, t = ALPHA_S_MZ, t0
    for _ in range(steps):
        k1 = dalpha_dt(al, math.exp(t))
        k2 = dalpha_dt(al + h * k1 / 2, math.exp(t + h / 2))
        k3 = dalpha_dt(al + h * k2 / 2, math.exp(t + h / 2))
        k4 = dalpha_dt(al + h * k3, math.exp(t + h))
        al += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t += h
    return al


def mu_of_alpha(target):
    lo, hi = math.log(1.3), math.log(1e19)
    if not (alpha_s(math.exp(hi), 800) < target < alpha_s(math.exp(lo), 800)):
        return None
    for _ in range(50):
        mid = (lo + hi) / 2
        if alpha_s(math.exp(mid), 800) > target:
            lo = mid
        else:
            hi = mid
    return math.exp((lo + hi) / 2)


def smallest_positive_root(coeffs):
    """Smallest positive root of sum c_k a^k by scanning and bisection."""
    f = lambda x: sum(c * x ** k for k, c in enumerate(coeffs))
    x, step = 1e-6, 1e-5
    while x < 1.0:
        if f(x) * f(x + step) < 0:
            lo, hi = x, x + step
            for _ in range(80):
                mid = (lo + hi) / 2
                lo, hi = (mid, hi) if f(lo) * f(mid) > 0 else (lo, mid)
            return (lo + hi) / 2
        x += step
    return None


def su3_rep(p, q):
    dim = (p + 1) * (q + 1) * (p + q + 2) // 2
    c2 = (p * p + q * q + p * q + 3 * p + 3 * q) / 3
    return dim, c2, dim * c2 / 8


# ---------------------------------------------------------------- sections
def sec_unit():
    head("1. One unit for the three relations: v = 264 m*, M_Z + M_H = 232 m*, m(D0) = 2 m*")
    s132, s100 = A.m_atomic(50, 132) * 1000, A.m_atomic(50, 100) * 1000
    rows = [("v / 264", V * 1000 / 264), ("m(D0) / 2", D0 / 2)]
    rows += [(f"(M_Z + M_H)/232, {n}", (MZ + m) * 1000 / 232) for n, m, _ in MH]
    rows += [("u", U), ("M(132Sn)/132 atomic", s132 / 132), ("M(132Sn)/132 nuclear", A.m_nuclear(50, 132) * 1000 / 132),
             ("[M(100Sn)+M(132Sn)]/232 atomic", (s100 + s132) / 232), ("M(alpha)/4", A.M_ALPHA / 4),
             ("M(232Th)/232 atomic", A.m_atomic(90, 232) * 1000 / 232), ("free nucleon mean", (A.M_P + A.M_N) / 2)]
    for name, val in rows:
        print(f"  {name:34s} {val:9.3f} MeV   vs u: {100 * (val / U - 1):+7.3f} %   vs m(D0)/2: {100 * (val / (D0 / 2) - 1):+7.3f} %")
    print(f"  v / m(D0) = {V * 1000 / D0:.4f}  (132: {1e4 * (V * 1000 / D0 / 132 - 1):+.1f}e-4)")
    for n, m, unc in MH:
        r = (MZ + m) * 1000 / D0
        print(f"  (M_Z + M_H)/m(D0), {n:13s} = {r:8.3f} +- {unc * 1000 / D0:.3f}  (116: {1e4 * (r / 116 - 1):+.1f}e-4)   (M_Z+M_H)/v / (29/33) - 1 = {1e4 * ((MZ + m) / V * 33 / 29 - 1):+.2f}e-4")
    print(f"  free nucleon minus unit: v/264 -> {(A.M_P + A.M_N) / 2 - V * 1000 / 264:.2f} MeV ; m(D0)/2 -> {(A.M_P + A.M_N) / 2 - D0 / 2:.2f} MeV ; (B_alpha - B_d)/4 = {(28.2957 - 2.2246) / 4:.2f} MeV")
    print(f"  precision asked of lambda: delta M_H = 0.1 GeV <-> delta lambda / lambda = {2 * 0.1 / 125.2 * 100:.2f} %")


def sec_magic():
    head("2. Magic numbers: oscillator closures plus the intruder level")
    for n in range(0, 7):
        ho = (n + 1) * (n + 2) * (n + 3) // 3
        intr = 2 * (n + 2)
        print(f"  n = {n}: oscillator closure {ho:4d} ; intruder j = n + 3/2 holds {intr:2d} ; sum {ho + intr:4d} = (n+2)(n^2+4n+9)/3 = {(n + 2) * (n * n + 4 * n + 9) // 3}")
    print("  50 + 82 = 132 ; 50 + 50 = 100 ; 82 + 126 = 208 ; 2 (50 + 82) = 264 ; 100 + 132 = 232")


def sec_anomaly():
    head("3. Higgs-originated fraction of a nuclear mass (trace anomaly and heavy-quark decoupling)")
    print("  one loop: Lambda_3 = Lambda_6^(7/9) (m_c m_b m_t)^(2/27) ; exponent per heavy quark 2/27 = %.4f, total 2/9 = %.4f" % (2 / 27, 2 / 9))
    for s in (0.08, 0.10, 0.12):
        print(f"  sum of light sigma fractions {s:.2f}: f_N = {s + 2 / 9 * (1 - s):.3f} ; Higgs-originated part of M(132Sn) = {(s + 2 / 9 * (1 - s)) * A.m_atomic(50, 132):.1f} GeV")
    print("  exact supersymmetric analogue: Lambda_L^(3 N_c) = Lambda^(3 N_c - N_f) det m ; N_c = 3, N_f = 5: exponent per flavour 1/9 = %.4f ; pure-glue scale without supersymmetry: 2/33 = %.4f" % (1 / 9, 2 / 33))


def sec_qcd_ewsb():
    head("4. QCD share of electroweak symmetry breaking")
    fpi = 0.0923
    g = 2 * MW / V
    print(f"  f_pi / v = {fpi / V:.3e} ; delta M_W / M_W = f_pi^2 / (2 v^2) = {fpi ** 2 / (2 * V ** 2):.2e} ; M_W from QCD alone = g f_pi / 2 = {1000 * g * fpi / 2:.1f} MeV, M_Z = {1000 * g * fpi / 2 * MZ / MW:.1f} MeV ; v / f_pi = {V / fpi:.0f}")


def sec_running():
    head("5. alpha_s (four-loop running from alpha_s(M_Z) = 0.1180, continuous at m_c, m_b, m_t)")
    for mu in (1.5, 2, 5, 10, 30, 60, 70, MW, MZ, 125.2, MT, V, 500, 1000, 3000, 1e4, 1e8, 1e16):
        print(f"  mu = {mu:10.4g} GeV : alpha_s = {alpha_s(mu):.4f}")
    at = alpha_s(MT)
    yt_pr = math.sqrt(2 / 9 * 4 * math.pi * at)
    print(f"  Pendleton-Ross point y_t^2 = (2/9) g_3^2 at mu = m_t: y_t = {yt_pr:.3f}, m_t = {yt_pr * V / math.sqrt(2):.1f} GeV ; observed y_t(MSbar mass 162.5) = {math.sqrt(2) * 162.5 / V:.3f}, ratio y_t^2/g_3^2 = {(math.sqrt(2) * 162.5 / V) ** 2 / (4 * math.pi * at):.3f}")


def sec_fixed_points():
    head("6. Infrared fixed points alpha* of SU(3) with n_f massless triplets (MSbar) and the scale where the measured alpha_s equals alpha*")
    for n in (12, 13, 14, 15, 16):
        b = beta_coeffs(n)
        vals = []
        for order in (2, 3, 4):
            r = smallest_positive_root(b[:order])
            vals.append(None if r is None else 4 * math.pi * r)
        mus = [None if v is None else mu_of_alpha(v) for v in vals]
        txt = "  ".join(f"{o}-loop {('%.4f' % v) if v else '  -   '} ({('%.3g GeV' % m) if m else 'outside 1.3 GeV..1e19'})" for o, v, m in zip((2, 3, 4), vals, mus))
        print(f"  n_f = {n}: {txt}")
    print("  two-loop fixed points with other colour content (n3 Dirac triplets, n6 Dirac sextets):")
    for n3, n6 in ((6, 2), (10, 1), (11, 1), (9, 1)):
        b0 = 11 - (4 / 3) * (0.5 * n3 + 2.5 * n6)
        b1 = 102 - n3 * 0.5 * (20 + 4 * 4 / 3) - n6 * 2.5 * (20 + 4 * 10 / 3)
        if b0 > 0 and b1 < 0:
            al = -4 * math.pi * b0 / b1
            m = mu_of_alpha(al)
            print(f"    ({n3}, {n6}): b0 = {b0:.3f}, b1 = {b1:.2f}, alpha* = {al:.4f} ({('%.3g GeV' % m) if m else 'outside range'})")
        else:
            print(f"    ({n3}, {n6}): b0 = {b0:.3f}, b1 = {b1:.2f}: no two-loop fixed point")


def sec_casimir():
    head("7. Casimir scaling: scale where alpha_s reaches the ladder critical value alpha_c(R) = pi / (3 C_2(R))")
    print("  rep (p,q)  dim   C_2     T(R)   C_2/C_2(3)  alpha_c   scale mu_R      b0 with one Dirac fermion / one complex scalar added to six flavours")
    for p, q in ((1, 0), (2, 0), (1, 1), (3, 0), (2, 1), (3, 1), (2, 2), (4, 0), (4, 1), (5, 0), (6, 0)):
        dim, c2, t = su3_rep(p, q)
        ac = math.pi / (3 * c2)
        m = mu_of_alpha(ac)
        print(f"  ({p},{q})     {dim:4d}  {c2:6.3f}  {t:6.2f}   {c2 / (4 / 3):6.2f}     {ac:.4f}   {('%9.3g GeV' % m) if m else '  below 1.3 GeV'}    {7 - 4 * t / 3:7.2f} / {7 - t / 3:6.2f}")
    b0 = 23 / 3
    print(f"  sensitivity for the (4,0) case: d ln mu_R / d ln alpha_c = -2 pi / (b0 alpha_s(mu_R)) = {-2 * math.pi / (b0 * math.pi / (3 * 28 / 3)):.1f}")


def sec_unification():
    head("8. Relations through a common ultraviolet coupling")
    a_em_inv, s2 = 127.95, 0.23122
    a2, a1 = a_em_inv * s2, 0.6 * a_em_inv * (1 - s2)
    for name, (b1, b2, b3) in (("Standard Model", (41 / 10, -19 / 6, -7)), ("MSSM", (33 / 5, 1, -3))):
        inv3 = -((b2 - b3) * a1 + (b3 - b1) * a2) / (b1 - b2)
        print(f"  {name:15s}: 1/alpha_1 = {a1:.2f}, 1/alpha_2 = {a2:.2f} -> one-loop 1/alpha_3(M_Z) = {inv3:.2f}, alpha_3 = {1 / inv3:.4f}")
    print(f"  shift of ln Lambda_5 per unit of 1/alpha_3: 2 pi / b0 = {2 * math.pi / (23 / 3):.3f} ; 0.19 % in v/m_N <-> delta(1/alpha_3) = {0.00187 / (2 * math.pi / (23 / 3) * 23 / 27):.4f} of {1 / ALPHA_S_MZ:.2f}")
    for lam in (0.34, 0.21):
        for mpl, tag in ((1.2209e19, "Planck mass"), (2.435e18, "reduced Planck mass")):
            print(f"  r = ln(M/v) / ln(M/Lambda) with Lambda = {lam} GeV, M = {tag}: {math.log(mpl / V) / math.log(mpl / lam):.4f}")


def sec_seiberg():
    head("9. Seiberg duality bookkeeping for N_c = 3")
    for nf in range(3, 10):
        nt = nf - 3
        if nf == 3:
            ph = "quantum-deformed moduli space"
        elif nf == 4:
            ph = "s-confinement"
        elif nf < 4.5:
            ph = "free magnetic"
        elif nf < 9:
            ph = "conformal window"
        else:
            ph = "infrared free electric"
        extra = f"dual group SU({nt}), b = {9 - nf}, b~ = {3 * nt - nf}, D(M) = {3 * nt / nf:.2f}" if nt >= 2 else "no dual gauge group"
        print(f"  N_f = {nf}: {ph:30s} {extra}")
    print("  matching: Lambda^(3N_c-N_f) Lambda~^(3N~_c-N_f) = (-1)^(N_f-N_c) mu^N_f ; mass m of one electric flavour <-> <q q~> = -mu m")


def sec_sw():
    head("10. Seiberg-Witten curve, SU(2) with one flavour: y^2 = x^3 - u x^2 + (m L^3/4) x - L^6/64")
    u, m, lam = 0.75, 0.75, 1.0
    c = (1.0, -u, m * lam ** 3 / 4, -lam ** 6 / 64)
    x0 = u / 3
    f = c[0] * x0 ** 3 + c[1] * x0 ** 2 + c[2] * x0 + c[3]
    f1 = 3 * c[0] * x0 ** 2 + 2 * c[1] * x0 + c[2]
    f2 = 6 * c[0] * x0 + 2 * c[1]
    print(f"  at m = 3L/4, u = 3L^2/4: f, f', f'' at x = u/3 = {f:.1e}, {f1:.1e}, {f2:.1e} (triple root: Argyres-Douglas point)")
    print("  pure SU(2): y^2 = (x^2 - u)^2 - L^4, singular at u = +L^2 and u = -L^2")


def sec_higgs():
    head("11. Frameworks that fix the Higgs mass, against the relations")
    crit = 129.6 + 2.0 * (172.60 - 173.34) - 0.5 * (ALPHA_S_MZ - 0.1184) / 0.0007
    print(f"  boundary of absolute stability (Buttazzo et al. 2013, eq. 64) with m_t = 172.60, alpha_s = 0.1180: M_H = {crit:.1f} GeV ; slope dM_H/d alpha_s = {-0.5 / 0.0007:.0f} GeV")
    print(f"  the R1 offset in alpha_s (3.9e-5) moves that M_H by {0.5 / 0.0007 * 3.9e-5 * 1000:.0f} MeV")
    print(f"  lambda = 1/8: M_H = v/2 = {V / 2:.3f} GeV ; observed lambda = {125.20 ** 2 / (2 * V ** 2):.4f} (PDG 2025), {125.065 ** 2 / (2 * V ** 2):.4f} (CMS Nov 2026)")
    print("  completions of the relations: 125.132, 125.187, 125.221, 125.243 GeV (audit section 7)")


def sec_fm():
    head("12. Fermium: spontaneous-fission partial half-lives T_SF = T_1/2 / b_SF (NUBASE2020)")
    data = [("252Fm", 25.39 * 3600, 0.0023e-2), ("254Fm", 3.240 * 3600, 0.0592e-2), ("256Fm", 157.1 * 60, 0.919),
            ("257Fm", 100.5 * 86400, 0.210e-2), ("258Fm", 370e-6, 1.0), ("259Fm", 1.5, 1.0)]
    prev = None
    for name, t, b in data:
        tsf = t / b
        print(f"  {name}: T_1/2 = {t:.4g} s, b_SF = {b:.3g}, T_SF = {tsf:.3g} s = {tsf / 3.156e7:.3g} y")
    tsf = {n: t / b for n, t, b in data}
    for a, b in (("254Fm", "256Fm"), ("256Fm", "258Fm"), ("257Fm", "258Fm")):
        r = tsf[a] / tsf[b]
        print(f"  T_SF({a}) / T_SF({b}) = {r:.2e} ; ln = {math.log(r):.1f} ; change of the WKB action = {math.log(r) / 2:.1f} hbar")


def main():
    for s in (sec_unit, sec_magic, sec_anomaly, sec_qcd_ewsb, sec_running, sec_fixed_points, sec_casimir,
              sec_unification, sec_seiberg, sec_sw, sec_higgs, sec_fm):
        s()


if __name__ == "__main__":
    main()
