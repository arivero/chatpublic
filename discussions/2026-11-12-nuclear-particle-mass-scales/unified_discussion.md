# Nuclear landmarks and electroweak masses: the unified discussion

Conversation of 12 November 2026. This document gathers in one place the author's brief, the two replies supplied by other agents (called A and B), and the passes of analysis made in this folder, and it writes out the mathematics behind each point. Sections 7 to 9 are new: they collect the ways in which masses that originate in the Higgs field and masses that originate in QCD can be tied together, including the exact results of supersymmetric gauge theory (holomorphic scale matching, Seiberg duality, Seiberg-Witten theory).

**Working hypothesis.** The relations of section 1 are treated as physical statements. The chance reading yields no prediction, and at the author's request the document leaves it aside. Every section asks the same question: what must be true for the relations to hold, and how can that be tested?

Numbers come from `calculations/audit.py`, `calculations/scale_links.py` and `calculations/fission_yields_check.py`, with outputs stored next to the scripts. Inputs and provenance are in `data/README.md`. The claim-by-claim audit of the brief and of the two replies is in `notes/01_audit_and_errata.md` and `notes/04_error_check.md`.

## Contents

1. The relations
2. The mathematics behind the three relations
3. The fission and fermium associations
4. What the relations pin in the Standard Model
5. Constraints that every explanation must respect
6. Three logical forms of an explanation
7. Links that already exist inside the Standard Model
8. Routes that turn v / Lambda_QCD into a pure number
9. Exact results of supersymmetric gauge theory
10. Fixing the quartic coupling and the charm Yukawa coupling
11. The fission-side hypotheses
12. Catalogue of explanations
13. Programme
14. References

## 1. The relations

### 1.1 Inputs and conventions

* Atomic masses from AME2020: $M_\mathrm{at}(A,Z) = A\,u + \Delta(A,Z)$, with $u = 931.49410242$ MeV and $\Delta$ the mass excess. Nuclear masses follow from $M_\mathrm{nuc} = M_\mathrm{at} - Z m_e + B_e(Z)$ with the electron binding energy $B_e(Z) = 14.4381\,Z^{2.39} + 1.55468\times 10^{-6}\,Z^{5.35}$ eV. For tin this removes 25.38 MeV per nucleus.
* The electroweak scale is $v = (\sqrt{2}\,G_F)^{-1/2} = 246.2196$ GeV.
* The tabulated Z mass, 91.1880 GeV, is a Breit-Wigner parameter. The pole mass is $M_Z/\sqrt{1+\Gamma_Z^2/M_Z^2} = 91.1539$ GeV, lower by 34 MeV.
* Higgs mass: 125.20 ± 0.11 GeV (PDG 2025, the value of the brief), 125.13 ± 0.11 (PDG 2026), 125.09 ± 0.07 (ATLAS and CMS preliminary combination, LHCP 2026), 125.065 ± 0.088 (CMS, 2 November 2026).
* $m_{D^0} = 1864.84 \pm 0.05$ MeV, $M_\alpha = 3727.3794$ MeV.

### 1.2 Three relations

```math
\begin{aligned}
\text{R1:}\quad & v = 2\,M(^{132}\mathrm{Sn})\,(1+\delta_1) \\
\text{R2:}\quad & M_Z + M_H = \left[M(^{100}\mathrm{Sn}) + M(^{132}\mathrm{Sn})\right](1+\delta_2) \\
\text{R3:}\quad & 2\,m_{D^0} = M_\alpha\,(1+\delta_3)
\end{aligned}
```

| Relation | Left side | Right side | Offset |
| --- | --- | --- | --- |
| R1 | 246.2196 GeV | 245.7613 GeV | $\delta_1$ = +0.186% (nuclear masses: +0.207%) |
| R2 | 216.388 GeV (PDG 2025) | 215.9729 GeV | $\delta_2$ = +0.192%; +0.160% (PDG 2026); +0.141% (LHCP); +0.130% (CMS) |
| R3 | 3729.68 MeV | 3727.379 MeV | $\delta_3$ = +0.0617%, a remainder of 2.301 ± 0.10 MeV |

For R2, nuclear masses add 0.024% and the pole Z mass subtracts 0.016%. Each relation pins one parameter of the Standard Model: R1 the ratio $v/\Lambda_\mathrm{QCD}$, R2 the quartic coupling $\lambda$ once the gauge couplings are given, R3 the charm Yukawa coupling in units of $\Lambda_\mathrm{QCD}/v$ (section 4).

Two members of the 2003 set stay outside: the top quark lies 10.9% below $^{208}$Pb, and $2m_B = 10.56$ GeV has no light-nucleus partner within 3%.

### 1.3 One unit for the three relations

The three relations can be written with one mass unit $m_\ast$:

```math
v = 264\,m_\ast, \qquad M_Z + M_H = 232\,m_\ast, \qquad m_{D^0} = 2\,m_\ast .
```

| Quantity | $m_\ast$ (MeV) | Relative to $u$ |
| --- | --- | --- |
| $v/264$ | 932.650 | +0.124% |
| $m_{D^0}/2$ | 932.420 | +0.099% |
| $(M_Z+M_H)/232$, PDG 2025 | 932.707 | +0.130% |
| $(M_Z+M_H)/232$, PDG 2026 | 932.405 | +0.098% |
| $(M_Z+M_H)/232$, LHCP 2026 | 932.233 | +0.079% |
| $(M_Z+M_H)/232$, CMS November 2026 | 932.125 | +0.068% |
| $M(^{132}\mathrm{Sn})/132$ | 930.914 | -0.062% |
| $[M(^{100}\mathrm{Sn})+M(^{132}\mathrm{Sn})]/232$ | 930.918 | -0.062% |
| $M_\alpha/4$ | 931.845 | +0.038% |
| free nucleon, mean of p and n | 938.919 | +0.797% |

The three particle-side quantities agree on a unit between 932.1 and 932.7 MeV, a spread of $6\times10^{-4}$. That unit lies 0.07% to 0.13% above $u$ and 6.2 to 6.8 MeV below the free nucleon mass, close to the binding per nucleon of $^{9}$Be and $^{10}$B (6.5 MeV). Nuclei themselves follow $M \simeq A\,u$ within about 0.1% from boron upward, which is the reason $u$ works as a unit. In this language the electroweak quantities sit on the nuclear mass surface with the integers 264 and 232.

The same content without any nuclear mass:

```math
v : (M_Z + M_H) : m_{D^0} = 132 : 116 : 1 .
```

The measured ratios are $v/m_{D^0} = 132.033$ and $(M_Z+M_H)/m_{D^0} = 116.036 \pm 0.059$ (PDG 2025), $115.998 \pm 0.059$ (PDG 2026), $115.977 \pm 0.038$ (LHCP), $115.963 \pm 0.047$ (CMS). The second ratio agrees with 116 within the Higgs-mass uncertainty for every input. The first differs from 132 by $2.5\times10^{-4}$, nine standard deviations of the $D^0$ mass. Nuclear physics enters this form through the integers, $132 = 50 + 82$ and $232 = 100 + 132$, and through the fact that the unit is a bound-nucleon mass.

### 1.4 Dates

* November 2003 (arXiv:nucl-th/0312003): the boson masses are compared with the subshell intervals that end at the doubly magic corners $^{100}$Sn, $^{132}$Sn and $^{208}$Pb; the only Higgs candidate is the 115 GeV hint.
* May 2004 (arXiv:hep-ph/0405076): a drip-line version listing 45, 68, 92, 115, 175 and 246 GeV, retired by the author.
* 2012 onward: the measured Higgs mass makes the pair sum R2 available.
* 2026: R1 and R3 in the present form, and the numerical audit.

## 2. The mathematics behind the three relations

### 2.1 The ratio form of R2 and its exact completions

Dividing R2 by R1 removes the nuclear mass scale:

```math
\frac{M_Z + M_H}{v} = \frac{M(^{100}\mathrm{Sn}) + M(^{132}\mathrm{Sn})}{2\,M(^{132}\mathrm{Sn})}\;\frac{1+\delta_2}{1+\delta_1}.
```

The tin ratio equals 0.878791, within 3.9 ppm of $232/264 = 29/33 = 0.878788$, because the two tins have nearly the same mass excess per nucleon (-0.580 and -0.571 MeV) and the same number of electrons. Since $\delta_1 \simeq \delta_2$, the pair of relations contains the purely electroweak statement

```math
\frac{M_Z + M_H}{v} = \frac{29}{33}
\qquad\Longleftrightarrow\qquad
M_H - \frac{v}{2} = \frac{25}{66}\,v - M_Z .
```

