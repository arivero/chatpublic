"""Numbers of ../alpha.md: relations that involve the fine-structure constant.

usage: python -I alpha_note.py > alpha_note_output.txt
"""
import math
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import audit as A  # noqa: E402

AI0 = 137.035999084          # 1/alpha at zero momentum transfer (CODATA 2018)
ME = A.M_E                   # MeV
V = A.V * 1000.0             # MeV
MN = (A.M_P + A.M_N) / 2
D0, MALPHA = 1864.84, A.M_ALPHA
U1, U2 = ME * AI0, ME * AI0 ** 2


def head(t):
    print("\n" + "=" * 96 + "\n" + t + "\n" + "=" * 96)


def half(x):
    h = round(2 * x) / 2
    return f"{x:8.4f}   nearest half-integer {h:5.1f} ({100 * (x / h - 1):+.2f} %)"


def inv_alpha_ew(mw, mz):
    """Tree-level 1/alpha from G_F, M_W, M_Z: alpha = sqrt2 G_F M_W^2 (1 - M_W^2/M_Z^2) / pi."""
    return math.pi / (math.sqrt(2) * A.G_F * mw * mw * (1 - mw * mw / (mz * mz)))


def main():
    head("1. The ladder")
    print(f"  m_e/alpha = {U1:.4f} MeV ; m_e/alpha^2 = {U2 / 1000:.4f} GeV ; m_e/alpha^3 = {U2 * AI0 / 1e6:.3f} TeV")

    head("2. Units of m_e/alpha (Nambu 1952: half-integer multiples)")
    for name, m in [("muon", 105.6584), ("pi+-", 139.5704), ("pi0", 134.9768), ("K+-", 493.677), ("proton", A.M_P), ("nucleon mean", MN),
                    ("unit m* = m(D0)/2", D0 / 2), ("unit m* = v/264", V / 264), ("u", A.U_MEV), ("Lambda", 1115.683), ("tau", 1776.93),
                    ("D0", D0), ("alpha particle", MALPHA)]:
        print(f"  {name:20s} {m:10.3f} MeV  {half(m / U1)}")

    head("3. Barut 1979: m_N = m_e (1 + (3 / 2 alpha) sum_{n<=N} n^4)")
    s = 0
    for n in range(0, 7):
        s += n ** 4
        print(f"  N = {n}: sum = {s:5d}   m = {ME * (1 + 1.5 * AI0 * s) / 1000:10.4f} GeV")
    print("  measured: muon 0.10566 GeV, tau 1.77693 GeV")

    head("4. 27/2 and 2/27")
    print(f"  b0(n_f = 3) / (2/3) = {9 / (2 / 3):.1f} = 33/2 - 3 ; exponent of a heavy-quark mass in Lambda_3: 2/27 = {2 / 27:.5f}")
    print(f"  (2/27) m_N = {2 / 27 * MN:.2f} MeV ; m_e/alpha = {U1:.2f} MeV ; ratio {2 / 27 * MN / U1:.4f}")
    for sig in (0.08, 0.10, 0.12):
        print(f"  with light sigma fractions {sig:.2f}: sigma_Q = (2/27)(1 - {sig:.2f}) m_N = {2 / 27 * (1 - sig) * MN:.1f} MeV")
    print(f"  27 / (2 alpha) = {13.5 * AI0:.1f} against m_p/m_e = {A.M_P / ME:.2f}")

    head("5. alpha as an electroweak quantity (tree level, G_F scheme)")
    for tag, mw, dmw, mz in [("PDG 2025 masses", 80.3692, 0.0133, 91.1880), ("PDG 2026 masses", 80.3625, 0.0077, 91.1879),
                             ("pole masses (2026)", 80.3625 - 2.14 ** 2 / (2 * 80.3625), 0.0077, 91.1539)]:
        x = inv_alpha_ew(mw, mz)
        dx = x * abs(2 - 2 * mw * mw / (mz * mz - mw * mw)) * dmw / mw
        print(f"  {tag:20s} M_W = {mw:.4f}: 1/alpha = {x:8.3f} +- {dx:.3f} ; alpha v = {V / x:8.2f} +- {V / x * dx / x:.2f} MeV ; "
              f"alpha v/2 = {V / x / 2:7.2f} MeV ; 1 - (1/alpha)/(1/alpha(0)) = {1 - x / AI0:.4f}")
    print(f"  compare: v/m(D0) = {V / D0:.3f} ; v/(M_alpha/2) = {V / (MALPHA / 2):.3f} ; 50 + 82 = 132 ; 1/alpha(0) = {AI0:.3f}")
    print(f"  compare: m(D0) = {D0} MeV ; M_alpha/2 = {MALPHA / 2:.2f} MeV ; m(D0)/2 = {D0 / 2:.2f} ; M_alpha/4 = {MALPHA / 4:.2f} ; u = {A.U_MEV:.3f} MeV")

    def w_for(target, mz=91.1879):
        lo, hi = 80.2, 80.5
        for _ in range(60):
            mid = (lo + hi) / 2
            lo, hi = (lo, mid) if inv_alpha_ew(mid, mz) > target else (mid, hi)
        return (lo + hi) / 2

    for t, why in ((132.0, "the integer"), (V / D0, "v/m(D0)"), (V / (MALPHA / 2), "v/(M_alpha/2)")):
        print(f"  1/alpha = {t:.3f} ({why}) corresponds to M_W = {w_for(t):.4f} GeV")
    x26 = inv_alpha_ew(80.3625, 91.1879)
    print(f"  slope: d(1/alpha)/dM_W = {x26 * (2 * 80.3625 ** 2 / (91.1879 ** 2 - 80.3625 ** 2) - 2) / 80.3625:.2f} per GeV")
    print(f"  Nambu unit with this alpha: m_e x 132.05 = {ME * 132.05:.2f} MeV ; nucleon = {MN / (ME * 132.05):.2f} units")

    head("6. Units of m_e/alpha^2 = 9.596 GeV")
    s132, s100 = A.m_atomic(50, 132), A.m_atomic(50, 100)
    for name, m in [("Upsilon(1S)", 9.4604), ("Barut N = 3", ME * (1 + 1.5 * AI0 * 98) / 1000), ("2 m(B0)", 10.55944), ("W", 80.3692), ("Z", 91.1880),
                    ("Z pole", 91.1539), ("H 125.20", 125.20), ("H 125.13", 125.13), ("top", 172.56), ("v", V / 1000), ("Z + H (2025)", 216.388),
                    ("Z + H (2026)", 216.3179), ("M(100Sn)+M(132Sn)", s100 + s132)]:
        print(f"  {name:20s} {m:9.4f} GeV  {half(m * 1000 / U2)}")
    print(f"  45/2 units = {22.5 * U2 / 1000:.3f} GeV")

    head("7. One power of alpha(0)")
    for name, m in [("m_tau/alpha", 1776.93), ("m(D0)/alpha", D0), ("m_p/alpha", A.M_P), ("m*/alpha", 932.5)]:
        print(f"  {name:12s} = {m * AI0 / 1000:8.3f} GeV")
    print(f"  v alpha(0) = {V / AI0:.1f} MeV ; v/m_tau = {V / 1776.93:.2f} ; v/m(D0) = {V / D0:.2f}")


if __name__ == "__main__":
    main()
