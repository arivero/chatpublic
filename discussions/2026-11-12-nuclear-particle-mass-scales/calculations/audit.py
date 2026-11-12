"""Numerical audit of the nuclear / particle mass-scale relations (see ../README.md).

usage: python -I audit.py [AME2020_CSV]        (default: ../data/ame2020_mass_table.csv)

Nothing is fitted. Inputs: AME2020 atomic masses (data/ame2020_mass_table.csv), CODATA 2018
constants, PDG summary tables of the editions named in the code. Output is written to
stdout; calculations/audit_output.txt holds a saved copy.
"""
import csv
import math
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
CSV_PATH = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE.parent / "data" / "ame2020_mass_table.csv"

# ------------------------------------------------------------------ constants
U_MEV = 931.49410242          # CODATA 2018 atomic mass unit (MeV)
U = U_MEV / 1000.0            # GeV
M_E = 0.51099895000           # MeV
M_P = 938.27208816            # MeV
M_N = 939.56542052            # MeV
M_ALPHA = 3727.3794066        # alpha-particle mass, CODATA 2018 (MeV)
M_DEUTERON = 1875.61294257    # MeV
G_F = 1.1663788e-5            # GeV^-2 (PDG)
V = (math.sqrt(2.0) * G_F) ** -0.5   # GeV, tree-level vev from G_F

# PDG summary tables, GeV (value, uncertainty); read from the PDF tables of each edition
PDG2025 = {"MZ": (91.1880, 0.0020), "MH": (125.20, 0.11), "MW": (80.3692, 0.0133), "MT": (172.56, 0.31)}
PDG2026 = {"MZ": (91.1879, 0.0020), "MH": (125.13, 0.11), "MW": (80.3625, 0.0077), "MT": (172.60, 0.27)}
GAMMA_Z = 2.4955              # GeV
D0 = (1864.84, 0.05)          # MeV, PDG 2025
DPLUS = (1869.66, 0.05)       # MeV, PDG 2025
H_EDITIONS = [                # (PDG edition, M_H, unc, M_Z) from the gauge/Higgs summary table of each edition
    ("2014", 125.7, 0.4, 91.1876), ("2016", 125.09, 0.24, 91.1876), ("2018", 125.18, 0.16, 91.1876),
    ("2020", 125.10, 0.14, 91.1876), ("2022", 125.25, 0.17, 91.1876), ("2024", 125.20, 0.11, 91.1880),
    ("2025", 125.20, 0.11, 91.1880), ("2026", 125.13, 0.11, 91.1879),
]
RATIO_2933 = 29.0 / 33.0


def load_ame(path):
    table = {}
    with open(path, newline="") as handle:
        for row in csv.DictReader(handle):
            table[(int(row["Z"]), int(row["A"]))] = {
                "sym": row["symbol"], "me": float(row["mass_excess_keV"]),
                "unc": float(row["mass_excess_unc_keV"]), "est": bool(int(row["estimated"]))}
    return table


AME = load_ame(CSV_PATH)


def m_atomic(z, a):
    """Atomic mass in GeV from the AME2020 mass excess."""
    return (a * U_MEV + AME[(z, a)]["me"] / 1000.0) / 1000.0


def be_electrons(z):
    """Total electron binding energy in GeV (Lunney, Pearson, Thibault, RMP 75, 1021 (2003))."""
    return (14.4381 * z ** 2.39 + 1.55468e-6 * z ** 5.35) * 1e-9


def m_nuclear(z, a):
    return m_atomic(z, a) - z * M_E / 1000.0 + be_electrons(z)


def mz_pole(mz_bw):
    return mz_bw / math.sqrt(1.0 + (GAMMA_Z / mz_bw) ** 2)


def head(text):
    print()
    print("=" * 100)
    print(text)
    print("=" * 100)


# ------------------------------------------------------------------ 1. inputs
def sec_inputs():
    head("1. Inputs")
    print(f"u = {U_MEV} MeV; electron mass = {M_E} MeV; v = (sqrt2 G_F)^-1/2 = {V:.5f} GeV (G_F = {G_F})")
    print(f"v / u = {V / U:.4f}   v/m_p = {V * 1000 / M_P:.3f}   v/m_N(mean) = {V * 1000 / ((M_P + M_N) / 2):.3f}")
    for tag, d in (("PDG 2025", PDG2025), ("PDG 2026", PDG2026)):
        print(f"{tag}: " + ", ".join(f"{k}={v[0]}+-{v[1]}" for k, v in d.items()) + " GeV")
    for z, a in [(50, 132), (50, 100), (82, 208), (90, 232), (40, 100), (2, 4)]:
        row = AME[(z, a)]
        flag = "estimated" if row["est"] else "experimental/derived"
        print(f"AME2020 {a}{row['sym']}: mass excess {row['me']:.3f} +- {row['unc']:.3f} keV ({flag}); "
              f"atomic {m_atomic(z, a):.6f} GeV, nuclear {m_nuclear(z, a):.6f} GeV")


