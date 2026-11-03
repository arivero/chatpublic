"""Rational-grid scan and QED/SM renormalization-group check for Kritov v13.

Rational knobs (lambda, g, eta, d, c; proton W, s, m) take simple ratios only;
alpha and the renormalization scale mu vary continuously.

RG schemes
  on-shell : pole masses, effective coupling alpha_eff(mu) = alpha/(1 - Delta alpha(-mu^2)),
             exact one-loop leptonic vacuum polarization + quark loops with an effective
             light-quark mass calibrated to Delta alpha_had^(5)(M_Z^2) = 0.02783 (PDG 2024)
  MS-bar   : running masses at a common scale mu and alpha_hat(mu), one-loop + two-loop beta,
             decoupling at thresholds, light-quark threshold calibrated to
             alpha_hat^(5)(M_Z)^-1 = 127.930 (PDG 2024); above M_Z, one-loop SM running of
             alpha_em with lepton mass ratios frozen (flavour-universal gauge terms).
"""
import json, math
from fractions import Fraction as Fr
import mpmath as mp

mp.mp.dps = 30
AINV = mp.mpf('137.035999177'); A0 = 1 / AINV; U_AINV = mp.mpf('2.1e-8')
ME, MMU, MTAU = mp.mpf('0.51099895069e-3'), mp.mpf('0.1056583755'), mp.mpf('1.77693')
MP, MZ = mp.mpf('0.93827208943'), mp.mpf('91.1876')
RMU, U_MU = MMU / ME, mp.mpf('0.0000046')
RTAU, U_TAU = MTAU / ME, mp.mpf('0.09e-3') / ME
RP, U_PREF = mp.mpf('1836.152673426'), mp.mpf('0.000000032')
U_P = mp.sqrt(U_PREF**2 + (mp.mpf(27) / 2 * U_AINV)**2)
TWO3 = mp.mpf(2) / 3


def Qk(a, b, c):
    return (a + b + c) / (mp.sqrt(a) + mp.sqrt(b) + mp.sqrt(c))**2


out = {}

# =============================================================== rational scan
def lep(c=Fr(3, 2), lam=Fr(1), g=Fr(1), eta=Fr(1), d=14, ainv=AINV):
    k = mp.mpf(c.numerator) / c.denominator * ainv * lam.denominator / lam.numerator
    G = 1 + 16 * mp.mpf(g.numerator) / g.denominator
    e = mp.mpf(eta.numerator) / eta.denominator
    return k + e * G / d, G * (k - e)


def lep_pull(**kw):
    rm, rt = lep(**kw)
    return float(abs(rm - RMU) / U_MU), float(abs(rt - RTAU) / U_TAU), float(Qk(1, rm, rt) / TWO3 - 1)


def prot(W=Fr(9), s=Fr(1), m=Fr(1, 3), ainv=AINV):
    a = 1 / ainv
    Wv = mp.mpf(W.numerator) / W.denominator
    return Wv * mp.mpf(3) / 2 * (ainv - mp.mpf(s.numerator) / s.denominator) - mp.mpf(m.numerator) / m.denominator * (1 - a**2 / (1 - a))


def grid(lo, hi, qmax):
    return sorted({Fr(p, q) for q in range(1, qmax + 1) for p in range(0, int(hi * q) + 1) if lo <= Fr(p, q) <= hi})


scan = []
for name, key, values, fn in [
    ("Dirac level c", "c", grid(Fr(1, 2), Fr(4), 2), lambda v: lep_pull(c=v)),
    ("Radius factor λ", "lam", [v for v in grid(Fr(1, 4), Fr(3), 4) if v > 0], lambda v: lep_pull(lam=v)),
    ("Structural weight g", "g", [v for v in grid(Fr(1, 4), Fr(3), 4) if v > 0], lambda v: lep_pull(g=v)),
    ("Calibration η", "eta", grid(Fr(0), Fr(3), 4), lambda v: lep_pull(eta=v)),
    ("Redistribution dimension d", "d", [Fr(n) for n in range(1, 21)], lambda v: lep_pull(d=int(v))),
]:
    pts = []
    for v in values:
        zm, zt, kq = fn(v)
        pts.append({"v": float(v), "lab": str(v), "zm": zm, "zt": zt, "z": max(zm, zt), "koide": kq})
    scan.append({"name": name, "key": key, "kind": "lepton", "pts": pts})
for name, key, values, fn in [
    ("Colour weight W", "W", grid(Fr(7), Fr(11), 4), lambda v: prot(W=v)),
    ("Reference length s", "s", grid(Fr(0), Fr(2), 4), lambda v: prot(s=v)),
    ("Mean-charge term m", "m", [v for v in grid(Fr(0), Fr(1), 4) if v > 0], lambda v: prot(m=v)),
]:
    pts = []
    for v in values:
        z = float(abs(fn(v) - RP) / U_P)
        pts.append({"v": float(v), "lab": str(v), "z": z})
    scan.append({"name": name, "key": key, "kind": "proton", "pts": pts})
