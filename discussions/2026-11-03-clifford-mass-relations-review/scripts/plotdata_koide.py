"""Data for the flexibility and Koide figures (Kritov v13 review). Writes plotdata.json."""
import json, math
from fractions import Fraction as Fr
from itertools import product
import mpmath as mp

mp.mp.dps = 40
AINV = mp.mpf('137.035999177'); U_AINV = mp.mpf('2.1e-8')
ME = mp.mpf('0.51099895069')
RMU, U_MU = mp.mpf('206.7682827'), mp.mpf('0.0000046')
MMU = RMU * ME
RTAU, U_TAU = mp.mpf('1776.93') / ME, mp.mpf('0.09') / ME
RP, U_PREF = mp.mpf('1836.152673426'), mp.mpf('0.000000032')
U_P = mp.sqrt(U_PREF**2 + (mp.mpf(27) / 2 * U_AINV)**2)
TWO3 = mp.mpf(2) / 3


def Q(rm, rt):
    return (1 + rm + rt) / (1 + mp.sqrt(rm) + mp.sqrt(rt))**2


def lep(lam=1, g=1, eta=1, ainv=AINV):
    k = mp.mpf(3) / 2 * ainv / lam
    G = 1 + 16 * g
    return k + eta * G / 14, G * (k - eta)


out = {}

# ---------------- Fig 1: one-sigma windows per knob (relative change) ----------
k0 = mp.mpf(3) / 2 * AINV
out["windows"] = [
    {"knob": "Radius factor λ", "muon": float(U_MU / k0), "tau": float(U_TAU / (17 * k0)), "proton": None},
    {"knob": "Structural weight g", "muon": float(U_MU / (mp.mpf(16) / 14)), "tau": float(U_TAU / (16 * (k0 - 1))), "proton": None},
    {"knob": "Calibration η", "muon": float(U_MU / (mp.mpf(17) / 14)), "tau": float(U_TAU / 17), "proton": None},
    {"knob": "Input α⁻¹", "muon": float(U_MU / (mp.mpf(3) / 2 * AINV)), "tau": float(U_TAU / (mp.mpf(51) / 2 * AINV)),
     "proton": float(U_PREF / (mp.mpf(27) / 2 * AINV))},
]
out["alpha_rel_unc"] = float(U_AINV / AINV)


# ---------------- Fig 2: parameter-plane slices --------------------------------
def solve(f, lo, hi, it=200):
    flo = f(lo)
    for _ in range(it):
        mid = (lo + hi) / 2
        fm = f(mid)
        if (fm > 0) == (flo > 0):
            lo, flo = mid, fm
        else:
            hi = mid
    return (lo + hi) / 2


planes = []
# (x-knob, y-knob, fixed) ; ranges in absolute deviation
specs = [
    ("lam", "eta", 1.5e-4, 0.03),
    ("g", "eta", 1.5e-4, 0.03),
    ("lam", "g", 1.5e-4, 1.5e-4),
]
for xk, yk, xr, yr in specs:
    xs = [(-1 + 2 * i / 60) * xr for i in range(61)]
    curves = {}

    def ev(dx, dy):
        p = {"lam": 1, "g": 1, "eta": 1}
        p[xk] += dx; p[yk] += dy
        return lep(p["lam"], p["g"], p["eta"])

    for name, fun, target in [
        ("mu_lo", lambda r: r[0], RMU - U_MU), ("mu_c", lambda r: r[0], RMU), ("mu_hi", lambda r: r[0], RMU + U_MU),
        ("tau_lo", lambda r: r[1], RTAU - U_TAU), ("tau_c", lambda r: r[1], RTAU), ("tau_hi", lambda r: r[1], RTAU + U_TAU),
        ("koide", lambda r: Q(*r) - TWO3, 0)]:
        pts = []
        for dx in xs:
            f = lambda dy: fun(ev(dx, dy)) - target
            a, b = mp.mpf(-50) * yr, mp.mpf(50) * yr
            if (f(a) > 0) == (f(b) > 0):
                pts.append(None); continue
            pts.append(float(solve(f, a, b, 120)))
        curves[name] = pts
    # Koide value at the paper point and pulls along the plane axes
    planes.append({"x": xk, "y": yk, "xr": xr, "yr": yr, "xs": xs, "curves": curves})
out["planes"] = planes

