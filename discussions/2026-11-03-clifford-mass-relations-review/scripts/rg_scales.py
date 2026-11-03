"""Scales below which each relation stays within one standard uncertainty (on-shell scheme),
and the ratio of the two lepton offsets at a few scales. Reuses the model in rg_scan.py."""
import contextlib
import io
import os
import runpy

with contextlib.redirect_stdout(io.StringIO()):
    G = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), "rg_scan.py"))
mp, aeff_inv = G["mp"], G["aeff_inv"]
RMU, RTAU = G["RMU"], G["RTAU"]
U_MU, U_TAU, U_P = G["U_MU"], G["U_TAU"], G["U_P"]
base = aeff_inv(mp.mpf("1e-9"))


def bisect(f, lo, hi, it=80):
    flo = f(lo)
    for _ in range(it):
        mid = (lo + hi) / 2
        fm = f(mid)
        if (fm > 0) == (flo > 0):
            lo, flo = mid, fm
        else:
            hi = mid
    return (lo + hi) / 2


for name, coef, u in [("muon", mp.mpf(3) / 2, U_MU), ("tau", mp.mpf(51) / 2, U_TAU), ("proton", mp.mpf(27) / 2, U_P)]:
    lq = bisect(lambda x: coef * (base - aeff_inv(mp.e**x)) - u, mp.log(mp.mpf("1e-8")), mp.log(mp.mpf("1e-1")))
    print(f"{name}: within 1 sigma for mu below {mp.nstr(mp.e**lq * 1e6, 4)} keV")
for q in ["0.001", "0.01", "0.1"]:
    q = mp.mpf(q)
    om, ot = RMU - mp.mpf(3) / 2 * aeff_inv(q), RTAU - mp.mpf(51) / 2 * aeff_inv(q)
    print(f"mu = {q} GeV: o_mu = {mp.nstr(om, 5)}, o_tau = {mp.nstr(ot, 5)}, o_tau/o_mu = {mp.nstr(ot / om, 4)}")
