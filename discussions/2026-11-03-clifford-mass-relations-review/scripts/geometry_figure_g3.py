"""Figure G3: origin of the weights 0, 1, 17 and alternative splits of the 16-dimensional carrier."""
import runpy
G = runpy.run_path(__import__("os").path.join(__import__("os").path.dirname(__import__("os").path.abspath(__file__)), "geometry_figures.py"))
T, svg = G["T"], G["svg"]
U_MU = 4.6e-6
OFF = 1.2142839


def strip(x0, y, groups, cw, ch, gin, gout, styles):
    """groups: list of sizes; styles: list of css classes per group. returns (svg list, centers)"""
    out, centers, x = [], [], x0
    for n, st in zip(groups, styles):
        w = n * cw + (n - 1) * gin
        for k in range(n):
            out.append(f'<rect x="{x + k * (cw + gin):g}" y="{y:g}" width="{cw}" height="{ch}" rx="2" class="{st}"/>')
        centers.append(x + w / 2)
        x += w + gout
    return out, centers


# ---------------- panel A: the two terms of the response
b = []
groups = [1, 4, 6, 4, 1]
rows = [
    (40, "traceless part: (1/32) Σ‖[Γ, X]‖²", ["cell-out", "cell-grey", "cell-grey", "cell-grey", "cell-grey"], ["0", "1", "1", "1", "1"]),
    (122, [("nilpotent part: ‖C X‖², C X = tr(ΣX)·I", "n")], ["cell-out", "cell-out", "cell-out", "cell-out", "cell-tau"], ["0", "0", "0", "0", "16"]),
    (204, "sum A: weights 0, 1, 17", ["cell-e-out", "cell-mu", "cell-mu", "cell-mu", "cell-tau"], ["0", "1", "1", "1", "17"]),
]
for y, title, st, vals in rows:
    b.append(T(170, y, title if isinstance(title, list) else title, "t", "middle"))
    cells, cen = strip(56, y + 20, groups, 13, 22, 2, 10, st)
    b += cells
    for c, v in zip(cen, vals):
        b.append(T(c, y + 58, v, "t", "middle"))
b += [T(30, 104, "+", "t big", "middle"), T(30, 186, "=", "t big", "middle")]
for c, w in zip(cen, ["I", "γ", "γγ", "γγγ", "Σ"]):
    b.append(T(c, 280, w, "t m", "middle"))
b.append(T(170, 298, "17 = 1 + (tr Σ²)² = 1 + (dim S)²", "t", "middle"))
PA = svg(340, 306, "The response is the sum of the traceless part, which gives 1 to every Clifford word except the identity, and the nilpotent part, which gives 16 to the pseudoscalar only; the sum is 0, 1 on the fourteen middle words, and 17", b)

# ---------------- panel B: alternative splits
b = []
specs = [
    ("rotations of S³: 1 · 4 · 3 · 3 · 4 · 1", [1, 4, 3, 3, 4, 1], ["cell-e", "cell-grey", "cell-grey", "cell-grey", "cell-grey", "cell-tau"], None, "minimum not unique"),
    ("spread over bivectors, d = 6", [1, 4, 6, 4, 1], ["cell-e", "cell-grey", "cell-mu", "cell-grey", "cell-tau"], 6, None),
    ("spread over γ and γγγ, d = 8", [1, 4, 6, 4, 1], ["cell-e", "cell-mu", "cell-grey", "cell-mu", "cell-tau"], 8, None),
    ("spread over the 14, U(14): manuscript", [1, 14, 1], ["cell-e", "cell-mu", "cell-tau"], 14, None),
    ("uniform over all 15 active directions", [1, 15], ["cell-e", "cell-mu"], 15, "uniform15"),
]
y = 30
for title, gr, st, d, note in specs:
    b.append(T(10, y, title, "t"))
    cells, _ = strip(10, y + 8, gr, 7, 16, 1, 5, st)
    b += cells
    if d:
        off = 16 / 15 if note == "uniform15" else 17 / d
        z = (off - OFF) / U_MU
        zs = f"{z:+.1e}".replace("e+0", "×10^").replace("e-0", "×10^-")
        mant, ex = f"{abs(z):.1e}".split("e")
        ztxt = f"{'+' if z > 0 else '−'}{mant}×10" if abs(z) >= 10 else f"{z:+.2f}"
        parts = [((f"16/15" if note == "uniform15" else f"17/{d}") + f" = {off:.4f}", "n")]
        b.append(T(200, y + 20, parts, "t"))
        if abs(z) >= 10:
            b.append(T(200, y + 35, [(f"pull {ztxt}", "n"), (str(int(ex)), "sup"), ("σ", "n")], "t m"))
        else:
            b.append(T(200, y + 35, f"pull {z:+.2f}σ", "t m"))
    else:
        b.append(T(200, y + 20, note, "t"))
        b.append(T(200, y + 35, "commutant dimension 10", "t m"))
    y += 54
b.append(T(10, 298, [("measured: m", "n"), ("μ", "sub"), ("/m", "n"), ("e", "sub"), (" − 3/(2α) = 1.2142839(46)", "n")], "t m"))
PB = svg(340, 306, "Rotations split the sixteen words as 1, 4, 3, 3, 4, 1; spreading the tau weight 17 over a block of dimension d gives the muon offset 17 over d, and only d = 14 matches the measured value", b)

fig = f'''  <figure class="fig geo" aria-labelledby="g3t">
    <p class="fig-title" id="g3t">Figure G3 · Where 0, 1, 17 come from, and other ways to split the 16</p>
    <div class="geo-panels">
      <div><p class="panel-title">The two terms of the response, Eqs. (5.3)–(5.6)</p>{PA}</div>
      <div><p class="panel-title">Alternatives to 1 + 14 + 1 and the muon offset 17/d</p>{PB}</div>
    </div>
    <figcaption>Left: the traceless part gives 1 to every Clifford word except the identity, and \\(\\|\\mathcal C X\\|^2\\) is nonzero only on Σ, where \\(\\mathcal C\\) multiplies the norm by \\(\\mathrm{{tr}}\\,\\Sigma^2 = 4 = \\dim S\\). Right: rotations of S³ split the 16 words into 1 + 4 + 3 + 3 + 4 + 1 (scalar, vectors, self-dual and anti-self-dual bivectors, pseudovectors, pseudoscalar); with only that symmetry the minimum of Sec. 6 is not unique. The manuscript merges the middle 14 by postulating the full U(14) isotropy (H1). Spreading the τ weight over a block of dimension d gives the muon offset 17/d; spreading the whole trace uniformly over all 15 active directions gives 16/15. Only d = 14 matches.</figcaption>
  </figure>
'''
open("geo_g3.html", "w", encoding="utf8").write(fig)
print(len(fig))