# ------------------------------------------------------------------ 2. the brief
def sec_brief():
    head("2. Numbers quoted in the brief")
    mz, mh, mw, mt = (PDG2025[k][0] for k in ("MZ", "MH", "MW", "MT"))
    for kind, f in (("atomic", m_atomic), ("nuclear", m_nuclear)):
        s132, s100 = f(50, 132), f(50, 100)
        print(f"[{kind}] 2M(132Sn) = {2 * s132:.3f} GeV  v/(2M)-1 = {100 * (V / (2 * s132) - 1):+.3f} %   (v-2M = {1000 * (V - 2 * s132):.1f} MeV)")
        print(f"[{kind}] M(100Sn)+M(132Sn) = {s100 + s132:.3f} GeV   (MZ+MH)/(sum)-1 = {100 * ((mz + mh) / (s100 + s132) - 1):+.3f} %   diff = {1000 * (mz + mh - s100 - s132):.1f} MeV")
        print(f"[{kind}] MZ vs 100Sn: {100 * (mz / s100 - 1):+.2f} %   MH vs 132Sn: {100 * (mh / s132 - 1):+.2f} %")
    print("Mass-number units (GeV / u):  W = %.2f  Z = %.2f  H = %.2f  top = %.2f" % (mw / U, mz / U, mh / U, mt / U))
    pb = m_atomic(82, 208)
    print(f"208Pb atomic = {pb:.3f} GeV; top vs 208Pb = {100 * (mt / pb - 1):+.1f} %")
    print(f"v/(2u) = {V / (2 * U):.3f} ; 132Sn atomic mass = {m_atomic(50, 132) / U:.5f} u ; v/(2 M(132Sn)/132) = {V / (2 * m_atomic(50, 132) / 132):.3f} nucleons")
    print(f"M_H + M_Z in u = {(mh + mz) / U:.3f}   (M_H - M_Z)/u = {(mh - mz) / U:.3f}")
    print(f"M(132Sn)-M(100Sn) = {m_atomic(50, 132) - m_atomic(50, 100):.4f} GeV  vs  M_H-M_Z = {mh - mz:.4f} GeV  (ratio {(mh - mz) / (m_atomic(50, 132) - m_atomic(50, 100)):.3f})")
    print(f"offsets from the pair: M_H - v/2 = {mh - V / 2:.3f} GeV ; M(100Sn) - M_Z = {m_atomic(50, 100) - mz:.3f} GeV")
    print(f"M(232Th) atomic = {m_atomic(90, 232):.4f} GeV ; M_Z+M_H - M(232Th) = {1000 * (mz + mh - m_atomic(90, 232)):.1f} MeV ({100 * ((mz + mh) / m_atomic(90, 232) - 1):+.3f} %)")


def sec_granularity():
    head("2b. Offsets in units of u against the nucleon-number rounding limit of 0.5 u")
    mz, mh = PDG2025["MZ"][0], PDG2025["MH"][0]
    s100, s132 = m_atomic(50, 100), m_atomic(50, 132)
    items = [
        ("R1: v/2 - M(132Sn)", V / 2 - s132),
        ("R2: M_Z + M_H - M(100Sn) - M(132Sn)", mz + mh - s100 - s132),
        ("M_H - M(132Sn)", mh - s132),
        ("M_Z - M(100Sn)", mz - s100),
        ("charm (no integer freedom; scale only)", (2 * D0[0] - M_ALPHA) / 1000.0),
    ]
    for name, val in items:
        print(f"{name:40s} {val * 1000:9.1f} MeV = {val / U:+7.3f} u = {abs(val / U) / 0.5:5.2f} x the 0.5 u limit")
    print(f"0.5 u as a fraction of M_Z + M_H = {100 * 0.5 * U / (mz + mh):.3f} % ; of v/2 = {100 * 0.5 * U / (V / 2):.3f} % ; of M_H = {100 * 0.5 * U / mh:.3f} %")
    print(f"common unit: v/264 = {V / 264 * 1000:.2f} MeV ; (M_Z+M_H)/232 = {(mz + mh) / 232 * 1000:.2f} MeV ; u = {U_MEV:.2f} MeV ; M(132Sn)/132 = {s132 / 132 * 1000:.2f} MeV")


# ------------------------------------------------------------------ 3. conventions
def sec_conventions():
    head("3. Convention matrix: atomic/nuclear masses, Z mass definition, Higgs mass value")
    h_sets = [("PDG2025 125.20", 125.20), ("PDG2026 125.13", 125.13), ("LHC prelim 125.09", 125.09), ("CMS Nov26 125.065", 125.065)]
    print("R1 = v/(2M(132Sn)) - 1 ; R2 = (MZ+MH)/(M100+M132) - 1 ; ratio = (MZ+MH)/v ; 29/33 = %.6f" % RATIO_2933)
    for kind, f in (("atomic", m_atomic), ("nuclear", m_nuclear)):
        s132, s100 = f(50, 132), f(50, 100)
        print(f"-- {kind} masses: R1 = {100 * (V / (2 * s132) - 1):+.3f} %; nuclear ratio (M100+M132)/(2 M132) = {(s100 + s132) / (2 * s132):.6f} (29/33 {((s100 + s132) / (2 * s132) / RATIO_2933 - 1) * 1e6:+.1f} ppm)")
        for zname, mz in (("Z mass BW 91.1880", 91.1880), ("Z mass pole %.4f" % mz_pole(91.1880), mz_pole(91.1880))):
            cells = []
            for label, mh in h_sets:
                r2 = 100 * ((mz + mh) / (s100 + s132) - 1)
                cells.append(f"{label}: R2={r2:+.3f}%  ratio-29/33={((mz + mh) / V - RATIO_2933) * 1e4:+.2f}e-4")
            print(f"   {zname:22s} " + " | ".join(cells))
    for zname, mz in (("BW", 91.1880), ("pole", mz_pole(91.1880))):
        print(f"M_H implied by the exact rational: (29/33) v - M_Z({zname}) = {RATIO_2933 * V - mz:.4f} GeV")
    sigma = math.hypot(0.11, 0.002) / V
    print(f"statistical resolution of the ratio from M_H = +-0.11 GeV: sigma(ratio) = {sigma:.2e}; 2025 value is {((91.1880 + 125.20) / V - RATIO_2933) / sigma:+.2f} sigma from 29/33")
    print(f"2026 PDG: {((91.1879 + 125.13) / V - RATIO_2933) / sigma:+.2f} sigma ; LHC prelim 125.09+-0.07: {((91.1879 + 125.09) / V - RATIO_2933) / (math.hypot(0.07, 0.002) / V):+.2f} sigma")


