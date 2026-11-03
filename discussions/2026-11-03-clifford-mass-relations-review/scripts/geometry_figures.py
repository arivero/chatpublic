"""Generate the inline-SVG geometry figures for the review page (section 'The construction at a glance')."""
import math

SUB_DY, SUP_DY = 3.5, -5


def T(x, y, parts, cls="t", anchor="start", extra=""):
    """text with optional sub/superscript parts: parts is a str or a list of (text, kind)."""
    if isinstance(parts, str):
        parts = [(parts, "n")]
    out, shift = [], 0.0
    for txt, kind in parts:
        txt = txt.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        if kind == "n":
            dy = -shift
            shift = 0.0
            out.append(f'<tspan dy="{dy:g}">{txt}</tspan>' if dy else txt)
        else:
            target = SUB_DY if kind == "sub" else SUP_DY
            dy = target - shift
            shift = target
            out.append(f'<tspan class="s" dy="{dy:g}">{txt}</tspan>')
    return f'<text x="{x:g}" y="{y:g}" class="{cls}" text-anchor="{anchor}"{extra}>{"".join(out)}</text>'


def marker(mid):
    return (f'<defs><marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="currentColor"/></marker></defs>')


def svg(w, h, label, body):
    return f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="{label}">' + "".join(body) + "</svg>"


# ------------------------------------------------------------------ panel 1: sphere and Dirac levels
b = [marker("ga1")]
cx, cy, R = 80, 128, 58
b += [f'<circle cx="{cx}" cy="{cy}" r="{R}" class="ln"/>',
      f'<ellipse cx="{cx}" cy="{cy}" rx="{R}" ry="17" class="ln thin"/>',
      f'<ellipse cx="{cx}" cy="{cy}" rx="22" ry="{R}" class="ln thin"/>',
      f'<line x1="{cx}" y1="{cy}" x2="128" y2="100" class="ln" marker-end="url(#ga1)"/>',
      T(101, 104, [("r", "n"), ("e", "sub")], "t halo", "middle"),
      T(cx, 210, [("S", "n"), ("3", "sup"), (" ≅ SU(2), round", "n")], "t", "middle"),
      T(cx, 227, [("r", "n"), ("e", "sub"), (" = αħ/(m", "n"), ("e", "sub"), ("c)", "n")], "t m", "middle"),
      T(cx, 244, "round shape minimizes Φ", "t m", "middle")]
ax = 215
y0 = 150
sc = 30
b.append(f'<line x1="{ax}" y1="36" x2="{ax}" y2="262" class="ln thin"/>')
b.append(T(ax, 28, "λ · r", "t m", "middle"))
for lv, mult in [(1.5, 2), (2.5, 6), (3.5, 12)]:
    for sgn in (1, -1):
        y = y0 - sgn * sc * lv
        hi = lv == 1.5
        cls = "ln lev" if hi else "ln mut"
        b.append(f'<line x1="{ax - 8}" y1="{y:g}" x2="{ax + 8}" y2="{y:g}" class="{cls}"/>')
        lab = ("+" if sgn > 0 else "−") + {1.5: "3/2", 2.5: "5/2", 3.5: "7/2"}[lv]
        b.append(T(ax - 13, y + 4, lab, "t" if hi else "t m", "end"))
        for k in range(mult):
            fill = "dot-hi" if hi else "dot-mut"
            b.append(f'<circle cx="{ax + 17 + 7 * k}" cy="{y:g}" r="2.6" class="{fill}"/>')
bx = 252
b += [f'<polyline points="{bx - 4},105 {bx},105 {bx},195 {bx - 4},195" class="ln"/>',
      T(bx + 6, 142, [("S = S", "n"), ("+", "sub"), (" ⊕ S", "n"), ("−", "sub")], "t"),
      T(bx + 6, 158, "dim 2 + 2 = 4", "t m"),
      T(bx + 6, 174, [("Σ = D/λ", "n"), ("0", "sub")], "t m"),
      T(250, 288, [("E", "n"), ("*", "sup"), (" = 3ħc/(2r", "n"), ("e", "sub"), (") = κ m", "n"), ("e", "sub"), ("c", "n"), ("2", "sup")], "t", "middle")]
P1 = svg(340, 300, "Round three-sphere of radius r_e and its Dirac levels; the lowest level plus and minus 3/2 over r has two modes of each sign, which form the four-dimensional carrier S", b)

# ------------------------------------------------------------------ panel 2: W = End S and the operator C
b = [marker("ga2")]
counts = [1, 4, 6, 4, 1]
xs = [42, 106, 170, 234, 298]
cls = ["cell-e", "cell-mu", "cell-mu", "cell-mu", "cell-tau"]
for n, x, c in zip(counts, xs, cls):
    top = 150 - (n * 22 + (n - 1) * 4) / 2
    for k in range(n):
        b.append(f'<rect x="{x - 11}" y="{top + 26 * k:g}" width="22" height="22" rx="3" class="{c}"/>')