out["scan"] = scan
for s in scan:
    srt = sorted(s["pts"], key=lambda p: p["z"])
    print(f"{s['name']:<28} best {srt[0]['lab']:>5} z={srt[0]['z']:.3g}; next {srt[1]['lab']:>5} z={srt[1]['z']:.3g}")

# muon offsets eta*G/d over the rational grids, coverage of random targets
offs = set()
for g in [v for v in grid(Fr(1, 4), Fr(3), 4) if v > 0]:
    for eta in [v for v in grid(Fr(0), Fr(3), 4) if v > 0]:
        for d in range(1, 21):
            o = eta * (1 + 16 * g) / d
            if 0 < o <= 3:
                offs.add(o)
cover = len(offs) * 2 * float(U_MU) / 3
hits = [str(o) for o in offs if abs(float(o) - float(RMU - mp.mpf(3) / 2 * AINV)) < 2 * float(U_MU)]
print("rational muon offsets in (0,3]:", len(offs), " 1-sigma coverage:", cover, " hits:", hits)
out["offset_family"] = {"n": len(offs), "coverage1": cover, "hits": hits}

# Koide at neighbouring rational weights
kn = []
for g in [Fr(1, 2), Fr(3, 4), Fr(1), Fr(5, 4), Fr(3, 2)]:
    rm, rt = lep(g=g)
    kn.append({"g": str(g), "G": float(1 + 16 * g), "koide": float(Qk(1, rm, rt) / TWO3 - 1)})
out["koide_rational"] = kn
print("Koide at rational g:", kn)

# =============================================================== RG: on-shell
def dal_f(Q, m, nc_q2):
    """one-loop vacuum polarization Delta alpha(-Q^2) / alpha for a fermion of mass m."""
    Q, m = mp.mpf(Q), mp.mpf(m)
    y = 4 * m * m / (Q * Q)
    if y > mp.mpf(10)**6:
        br = (Q * Q / (m * m)) / 5
    else:
        s = mp.sqrt(1 + y)
        br = -mp.mpf(5) / 3 + y + (1 - y / 2) * s * mp.log((s + 1) / (s - 1))
    return nc_q2 / (3 * mp.pi) * br


LEPT = [(ME, 1), (MMU, 1), (MTAU, 1)]
# dispersive hadronic model: narrow vector resonances (mass, Gamma_ee in GeV) + perturbative continua
RES = [(mp.mpf('0.77526'), mp.mpf('7.04e-6')), (mp.mpf('0.78266'), mp.mpf('0.60e-6')), (mp.mpf('1.019461'), mp.mpf('1.27e-6')),
       (mp.mpf('3.096900'), mp.mpf('5.53e-6')), (mp.mpf('3.686097'), mp.mpf('2.33e-6')), (mp.mpf('9.46030'), mp.mpf('1.34e-6')),
       (mp.mpf('10.02326'), mp.mpf('0.612e-6')), (mp.mpf('10.3552'), mp.mpf('0.443e-6'))]


def dal_had(Q, s_uds, R_uds=mp.mpf('2.15'), R_c=mp.mpf('1.41'), sc=mp.mpf('3.9')**2, R_b=mp.mpf('0.347'), sb=mp.mpf('11.0')**2):
    Q2 = mp.mpf(Q)**2
    res = sum(3 * Q2 * gee / (A0 * m * (m * m + Q2)) for m, gee in RES)
    cont = A0 / (3 * mp.pi) * (R_uds * mp.log(1 + Q2 / s_uds) + R_c * mp.log(1 + Q2 / sc) + R_b * mp.log(1 + Q2 / sb))
    return res + cont


def calib_suds(target, R_uds=mp.mpf('2.15')):
    return mp.e**mp.findroot(lambda ls: dal_had(MZ, mp.e**ls, R_uds) - target, mp.log(mp.mpf('1.1')))


SUDS = calib_suds(mp.mpf('0.02783'))
print("uds continuum threshold sqrt(s) =", mp.sqrt(SUDS), "GeV;  Delta alpha_had at m_mu, m_tau, 10 GeV:",
      [mp.nstr(dal_had(q, SUDS), 4) for q in (MMU, MTAU, 10)])


def dal_lep(Q):
    return A0 * sum(dal_f(Q, m, w) for m, w in LEPT)


def aeff_inv(Q, s_uds=None, R_uds=mp.mpf('2.15')):
    s_uds = SUDS if s_uds is None else s_uds
    return AINV * (1 - dal_lep(Q) - dal_had(Q, s_uds, R_uds))