The second form says that the Higgs boson lies above $v/2$ by the amount by which the Z boson lies below $25v/66$; the two displacements are 2.090 and 2.077 GeV with PDG 2025. At tree level $M_Z/v = \tfrac12\sqrt{g^2+g'^2}$ and $M_H/v = \sqrt{2\lambda}$, so the statement fixes the quartic coupling in terms of the gauge couplings:

```math
\sqrt{2\lambda} = \frac{29}{33} - \frac{1}{2}\sqrt{g^2 + g'^2}\;\;\Rightarrow\;\; \lambda = 0.1293 .
```

Measured deviations of $(M_Z+M_H)/v$ from 29/33: $+5.3\times10^{-5}$ (PDG 2025), $-2.3\times10^{-4}$ (PDG 2026), $-3.9\times10^{-4}$ (LHCP), $-5.0\times10^{-4}$ (CMS). The resolution set by the Higgs mass is $4.5\times10^{-4}$ for the PDG entries, so these are +0.1, -0.5, -1.4 and -1.4 standard deviations. Through the PDG editions 2016 to 2025 the deviation stayed within one standard deviation (audit section 7).

The approximate relations admit several exact completions. Each is a prediction of the Higgs mass:

| Completion | $M_H$ (GeV) | Pull PDG 2026 | Pull LHCP | Pull CMS |
| --- | --- | --- | --- | --- |
| B: $2M(^{232}\mathrm{Th}) - M(^{132}\mathrm{Sn}) - M(^{100}\mathrm{Zr}) - M_Z^\mathrm{pole}$ | 125.132 | -0.02 | -0.60 | -0.76 |
| unit form: $116\,m_{D^0} - M_Z$ | 125.133 | -0.03 | -0.62 | -0.78 |
| $\tfrac{29}{33}v - M_Z$ | 125.187 | -0.52 | -1.38 | -1.39 |
| $\tfrac{29}{33}v - M_Z^\mathrm{pole}$ | 125.221 | -0.83 | -1.87 | -1.77 |
| A: $v - M_Z + M(^{100}\mathrm{Sn}) - M(^{132}\mathrm{Sn})$ | 125.243 | -1.03 | -2.19 | -2.03 |

The pulls are (measured minus predicted) over the experimental uncertainty. A Higgs mass known to 0.02 or 0.03 GeV separates the five. Two remarks on precision. The quantity $v$ defined from $G_F$ is an observable, while the tree-level translation into $g$, $g'$ and $\lambda$ depends on the renormalization scheme at the $10^{-3}$ level, so a sharp relation has to be stated for observables. The Z-mass convention alone moves the prediction by 34 MeV.

### 2.2 Granularity

Every mass lies within $0.5\,u$ of an integer multiple of $u$. The offsets of the tin relations in these units are

```math
\frac{v}{2} - M(^{132}\mathrm{Sn}) = 0.246\,u, \qquad M_Z + M_H - M(^{100}\mathrm{Sn}) - M(^{132}\mathrm{Sn}) = 0.446\,u ,
```

while the single offsets are $+2.49\,u$ (H against $^{132}$Sn) and $-2.04\,u$ (Z against $^{100}$Sn). The pair $(^{100}\mathrm{Sn}, ^{132}\mathrm{Sn})$ was named in 2003, before the Higgs mass was known, so the offset of R2 measures the distance to a preset target. The content of R1 beyond rounding is the identity of the integer: $264 = 2(50+82)$ among its neighbours, which are $7.9\times10^{-5}$ apart in $\alpha_s(M_Z)$ (section 4.3).

### 2.3 The charm relation

With $B_\alpha = 2m_p + 2m_n - M_\alpha = 28.296$ MeV,

```math
2m_{D^0} - M_\alpha = 2.301 \pm 0.10\ \mathrm{MeV}, \qquad 2m_p + 2m_n - 2m_{D^0} = 25.995\ \mathrm{MeV}, \qquad m_{D^0} = \tfrac12 M_\alpha + 1.150\ \mathrm{MeV}.
```

The charged threshold $2m_{D^\pm}$ lies 11.94 MeV above $M_\alpha$, so the match belongs to the neutral pair. Two surveys place it in context (audit section 14):

* Nineteen mesons from the kaons to the $\Upsilon(4S)$, taken singly and as pair thresholds, against fourteen nuclei from the deuteron to $^{16}$O. The entries below 1% are all charmed: $2m_{D^0}$ against $^4$He (+0.06%), $m_{D^\pm}$ against $d$ (-0.32%), $2m_{D^\pm}$ against $^4$He (+0.32%), $m_{D^0}$ against $d$ (-0.57%). The next entry is $\Upsilon(1S)$ against $^{10}$B at +1.46%.
* The remainder of 2.301 MeV against nineteen light-nucleus energies (binding energies of $d$, $t$, $^3$He, $^4$He; $m_n - m_p$; $m_e$ and $2m_e$; $m_{D^\pm}-m_{D^0}$; eleven fusion and breakup Q-values). One lies within a standard deviation: the deuteron binding energy $B_d = 2.2246$ MeV, leaving $0.076 \pm 0.10$ MeV. The next candidate is 9.7 standard deviations away.

The completed form and its prediction:

```math
2m_{D^0} + M_d = M_\alpha + m_p + m_n \;\;\Rightarrow\;\; m_{D^0} = 1864.802\ \mathrm{MeV}, \qquad \frac{m_{D^0}}{2} = m_N - \frac{B_\alpha - B_d}{4} .
```

PDG 2026 gives $1864.84 \pm 0.04$ MeV. The completion was found in this folder among nineteen candidates and carries that label.

### 2.4 The magic numbers and the 2003 bracketing

The harmonic-oscillator shell $n$ closes at $(n+1)(n+2)(n+3)/3$ nucleons. The spin-orbit force lowers the level $j = n + \tfrac32$ of the next shell, which holds $2(n+2)$ nucleons, into shell $n$. The closures become

```math
\mathcal{M}(n) = \frac{(n+1)(n+2)(n+3)}{3} + 2(n+2) = \frac{(n+2)(n^2+4n+9)}{3} = 28,\ 50,\ 82,\ 126,\ 184 \quad (n = 2,\dots,6).
```

The landmarks of the relations are sums of these numbers: $100 = 2\mathcal{M}(3)$, $132 = \mathcal{M}(3)+\mathcal{M}(4)$, $208 = \mathcal{M}(4)+\mathcal{M}(5)$, $264 = 2[\mathcal{M}(3)+\mathcal{M}(4)]$, $232 = 3\mathcal{M}(3)+\mathcal{M}(4)$.

The 2003 text draws, below each doubly magic corner, the rectangle of nuclei in which the two intruder subshells are filling. In mass number the rectangles span $[82, 100]$, $[112, 132]$ (or $[106, 126]$ with the Klinkenberg subshell order) and $[184, 208]$. The boson positions are $W = 86.3$, $Z = 97.9$, top $= 185.3$, all inside, and the 115 GeV hint at 123.5, inside. The measured Higgs mass sits at 134.41, which is 2.4 mass units beyond the $^{132}$Sn corner. The tin relations R1 and R2 are therefore a second statement, of nearest-nucleus type, with the dates given in section 1.4.

## 3. The fission and fermium associations

In mass-number units the bosons sit at $W = 86.28$, $Z = 97.89$, $H = 134.41$, and $v = 264.33$.

### 3.1 Fragment modes

Low-energy fission of the actinides is described by a symmetric mode and two asymmetric modes, Standard I and Standard II. The measured positions are:

* **Charge.** In the GSI secondary-beam data (15 systems from $^{223}$Ac to $^{234}$U, Böckstiegel et al. 2008) the heavy-fragment charges are $Z_H(\mathrm{S1}) = 52.73 \pm 0.58$ and $Z_H(\mathrm{S2}) = 55.18 \pm 0.57$, mean and scatter over the systems.
* **Mass from charge.** The unchanged-charge-density rule $A_H = Z_H\,A/Z$ gives $132.6 \pm 1.4$ and $138.8 \pm 1.4$. Five of the fifteen systems have $A_H(\mathrm{S1})$ within one unit of 134.4.
* **Mass after neutron emission** (ENDF/B-VIII.0). The largest single-mass yield of the heavy group is at $A = 134$ for $^{235}$U and $^{239}$Pu with thermal neutrons and for $^{238}$U with fast neutrons. The centroids of the heavy group are 138.1 to 139.7 from thorium to plutonium and 142.0 for $^{252}$Cf. The light centroids are 91.1 ($^{232}$Th), 93.4, 94.9, 97.4, 99.0 ($^{239}$Pu) and 106.1 ($^{252}$Cf).

The Higgs value coincides with the Standard I component at the level of two mass units, and the heavy group as a whole is centred four to five units higher. The light group moves with the parent as $A_L = A - A_H$; it passes the Z value near $^{238}$U and $^{239}$Pu and reaches the W value for parents near $A = 228$.

### 3.2 The symmetric-to-asymmetric transition

In the GSI data (excitation energy near 11 MeV) the share $s$ of asymmetric fission behaves as a function of the parent mass number. Isobars agree ($A = 232$: 82.1% and 81.9%; $A = 228$: 62.5% and 64.5%; $A = 223$: 16.0% and 11.6%), and isotones differ by up to 12.6 points. A logistic fit gives

```math
s(A) = \frac{100}{1 + e^{-(A - A_{50})/w}}, \qquad A_{50} = 226.93, \quad w = 2.65 ,
```

with an rms residual of 3.9 points. For comparison $(M_H + M_W)/u = 220.69$, $(M_H + M_Z)/u = 232.30$, and their midpoint is 226.49.

### 3.3 Energetics

The ground-state energy release of a binary split is $Q = M(A,Z) - M(A_H,Z_H) - M(A-A_H, Z-Z_H)$. Maximized over $Z_H$ at each $A_H$ with AME2020 masses, it peaks at the tin-like split $A_H = 130$ to 132, $Z_H = 50$, for $^{226}$Th, $^{232}$Th, $^{236}$U, $^{240}$Pu and $^{252}$Cf (188.8, 188.4, 199.3, 210.3, 236.8 MeV). The tellurium split at $A_H = 134$ lies 0.2 to 4 MeV lower. In particular $Q(^{232}\mathrm{Th} \to {}^{132}\mathrm{Sn} + {}^{100}\mathrm{Zr}) = 188.4$ MeV, and self-consistent calculations describe the hyperdeformed configuration of $^{232}$Th as a quasi-molecule of these two fragments (Zhang, Schuetrumpf and Nazarewicz 2016), with a shallow third minimum (McDonnell, Nazarewicz and Sheikh 2013).

### 3.4 Fermium

The partial half-life for spontaneous fission is $T_\mathrm{SF} = T_{1/2}/b_\mathrm{SF}$. In the WKB picture

```math
T_\mathrm{SF} \propto \exp\!\left(\frac{2S}{\hbar}\right), \qquad S = \int \sqrt{2\,B(q)\,[V(q) - E]}\;dq ,
```

with $V(q)$ the barrier along the fission path and $B(q)$ the collective inertia.

| Nuclide | $T_{1/2}$ | SF branch | $T_\mathrm{SF}$ |
| --- | --- | --- | --- |
| $^{254}$Fm | 3.240 h | 0.0592% | 0.62 y |
| $^{256}$Fm | 157.1 min | 91.9% | 2.85 h |
| $^{257}$Fm | 100.5 d | 0.210% | 131 y |
| $^{258}$Fm | 0.37 ms | about 100% | 0.37 ms |
| $^{259}$Fm | 1.5 s | 100% | 1.5 s |

Between the even isotopes $^{256}$Fm and $^{258}$Fm the partial half-life falls by $2.8\times10^{7}$, a change of the action by $8.6\,\hbar$; the previous even step, 254 to 256, is a factor $1.9\times10^{3}$. From $^{257}$Fm to $^{258}$Fm the factor is $1.1\times10^{13}$ ($15.0\,\hbar$), which includes the hindrance of the odd neutron: $^{257}$Fm lives $2\times10^{9}$ times longer than the geometric mean of its even neighbours. The energy release for a split into two tin isotopes rises smoothly, from 248.8 MeV at $A = 252$ to 256.0 MeV at $A = 260$, so the collapse of the half-life is a barrier effect. The symmetric fragments of $^{258}$Fm are $^{129}$Sn; $^{264}$Fm equals two $^{132}$Sn in proton and neutron number, lies beyond the measured isotopes, and is predicted to fission symmetrically through two $^{132}$Sn-like prefragments (Bernard et al. 2024; Chen et al. 2026).

## 4. What the relations pin in the Standard Model

### 4.1 Parameter map

```math
M_W = \tfrac12\,g\,v, \qquad M_Z = \tfrac12\,v\sqrt{g^2 + g'^2}, \qquad M_H = v\sqrt{2\lambda}, \qquad m_q = \frac{y_q\,v}{\sqrt2} .
```

Nuclear masses are $M(A,Z) = Z m_p + N m_n - B(A,Z)$, and the nucleon mass is set by QCD. R1 fixes $v/\Lambda_\mathrm{QCD}$, R2 fixes $\lambda$ given $g$ and $g'$, R3 fixes $y_c\,v/\Lambda_\mathrm{QCD}$.

### 4.2 The Higgs-originated part of a nuclear mass

The nucleon mass is the matrix element of the trace of the energy-momentum tensor. To leading order

```math
\theta^\mu{}_\mu = \frac{\beta(g)}{2g}\,G^a_{\mu\nu}G^{a\,\mu\nu} + \sum_q m_q\,\bar q q , \qquad m_N = \langle N|\,\theta^\mu{}_\mu\,|N\rangle , \qquad \frac{\beta(g)}{2g} = -\frac{b_0\,\alpha_s}{8\pi}, \quad b_0 = 11 - \tfrac23 n_f .
```

A heavy quark can be traded for gluons, $m_Q\bar Q Q \to -\frac{\alpha_s}{12\pi}G^2$ (Shifman, Vainshtein and Zakharov 1978), which cancels its share of $b_0$. With $c$, $b$, $t$ removed, $\theta^\mu{}_\mu = -\frac{9\alpha_s}{8\pi}G^2 + \sum_{u,d,s} m_q\bar q q$. Writing $f_{Tq} = \langle N|m_q\bar q q|N\rangle/m_N$ for the light quarks, each heavy quark carries $f_{TQ} = \tfrac{2}{27}\big(1 - \sum_{uds} f_{Tq}\big)$ and

```math
f_N \equiv \sum_{\text{all } q} f_{Tq} = \sum_{uds} f_{Tq} + \frac{2}{9}\Big(1 - \sum_{uds} f_{Tq}\Big) = 0.28 \text{ to } 0.32 \quad \text{for} \quad \sum_{uds} f_{Tq} = 0.08 \text{ to } 0.12 .
```

The Feynman-Hellmann theorem, $\partial m_N/\partial m_q = \langle N|\bar q q|N\rangle$, turns this into a response to the Higgs field at fixed Yukawa couplings and fixed ultraviolet QCD coupling:

```math
K_N \equiv \frac{\partial \ln m_N}{\partial \ln v} = f_N , \qquad g_{hNN} = \frac{f_N\,m_N}{v} = 1.2\times10^{-3} .
```

The same exponent follows from decoupling. Continuity of $\alpha_s$ at each heavy-quark threshold gives, at one loop,

```math
\Lambda_3^{\,9} = \Lambda_6^{\,7}\,(m_c\,m_b\,m_t)^{2/3} \quad\Longrightarrow\quad \Lambda_3 = \Lambda_6^{7/9}\,(m_c\,m_b\,m_t)^{2/27} .
```

For a nucleus $K_A = f_N$ up to corrections of relative size $B/M \simeq 0.9\%$. Between 35 and 39 GeV of the 122.9 GeV of $^{132}$Sn respond to $v$: about 30% of every nuclear mass is Higgs-originated in this sense, and 70% scales with the six-flavour QCD scale.

### 4.3 R1 expressed as the strong coupling

With $\beta(\alpha_s) = d\alpha_s/d\ln\mu$, the scale $\Lambda = \mu\exp[-\int^{\alpha_s(\mu)} d\alpha/\beta(\alpha)]$ satisfies

```math
\frac{d\ln\Lambda_5}{d\alpha_s(M_Z)} = \frac{1}{|\beta|} = 56, \qquad |\beta| = \frac{b_0\,\alpha_s^2}{2\pi} + \frac{b_1\,\alpha_s^3}{8\pi^2} = 0.0178 \quad (n_f = 5,\ b_0 = \tfrac{23}{3},\ b_1 = \tfrac{116}{3}) ,
```

and $\Lambda_3 \propto \Lambda_5^{23/27}$ brings the slope of $\ln m_N$ to 48. The offset $\delta_1 = 0.186\%$ therefore corresponds to $\delta\alpha_s = 3.9\times10^{-5}$, and one unit of mass number at $A = 264$ to $7.9\times10^{-5}$. The world average $0.1180 \pm 0.0009$ spans about 23 consecutive integers. Since the running is smooth, the preference for 132 has to come from the structure that produces the integer.

### 4.4 The one-parameter family

Let $v$ vary with the Yukawa couplings, the gauge couplings, $\lambda$ and the ultraviolet QCD coupling held fixed. Electroweak masses scale as $v$, nuclear masses as $v^{K_A}$, and the $D^0$ mass as $v^{K_D}$ with $K_D \simeq (m_c + \tfrac29\bar\Lambda)/m_D = 0.75$ to 0.9 from the heavy-quark expansion $m_D = m_c + \bar\Lambda + \dots$. The ratios of the two sides then run as

```math
R_{1,2}(v) \propto v^{\,1-K_A}, \qquad R_3(v) \propto v^{\,K_D - K_\alpha}, \qquad \delta\ln v\,\big|_{R_i = 1} = -\frac{\ln R_i}{\text{exponent}} .
```

With $K_A = 0.30$, R1 becomes exact at $\delta\ln v = -0.266\%$ and R2 at $-0.274\%$ (PDG 2025) or $-0.228\%$ (PDG 2026). R3 becomes exact at $-0.11\%$ for $K_D = 0.85$ and would join the other two for $K_D = 0.53$. R1 and R2 thus behave as one statement about $v/\Lambda_\mathrm{QCD}$ plus the electroweak ratio 29/33, and R3 is independent.

### 4.5 Requirements

| Relation | Parameter | Precision asked of a mechanism |
| --- | --- | --- |
| R1 | $\alpha_s(M_Z)$, equivalently $v/\Lambda_\mathrm{QCD}$ | $3.9\times10^{-5}$ in $\alpha_s$; the integer 264 among neighbours $7.9\times10^{-5}$ apart |
| R2 | $\lambda$ | 0.16% in $\lambda$ for each 0.1 GeV of $M_H$; a statement in terms of observables |
| R3 | $y_c$ | 0.09% of $m_c$ (1.15 MeV) for the full remainder |
| all | the integers | a rule that names sums of magic numbers |

## 5. Constraints that every explanation must respect

These points come from the brief and are kept as fixed ground.

### 5.1 Strength of electroweak exchange

Static exchange of a boson of mass $M$ with coupling $g$ gives $V(r) = \pm\frac{g^2}{4\pi}\frac{e^{-Mr}}{r}$. For $Mr \gg 1$ it acts as a contact term of strength $g^2/M^2$, and in nuclear matter of density $\rho$ the mean-field energy per nucleon is

```math
\epsilon = \frac{g^2\,\rho}{2M^2} .
```

| Exchange | Coupling | $g^2/M^2$ (GeV$^{-2}$) | $\epsilon$ at $\rho = 0.16$ fm$^{-3}$ |
| --- | --- | --- | --- |
| $\omega$ | $g = 10.6$ | 183 | 113 MeV |
| $\sigma$ | $g = 10$, $m = 0.55$ GeV | 331 | 203 MeV |
| Z, vector, weak charge | $g/(4\cos\theta_W) = 0.185$ | $4.1\times10^{-6}$ | 0.89 eV |
| Higgs | $f_N m_N/v = 1.16\times10^{-3}$ | $8.6\times10^{-11}$ | $5.3\times10^{-5}$ eV |

The ratios are $2\times10^{-8}$ for Z against $\omega$ and $3\times10^{-13}$ for the Higgs against $\sigma$, the orders quoted in the brief, and hadronic parity violation confirms the $10^{-7}$ scale. The bosons mark the closures; the strong force makes them.

### 5.2 Propagator

An exchange amplitude is proportional to $1/(q^2 - M^2)$ with $|q| \simeq 250$ MeV inside a nucleus. The rest mass of the nucleus appears in no denominator.

### 5.3 Baryon number

Baryon number is a superselection rule: $\langle B = 0|\,\mathcal{O}\,|B = A\rangle = 0$ for every operator that conserves it. A boson and a nucleus have no mixing, and an intermediate state made of the nucleus plus Z and H lies 216 GeV above the nucleus.

### 5.4 Coherent couplings

Both neutral bosons couple to the whole nucleus at low momentum transfer. For the Higgs, $g_{hAA} = \partial M_A/\partial v = K_A M_A/v = 0.15$ for $^{132}$Sn. For the Z, the vector coupling is $g\,Q_W/(4\cos\theta_W)$ with the weak charge $Q_W = N - (1 - 4\sin^2\theta_W)Z$, which gives 14.8 for $^{132}$Sn, above $4\pi$. The nuclear form factor $F(q) \simeq \exp(-q^2R^2/6)$ confines the coherence to $q \lesssim 1/R \simeq 32$ MeV, three thousand times below $M_Z$. Coherent neutrino-nucleus scattering demonstrates the coupling experimentally. These couplings give smooth responses and no feature at a mass equality.

### 5.5 Spin-orbit splitting

For a Dirac nucleon in a scalar potential $S$ and a vector potential $V$, with $m_\mathrm{eff} = m + \tfrac12(S - V)$, the reduction to the large component gives a central potential $V + S$ and

```math
U_\mathrm{so} = \frac{1}{2\,m_\mathrm{eff}^2}\,\frac{1}{r}\,\frac{d(V - S)}{dr}\;\boldsymbol{\ell}\cdot\boldsymbol{s} .
```

With $V \simeq +350$ MeV and $S \simeq -400$ MeV the central depth is 50 MeV while the spin-orbit term is driven by $V - S \simeq 750$ MeV. In meson language these are the $\omega$ and the effective $\sigma$ field; the $\rho$, through its tensor coupling, distinguishes neutrons from protons. A pure scalar potential $U$ reproduces the Thomas term $-\frac{1}{2m^2}\frac1r\frac{dU}{dr}\,\boldsymbol\ell\cdot\boldsymbol s$, and a pure vector potential reproduces the atomic formula with the opposite sign. The observed splitting, which lowers $j = \ell + \tfrac12$, therefore has the sign of the Thomas term of the net potential and exceeds it by $\frac{|V - S|}{|V + S|}\,(m/m_\mathrm{eff})^2$, a factor 15 to 40.

**Correction to the brief.** The brief describes the required strength as an order of magnitude above the Thomas term "and of opposite sign". The sign is opposite to the atomic (magnetic plus Thomas) formula applied to the nuclear potential; it agrees with the Thomas term itself.

### 5.6 Status of the derivations of shell structure

The shell model and its spin-orbit term date from 1949. Present ab initio theory solves the many-body problem from nucleon forces fitted to two- and three-body data; in chiral effective field theory the short-range physics sits in fitted contact constants; lattice QCD reaches $A \le 4$. The closures at 50, 82 and 126 are reproduced with fitted strengths and await a derivation from QCD.

## 6. Three logical forms of an explanation

Under the working hypothesis an explanation takes one of three forms.

**(a) A relation among constants.** The parameters of the Lagrangian are tied by a symmetry, a fixed point or a boundary condition. Sections 7, 8 and 10 collect the known structures of this kind. The tests are the values of $\alpha_s$, $M_H$ and $m_c$ at the precision of section 4.5, together with the new states that each structure requires.

**(b) A dynamical selection.** A field scans a parameter and stops at a feature. The feature has to be as sharp as the offsets, about 0.3% of $v$. Among nuclear thresholds, the experimental entries of AME2020 contain no nuclide within 6 keV of a nucleon or alpha threshold. The sharpest features are two weak-decay thresholds, $^{187}\mathrm{Re} \to {}^{187}\mathrm{Os}$ ($Q = 2.47$ keV) and $^{163}\mathrm{Ho} \to {}^{163}\mathrm{Dy}$ ($Q = 2.83$ keV), which change sign within 0.05% to 0.3% of $v$; neither involves tin or charm. Published anthropic windows are 8 to 90 times wider than the offsets. Sections 8.6 and 9.3 give the two selection mechanisms with exact or controlled mathematics.

**(c) A common mass formula.** The masses on both sides are values of one function of conserved charges. Mass relations across superselection sectors then follow from the function itself, with no mixing between the sectors. The prototype is the central-charge formula of extended supersymmetry (section 9.3). This form is where the suggestion of the brief, "states carrying the nucleus's own baryon number", leads. Reply A phrased it as a competing branch $X_A$ with $M_X \propto v^{K_X}$: at the observed $v$ its splitting from the nucleus would be $0.33\,(K_X - K_A)$ GeV, and a state that draws its whole mass from the Higgs field ($K_X = 1$) would need a Yukawa coupling $\sqrt2\,M_A/v = 0.71$, which restates R1. The Standard Model has no such state, and form (c) replaces it by a statement about the mass formula.

The unit formulation of section 1.3 reads differently in the two static forms. In form (a) it is two numerical conditions, $v/m_\ast = 264$ and $\tfrac12\sqrt{g^2+g'^2} + \sqrt{2\lambda} = \tfrac{29}{33}$. In form (c) the numbers 264, 232 and 2 are charges of one central charge with unit $m_\ast$. Form (c) also accounts for a feature that the brief stressed: the sum $M_Z + M_H$ is sharp while the single masses are displaced by $\pm 2.08$ GeV. That is the signature of two aligned central charges whose individual values contain a second period that cancels in the sum.

## 7. Links that already exist inside the Standard Model

Five ties between the Higgs sector and QCD are part of the Standard Model.

### 7.1 Heavy-quark thresholds

Section 4.2: $\Lambda_3 = \Lambda_6^{7/9}(m_c m_b m_t)^{2/27}$. Each heavy Yukawa coupling enters every hadron mass with the exponent 2/27, and nuclear masses scale as $v^{0.3}$.

### 7.2 QCD breaks the electroweak symmetry too

The quark condensate carries weak isospin, so the pions add to the mass of the gauge bosons:

```math
M_W^2 = \frac{g^2}{4}\left(v^2 + f_\pi^2\right), \qquad \text{eaten Goldstone boson} = \frac{v\,\phi^\pm + f_\pi\,\pi^\pm}{\sqrt{v^2 + f_\pi^2}} .
```

With $f_\pi = 92.3$ MeV the admixture is $f_\pi/v = 3.75\times10^{-4}$ and the shift is $\delta M_W/M_W = f_\pi^2/2v^2 = 7.0\times10^{-8}$. In a world without the Higgs potential the same formula gives $M_W = g f_\pi/2 = 30$ MeV and $M_Z = 34$ MeV: the electroweak masses would be QCD-originated with a fixed ratio. The number that separates the two worlds is $v/f_\pi = 2668$.

### 7.3 Condensates

The vacuum counterpart of section 4.2 is $m_Q\langle\bar Q Q\rangle = -\tfrac{1}{12}\langle\tfrac{\alpha_s}{\pi}G^2\rangle$ for each heavy quark, and $(m_u + m_d)\,|\langle\bar q q\rangle| = m_\pi^2 f_\pi^2$ for the light ones. Through the Yukawa terms these condensates act as a source for the Higgs field and shift its vacuum value by $\delta v = \sum_q m_q|\langle\bar q q\rangle|/(v\,M_H^2) \sim 10^{-9}$ GeV.

### 7.4 The infrared structure of the top Yukawa coupling

At one loop, with $t = \ln\mu$ and the electroweak couplings dropped,

```math
16\pi^2\,\frac{dy_t}{dt} = y_t\left(\tfrac92\,y_t^2 - 8\,g_3^2\right), \qquad 16\pi^2\,\frac{dg_3}{dt} = -7\,g_3^3
\quad\Longrightarrow\quad
16\pi^2\,\frac{d\rho}{dt} = g_3^2\,\rho\,(9\rho - 2), \qquad \rho = \frac{y_t^2}{g_3^2} .
```

The ratio has an infrared-attractive point at $\rho = 2/9$ (Pendleton and Ross 1981), which corresponds to $m_t = 95.5$ GeV. The observed value is $\rho = 0.644$, between this point and the quasi-fixed point near 220 GeV (Hill 1981). The top mass is tied to the strong coupling loosely.

### 7.5 The Higgs mass and the strong coupling

When the quartic coupling is fixed by a condition at a high scale, the Higgs mass becomes a function of the other couplings. For $\lambda(M_\mathrm{Pl}) = 0$ (Buttazzo et al. 2013),

```math
M_H = 129.6 + 2.0\,(m_t - 173.34) - 0.5\;\frac{\alpha_s(M_Z) - 0.1184}{0.0007}\ \ \mathrm{GeV} \;=\; 128.4\ \mathrm{GeV}\ \text{for present inputs} .
```

The slope is $dM_H/d\alpha_s = -714$ GeV: the shift of $\alpha_s$ that corresponds to the R1 offset moves this $M_H$ by 28 MeV. In every framework of this kind R1 and R2 are correlated through $\alpha_s$.

These five ties make nuclear masses respond to $v$ and electroweak quantities respond to $\alpha_s$. The ratio $v/\Lambda_\mathrm{QCD}$ stays free, as the brief states. Section 8 lists the structures that remove this freedom.

## 8. Routes that turn v / Lambda_QCD into a pure number

The ratio is free in the Standard Model for two reasons: the strong coupling at a reference scale is an input, and $v$ comes from an independent mass parameter. Each route below removes one or both.

### 8.1 A second condensation channel of QCD

In the ladder approximation a fermion in the colour representation $R$ condenses when $C_2(R)\,\alpha_s \ge \pi/3$. Its condensation scale $\mu_R$ is the point where the running coupling reaches $\alpha_c(R) = \pi/3C_2(R)$, and at one loop

```math
\ln\frac{\mu_R}{\mu_3} = \frac{2\pi}{b_0}\left[\frac{1}{\alpha_s(\mu_R)} - \frac{1}{\alpha_s(\mu_3)}\right] = \frac{6\,[\,C_2(R) - C_2(3)\,]}{b_0} .
```

The hierarchy between two condensation scales of one gauge group is the exponential of a group-theory number. With four-loop running from $\alpha_s(M_Z) = 0.1180$:

| Representation | Dimension | $C_2$ | $C_2/C_2(3)$ | $\alpha_c$ | $\mu_R$ |
| --- | --- | --- | --- | --- | --- |
| (2,0) | 6 | 10/3 | 2.5 | 0.314 | 1.8 GeV |
| (3,0) | 10 | 6 | 4.5 | 0.175 | 11 GeV |
| (2,2) | 27 | 8 | 6 | 0.131 | 48 GeV |
| (3,1) | 24 | 25/3 | 6.25 | 0.126 | 61 GeV |
| (4,0) | 15' | 28/3 | 7 | 0.112 | 128 GeV |
| (4,1) | 35 | 12 | 9 | 0.087 | 1.15 TeV |
| (5,0) | 21 | 40/3 | 10 | 0.079 | 3.5 TeV |

The electroweak scale corresponds to a Casimir ratio near 7: for $C_2(R) - C_2(3) = 8$ and $b_0 = 23/3$ the formula gives $e^{6.26} = 523$. Two versions exist in the literature.

* The condensate itself breaks $SU(2)\times U(1)$, as in technicolour with QCD as the gauge group (Marciano 1980, with sextet quarks). The W and Z masses are then QCD-originated, $M_W = \tfrac12 g F_R$.
* A classically scale-invariant coloured scalar $S$ in a larger representation condenses near 1 TeV and feeds the Higgs mass term through a portal coupling (Kubo, Lim and Lindner 2014): $\mu_H^2 = \lambda_{HS}\langle S^\dagger S\rangle$ and $v^2 = \lambda_{HS}\langle S^\dagger S\rangle/\lambda$. The coloured boson lies between 0.35 and 3 TeV.

In both versions $v/\Lambda_\mathrm{QCD}$ is a number of QCD with the extra matter, multiplied by $\sqrt{\lambda_{HS}/\lambda}$ in the second. The ultraviolet coupling drops out because both scales come from one running coupling. The number is nonperturbative: $d\ln\mu_R/d\ln\alpha_c = -7.3$ for the (4,0) case, so a statement at 0.19% needs the critical coupling to 0.03%, a task for the lattice. Fermions in representations beyond the sextet remove asymptotic freedom ($b_0 = -16.3$ with one Dirac 15'), while a complex scalar 15' keeps it ($b_0 = 1.17$).

### 8.2 An infrared fixed point above the weak scale

With $\mu\,d\alpha_s/d\mu = -\frac{b_0}{2\pi}\alpha_s^2 - \frac{b_1}{8\pi^2}\alpha_s^3$, a matter content with $b_0 > 0 > b_1$ has a fixed point $\alpha^\ast = -4\pi b_0/b_1$ (Caswell 1974; Banks and Zaks 1982). If QCD sits at $\alpha^\ast$ above a threshold $M_\ast$ where extra coloured matter decouples, then $\alpha_s(M_\ast) = \alpha^\ast$ is a computed number and

```math
\ln\frac{M_\ast}{\Lambda_\mathrm{QCD}} = \frac{2\pi}{b_0^\mathrm{low}\,\alpha^\ast} + \dots
```

is a pure number: the ultraviolet value of the coupling is forgotten.

| Colour content | $\alpha^\ast$, 2 loops | 3 loops | 4 loops | Scale where the measured $\alpha_s$ equals $\alpha^\ast$ |
| --- | --- | --- | --- | --- |
| 16 triplets | 0.0416 | 0.0397 | 0.0398 | $10^{8}$ GeV |
| 15 triplets | 0.143 | 0.123 | 0.126 | 61 to 68 GeV (29 GeV at two loops) |
| 10 triplets and 1 sextet | 0.116 | | | 100 GeV |
| 6 triplets and 2 sextets | 0.030 | | | $4\times10^{11}$ GeV |

A fixed point with fifteen triplet-equivalents has $\alpha^\ast$ equal to the measured coupling at the weak scale. Beyond two loops $\alpha^\ast$ depends on the scheme (the table uses MS-bar), and the invariant statement is the ratio $M_\ast/\Lambda_\mathrm{QCD}$. Nine extra light triplets are excluded by experiment. Viable versions place $M_\ast$ at 1 to 10 TeV, where $\alpha_s = 0.089$ to 0.072, and need a content whose fixed point falls there. When $M_\ast$ is generated by the Higgs field or by the dynamics of section 8.1, $v/\Lambda_\mathrm{QCD}$ is a pure number. The experimental signature is a flattening of the running of $\alpha_s$ above $M_\ast$ together with new coloured matter.

### 8.3 Infrared attraction without a fixed point

If the coupling grows toward the ultraviolet above $M_\ast$ ($b < 0$), then

```math
\frac{1}{\alpha_s(M_\ast)} = \frac{1}{\alpha_s(M_U)} + \frac{|b|}{2\pi}\ln\frac{M_U}{M_\ast} .
```

For a strong coupling at $M_U$ the first term drops out, and $\alpha_s(M_\ast)$ is fixed by a ratio of scales and by the matter content (Maiani, Parisi and Petronzio 1978).

### 8.4 A common ultraviolet coupling

Two confining gauge factors that share one coupling $\alpha_U$ at $M_U$ satisfy

```math
b_3\ln\frac{M_U}{\Lambda_3} = b'\ln\frac{M_U}{\Lambda'} = \frac{2\pi}{\alpha_U}
\quad\Longrightarrow\quad
\Lambda' = M_U^{\,1-r}\,\Lambda_3^{\,r}, \qquad r = \frac{b_3}{b'} .
```

If the second factor sets $v$, the observed exponent is $r = \ln(M_\mathrm{Pl}/v)/\ln(M_\mathrm{Pl}/\Lambda_\mathrm{QCD}) = 0.84$ to 0.85, a ratio of beta-function coefficients. Unification with the electroweak couplings gives the one-loop relation

```math
\frac{b_2 - b_3}{\alpha_1} + \frac{b_3 - b_1}{\alpha_2} + \frac{b_1 - b_2}{\alpha_3} = 0 \quad \text{at } M_Z ,
```

which yields $\alpha_3(M_Z) = 0.117$ with the coefficients of the supersymmetric model $(\tfrac{33}{5}, 1, -3)$ and 0.071 with those of the Standard Model. In the supersymmetric case nuclear masses in units of $M_Z$ become a function of the electroweak gauge couplings. The precision is limited by thresholds: 0.19% in $v/m_N$ corresponds to $\delta(1/\alpha_3) = 0.0027$ out of 8.47, while threshold and two-loop terms are of order 0.1 to 1.

### 8.5 The QCD-triggered electroweak transition

In classically scale-invariant models the universe can supercool down to the QCD transition (Witten 1981; Iso, Serpico and Shimada 2017). Six massless quarks condense at $T \sim \Lambda_\mathrm{QCD}$, the top condensate gives the Higgs field a linear term $y_t\langle\bar t t\rangle h/\sqrt2$, and the induced value $h^3 = y_t|\langle\bar t t\rangle|/\sqrt2\lambda$, of order $\Lambda_\mathrm{QCD}$, triggers the electroweak transition. This ties the epoch of the transition to $\Lambda_\mathrm{QCD}$; the final $v$ is set by the scalar sector.

### 8.6 Relaxation of the weak scale on QCD barriers

A scalar $\phi$ scans the Higgs mass term (Graham, Kaplan and Rajendran 2015):

```math
V = \left(-M^2 + g\,\phi\right)|H|^2 + g\,M^2\phi + \dots + \Lambda_b^4(v)\,\cos\frac{\phi}{f}, \qquad \Lambda_b^4(v) = m_\pi^2 f_\pi^2 = (y_u + y_d)\,\frac{v}{\sqrt2}\,|\langle\bar q q\rangle| .
```

Once $v$ turns on, the barriers grow in proportion to $v$, and the field stops when $g M^2 f \simeq \Lambda_b^4(v)$:

```math
v \simeq \frac{\sqrt2\;g\,M^2 f}{(y_u + y_d)\,|\langle\bar q q\rangle|} .
```

The weak scale is inversely proportional to the quark condensate, with three new parameters. The minimal version leaves the strong CP angle of order one and needs an extension. The stopping feature belongs to the pion sector: the potential is a vacuum quantity, and nuclear structure plays no part in it.

### 8.7 What these routes give

Routes 8.1 and 8.2 combine naturally. Near an infrared fixed point a condensing channel is accompanied by a light scalar, as lattice studies of SU(3) with eight flavours and with two sextet flavours report (LatKMI 2014; LSD 2016; Fodor et al. 2012 to 2016). In such a theory both $v/\Lambda_\mathrm{QCD}$ and $M_H/v$ are numbers of one gauge dynamics, and R1 and R2 become statements that a calculation can confirm or refute. The routes of this section produce real numbers; the integers 264 and 232 belong to form (c) of section 6, developed next.

## 9. Exact results of supersymmetric gauge theory

Supersymmetric gauge theories are the setting in which relations between Higgs vacuum values, quark masses and dynamical scales are exact. They supply mathematical models for the three forms of section 6.

### 9.1 Holomorphic scale matching

Take $SU(N_c)$ with $N_f$ flavours $Q$, $\tilde Q$ and dynamical scale $\Lambda$. Holomorphy fixes what happens when a flavour of mass $m$ is removed, with no higher-order corrections:

```math
\Lambda_L^{\,3N_c - N_f + 1} = m\,\Lambda^{\,3N_c - N_f} .
```

With every flavour massive the low-energy theory is pure super Yang-Mills, and

```math
\Lambda_L^{\,3N_c} = \Lambda^{\,3N_c - N_f}\,\det m , \qquad \langle\lambda\lambda\rangle \propto \Lambda_L^3 , \qquad m_i\,\langle\tilde Q_i Q_i\rangle = \Lambda_L^3 \ \text{ for each flavour } i .
```

For $N_c = 3$ and $N_f = 5$ this reads $\Lambda_L = \Lambda^{4/9}(m_1\cdots m_5)^{1/9}$. The comparison with section 4.2 is direct: the exponent per flavour is $1/9$, exact, where QCD has $2/27$ at one loop, and the flavour-independent product $m_i\langle\tilde Q_i Q_i\rangle$ is the counterpart of $m_Q\langle\bar Q Q\rangle = -\tfrac{1}{12}\langle\tfrac{\alpha_s}{\pi}G^2\rangle$. The tie of section 7.1 is the shadow of an exact statement: Higgs-originated quark masses feed the confinement scale with fixed rational exponents.

### 9.2 Seiberg duality: confinement as a Higgs phase

The electric theory is $SU(N_c)$ with $N_f$ flavours. The magnetic theory is $SU(N_f - N_c)$ with $N_f$ flavours of dual quarks $q$, $\tilde q$ and $N_f^2$ gauge-singlet mesons $M \sim \tilde Q Q/\mu$, coupled by

```math
W = \frac{1}{\mu}\,M^i{}_j\,q_i\,\tilde q^{\,j} , \qquad \Lambda^{3N_c - N_f}\;\tilde\Lambda^{\,3(N_f - N_c) - N_f} = (-1)^{N_f - N_c}\,\mu^{N_f} .
```

Both describe the same infrared physics (Seiberg 1994). A mass term $m\,Q\tilde Q$ for one electric flavour becomes a term linear in the meson, and the equation of motion of the meson forces a vacuum value of the dual quarks:

```math
\langle q\,\tilde q\rangle = -\mu\,m \qquad\Longrightarrow\qquad v_\mathrm{mag}^2 = \mu\,m , \qquad M_V^2 \sim g_\mathrm{mag}^2\,\mu\,m .
```

A quark mass on the electric side is a Higgs vacuum value on the magnetic side, and the confinement of electric colour is the Higgs mechanism of the magnetic group. For $N_c + 1 < N_f < \tfrac32 N_c$ the magnetic theory is infrared free and its gauge bosons are composite vector mesons of the electric theory (Komargodski 2011). For three colours:

| $N_f$ | Phase | Dual gauge group | Dimension of the meson |
| --- | --- | --- | --- |
| 3 | confinement, deformed moduli space | none | |
| 4 | confinement without symmetry breaking | none | |
| 5 | conformal window | $SU(2)$ | 6/5 |
| 6 | conformal window | $SU(3)$ | 3/2 |
| 7, 8 | conformal window | $SU(4)$, $SU(5)$ | 12/7, 15/8 |

With five flavours the dual gauge group has the rank of weak isospin and the theory contains 25 mesons as elementary fields; with six flavours the dual group is again $SU(3)$. Five flavours without the top is also the content of the sBootstrap proposal of the author (composites of the five light flavours); whether the dual $SU(2)$ relates to it is left open here.

Published uses of the duality go in both directions. Kitano (2011) identifies the $\rho$ meson with the massive magnetic gauge boson in the dual of softly broken supersymmetric QCD, where one Higgs mechanism describes colour confinement and chiral symmetry breaking. Csáki, Shirman and Terning (2011) take the $SU(2)$ of the Standard Model as a magnetic dual group, with a composite Higgs and top and partially composite W and Z; Craig, Stolarski and Thaler (2011) build a related model. In these constructions the weak scale is a geometric mean, $v^2 \sim \mu\,m$, of an electric quark mass and the duality scale.

For the working hypothesis the duality offers a setting in which a Higgs-originated mass and a confinement-originated mass are two descriptions of one quantity, and in which a vector-boson mass is computed from a quark mass and a strong scale. A realization with QCD as the electric theory requires three things: supersymmetry restored at an accessible scale, an embedding of chiral weak isospin (the magnetic group acts alike on left and right dual quarks), and a value for $\mu$. The published models supply them with a new strong sector.

### 9.3 Seiberg-Witten theory: a vacuum value locked to the strong scale

In $N = 2$ $SU(2)$ Yang-Mills theory the adjoint scalar has a continuous family of vacua labelled by $u = \langle\mathrm{Tr}\,\phi^2\rangle$. The exact low-energy theory is encoded in a curve whose periods $a(u)$ and $a_D(u)$ give the mass of every BPS state:

```math
y^2 = (x^2 - u)^2 - \Lambda^4 , \qquad M = \sqrt2\,|Z| , \qquad Z = n_e\,a + n_m\,a_D .
```

At $u = \pm\Lambda^2$ the curve degenerates and a monopole or dyon becomes massless. A mass term $m\,\mathrm{Tr}\,\Phi^2$ for the adjoint multiplet breaks $N = 2$ to $N = 1$. Near $u = \Lambda^2$ the effective superpotential is $W = \sqrt2\,a_D\,M\tilde M + m\,u(a_D)$, with stationary points at $a_D = 0$ and $\langle M\tilde M\rangle = -\tfrac{m}{\sqrt2}\,du/da_D$. The continuous family collapses onto the two singular points:

```math
\langle\mathrm{Tr}\,\phi^2\rangle = \pm\Lambda^2 .
```

The vacuum value is fixed by the strong scale with an exact coefficient, the monopoles condense and electric charge is confined (Seiberg and Witten 1994a). This is the cleanest example of form (b): a continuous parameter selected at a sharp locus by energetics.

With $N_f$ flavours of mass $m_i$ the central charge gains flavour terms (Seiberg and Witten 1994b):

```math
Z = n_e\,a + n_m\,a_D + \sum_i S_i\,\frac{m_i}{\sqrt2} ,
```

where the $S_i$ are the quark-number charges. Three consequences matter here.

1. Masses are linear in conserved charges, the quark numbers among them. A quark becomes massless on the locus $a = \pm m_i/\sqrt2$, where a vacuum value equals a bare mass exactly.
2. When the central charges of two states are aligned their masses add exactly, $M(\gamma_1 + \gamma_2) = M(\gamma_1) + M(\gamma_2)$. Sum rules between sectors with different conserved charges hold with no mixing between the sectors.
3. Special points fix a mass parameter in units of $\Lambda$. For one flavour the curve is $y^2 = x^2(x - u) + \tfrac14 m\Lambda^3 x - \tfrac{1}{64}\Lambda^6$, and its three branch points collide at $m = \tfrac34\Lambda$, $u = \tfrac34\Lambda^2$, an Argyres-Douglas point where mutually non-local states are massless together.

These are the three ingredients that the relations ask for: a vacuum value tied to the strong scale (R1), additivity of masses across sectors (R2), and a quark mass fixed in units of $\Lambda$ (R3). In this language nuclei are nearly aligned states of charge $A$, with $M(A) = A\,m_\ast(1 - \epsilon_A)$ and $\epsilon_A$ between $-0.1\%$ and $+0.2\%$; the periods of the electroweak vacuum are commensurate with the same unit, $v = 264\,m_\ast$; and the pair Z, H carries 232 units in the sum while each member holds a second period that cancels.

What the real world lacks for this model is extended supersymmetry and the central charge itself. Baryon number is the natural charge on the nuclear side. The electroweak quantities carry zero baryon number, so their integers have to arise as commensurability conditions on the periods, which are conditions on $g$, $g'$, $\lambda$ and $v/\Lambda_\mathrm{QCD}$. The exact model thus shows how forms (a) and (c) meet: a vacuum selected at a locus where periods are commensurate.

### 9.4 Geometry, complementarity and bridges to QCD

* In brane constructions the Higgs vacuum values and the quark masses are distances between branes in one space, and Seiberg duality is an exchange of branes (Elitzur, Giveon and Kutasov 1997). Linear mass relations then express collinear or commensurate positions.
* With a scalar in the fundamental representation the Higgs phase and the confining phase are one phase (Fradkin and Shenker 1979; 't Hooft 1980). The electroweak spectrum can be written with gauge-invariant composites, for instance $W_\mu \sim \Phi^\dagger D_\mu\Phi$ (Abbott and Farhi 1981). The split between Higgs-originated and confinement-originated masses is a choice of description for the weak sector as well.
* Planar equivalence relates one-flavour QCD to $N = 1$ super Yang-Mills theory at large $N$ and carries the exact gluino condensate over to the quark condensate (Armoni, Shifman and Veneziano 2003). Bridges of this kind indicate how the statements of 9.1 can be imported into QCD.

### 9.5 What the exact results provide

| Need of the working hypothesis | Exact model |
| --- | --- |
| $v/\Lambda$ fixed | vacuum locked at a singular locus, $\langle\mathrm{Tr}\,\phi^2\rangle = \pm\Lambda^2$ (9.3); $v^2 = \mu m$ in a dual Higgs phase (9.2) |
| boson masses related to masses of baryon-number carriers | central charge linear in gauge and flavour charges (9.3) |
| a sum that is sharp while its members are displaced | aligned central charges (9.3) |
| charm mass fixed in units of $\Lambda$ | Argyres-Douglas-type point, $m = \tfrac34\Lambda$ in the one-flavour model (9.3) |
| Higgs-originated masses feeding the QCD scale | holomorphic matching, exponent $1/N_c$ per flavour (9.1) |

The price is supersymmetry, softly broken, and for 9.3 extended supersymmetry.

## 10. Fixing the quartic coupling and the charm Yukawa coupling

### 10.1 Frameworks that compute the Higgs mass

| Framework | Condition | $M_H$ |
| --- | --- | --- |
| Supersymmetric quartic | $\lambda = \tfrac18(g^2+g'^2)\cos^2 2\beta$ at tree level, so $M_H \le M_Z$; raised by top and stop loops | model dependent, up to about 130 GeV |
| Criticality | $\lambda(M_\mathrm{Pl}) = 0$ | 128.4 GeV for present $m_t$ and $\alpha_s$ |
| Asymptotic safety with gravity (Shaposhnikov and Wetterich 2010) | $\lambda$ and its beta function vanish at the Planck scale | 126 GeV with a few GeV of uncertainty |
| Multiple-point principle (Froggatt and Nielsen 1996) | two degenerate vacua, one near the Planck scale | $135 \pm 9$ GeV, with $m_t = 173 \pm 5$ GeV |
| Reduction of couplings in the Standard Model (Kubo, Sibold and Zimmermann 1985) | $\lambda$ and $y_t$ as functions of $g_3$ | about 61 GeV, with $m_t$ about 81 GeV |
| Finite unified theories (Heinemeyer, Mondragón and Zoupanos 2008) | all-loop finiteness | about 121 to 126 GeV |
| $\lambda = 1/8$ | $M_H = v/2$ | 123.11 GeV |
| Completions of R2 (section 2.1) | | 125.13 to 125.24 GeV |

Several frameworks land within a few GeV of the measured mass, each with an intrinsic precision of order 1 GeV. The completions of R2 are fifty times sharper. Under the working hypothesis R2 asks either for one of these frameworks refined to 0.1 GeV or for a relation of form (c). Every framework in the table computes $\lambda$ from the gauge and Yukawa couplings, so $\lambda$, $y_t$ and $\alpha_s$ arrive tied together and R1 with R2 becomes a joint constraint (section 7.5).

### 10.2 The charm mass

The heavy-quark expansion gives $m_D = m_c + \bar\Lambda - (\lambda_1 + 3\lambda_2)/2m_c + \dots$, with $\bar\Lambda$ and $\lambda_{1,2}$ set by $\Lambda_\mathrm{QCD}$. R3 fixes the left side in nuclear units, $m_{D^0} = 2m_N - \tfrac12 B_\alpha + 1.15$ MeV. In constituent language, with three light constituents in a nucleon and one in the $D$ meson, the unit form $m_{D^0} = 2m_\ast$ reads

```math
m_c^\mathrm{const} = 2\,m_\ast - \tfrac13\,m_\ast = \tfrac53\,m_\ast = 1554\ \mathrm{MeV} ,
```

five light constituent masses, inside the range that quark models use. The MS-bar mass is $1.273$ GeV and $y_c = 7.3\times10^{-3}$. Known theory ties $y_c$ to $\Lambda_\mathrm{QCD}$ only through the threshold exponent 2/27; the exact models add the special points of section 9.3; the routes of section 8 leave $y_c$ free. R3 is therefore the relation with the fewest candidate mechanisms and the cleanest test, the $D^0$ mass.

### 10.3 The sharpest joint statement

The unit form combines R2 and R3 into a relation between two particle masses,

```math
M_Z + M_H = 116\,m_{D^0} \quad\Longrightarrow\quad M_H = 125.133 \pm 0.006\ \mathrm{GeV}
```

(Breit-Wigner Z mass; 125.168 GeV with the pole mass). The uncertainty comes from the $D^0$ mass. PDG 2026 gives $125.13 \pm 0.11$ GeV.

## 11. The fission-side hypotheses

### 11.1 The standard description

The energy of a fissioning nucleus as a function of its shape $q$ is $E(q) = E_\mathrm{LD}(q) + \delta E_\mathrm{shell}(q) + \delta E_\mathrm{pair}(q)$, with the Strutinsky shell correction

```math
\delta E_\mathrm{shell} = \sum_{i\,\in\,\mathrm{occ}} \epsilon_i - \int^{\tilde\mu} \epsilon\,\tilde g(\epsilon)\,d\epsilon .
```

Around reflection symmetry, $V(\beta_2,\beta_3) = V_0(\beta_2) + \tfrac12 C_3(\beta_2)\,\beta_3^2 + \tfrac14 D_3\,\beta_3^4$, and the fission is asymmetric when $C_3 < 0$ along the path. Shell effects of the nascent fragments drive $C_3$: a compact $^{132}$Sn-like heavy prefragment for Standard I, octupole-deformed proton shells at $Z = 52$ to 56 (Scamps and Simenel 2018). The two standard modes can belong to one valley of an anharmonic potential (McGlynn and Simenel 2025).

### 11.2 Lobe-mass preference (the author; reply A)

The hypothesis adds to $E(q)$ a term that depends on the mass of each prefragment and is lowest when the lobes weigh $M_H$ and $M_Z$. It predicts a heavy fragment fixed at 134.4 u for every parent, a single channel $134 + 98$ for $A = 232$, and two channels, $134 + 106$ and $142 + 98$, for $A = 240$. The shell description predicts a fixed charge. With the round value $Z_H = 52.5$ of the GSI paper and the unchanged-charge-density rule the Standard I mass runs from 129.5 ($^{222}$Th) to 135.8 ($^{238}$U), so the two predictions differ by up to five units for neutron-deficient thorium. The GSI data measure the charge for those parents, and the single-mass maximum at 134 in the U and Pu yields agrees with both. Mass- and charge-resolved yields along isotopic chains (Lohengrin, VAMOS, SOFIA) decide.

An earlier variant of reply A used a neutron-specific spin-orbit term, $\delta E(q) = F(M_\mathrm{parent})\,I_n(q)$ with $I_n = \int d^3r\,\mathbf{J}_n\cdot\nabla(\rho_n + \rho_p)$. The constancy of the heavy-fragment charge points to proton shells, and the lobe form replaced it.

### 11.3 Asymmetry enhanced for parents near $M_H + M_Z$ (the author; reply B)

Here $C_3 \to C_3 - \delta C(M_\mathrm{parent})$, with $\delta C$ concentrated in the band from $(M_H + M_W)/u = 220.7$ to $(M_H + M_Z)/u = 232.3$. The GSI transition has its midpoint at $A_{50} = 226.93$ with width 2.65, against a band centre of 226.49 (section 3.2). The shell description also produces a dependence on the parent mass, because the heavy fragment is pinned and the size of the light partner decides the competition. The discriminator is the behaviour of $A_{50}$ with excitation energy and with proton number: an electroweak band keeps it in place, and a shell-driven competition moves it as the shell effects fade.

### 11.4 Fermium and Standard II

The value $v/u = 264.33$ points to $^{264}$Fm, two $^{132}$Sn. The measured collapse of the fission half-life occurs at $^{258}$Fm, six units earlier, and calculations for $^{264}$Fm predict symmetric fission through two compact prefragments. Half-lives and yields of $^{260}$Fm and beyond are the test. The Standard II component, 138 to 143 u or 128.5 to 133 GeV, was compared in reply B with the ATLAS excess for a charged scalar at 130 GeV (local significance about 3, global 2.5). A charged scalar has no diagonal coherent coupling to a nucleus, and the experimental follow-up is pending.

## 12. Catalogue of explanations

Status is given under the working hypothesis. Sources: the 2003 text, the brief, replies A and B, the passes in this folder, and the literature of sections 7 to 10.

| # | Explanation | Source | What it fixes or predicts | Status |
| --- | --- | --- | --- | --- |
| 1 | Bosons inside the effective meson exchange, enhanced when the nuclear mass equals a boson mass | 2003 text | | excluded by strength (5.1) and by the propagator (5.2) |
| 2 | Direct mixing of a boson with a nucleus | | | excluded by baryon number (5.3) |
| 3 | Coherent Higgs coupling through the trace anomaly | brief, B | response $K_A = 0.3$ | real and smooth (4.2, 5.4) |
| 4 | Coherent Z coupling to the weak charge | B | 0.9 eV per nucleon | real and smooth (5.4) |
| 5 | Terms from the hZZ vertex, two-neutrino exchange, parity violation enhanced in octupole nuclei | B | | real, negligible for masses |
| 6 | Scalar coupled to the full trace with $f = v$ | B, first pass | coupling $M_A/v = 0.50$ for $^{132}$Sn | $3\times10^{-12}$ of $\sigma$ exchange |
| 7 | Heavy-quark decoupling | A | exponent 2/27 per heavy quark | real, part of every route (7.1) |
| 8 | Relation among parameters, $v/\Lambda_\mathrm{QCD} = F(g, g', \lambda, y)$ | A | $\alpha_s$ to $3.9\times10^{-5}$ | open; rows 14 to 17 and 20 to 22 are the candidates |
| 9 | Competing branch with the baryon number of the nucleus | brief, A | splitting $0.33\,(K_X - K_A)$ GeV | no state; developed into row 22 |
| 10 | $\lambda$ near 1/8, the 2003 Higgs slot | brief, first pass | $M_H = v/2$ displaced by 1.7% | reformulation of R1 with R2 |
| 11 | Two-level (trace) reading of R2 | first pass | | formal; replaced by aligned central charges (9.3) |
| 12 | Lobe-mass preference at scission | the author, A | heavy fragment fixed at 134.4 u | testable (11.2) |
| 13 | Asymmetry enhanced near $M_H + M_Z$ | the author, B | $A_{50}$ fixed near 226.5 | testable (11.3) |
| 14 | Second condensation channel of QCD | Marciano 1980; Kubo, Lim and Lindner 2014; hidden-sector versions by Hur and Ko 2011, Holthausen et al. 2013 | $v/\Lambda_\mathrm{QCD}$ as a number of QCD, up to one portal coupling | open and constructive (8.1) |
| 15 | Infrared fixed point above the weak scale | Banks and Zaks 1982 | $\alpha_s(M_\ast) = \alpha^\ast$ | open (8.2) |
| 16 | Infrared attraction with non-asymptotically-free content | Maiani, Parisi and Petronzio 1978 | $\alpha_s(M_\ast)$ from a ratio of scales | open (8.3) |
| 17 | Common ultraviolet coupling; unification with the electroweak couplings | technicolour and unification literature | exponent $r$; $\alpha_3$ from $\alpha_1$, $\alpha_2$ | coarse, limited by thresholds (8.4) |
| 18 | QCD-triggered electroweak transition | Witten 1981; Iso, Serpico and Shimada 2017 | epoch of the transition | leaves $v$ to the scalar sector (8.5) |
| 19 | Relaxation of the weak scale on QCD barriers | Graham, Kaplan and Rajendran 2015 | $v \propto gM^2f/\langle\bar q q\rangle$ | open; pion sector only (8.6) |
| 20 | Seiberg duality: the Higgs phase as the dual of confinement | Seiberg 1994; Kitano 2011; Csáki, Shirman and Terning 2011 | $v^2 = \mu m$, vector masses from quark masses | needs supersymmetry near the weak scale (9.2) |
| 21 | Vacuum selected at a singular locus | Seiberg and Witten 1994 | vacuum value equal to a number times $\Lambda^2$ | exact model of form (b) (9.3) |
| 22 | Masses as central charges, commensurate periods | Seiberg and Witten 1994; this document | integers, exact sum rules, displaced members | exact model of form (c); the charge is missing (9.3) |
| 23 | Criticality, asymptotic safety, multiple-point principle, reduction of couplings | brief; section 10.1 | $\lambda$ and $y_t$ from gauge couplings | $M_H$ within a few GeV; precision of order 1 GeV |
| 24 | Selection at a nuclear threshold | brief, first pass | | sharpest thresholds: $^{187}$Re and $^{163}$Ho, unrelated to tin or charm (6) |
| 25 | Anthropic windows | brief | | 8 to 90 times wider than the offsets |
| 26 | Neutron spin-orbit term on the fission path | A | | replaced by row 12 |
| 27 | Standard II and a charged scalar at 130 GeV | the author, B | | speculative; follow-up pending (11.4) |
| 28 | Drip-line version | 2004 preprint | | retired by the author |

## 13. Programme

Measurements and data.

1. **Higgs mass to 0.02 or 0.03 GeV.** It separates the completions of section 2.1: 125.13 (unit form and reply B), 125.19 and 125.22 (the ratio 29/33 with the two Z-mass conventions), 125.24 (reply A).
2. **$D^0$ mass to 0.01 or 0.02 MeV.** It tests the completion $2m_{D^0} + M_d = M_\alpha + m_p + m_n$ (1864.802 MeV) and sharpens the unit-form prediction of $M_H$.
3. **Mass- and charge-resolved Standard I yields along isotopic chains.** A fixed mass of 134.4 u against a fixed charge of 52.7.
4. **The midpoint of the symmetric-to-asymmetric transition** as a function of excitation energy and proton number.
5. **Fission of $^{260}$Fm and heavier isotopes.**
6. **Running of $\alpha_s$ in the multi-TeV range and coloured states between 0.35 and 3 TeV.**

Calculations.

7. **Lattice.** The ratio of condensation scales $\Lambda_R/\Lambda_3$ for higher colour representations; the scalar spectrum near the conformal window; the exponents $K_A$ for light nuclei and $K_D$ for the $D$ meson, which locate the crossing points of section 4.4.
8. **Model building.** A gauge theory whose central charge counts baryon number, with a softly broken vacuum at a commensurate point (9.3); the dual pair with three colours and five flavours combined with chiral weak isospin (9.2); a framework for $\lambda$ refined to 0.1 GeV (10.1).
9. **Bookkeeping.** Each number quoted with its mass convention, Z-mass convention and Higgs-mass input; the audit rerun on every new release of $M_H$, $m_{D^0}$ and $\alpha_s$.

## 14. References

Data: AME2020 (Wang et al., Chin. Phys. C 45, 030003, 2021); NUBASE2020 (Kondev et al., Chin. Phys. C 45, 030001, 2021); Particle Data Group, Review of Particle Physics, editions 2014 to 2026; ENDF/B-VIII.0 fission yields; CMS, physics analysis summary HIG-26-010 (2 November 2026); ATLAS, JHEP 09 (2023) 004, arXiv:2302.11739.

The author's preprints: arXiv:nucl-th/0312003; arXiv:hep-ph/0405076.

Fission: Böckstiegel et al., Nucl. Phys. A 802 (2008) 12, arXiv:0712.3808; Dubray, Goutte and Delaroche, Phys. Rev. C 77, 014310 (2008), arXiv:0712.0252; McDonnell, Nazarewicz and Sheikh, Phys. Rev. C 87, 054327 (2013), arXiv:1302.1165; Zhang, Schuetrumpf and Nazarewicz, Phys. Rev. C 94, 064323 (2016), arXiv:1607.00422; Scamps and Simenel, Nature 564 (2018) 382; Bernard et al., Eur. Phys. J. A 60, 192 (2024), arXiv:2409.02818; McGlynn and Simenel, Phys. Rev. C 111, 034619 (2025), arXiv:2410.02187; Chen et al., Phys. Rev. C 114, 024329 (2026), arXiv:2605.30828.

Standard Model links: Shifman, Vainshtein and Zakharov, Phys. Lett. B 78 (1978) 443; Pendleton and Ross, Phys. Lett. B 98 (1981) 291; Hill, Phys. Rev. D 24 (1981) 691; Buttazzo et al., JHEP 12 (2013) 089, arXiv:1307.3536.

Routes of section 8: Marciano, Phys. Rev. D 21 (1980) 2425; Kubo, Lim and Lindner, Phys. Rev. Lett. 113, 091604 (2014), arXiv:1403.4262; Hur and Ko, Phys. Rev. Lett. 106, 141802 (2011), arXiv:1103.2571; Holthausen, Kubo, Lim and Lindner, JHEP 12 (2013) 076, arXiv:1310.4423; Caswell, Phys. Rev. Lett. 33 (1974) 244; Banks and Zaks, Nucl. Phys. B 196 (1982) 189; Ryttov and Shrock, Phys. Rev. D 83, 056011 (2011), arXiv:1011.4542; Maiani, Parisi and Petronzio, Nucl. Phys. B 136 (1978) 115; Witten, Nucl. Phys. B 177 (1981) 477; Iso, Serpico and Shimada, Phys. Rev. Lett. 119, 141301 (2017), arXiv:1704.04955; Graham, Kaplan and Rajendran, Phys. Rev. Lett. 115, 221801 (2015), arXiv:1504.07551; lattice results on light scalars by the LatKMI collaboration (2014), the LSD collaboration (2016) and Fodor et al. (2012).

Supersymmetric gauge theory: Seiberg, Nucl. Phys. B 435 (1995) 129, arXiv:hep-th/9411149; Intriligator and Seiberg, arXiv:hep-th/9509066; Seiberg and Witten, Nucl. Phys. B 426 (1994) 19, arXiv:hep-th/9407087, and Nucl. Phys. B 431 (1994) 484, arXiv:hep-th/9408099; Argyres and Douglas, Nucl. Phys. B 448 (1995) 93, arXiv:hep-th/9505062; Elitzur, Giveon and Kutasov, Phys. Lett. B 400 (1997) 269, arXiv:hep-th/9702014; Armoni, Shifman and Veneziano, Nucl. Phys. B 667 (2003) 170, arXiv:hep-th/0302163; Komargodski, JHEP 02 (2011) 019, arXiv:1010.4105; Kitano, arXiv:1109.6158; Abel and Barnard, arXiv:1202.2863; Csáki, Shirman and Terning, Phys. Rev. D 84, 095011 (2011), arXiv:1106.3074; Craig, Stolarski and Thaler, arXiv:1106.2164; Fradkin and Shenker, Phys. Rev. D 19 (1979) 3682; Abbott and Farhi, Phys. Lett. B 101 (1981) 69; 't Hooft, Cargèse lectures (1980).

Higgs-mass frameworks: Kubo, Sibold and Zimmermann, Nucl. Phys. B 259 (1985) 331; Froggatt and Nielsen, Phys. Lett. B 368 (1996) 96, arXiv:hep-ph/9511371; Heinemeyer, Mondragón and Zoupanos, JHEP 07 (2008) 135, arXiv:0712.3630; Shaposhnikov and Wetterich, Phys. Lett. B 683 (2010) 196, arXiv:0912.0208.