for n, x, w in zip(counts, xs, ["I", "γ", "γγ", "γγγ", "Σ"]):
    b.append(T(x, 248, str(n), "t", "middle"))
    b.append(T(x, 263, w, "t m", "middle"))
b += ['<path d="M298 136 C 298 28, 42 28, 42 134" class="ln" marker-end="url(#ga2)"/>',
      T(170, 24, "C X = tr(ΣX) · I", "t", "middle"),
      T(170, 40, "‖C p‖ = 4 ‖s‖", "t m", "middle")]
b += ['<polyline points="95,272 95,277 245,277 245,272" class="ln thin"/>',
      '<line x1="42" y1="272" x2="42" y2="277" class="ln thin"/>',
      '<line x1="298" y1="272" x2="298" y2="277" class="ln thin"/>',
      T(42, 293, "e · im C", "t", "middle"),
      T(170, 293, "μ · ker Δ · 14", "t", "middle"),
      T(298, 293, "τ · im C†", "t", "middle")]
P2 = svg(340, 300, "The sixteen-dimensional matrix carrier W = End S by Clifford grade 1, 4, 6, 4, 1; the operator C maps the pseudoscalar line to the scalar line and splits W into 1 + 14 + 1", b)

# ------------------------------------------------------------------ panel 3: response weights and minimum
b = [marker("ga3")]
base, u = 232, 8
b += [f'<line x1="18" y1="{base}" x2="164" y2="{base}" class="ln thin"/>',
      f'<line x1="182" y1="{base}" x2="328" y2="{base}" class="ln thin"/>']
# left: A
b.append(f'<line x1="23" y1="{base - 1}" x2="33" y2="{base - 1}" class="ln e-mark"/>')
for i in range(14):
    b.append(f'<rect x="{42 + 7 * i}" y="{base - u}" width="5" height="{u}" class="cell-mu"/>')
b.append(f'<rect x="146" y="{base - 17 * u}" width="10" height="{17 * u}" class="cell-tau"/>')
b += [T(28, base - 8, "0", "t", "middle"), T(90, base - u - 6, "1", "t", "middle"), T(151, base - 17 * u - 6, "17", "t", "middle"),
      T(28, 250, "e", "t", "middle"), T(90, 250, "μ ×14", "t", "middle"), T(151, 250, "τ", "t", "middle"),
      T(90, 34, "A, graph response", "t", "middle"), T(90, 50, "weights 0, 1, 17 · trace 31", "t m", "middle")]
# right: Z*
h2 = 31 / 14 * u
b.append(f'<line x1="189" y1="{base - 1}" x2="199" y2="{base - 1}" class="ln e-mark"/>')
for i in range(14):
    b.append(f'<rect x="{206 + 7 * i}" y="{base - h2:.2f}" width="5" height="{h2:.2f}" class="cell-mu"/>')
b.append(f'<line x1="311" y1="{base - 1}" x2="323" y2="{base - 1}" class="ln tau-mark"/>')
b += [T(194, base - 8, "0", "t", "middle"), T(254, base - h2 - 6, "31/14", "t", "middle"), T(317, base - 8, "0", "t", "middle"),
      T(194, 250, "e", "t", "middle"), T(254, 250, "μ ×14", "t", "middle"), T(317, 250, "τ", "t", "middle"),
      T(256, 34, [("Z", "n"), ("*", "sup"), (", minimum", "n")], "t", "middle"), T(256, 50, "weights 0, 31/14, 0 · trace 31", "t m", "middle")]
b += ['<path d="M160 112 C 214 104, 246 150, 252 200" class="ln" marker-end="url(#ga3)"/>',
      T(226, 84, "loss on the τ line,", "t m", "middle"), T(226, 99, "uniform return to the 14", "t m", "middle"),
      T(170, 284, [("B = Z", "n"), ("*", "sup"), (" − A: +17/14 on each μ direction, −17 on τ", "n")], "t", "middle")]
P3 = svg(340, 300, "Response weights 0, 1 and 17 with trace 31; the trace-preserving minimum moves the tau weight 17 uniformly into the fourteen muon directions, each gaining 17 over 14", b)

# ------------------------------------------------------------------ panel 4: masses on a log scale
b = []
ax, ytop, ybot = 118, 40, 262
dec = (ybot - ytop) / 3.7
Y = lambda v: ybot - dec * math.log10(v)
b.append(f'<line x1="{ax}" y1="{ytop - 6}" x2="{ax}" y2="{ybot}" class="ln thin"/>')
for v, lab in [(1, "1"), (10, "10"), (100, "100"), (1000, "1000")]:
    b.append(f'<line x1="{ax - 4}" y1="{Y(v):.1f}" x2="{ax}" y2="{Y(v):.1f}" class="ln thin"/>')
    b.append(T(ax - 8, Y(v) + 4, lab, "t m", "end"))