# ------------------------------------------------------------------ 4. feedback A algebra
def sec_feedback_a():
    head("4. Algebra of the first feedback (tin pair relations)")
    s132, s100 = m_atomic(50, 132), m_atomic(50, 100)
    mz, mh = PDG2025["MZ"][0], PDG2025["MH"][0]
    print(f"v - 2M(132Sn) = {1000 * (V - 2 * s132):.2f} MeV (feedback: 458.68)")
    print(f"MZ+MH-M(100Sn)-M(132Sn) = {1000 * (mz + mh - s100 - s132):.2f} MeV (feedback: 414.69)")
    print(f"MH+MZ-v = {1000 * (mh + mz - V):.1f} MeV ; M(100Sn)-M(132Sn) = {1000 * (s100 - s132):.1f} MeV ; residual {1000 * (mh + mz - V - (s100 - s132)):.1f} MeV (feedback: -44)")
    print(f"M_H predicted = v - MZ + M(100Sn) - M(132Sn) = {V - mz + s100 - s132:.4f} GeV (feedback: 125.244)")
    print(f"M_H predicted by (29/33) v - MZ = {RATIO_2933 * V - mz:.4f} GeV (second feedback: 125.18694)")
    print("Candidate lobe pairs for A = 232 (atomic masses, AME2020); offsets m_H - M(heavy), m_Z - M(light) in GeV")
    for heavy, light in [((50, 132), (40, 100)), ((52, 134), (38, 98)), ((50, 134), (40, 98)), ((50, 132), (50, 100)), ((51, 132), (40, 100))]:
        mhv, mlt = m_atomic(*heavy), m_atomic(*light)
        print(f"  {heavy[1]}{AME[heavy]['sym']} + {light[1]}{AME[light]['sym']}: mH-M_heavy = {mh - mhv:+.3f}, mZ-M_light = {mz - mlt:+.3f}, sum offset = {mh + mz - mhv - mlt:+.3f} GeV, Z_tot = {heavy[0] + light[0]}")
    for kind, f in (("atomic", m_atomic), ("nuclear", m_nuclear)):
        q = f(90, 232) - f(50, 132) - f(40, 100)
        print(f"Q(232Th -> 132Sn + 100Zr) [{kind}] = {1000 * q:.2f} MeV")
    qn = m_nuclear(90, 232) - m_nuclear(50, 132) - m_nuclear(40, 100)
    mzp = mz_pole(91.1880)
    print(f"second feedback relation: MH + MZpole - M(232Th) = {1000 * (125.13 + mzp - m_nuclear(90, 232)):.1f} MeV vs Q = {1000 * qn:.1f} MeV (M_H = 125.13)")
    print(f"   the same difference with M_H = 125.20: {1000 * (125.20 + mzp - m_nuclear(90, 232)):.1f} MeV; the M_H uncertainty (110 MeV) is {110 / (1000 * qn) * 100:.0f} % of Q")


# ------------------------------------------------------------------ 5. charm
def sec_charm():
    head("5. Charm threshold and the alpha particle")
    two_d0 = 2 * D0[0]
    print(f"2 m(D0) = {two_d0:.2f} +- {2 * D0[1]:.2f} MeV ; M(alpha) = {M_ALPHA:.4f} MeV ; difference = {two_d0 - M_ALPHA:.3f} MeV = {100 * (two_d0 / M_ALPHA - 1):.4f} %  ({(two_d0 - M_ALPHA) / (2 * D0[1]):.1f} sigma of the D0 mass)")
    print(f"M(alpha)/2 = {M_ALPHA / 2:.3f} MeV ; m(D0) - M(alpha)/2 = {D0[0] - M_ALPHA / 2:+.3f} MeV")
    free4 = 2 * M_P + 2 * M_N
    print(f"4 free nucleons = {free4:.3f} MeV ; B(alpha) = {free4 - M_ALPHA:.3f} MeV ; 4N - 2m(D0) = {free4 - two_d0:.3f} MeV ; remainder = {two_d0 - M_ALPHA:.3f} MeV")
    print(f"charged threshold: 2 m(D+) = {2 * DPLUS[0]:.2f} ; minus M(alpha) = {2 * DPLUS[0] - M_ALPHA:.3f} MeV ; D+ - D0 = {DPLUS[0] - D0[0]:.2f} MeV")
    print(f"m(D0) vs deuteron: {D0[0] - M_DEUTERON:+.2f} MeV ({100 * (D0[0] / M_DEUTERON - 1):+.2f} %)")
    print(f"m(D0)/u = {D0[0] / U_MEV:.5f} ; v/m(D0) = {V * 1000 / D0[0]:.4f} ; 1/132 = {1 / 132:.7f} vs m(D0)/v = {D0[0] / (V * 1000):.7f}")
    print(f"4 M(132Sn)/M(alpha) = {4 * m_atomic(50, 132) * 1000 / M_ALPHA:.3f} (v/m(D0) implied by R1 and R3 alone; observed {V * 1000 / D0[0]:.3f})")
    mc = 1.2730
    print(f"MSbar m_c = {mc} GeV -> y_c = sqrt2 m_c / v = {math.sqrt(2) * mc / V:.5f} ; shift of m_c that moves 2 m(D0) by the 2.30 MeV remainder: {2.301 / 2:.3f} MeV = {100 * 1.1505e-3 / mc:.3f} % of m_c")