variants = []
for tgt, Ru in [('0.02761', '2.15'), ('0.02795', '2.15'), ('0.02783', '2.0'), ('0.02783', '2.3')]:
    Ru = mp.mpf(Ru)
    variants.append((calib_suds(mp.mpf(tgt), Ru), Ru))
print("Delta alpha_lep(M_Z) one loop:", dal_lep(MZ))

# =============================================================== RG: MS-bar
def lepton_path():
    th = [(ME, 1), (MMU, 2), (MTAU, 3)]
    table, a = [], A0
    for i, (m, n2) in enumerate(th):
        hi = th[i + 1][0] if i + 1 < len(th) else MZ
        steps = 80
        t0, t1 = mp.log(m), mp.log(hi)
        h = (t1 - t0) / steps
        f = lambda aa: 2 * aa * aa / (3 * mp.pi) * n2 + aa**3 / (2 * mp.pi**2) * n2
        t = t0
        table.append((t, a))
        for _ in range(steps):
            k1 = f(a); k2 = f(a + h * k1 / 2); k3 = f(a + h * k2 / 2); k4 = f(a + h * k3)
            a = a + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
            t += h
            table.append((t, a))
    return table


LTAB = lepton_path()


def interp(table, mu):
    t = mp.log(mu)
    if t <= table[0][0]:
        return table[0][1]
    for (t0, a0), (t1, a1) in zip(table, table[1:]):
        if t0 <= t <= t1:
            return a0 + (a1 - a0) * (t - t0) / (t1 - t0)
    return table[-1][1]


HAD_SCALE = (1 / interp(LTAB, MZ) - mp.mpf('127.930')) / (AINV * dal_had(MZ, SUDS))
print("MS-bar: hadronic rescaling factor at M_Z:", HAD_SCALE)


def ahat_inv(mu):
    return 1 / interp(LTAB, mu) - HAD_SCALE * AINV * dal_had(mu, SUDS)


TAB = [(mp.log(mu), 1 / ahat_inv(mu)) for mu in [ME * mp.e**(i * mp.log(MZ / ME) / 400) for i in range(401)]]
print("alpha_hat^-1 at m_mu, m_tau, M_Z:", [mp.nstr(1 / interp(TAB, q), 8) for q in (MMU, MTAU, MZ)])


def gamma_int(m_lo, m_hi):
    n = 120
    t0, t1 = mp.log(m_lo), mp.log(m_hi)
    h = (t1 - t0) / n
    s = 0
    for i in range(n + 1):
        w = 1 if i in (0, n) else (4 if i % 2 else 2)
        s += w * 3 * interp(TAB, mp.e**(t0 + i * h)) / (2 * mp.pi)
    return s * h / 3


def mbar_self(mpole):
    a = interp(TAB, mpole)
    return mpole / (1 + a / mp.pi)


MB = {"e": mbar_self(ME), "mu": mbar_self(MMU), "tau": mbar_self(MTAU)}
MCACHE = {}


def mbar(name, mu):
    key = (name, float(mu))
    if key not in MCACHE:
        MCACHE[key] = MB[name] * mp.e**(-gamma_int({"e": ME, "mu": MMU, "tau": MTAU}[name], mu))
    return MCACHE[key]


R_mu_ms = mbar("mu", MZ) / mbar("e", MZ)
R_tau_ms = mbar("tau", MZ) / mbar("e", MZ)
print("MS-bar m_e(M_Z) [MeV]:", mbar("e", MZ) * 1000, " R_mu:", R_mu_ms, " R_tau:", R_tau_ms,
      " Koide MS-bar:", Qk(mbar("e", MZ), mbar("mu", MZ), mbar("tau", MZ)) / TWO3 - 1)


def sm_ainv(mu):
    return mp.mpf('127.930') - mp.mpf(22) / 6 / (2 * mp.pi) * mp.log(mu / MZ)


def ms_ainv(mu):
    return 1 / interp(TAB, mu) if mu <= MZ else sm_ainv(mu)


# =============================================================== curves
mus = [mp.mpf(10)**(-4 + 0.1 * i) for i in range(0, int((16 + 4) / 0.1) + 1)]
IRval = {"mu": float(RMU - mp.mpf(3) / 2 * AINV), "tau": float(RTAU - mp.mpf(51) / 2 * AINV),
         "p": float(RP - mp.mpf(27) / 2 * AINV + mp.mpf(27) / 2)}