# ---------------- Fig 3: lepton family result space ----------------------------
rules = {
    "R1": lambda g, d, e: (e * Fr(g, d), -e * g),
    "R2": lambda g, d, e: (e, e),
    "R3": lambda g, d, e: (Fr(0), Fr(0)),
    "R4": lambda g, d, e: (e * Fr(g, d), -e * g + e * Fr(g, d)),
    "R5": lambda g, d, e: (e * Fr(g - 1, d), -e * (g - 1)),
}
rulename = {"R1": "(+g/d, −g)", "R2": "Barut (+η, +η)", "R3": "no offset", "R4": "(+g/d, −g+g/d)", "R5": "(+(g−1)/d, −(g−1))"}
seen = {}
for c, n, tn, dsel, eta, rk in product([Fr(1, 2), Fr(1), Fr(3, 2), Fr(2), Fr(5, 2), Fr(3)], [2, 4, 8],
                                       ["1+n²", "1+n", "2"], ["n²−2", "n²−1", "n²", "3"], [Fr(1, 2), Fr(1), Fr(2)], rules):
    g = {"1+n²": 1 + n * n, "1+n": 1 + n, "2": 2}[tn]
    d = {"n²−2": n * n - 2, "n²−1": n * n - 1, "n²": n * n, "3": 3}[dsel]
    om, ot = rules[rk](g, d, eta)
    k = mp.mpf(c.numerator) / c.denominator * AINV
    rm = k + mp.mpf(om.numerator) / om.denominator
    rt = g * k + mp.mpf(ot.numerator) / ot.denominator
    zm, zt = float(abs(rm - RMU) / U_MU), float(abs(rt - RTAU) / U_TAU)
    key = (round(zm, 3), round(zt, 3))
    lab = f"c={c}, dim S={n}, g_τ={g}, d={d}, η={eta}, rule {rulename[rk]}"
    if key not in seen:
        seen[key] = {"zm": zm, "zt": zt, "n": 0, "ex": lab, "paper": False}
    seen[key]["n"] += 1
    if c == Fr(3, 2) and n == 4 and g == 17 and d == 14 and eta == 1 and rk == "R1":
        seen[key]["paper"] = True; seen[key]["ex"] = lab
out["lepton_family"] = list(seen.values())
out["lepton_family_size"] = sum(v["n"] for v in seen.values())

# proton family
forms = {
    "1 − α²/(1−α)": lambda a: 1 - a**2 / (1 - a), "1 − α²": lambda a: 1 - a**2,
    "1 − α²/(1+α)": lambda a: 1 - a**2 / (1 + a), "1/(1+α²)": lambda a: 1 / (1 + a**2),
    "√(1−2α²)": lambda a: mp.sqrt(1 - 2 * a**2), "1 − α²/2": lambda a: 1 - a**2 / 2,
    "1 − 2α²": lambda a: 1 - 2 * a**2, "1": lambda a: mp.mpf(1)}
a0 = 1 / AINV
ss = {"none": 0, "Compton": 1, "1/2": mp.mpf(1) / 2, "Bohr": a0, "2": 2}
ms = sorted({Fr(p, q) for p in range(1, 10) for q in range(1, 10)})
pz = []
for W, (sn, s), m, sg, (fn, f) in product([Fr(k, 2) for k in range(14, 23)], ss.items(), ms, [1, -1], forms.items()):
    rp = mp.mpf(W.numerator) / W.denominator * mp.mpf(3) / 2 * (AINV - s) - sg * mp.mpf(m.numerator) / m.denominator * f(a0)
    pz.append(float(abs(rp - RP) / U_P))
lz = []
for v in seen.values():
    lz += [max(v["zm"], v["zt"])] * v["n"]
thr = [10**(e / 4) for e in range(-8, 49)]
out["cumulative"] = {"thr": thr,
                     "lepton": [sum(1 for z in lz if z < t) for t in thr],
                     "proton": [sum(1 for z in pz if z < t) for t in thr],
                     "nl": len(lz), "np": len(pz)}

# ---------------- Fig 5: Koide vs alpha^-1 -------------------------------------
wide = []
for i in range(241):
    x = mp.mpf(10) ** (1 + 3 * i / 240)
    rm, rt = lep(ainv=x)
    wide.append([float(x), float(Q(rm, rt) / TWO3 - 1)])
zoom = []
for i in range(201):
    x = mp.mpf('136.95') + mp.mpf('0.2') * i / 200
    rm, rt = lep(ainv=x)
    zoom.append([float(x), float((Q(rm, rt) / TWO3 - 1) * 10**6)])
Qexp = Q(RMU, RTAU)
dQdt = (Q(RMU, RTAU + mp.mpf('1e-6')) - Q(RMU, RTAU - mp.mpf('1e-6'))) / mp.mpf('2e-6')
uQ = abs(dQdt) * U_TAU
xK = solve(lambda x: Q(*lep(ainv=x)) - TWO3, mp.mpf(100), mp.mpf(170))
out["koide_alpha"] = {"wide": wide, "zoom": zoom, "Qexp_rel": float((Qexp / TWO3 - 1) * 10**6),
                      "uQ_rel": float(uQ / TWO3 * 10**6), "xK": float(xK), "xC": float(AINV),
                      "Qmodel_rel": float((Q(*lep()) / TWO3 - 1) * 10**6),
                      "Qinf_rel": float((mp.mpf(18) / (1 + mp.sqrt(17))**2) / TWO3 - 1)}