# ------------------------------------------------------------------ 6. sensitivity to alpha_s
def sec_alpha_s():
    head("6. What the 0.19 % of R1 means for alpha_s(M_Z)")
    a = 0.1180
    nf = 5
    b0 = 11 - 2 * nf / 3
    b1 = 102 - 38 * nf / 3
    beta_abs = b0 * a * a / (2 * math.pi) + b1 * a ** 3 / (8 * math.pi ** 2)
    dlnL = 1.0 / beta_abs
    # Lambda^(3) ~ Lambda^(5)^(23/27) at leading order through the b and c thresholds
    dln_mN = dlnL * 23.0 / 27.0
    print(f"two-loop beta: |beta(alpha_s)| = {beta_abs:.5f} ; d ln Lambda5 / d alpha_s = {dlnL:.1f} ; d ln Lambda3 / d alpha_s = {dln_mN:.1f}")
    off = 0.001865
    print(f"offset of R1 = {off * 100:.3f} % -> delta alpha_s = {off / dln_mN:.2e} ({100 * off / dln_mN / a:.3f} % of alpha_s); PDG world average is 0.1180 +- 0.0009")
    print(f"integer spacing: one unit of mass number at A = 264 (0.38 %) corresponds to delta alpha_s = {1 / 264 / dln_mN:.2e}")
    print(f"Z-vector coherent coupling of 132Sn: g_Z Q_W = {0.653 / (4 * 0.8815) * (82 - (1 - 4 * 0.2386) * 50):.2f} ; Higgs: f_N m_N A / v = {0.305 * 0.939 * 132 / V:.3f}")
    # contact energies per nucleon at saturation density, as in the second feedback's script
    hbarc = 0.1973269804
    rho = 0.16 * hbarc ** 3
    g_h = 0.305 * 0.939 / V
    g_z = 0.653 / (4 * 0.8815)
    w_scale = 0.61 - (1 - 4 * 0.2386) * 0.39
    e_h = g_h ** 2 * rho / (2 * PDG2025["MH"][0] ** 2)
    e_z = g_z ** 2 * rho * w_scale ** 2 / (2 * PDG2025["MZ"][0] ** 2)
    print(f"contact energy per nucleon at 0.16 fm^-3: Higgs {e_h * 1e9:.2e} eV, Z vector {e_z * 1e9:.3f} eV")
    g_dil = 0.939 / V
    print(f"dilaton-like Higgs (f = v): g = m_N/v = {g_dil:.3e}, contact (m_N/v)^2/m_H^2 = {g_dil ** 2 / PDG2025['MH'][0] ** 2:.2e} GeV^-2 ; "
          f"sigma exchange 10^2/0.55^2 = {100 / 0.55 ** 2:.0f} GeV^-2 ; ratio {g_dil ** 2 / PDG2025['MH'][0] ** 2 / (100 / 0.55 ** 2):.1e}; g_hAA(132Sn) = M/v = {m_atomic(50, 132) / V:.3f}")
    d1, d2 = m_atomic(50, 100), m_atomic(50, 132)
    print(f"2x2 reading of R2: V^2 from the difference = {((PDG2025['MH'][0] - PDG2025['MZ'][0]) ** 2 - (d2 - d1) ** 2) / 4:.1f} GeV^2 ; from the product = {d1 * d2 - PDG2025['MH'][0] * PDG2025['MZ'][0]:.1f} GeV^2")


# ------------------------------------------------------------------ 7. Higgs mass history
def sec_history():
    head("7. R2 and the exact rational (29/33) through the PDG editions (atomic masses)")
    s100, s132 = m_atomic(50, 100), m_atomic(50, 132)
    print("edition   M_H +- unc      M_Z       R2 offset   sum-diff(MeV)   (MZ+MH)/v - 29/33   sigma")
    for ed, mh, unc, mz in H_EDITIONS + [("LHCP26 prelim.", 125.09, 0.07, 91.1879), ("CMS 2 Nov 2026", 125.065, 0.088, 91.1879)]:
        r2 = 100 * ((mz + mh) / (s100 + s132) - 1)
        dr = (mz + mh) / V - RATIO_2933
        sig = math.hypot(unc, 0.002) / V
        print(f"{ed:14s} {mh:8.3f} +- {unc:5.3f}  {mz:8.4f}  {r2:+8.3f}%  {1000 * (mz + mh - s100 - s132):9.1f}     {dr:+.2e}        {dr / sig:+.2f}")
    preds = [("(29/33) v - M_Z(BW)", RATIO_2933 * V - 91.1879), ("(29/33) v - M_Z(pole)", RATIO_2933 * V - mz_pole(91.1879)),
             ("v - M_Z + M(100Sn) - M(132Sn)", V - 91.1879 + s100 - s132),
             ("2M(232Th) - M(132Sn) - M(100Zr) - M_Z(pole), nuclear", 2 * m_nuclear(90, 232) - m_nuclear(50, 132) - m_nuclear(40, 100) - mz_pole(91.1879))]
    meas = [("PDG 2026", 125.13, 0.11), ("LHCP 2026 prelim.", 125.09, 0.07), ("CMS 2 Nov 2026", 125.065, 0.088)]
    print("exact completions of the approximate relations, as Higgs-mass predictions (GeV), and pulls (measured - predicted)/sigma:")
    for name, val in preds:
        print(f"  {name:55s} {val:9.4f}   " + "   ".join(f"{m}: {(x - val) / u:+.2f}" for m, x, u in meas))