osc, msc = {k: [] for k in ["mu", "tau", "p", "koide", "ainv"]}, {k: [] for k in ["mu", "tau", "p", "koide", "ainv"]}
band = {k: [] for k in ["mu_lo", "mu_hi", "tau_lo", "tau_hi"]}
for mu in mus:
    x = float(mu)
    if mu <= MZ:
        ai = aeff_inv(mu)
        osc["ainv"].append([x, float(ai)])
        osc["mu"].append([x, float(RMU - mp.mpf(3) / 2 * ai)])
        osc["tau"].append([x, float(RTAU - mp.mpf(51) / 2 * ai)])
        osc["p"].append([x, float(RP - mp.mpf(27) / 2 * ai + mp.mpf(27) / 2)])
        osc["koide"].append([x, float((Qk(1, RMU, RTAU) / TWO3 - 1) * 10**6)])
        vals = [aeff_inv(mu, su, Ru) for su, Ru in variants]
        band["mu_lo"].append([x, float(RMU - mp.mpf(3) / 2 * max(vals))]); band["mu_hi"].append([x, float(RMU - mp.mpf(3) / 2 * min(vals))])
        band["tau_lo"].append([x, float(RTAU - mp.mpf(51) / 2 * max(vals))]); band["tau_hi"].append([x, float(RTAU - mp.mpf(51) / 2 * min(vals))])
    # MS-bar
    if mu >= ME:
        ai = ms_ainv(mu)
        msc["ainv"].append([x, float(ai)])
        me_mu = mbar("e", min(mu, MZ))
        msc["p"].append([x, float(MP / me_mu - mp.mpf(27) / 2 * ai + mp.mpf(27) / 2)])
        if mu >= MMU:
            r = mbar("mu", min(mu, MZ)) / me_mu
            msc["mu"].append([x, float(r - mp.mpf(3) / 2 * ai)])
        if mu >= MTAU:
            rt = mbar("tau", min(mu, MZ)) / me_mu
            msc["tau"].append([x, float(rt - mp.mpf(51) / 2 * ai)])
            msc["koide"].append([x, float((Qk(me_mu, mbar("mu", min(mu, MZ)), mbar("tau", min(mu, MZ))) / TWO3 - 1) * 10**6)])
out["rg"] = {"onshell": osc, "msbar": msc, "band": band, "IR": IRval, "paper": {"mu": 17 / 14, "tau": -17.0, "p": float(-mp.mpf(1) / 3 + A0**2 / (3 * (1 - A0)))},
             "suds": float(mp.sqrt(SUDS)), "had_scale": float(HAD_SCALE), "MZ": float(MZ), "mtau": float(MTAU), "mmu": float(MMU), "me": float(ME)}

# table of values at named scales
named = [("μ → 0", mp.mpf('1e-6')), ("m_e", ME), ("m_μ", MMU), ("m_τ", MTAU), ("10 GeV", mp.mpf(10)), ("M_Z", MZ), ("10¹⁶ GeV", mp.mpf('1e16'))]
rows = []
for lab, mu in named:
    row = {"scale": lab}
    if mu <= MZ:
        ai = aeff_inv(mu)
        row.update({"os_ainv": float(ai), "os_mu": float(RMU - 1.5 * ai), "os_tau": float(RTAU - 25.5 * ai), "os_p": float(RP - 13.5 * ai + 13.5)})
    if mu >= ME:
        ai = ms_ainv(mu)
        mm = min(mu, MZ)
        me_mu = mbar("e", mm)
        row["ms_ainv"] = float(ai)
        row["ms_p"] = float(MP / me_mu - 13.5 * ai + 13.5)
        if mu >= MMU:
            row["ms_mu"] = float(mbar("mu", mm) / me_mu - 1.5 * ai)
        if mu >= MTAU:
            row["ms_tau"] = float(mbar("tau", mm) / me_mu - 25.5 * ai)
            row["ms_koide"] = float((Qk(me_mu, mbar("mu", mm), mbar("tau", mm)) / TWO3 - 1) * 10**6)
    rows.append(row)
out["rg"]["table"] = rows
for r in rows:
    print(r)

# offset ratio o_tau/o_mu in on-shell scheme vs scale (manuscript rule needs -14)
ratio_pts = [(float(p[0]), p[1] / q[1]) for p, q in zip(osc["tau"], osc["mu"])]
for x, r in ratio_pts[::40]:
    print("mu=%.3g GeV  o_tau/o_mu = %.3f" % (x, r))
out["rg"]["ratio"] = [[x, r] for x, r in ratio_pts]
# scales where the on-shell muon offset reaches simple values
for target in [1.5, 2, 3, 17 / 14 + 0.01]:
    f = lambda lm: RMU - 1.5 * aeff_inv(mp.e**lm) - target
    try:
        lm = mp.findroot(f, mp.log(mp.mpf('0.01')))
        print("on-shell muon offset", target, "at mu =", mp.e**lm, "GeV")
    except Exception as e:
        print("no root", target, e)
json.dump(out, open("rgdata.json", "w"))
