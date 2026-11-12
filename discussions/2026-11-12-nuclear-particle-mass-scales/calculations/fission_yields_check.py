"""Post-neutron mass yields from ENDF/B-VIII.0 fission-product yield files (MF=8, MT=454).

usage: python -I fission_yields_check.py NFY_DIR SFY_DIR

NFY_DIR and SFY_DIR are the unpacked neutron-induced and spontaneous fission-yield
sublibraries of ENDF/B-VIII.0 (NNDC). For each system the script sums the independent
yields over Z at fixed A, which gives the mass distribution after prompt-neutron emission,
then prints the yield-weighted centroids and the single-mass maxima of the light and heavy
groups (split at A_f/2). Pre-neutron masses are higher by the prompt neutrons of each group.
"""
import pathlib
import re
import sys

NUM = re.compile(r"([0-9.])([+-])(\d)")


def endf_float(field):
    field = field.strip()
    if not field:
        return 0.0
    return float(NUM.sub(r"\1e\2\3", field))


def read_mt454(path):
    """Return {incident energy (eV): {A: summed independent yield}}."""
    values = []
    for line in pathlib.Path(path).read_text(errors="replace").splitlines():
        if len(line) < 75:
            continue
        try:
            mf, mt = int(line[70:72]), int(line[72:75])
        except ValueError:
            continue
        if mf == 8 and mt == 454:
            values.extend(endf_float(line[i:i + 11]) for i in range(0, 66, 11))
    out = {}
    pos = 6                      # skip the HEAD record (ZA, AWR, LE+1, 0, 0, 0)
    while pos + 6 <= len(values):
        energy, nn = values[pos], int(values[pos + 4])
        if nn <= 0:
            break
        block = values[pos + 6: pos + 6 + nn]
        yields = {}
        for k in range(0, nn, 4):
            za, y = int(round(block[k])), block[k + 2]
            a = za % 1000
            yields[a] = yields.get(a, 0.0) + y
        out[energy] = yields
        pos += 6 + nn + ((-nn) % 6)    # LIST records are padded to full lines of 6 numbers
    return out


def summarize(label, yields, a_f):
    total = sum(yields.values())
    light = {a: y for a, y in yields.items() if a < a_f / 2}
    heavy = {a: y for a, y in yields.items() if a > a_f / 2}
    c_l = sum(a * y for a, y in light.items()) / sum(light.values())
    c_h = sum(a * y for a, y in heavy.items()) / sum(heavy.values())
    m_l = max(light, key=light.get)
    m_h = max(heavy, key=heavy.get)
    print(f"{label:28s} sum Y = {total:5.3f}  centroids L/H = {c_l:6.2f} / {c_h:6.2f}   "
          f"single-mass maxima L/H = {m_l} ({100 * light[m_l]:.2f}%) / {m_h} ({100 * heavy[m_h]:.2f}%)   "
          f"Y(134) = {100 * yields.get(134, 0):.2f}%  Y(98) = {100 * yields.get(98, 0):.2f}%")


def main():
    nfy, sfy = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    cases = [  # (label, file, compound mass number, energy choice)
        ("232Th(n, 0.5 MeV)", nfy / "nfy-090_Th_232.endf", 233, "fast"),
        ("233U(n, thermal)", nfy / "nfy-092_U_233.endf", 234, "thermal"),
        ("235U(n, thermal)", nfy / "nfy-092_U_235.endf", 236, "thermal"),
        ("238U(n, 0.5 MeV)", nfy / "nfy-092_U_238.endf", 239, "fast"),
        ("239Pu(n, thermal)", nfy / "nfy-094_Pu_239.endf", 240, "thermal"),
        ("242Cm(n, 0.5 MeV) [243Cm*]", nfy / "nfy-096_Cm_242.endf", 243, "fast"),
        ("244Cm(sf)", sfy / "sfy-096_Cm_244.endf", 244, "sf"),
        ("252Cf(sf)", sfy / "sfy-098_Cf_252.endf", 252, "sf"),
    ]
    for label, path, a_f, kind in cases:
        if not path.exists():
            print(f"{label:28s} file missing: {path.name}")
            continue
        data = read_mt454(path)
        energies = sorted(data)
        if kind == "thermal":
            e = min(energies, key=lambda x: abs(x - 0.0253))
        elif kind == "fast":
            e = min(energies, key=lambda x: abs(x - 5.0e5))
        else:
            e = energies[0]
        summarize(f"{label} E={e:.3g} eV", data[e], a_f)


if __name__ == "__main__":
    main()