# ------------------------------------------------------------------ 8. fragment masses
def sec_fragments():
    head("8. Heavy-fragment mass number if the proton number is fixed (unchanged charge density)")
    hmass = PDG2025["MH"][0] / U
    print(f"H = {hmass:.2f} u. Rows: A_H = Z_H * A/Z for Z_H = 52.5 (S1) and 55 (S2), against a fixed A_H = {hmass:.1f}")
    parents = [(90, 222), (90, 226), (90, 230), (90, 232), (92, 233), (92, 235), (92, 238), (94, 239), (98, 252), (100, 258)]
    for z, a in parents:
        sym = AME[(z, a)]["sym"]
        print(f"  {a}{sym}: A/Z = {a / z:.3f}  A_H(S1,52.5) = {52.5 * a / z:6.1f}  A_H(S2,55) = {55 * a / z:6.1f}  A_L(S1) = {a - 52.5 * a / z:5.1f}  [GeV: {52.5 * a / z * U:6.1f} / {55 * a / z * U:6.1f}]")
    print("A_H(S1) reaches the H value at A/Z = %.3f (Th: A = %.1f, U: A = %.1f)" % (hmass / 52.5, hmass / 52.5 * 90, hmass / 52.5 * 92))


# ------------------------------------------------------------------ 9. Q landscape
def q_landscape(z, a):
    parent = m_atomic(z, a)
    out = {}
    for ah in range(a // 2, a - 60):
        best = None
        for zh in range(max(1, round(z * ah / a) - 9), round(z * ah / a) + 10):
            key_h, key_l = (zh, ah), (z - zh, a - ah)
            if key_h in AME and key_l in AME:
                q = parent - m_atomic(*key_h) - m_atomic(*key_l)
                if best is None or q > best[0]:
                    best = (q, zh)
        if best:
            out[ah] = best
    return out


def sec_q():
    head("9. Ground-state Q-value landscape of binary splits (AME2020 atomic masses, best Z_H for each A_H)")
    print("local maxima over even A_H (pairing staggering removed), heavy fragment A_H > A/2 + 4; Q in MeV")
    for z, a in [(90, 226), (90, 232), (92, 236), (94, 240), (98, 252), (100, 258)]:
        q = q_landscape(z, a)
        peaks = []
        for ah in sorted(q):
            if ah % 2 or ah < a // 2 + 4:
                continue
            nb = [q.get(ah - 2), q.get(ah + 2)]
            if all(n is not None and q[ah][0] > n[0] for n in nb):
                peaks.append((q[ah][0] * 1000, ah, q[ah][1]))
        peaks.sort(reverse=True)
        txt = "; ".join(f"A_H={ah} (Z_H={zh}) Q={qq:.1f}" for qq, ah, zh in peaks[:4])
        sym = AME[(z, a)]["sym"]
        extra = ", ".join(f"Q({ah})={q[ah][0] * 1000:.1f}" for ah in (132, 134, 138, 140) if ah in q)
        print(f"{a}{sym}: {txt}   |   {extra}   |   symmetric Q={q[a // 2][0] * 1000:.1f}" if a // 2 in q else f"{a}{sym}: {txt}")
    print("Fermium chain: symmetric split into two tin isotopes (Z_H = Z_L = 50), Q in MeV; AME2020 values beyond A = 257 are extrapolations")
    for a in range(252, 262):
        if (100, a) in AME and (50, a // 2) in AME and (50, a - a // 2) in AME:
            q = m_atomic(100, a) - m_atomic(50, a // 2) - m_atomic(50, a - a // 2)
            flag = "est." if AME[(100, a)]["est"] else "exp."
            print(f"  {a}Fm -> {a // 2}Sn + {a - a // 2}Sn : Q = {q * 1000:7.1f} MeV ({flag})")


# ------------------------------------------------------------------ 10. 2003 bracketing
def sec_bracketing():
    head("10. Subshell rectangles of the November 2003 text (mass-number intervals) against boson mass numbers")
    boxes = {"square 5g9/2 x 5g9/2 (to 100Sn)": (82, 100), "rectangle 5g9/2 x 6h11/2 (to 132Sn)": (112, 132), "rectangle 6h11/2 x 7i13/2 (to 208Pb)": (184, 208)}
    lines = {"W 2003 (80.423)": 80.423 / U, "Z 2003 (91.1876)": 91.1876 / U, "H LEP hint (115)": 115.0 / U, "top 2003 (174.3)": 174.3 / U,
             "W PDG2025": PDG2025["MW"][0] / U, "Z PDG2025": PDG2025["MZ"][0] / U, "H PDG2025": PDG2025["MH"][0] / U, "top PDG2025": PDG2025["MT"][0] / U}
    for name, (lo, hi) in boxes.items():
        print(f"{name}: A in [{lo}, {hi}]")
    for name, a in lines.items():
        verdict = []
        for box, (lo, hi) in boxes.items():
            if lo - 6 <= a <= hi + 6:
                verdict.append(f"{'inside' if lo <= a <= hi else 'outside'} {box.split('(')[1][:-1]} (margin to upper edge {hi - a:+.1f})")
        print(f"  {name:18s} A = {a:6.2f} -> " + "; ".join(verdict))


def sec_family():
    head("11. One-parameter family: v varied with Yukawas, gauge couplings, lambda and the UV QCD coupling held fixed")
    print("Scaling assumed: v, M_Z, M_H, quark masses ~ v ; nuclear masses ~ v^K_A (K_A ~ 0.3 from the trace anomaly, 2/9 + sigma term) ; D0 ~ v^K_D (heavy-quark estimate 0.75-0.92)")
    mz, mh = PDG2025["MZ"][0], PDG2025["MH"][0]
    s100, s132 = m_atomic(50, 100), m_atomic(50, 132)
    r1, r2, r3 = V / (2 * s132), (mz + mh) / (s100 + s132), 2 * D0[0] / M_ALPHA
    print(f"present ratios: R1 = {r1:.6f}, R2 = {r2:.6f}, R3 = {r3:.6f}")
    for k_a in (0.27, 0.30, 0.33):
        d1, d2 = -math.log(r1) / (1 - k_a), -math.log(r2) / (1 - k_a)
        print(f"K_A = {k_a:.2f}: R1 becomes exact at delta ln v = {d1 * 100:+.3f} %, R2 at {d2 * 100:+.3f} %, separation {abs(d2 - d1) * 100:.4f} %")
    for k_d in (0.75, 0.85, 0.92):
        d3 = -math.log(r3) / (k_d - 0.30)
        print(f"K_D = {k_d:.2f}: R3 becomes exact at delta ln v = {d3 * 100:+.3f} %")
    needed = 0.30 + math.log(r3) * 0.70 / math.log(r1)
    print(f"K_D required for R3 to become exact at the same v as R1: {needed:.2f}")


# Boeckstiegel et al., Nucl. Phys. A 802 (2008) 12, arXiv:0712.3808, Table 1 (GSI secondary-beam fission).
# (nuclide, Z, A, Z_H of Standard I, error, Z_H of Standard II, error, yield of the super-long channel in %)
BOECK = [
    ("234U", 92, 234, 52.7, 0.6, 55.2, 0.5, 11.2), ("233U", 92, 233, 51.8, 0.2, 54.6, 0.2, 13.8),
    ("232U", 92, 232, 52.4, 0.2, 55.1, 0.2, 17.9), ("232Pa", 91, 232, 52.5, 0.4, 55.1, 0.2, 18.1),
    ("231Pa", 91, 231, 52.5, 0.1, 55.0, 0.1, 19.4), ("230Pa", 91, 230, 52.6, 0.2, 54.9, 0.1, 22.5),
    ("229Pa", 91, 229, 52.5, 0.1, 54.9, 0.1, 25.4), ("228Pa", 91, 228, 52.0, 0.3, 54.4, 0.1, 35.5),
    ("228Th", 90, 228, 52.9, 0.3, 55.0, 0.2, 37.5), ("226Th", 90, 226, 53.6, 0.3, 55.7, 0.3, 55.6),
    ("225Th", 90, 225, 53.8, 0.2, 56.1, 0.5, 68.6), ("224Th", 90, 224, 52.8, 0.3, 55.0, 0.3, 75.8),
    ("223Th", 90, 223, 53.4, 0.1, 56.2, 0.1, 84.0), ("222Th", 90, 222, 53.3, 0.2, 56.0, 0.2, 88.2),
    ("223Ac", 89, 223, 52.2, 0.2, 54.5, 0.7, 88.4),
]


def sec_boeckstiegel():
    head("12. Heavy-fragment positions measured in Z (Boeckstiegel et al. 2008, Table 1) and the masses implied by UCD")
    hmass = PDG2025["MH"][0] / U
    print(f"A_H = Z_H * A/Z is the unchanged-charge-density conversion used in the paper (evaporation neglected); H = {hmass:.2f} u")
    print("system   asym.share%   Z_H(S1)       A_H(S1)   A_H(S1)-134.4   Z_H(S2)       A_H(S2)   [GeV S1 / S2]")
    z1, a1, z2, a2 = [], [], [], []
    for name, z, a, p1, e1, p2, e2, sl in BOECK:
        ah1, ah2 = p1 * a / z, p2 * a / z
        z1.append(p1); a1.append(ah1); z2.append(p2); a2.append(ah2)
        print(f"{name:6s}   {100 - sl:6.1f}     {p1:5.1f}+-{e1:3.1f}   {ah1:7.1f}   {ah1 - hmass:+7.1f}        {p2:5.1f}+-{e2:3.1f}   {ah2:7.1f}   [{ah1 * U:6.1f} / {ah2 * U:6.1f}]")

    def stats(x):
        mean = sum(x) / len(x)
        sd = math.sqrt(sum((v - mean) ** 2 for v in x) / (len(x) - 1))
        return mean, sd, min(x), max(x)

    for label, arr in (("Z_H(S1)", z1), ("A_H(S1) via UCD", a1), ("Z_H(S2)", z2), ("A_H(S2) via UCD", a2)):
        mean, sd, lo, hi = stats(arr)
        print(f"{label:16s} mean {mean:7.2f}  sd {sd:5.2f} ({100 * sd / mean:4.2f} %)  range {lo:6.1f} to {hi:6.1f}")
    inside = [n for (n, *_), a in zip(BOECK, a1) if abs(a - hmass) <= 1.0]
    print(f"systems with A_H(S1) within 1 u of H: {len(inside)} of {len(a1)} ({', '.join(inside)})")
    print(f"mean A_H(S1) - H = {sum(a1) / len(a1) - hmass:+.2f} u = {(sum(a1) / len(a1) - hmass) * U * 1000:+.0f} MeV")
    print("The Z positions are measured; every A_H in this table is derived, so the table cannot separate a fixed-mass ridge from a fixed-charge ridge.")


def sec_thresholds():
    head("13. Near-zero thresholds in AME2020 (experimental entries only): how many nuclides sit within a few keV of a threshold")
    me_n, me_h1, me_he4 = 8071.31806, 7288.971064, 2424.91587
    exp = {k: v for k, v in AME.items() if not v["est"]}
    channels = [("S_n", (0, 1), me_n), ("S_p", (1, 1), me_h1), ("S_2n", (0, 2), 2 * me_n), ("S_2p", (2, 2), 2 * me_h1),
                ("S_alpha", (2, 4), me_he4)]
    print("window |S| < w with combined uncertainty < w/2; counts over nuclides (parent entries)")
    for label, (dz, da), me_emit in channels:
        counts = {6: 0, 20: 0, 60: 0}
        for (z, a), row in exp.items():
            d = exp.get((z - dz, a - da))
            if d is None:
                continue
            s = d["me"] + me_emit - row["me"]
            unc = math.hypot(d["unc"], row["unc"])
            for w in counts:
                if abs(s) < w and unc < w / 2:
                    counts[w] += 1
        print(f"  {label:8s} within 6 keV: {counts[6]:3d}   within 20 keV: {counts[20]:3d}   within 60 keV: {counts[60]:3d}")
    for label, dz in (("Q_beta-", 1), ("Q_EC", -1)):
        counts = {6: 0, 20: 0, 60: 0}
        for (z, a), row in exp.items():
            d = exp.get((z + dz, a))
            if d is None:
                continue
            q = row["me"] - d["me"]
            unc = math.hypot(d["unc"], row["unc"])
            for w in counts:
                if abs(q) < w and unc < w / 2:
                    counts[w] += 1
        print(f"  {label:8s} within 6 keV: {counts[6]:3d}   within 20 keV: {counts[20]:3d}   within 60 keV: {counts[60]:3d}")
    pairs = []
    for (z, a), row in exp.items():
        d = exp.get((z + 1, a))
        if d is not None and abs(row["me"] - d["me"]) < 20 and math.hypot(d["unc"], row["unc"]) < 10:
            pairs.append((abs(row["me"] - d["me"]), f"{a}{row['sym']} -> {a}{d['sym']}: Q = {row['me'] - d['me']:+.2f} keV"))
    print("isobar pairs with |Q| < 20 keV:", "; ".join(text for _, text in sorted(pairs)))
    s_energy = 0.22 * 8000.0
    print(f"sensitivity of a separation energy of 8 MeV to v if it scales as Lambda_QCD ~ v^(2/9): {s_energy / 1000:.2f} MeV per unit ln v; "
          f"a threshold flips within 0.3 % of v when the nuclide lies {s_energy * 0.003:.1f} keV from it")


# PDG 2025 meson masses (MeV), read from rpp2025-sum-mesons.pdf
MESONS = [("K+-", 493.677), ("K0", 497.611), ("eta", 547.862), ("omega", 782.66), ("eta'", 957.78),
          ("phi", 1019.460), ("D0", 1864.84), ("D+-", 1869.66), ("Ds+-", 1968.35), ("D*0", 2006.85),
          ("D*+-", 2010.26), ("eta_c", 2984.1), ("J/psi", 3096.900), ("chi_c1(3872)", 3871.64),
          ("B+-", 5279.41), ("B0", 5279.72), ("Bs", 5366.93), ("Upsilon(1S)", 9460.40), ("Upsilon(4S)", 10579.4)]
LIGHT = [(1, 2, "d"), (1, 3, "t"), (2, 3, "3He"), (2, 4, "4He"), (3, 6, "6Li"), (3, 7, "7Li"), (4, 7, "7Be"),
         (4, 8, "8Be"), (4, 9, "9Be"), (5, 10, "10B"), (5, 11, "11B"), (6, 12, "12C"), (7, 14, "14N"), (8, 16, "16O")]


def sec_fusion_side():
    head("14. Fusion side: heavy-meson masses and pair thresholds against light nuclei, and the charm remainder against light-nucleus energies")
    nuc = {name: m_nuclear(z, a) * 1000 for z, a, name in LIGHT}
    print(f"check: alpha from AME2020 = {nuc['4He']:.4f} MeV (CODATA {M_ALPHA}); deuteron {nuc['d']:.4f} (CODATA {M_DEUTERON})")
    print("meson           m(X) nearest nucleus (offset %)        2m(X) nearest nucleus (offset %)")
    for name, m in MESONS:
        n1 = min(nuc, key=lambda k: abs(nuc[k] - m))
        n2 = min(nuc, key=lambda k: abs(nuc[k] - 2 * m))
        print(f"  {name:13s} {m:9.2f}  {n1:4s} {100 * (m / nuc[n1] - 1):+7.2f}      {2 * m:9.2f}  {n2:4s} {100 * (2 * m / nuc[n2] - 1):+7.2f}")
    mp, mn, me = M_P, M_N, M_E
    b = {k: None for k in ("d", "t", "3He", "4He")}
    b["d"] = mp + mn - nuc["d"]
    b["t"] = mp + 2 * mn - nuc["t"]
    b["3He"] = 2 * mp + mn - nuc["3He"]
    b["4He"] = 2 * mp + 2 * mn - nuc["4He"]
    q = lambda *pairs: sum(s * v for s, v in pairs)
    energies = [
        ("B(d)", b["d"]), ("B(t)", b["t"]), ("B(3He)", b["3He"]), ("B(4He)", b["4He"]),
        ("m_n - m_p", mn - mp), ("m_e", me), ("2 m_e", 2 * me), ("m(D+) - m(D0)", DPLUS[0] - D0[0]),
        ("Q(d+d -> 3He+n)", 2 * nuc["d"] - nuc["3He"] - mn), ("Q(d+d -> t+p)", 2 * nuc["d"] - nuc["t"] - mp),
        ("Q(d+t -> 4He+n)", nuc["d"] + nuc["t"] - nuc["4He"] - mn), ("Q(d+3He -> 4He+p)", nuc["d"] + nuc["3He"] - nuc["4He"] - mp),
        ("Q(t+t -> 4He+2n)", 2 * nuc["t"] - nuc["4He"] - 2 * mn), ("Q(3He+3He -> 4He+2p)", 2 * nuc["3He"] - nuc["4He"] - 2 * mp),
        ("Q(d+d -> 4He)", 2 * nuc["d"] - nuc["4He"]), ("Q(p+11B -> 3 4He)", nuc["11B"] + mp - 3 * nuc["4He"]),
        ("Q(8Be -> 2 4He)", nuc["8Be"] - 2 * nuc["4He"]), ("Q(3 4He -> 12C)", 3 * nuc["4He"] - nuc["12C"]),
        ("Q(12C+4He -> 16O)", nuc["12C"] + nuc["4He"] - nuc["16O"]),
    ]
    rem = 2 * D0[0] - M_ALPHA
    sig = 2 * D0[1]
    print(f"charm remainder 2 m(D0) - M(alpha) = {rem:.3f} +- {sig:.2f} MeV, compared with {len(energies)} light-nucleus energies:")
    for name, e in sorted(energies, key=lambda x: abs(x[1] - rem)):
        print(f"  {name:22s} {e:9.4f} MeV   remainder - E = {rem - e:+8.3f} MeV ({(rem - e) / sig:+6.1f} sigma of 2 m(D0))")
    print(f"equivalent form: 2 m(D0) + M(d) - M(alpha) - m_p - m_n = {2 * D0[0] + nuc['d'] - M_ALPHA - mp - mn:+.3f} MeV")


def sec_share():
    head("15. Asymmetric share against parent mass number and neutron number (Boeckstiegel et al. 2008, Table 1)")
    pts = [(a, z, a - z, 100 - sl, name) for name, z, a, *_rest, sl in [(r[0], r[1], r[2], r[7]) for r in BOECK]]
    print("isobars (same A):")
    for a in sorted({p[0] for p in pts}):
        grp = [p for p in pts if p[0] == a]
        if len(grp) > 1:
            print("  A = %d: " % a + ", ".join(f"{p[4]} {p[3]:.1f}%" for p in grp) + f"  spread {max(p[3] for p in grp) - min(p[3] for p in grp):.1f}")
    print("isotones (same N):")
    for n in sorted({p[2] for p in pts}):
        grp = [p for p in pts if p[2] == n]
        if len(grp) > 1:
            print("  N = %d: " % n + ", ".join(f"{p[4]} {p[3]:.1f}%" for p in grp) + f"  spread {max(p[3] for p in grp) - min(p[3] for p in grp):.1f}")
    best = None
    for i in range(0, 1201):
        a50 = 220 + i * 0.01
        for j in range(1, 101):
            w = j * 0.05
            sse = sum((s - 100 / (1 + math.exp(-(a - a50) / w))) ** 2 for a, _, _, s, _ in pts)
            if best is None or sse < best[0]:
                best = (sse, a50, w)
    rms = math.sqrt(best[0] / len(pts))
    print(f"logistic fit share(A) = 100/(1+exp(-(A-A50)/w)): A50 = {best[1]:.2f}, w = {best[2]:.2f}, rms residual {rms:.1f} points")
    mw, mz, mh = PDG2025["MW"][0], PDG2025["MZ"][0], PDG2025["MH"][0]
    print(f"band (M_H+M_W)/u = {(mh + mw) / U:.2f} to (M_H+M_Z)/u = {(mh + mz) / U:.2f}; midpoint {(2 * mh + mw + mz) / 2 / U:.2f}")
    print("excitation energy of the fissioning nuclei in these data: about 11 MeV (Coulomb excitation of secondary beams)")


def main():
    for section in (sec_inputs, sec_brief, sec_granularity, sec_conventions, sec_feedback_a, sec_charm, sec_alpha_s,
                    sec_history, sec_fragments, sec_q, sec_bracketing, sec_family, sec_boeckstiegel, sec_thresholds,
                    sec_fusion_side, sec_share):
        section()


if __name__ == "__main__":
    main()