b.append(T(ax, 24, [("m / m", "n"), ("e", "sub"), (", log scale", "n")], "t m", "middle"))
ye, ym, yt = Y(1), Y(206.7682845), Y(3477.418)
b += [f'<polyline points="70,{ye:.1f} 64,{ye:.1f} 64,{ym:.1f} 70,{ym:.1f}" class="ln thin"/>',
      f'<polyline points="70,{ym:.1f} 64,{ym:.1f} 64,{yt:.1f} 70,{yt:.1f}" class="ln thin"/>',
      T(58, (ye + ym) / 2 + 4, "× κ", "t", "end"), T(58, (ym + yt) / 2 + 4, "≈ × 17", "t", "end")]
b += [f'<circle cx="{ax}" cy="{ye:.1f}" r="5" class="dot-e ring"/>',
      f'<circle cx="{ax}" cy="{ym:.1f}" r="5" class="dot-mu ring"/>',
      f'<circle cx="{ax}" cy="{yt:.1f}" r="5" class="dot-tau ring"/>',
      T(132, ye + 4, "e: 1, kernel of A", "t"),
      T(132, ym + 4, "μ: κ + 17/14 = 206.768", "t"),
      T(132, ym + 20, [("E", "n"), ("*", "sup"), ("·1 + m", "n"), ("e", "sub"), ("c", "n"), ("2", "sup"), ("·17/14", "n")], "t m"),
      T(132, yt + 4, "τ: 17κ − 17 = 3477.42", "t"),
      T(132, yt + 20, [("E", "n"), ("*", "sup"), ("·17 − m", "n"), ("e", "sub"), ("c", "n"), ("2", "sup"), ("·17", "n")], "t m"),
      T(132, 292, "κ = 3/(2α) = 205.554", "t m")]
P4 = svg(340, 300, "Masses in electron units on a logarithmic scale: electron 1, muon kappa plus 17 over 14, tau 17 kappa minus 17, with kappa = 3 over 2 alpha", b)

# ------------------------------------------------------------------ proton panel 1: two radii
b = [marker("ga5")]
cx, cy = 95, 128
b += [f'<circle cx="{cx}" cy="{cy}" r="85" class="ln"/>',
      f'<circle cx="{cx}" cy="{cy}" r="13" class="ln"/>',
      f'<line x1="{cx}" y1="{cy}" x2="{cx - 85}" y2="{cy}" class="ln thin" marker-end="url(#ga5)"/>',
      f'<line x1="{cx}" y1="{cy}" x2="{cx + 13}" y2="{cy}" class="ln"/>',
      T(cx - 44, cy - 7, [("ℓ", "n"), ("e", "sub"), (" = ħ/(m", "n"), ("e", "sub"), ("c)", "n")], "t halo", "middle"),
      T(cx, cy + 32, [("r", "n"), ("e", "sub"), (" = α ℓ", "n"), ("e", "sub")], "t halo", "middle"),
      T(cx, 238, [("not to scale: ℓ", "n"), ("e", "sub"), (" = 137 r", "n"), ("e", "sub")], "t m", "middle")]
lx = 280
b += [f'<line x1="246" y1="48" x2="314" y2="48" class="ln lev"/>',
      f'<line x1="246" y1="212" x2="314" y2="212" class="ln lev"/>',
      T(lx, 37, [("3ħc/(2r", "n"), ("e", "sub"), (")", "n")], "t", "middle"),
      T(lx, 231, [("3ħc/(2ℓ", "n"), ("e", "sub"), (")", "n")], "t", "middle"),
      f'<line x1="{lx}" y1="56" x2="{lx}" y2="204" class="ln" marker-start="url(#ga5)" marker-end="url(#ga5)"/>',
      T(lx - 8, 122, [("ΔE", "n"), ("S", "sub"), (" =", "n")], "t", "end"),
      T(lx - 8, 139, [("(3/2)(α", "n"), ("−1", "sup"), (" − 1)", "n")], "t", "end"),
      T(lx - 8, 156, [("× m", "n"), ("e", "sub"), ("c", "n"), ("2", "sup")], "t", "end")]
Q1 = svg(340, 260, "The lowest Dirac level compared between spheres of radius r_e and the Compton length l_e = r_e over alpha; the difference is three halves of alpha inverse minus one in electron rest energies", b)

# ------------------------------------------------------------------ proton panel 2: colour singlet
b = []
V = [(110, 58), (50, 162), (170, 162)]
b.append(f'<polygon points="{" ".join(f"{x},{y}" for x, y in V)}" class="ln"/>')
for (x, y), lab in zip(V, ["q1", "q2", "q3"]):
    b.append(f'<circle cx="{x}" cy="{y}" r="10" class="dot-p"/>')
    b.append(T(x, y + 4, [(lab[0], "n"), (lab[1], "sub")], "t on-fill", "middle"))
