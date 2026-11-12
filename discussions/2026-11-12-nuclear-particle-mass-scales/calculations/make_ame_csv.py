"""Convert the AME2020 atomic-mass table (mass_1.mas20.txt) into a compact CSV.

usage: python -I make_ame_csv.py MASS_TABLE.txt OUT.csv

The AMDC file is fixed width (format a1,i3,i5,i5,i5,1x,a3,a4,1x,f14.6,f12.6,f13.5,
1x,f10.5,1x,a2,f13.5,f11.5,1x,i3,1x,f13.6,f12.6). Values written with '#' in place
of the decimal point are estimates from systematics (non-experimental); the CSV keeps
that information in the column `estimated`. Columns:

  Z, N, A, symbol, mass_excess_keV, mass_excess_unc_keV, estimated,
  atomic_mass_micro_u

Source: W.J. Huang, M. Wang, F.G. Kondev, G. Audi, S. Naimi, Chin. Phys. C 45, 030002 (2021)
and M. Wang et al., Chin. Phys. C 45, 030003 (2021). File obtained from
https://www-nds.iaea.org/amdc/ame2020/mass_1.mas20.txt
"""
import csv
import hashlib
import pathlib
import sys

src = pathlib.Path(sys.argv[1])
dst = pathlib.Path(sys.argv[2])
raw = src.read_bytes()
print("sha256", hashlib.sha256(raw).hexdigest())

rows = []
# every line is tried; header and ruler lines fail the integer parse of N, Z and A below
for line in raw.decode("latin-1").splitlines():
    if len(line) < 124:
        continue
    try:
        n = int(line[4:9])
        z = int(line[9:14])
        a = int(line[14:19])
    except ValueError:
        continue
    symbol = line[20:23].strip()
    me_txt = line[28:42].strip()
    unc_txt = line[42:54].strip()
    estimated = "#" in me_txt or "#" in unc_txt
    me_txt = me_txt.replace("#", ".")
    unc_txt = unc_txt.replace("#", ".")
    if "*" in me_txt:
        continue
    am_int = line[106:109].strip()
    am_frac = line[110:123].strip().replace("#", ".")
    try:
        mass_excess = float(me_txt)
        unc = float(unc_txt)
        atomic_micro_u = int(am_int) * 1e6 + float(am_frac)
    except ValueError:
        continue
    rows.append((z, n, a, symbol, mass_excess, unc, int(estimated), atomic_micro_u))

with dst.open("w", newline="") as handle:
    writer = csv.writer(handle)
    writer.writerow(["Z", "N", "A", "symbol", "mass_excess_keV", "mass_excess_unc_keV",
                     "estimated", "atomic_mass_micro_u"])
    for row in rows:
        writer.writerow(row)

print(len(rows), "nuclides written to", dst)
lookup = {(r[0], r[2]): r for r in rows}
for key in [(50, 132), (50, 100), (2, 4), (6, 12), (90, 232), (40, 100), (100, 258)]:
    r = lookup.get(key)
    print(key, r)