# ---------------- Fig 6: Koide-exact weight G vs alpha^-1 -----------------------
def lepG(G, ainv):
    k = mp.mpf(3) / 2 * ainv
    return k + G / 14, G * (k - 1)


gk = []
for i in range(121):
    x = mp.mpf(10) ** (1 + 4 * i / 120)
    roots = []
    grid = [mp.mpf(2) + j * mp.mpf('0.05') for j in range(800)]
    vals = [Q(*lepG(G, x)) - TWO3 for G in grid]
    for j in range(len(grid) - 1):
        if (vals[j] > 0) != (vals[j + 1] > 0):
            roots.append(float(solve(lambda G: Q(*lepG(G, x)) - TWO3, grid[j], grid[j + 1], 80)))
    gk.append([float(x), roots])
GK_phys = [r for r in gk if True]
out["koide_G"] = {"curve": gk, "Ginf": float(7 + 4 * mp.sqrt(3))}

# ---------------- Koide-exact points nearest the paper ---------------------------
near = {}
for name, f, span in [("lam", lambda d: Q(*lep(lam=1 + d)) - TWO3, 1e-3), ("g", lambda d: Q(*lep(g=1 + d)) - TWO3, 1e-3),
                      ("eta", lambda d: Q(*lep(eta=1 + d)) - TWO3, 0.5), ("ainv", lambda d: Q(*lep(ainv=AINV + d)) - TWO3, 1)]:
    d = solve(f, mp.mpf(-span), mp.mpf(span), 200)
    p = {"lam": 1, "g": 1, "eta": 1, "ainv": AINV}
    p[name] = p[name] + d
    rm, rt = lep(p["lam"], p["g"], p["eta"], p["ainv"])
    near[name] = {"delta": float(d), "zmu": float((rm - RMU) / U_MU), "ztau": float((rt - RTAU) / U_TAU)}
# muon held fixed: move g and eta together along the muon line
def along(dg):
    # eta chosen so rho_mu stays at the paper value
    G = 1 + 16 * (1 + dg)
    eta = (lep()[0] - k0) * 14 / G
    return lep(g=1 + dg, eta=eta), eta
dg = solve(lambda d: Q(*along(d)[0]) - TWO3, mp.mpf(-1e-2), mp.mpf(1e-2), 200)
(rm, rt), eta = along(dg)
near["g_eta_muon_fixed"] = {"dg": float(dg), "deta": float(eta - 1), "ztau": float((rt - RTAU) / U_TAU),
                            "mtau": float(rt * ME)}
mtauK = solve(lambda r: Q(RMU, r) - TWO3, mp.mpf(3400), mp.mpf(3550)) * ME
near["koide_mtau_MeV"] = float(mtauK)
near["model_mtau_MeV"] = float(lep()[1] * ME)
th = mp.acos(1 / mp.sqrt(3 * Q(*lep())))
near["theta_model_deg"] = float(th * 180 / mp.pi)
near["theta_exp_deg"] = float(mp.acos(1 / mp.sqrt(3 * Qexp)) * 180 / mp.pi)
out["near"] = near

json.dump(out, open("plotdata.json", "w"))
print(json.dumps({k: out[k] for k in ["windows", "alpha_rel_unc", "near", "lepton_family_size"]}, indent=1))
print("koide alpha:", {k: v for k, v in out["koide_alpha"].items() if k not in ("wide", "zoom")})
print("unique lepton outputs:", len(out["lepton_family"]))
print("cumulative lepton at thr 1,10,100:", [out["cumulative"]["lepton"][out["cumulative"]["thr"].index(t)] for t in [1.0, 10.0, 100.0]],
      "proton:", [out["cumulative"]["proton"][out["cumulative"]["thr"].index(t)] for t in [1.0, 10.0, 100.0]])
for x, r in gk[::10]:
    print("alpha^-1 %10.2f  Koide-exact G roots %s" % (x, [round(v, 4) for v in r]))
pl = out["planes"][0]
print("plane0 koide first/mid/last:", pl["curves"]["koide"][0], pl["curves"]["koide"][30], pl["curves"]["koide"][-1])
print("plane0 mu_c mid:", pl["curves"]["mu_c"][30], "tau_c mid", pl["curves"]["tau_c"][30])