b += [T(70, 106, "3", "t", "end"), T(150, 106, "3", "t", "start"), T(110, 182, "3", "t", "middle"),
      T(110, 134, [("ε", "n"), ("abc", "sub")], "t", "middle")]
rx = 204
b += [T(rx, 56, "pair response", "t"),
      T(rx, 72, [("K", "n"), ("c", "sub"), (" σ", "n"), ("s", "sub"), (" = 9 σ", "n"), ("s", "sub")], "t m"),
      T(rx, 104, "mean colour charge", "t"),
      T(rx, 120, [("L", "n"), ("c", "sub"), (": singlet 0", "n")], "t m"),
      T(rx, 136, [("uncorrelated σ", "n"), ("0", "sub"), (": 1/3", "n")], "t m"),
      T(rx, 168, "screened by", "t"),
      T(rx, 184, [("f", "n"), ("α", "sub"), (" = 1 − α", "n"), ("2", "sup"), ("/(1−α)", "n")], "t m"),
      T(170, 220, [("m", "n"), ("p", "sub"), ("/m", "n"), ("e", "sub"), (" = 9 ΔE", "n"), ("S", "sub"), ("/(m", "n"), ("e", "sub"), ("c", "n"), ("2", "sup"), (") − f", "n"), ("α", "sub"), ("/3", "n")], "t", "middle"),
      T(170, 240, [("= 27/(2α) − 27/2 − 1/3 + α", "n"), ("2", "sup"), ("/(3(1−α))", "n")], "t", "middle")]
Q2 = svg(340, 260, "Three quarks in the antisymmetric colour singlet: three pairs each contribute 3 to the pair response, total 9; the mean colour charge is 0 on the singlet and 1/3 on the uncorrelated reference, screened by f_alpha", b)

section = f'''<section aria-labelledby="hgeo">
  <h2 id="hgeo">The construction at a glance</h2>
  <p>Figures G1 and G2 draw what the manuscript builds and where each number in its mass formulas comes from. Equation numbers refer to the manuscript.</p>
  <figure class="fig geo" aria-labelledby="g1t">
    <p class="fig-title" id="g1t">Figure G1 · From the sphere to the lepton masses, Eq. (4.5)</p>
    <div class="multiples">
      <div><p class="panel-title">1 · Round S³ and its lowest Dirac level, Eqs. (2.1)–(2.6)</p>{P1}</div>
      <div><p class="panel-title">2 · Matrix carrier W = End S and the operator C, Eqs. (3.1)–(3.6)</p>{P2}</div>
      <div><p class="panel-title">3 · Response weights and their minimum, Eqs. (5.5), (6.4), (6.13)</p>{P3}</div>
      <div><p class="panel-title">4 · Resulting masses, Eqs. (7.3)–(7.4)</p>{P4}</div>
    </div>
    <figcaption>(1) The round S³ of radius \\(r_e\\) has two Killing spinors of each sign at \\(\\lambda r = \\pm3/2\\); they form the carrier \\(S\\) and fix \\(E_* = \\kappa m_ec^2\\). (2) The 16 Clifford words of \\(\\mathcal W = \\mathrm{{End}}\\,S\\) split under \\(\\mathcal C\\) into the scalar line (e), 14 harmonic directions (μ) and the pseudoscalar line (τ); \\(\\mathcal C\\) maps the pseudoscalar to four times the scalar, which gives the τ weight \\(1+4^2\\). (3) The trace-preserving minimum moves the τ weight into the harmonic block. (4) Leading weights times \\(E_*\\) plus the change \\(B\\) in units of \\(m_ec^2\\) give the three masses.</figcaption>
  </figure>
  <figure class="fig geo" aria-labelledby="g2t">
    <p class="fig-title" id="g2t">Figure G2 · The proton extension, Eqs. (10.1)–(10.12)</p>
    <div class="multiples">
      <div><p class="panel-title">Relative energy between two radii, Eqs. (10.6)–(10.7)</p>{Q1}</div>
      <div><p class="panel-title">Colour singlet and its two responses, Eqs. (10.2)–(10.10)</p>{Q2}</div>
    </div>
    <figcaption>The proton uses the same lowest level, compared between radius \\(r_e\\) and the reduced Compton length \\(\\ell_e = r_e/\\alpha\\), weighted by the pair response 9 of the colour singlet, minus the screened mean-charge term 1/3. Both prescriptions are specific to the proton; the leptons use the absolute level \\(E_*\\).</figcaption>
  </figure>
</section>
'''
open("geo_section.html", "w", encoding="utf8").write(section)
print(len(section))
