# Side note: relations that involve the fine-structure constant

This note is kept apart from `unified_discussion.md`. Its content is numerological in character: it records where the mass rules built on $\alpha$ in the literature, and the electroweak value of $\alpha$, meet the landmarks of the conversation. Precisions are stated for the record and carry little weight (section 6 of the unified discussion). Numbers come from `calculations/alpha_note.py`, with the output in `calculations/alpha_note_output.txt`.

## 1. Three scales

```math
\frac{m_e}{\alpha} = 70.03\ \mathrm{MeV}, \qquad \frac{m_e}{\alpha^2} = 9.596\ \mathrm{GeV}, \qquad \frac{m_e}{\alpha^3} = 1.315\ \mathrm{TeV} .
```

## 2. The 70 MeV grid

Nambu (1952) observed that particle masses lie near $m = \tfrac{N}{2}\,\frac{m_e}{\alpha}$ with integer $N$. The table gives the present masses in this unit, with the nearest half-integer computed here.

| State | Mass in units of $m_e/\alpha$ | Nearest half-integer |
| --- | --- | --- |
| muon | 1.509 | 3/2 (+0.6%) |
| charged pion | 1.993 | 2 (-0.3%) |
| charged kaon | 7.050 | 7 (+0.7%) |
| nucleon | 13.41 | 27/2 (-0.7%) |
| unit $m_\ast$ of the three relations | 13.32 | 27/2 (-1.4%) |
| $\Lambda$ | 15.93 | 16 (-0.4%) |
| tau | 25.38 | 51/2 (-0.5%) |
| $D^0$ | 26.63 | 53/2 (+0.5%) |
| alpha particle | 53.23 | 53 (+0.4%) |

The grid meets the relations of the conversation through the nucleon. The unit $m_\ast$, the $D^0$ and the alpha particle have no distinguished place on it.

**What the unit is and what it pins.** The unit is the energy of the classical electron radius, $m_e/\alpha = \hbar c/r_e$ with $r_e = 2.82$ fm, a nuclear length. The grid therefore restates an old link: a length built from the electron mass and $\alpha$ falls at the range of the nuclear force. In Standard Model terms the electron mass comes from the Higgs field through a Yukawa coupling $y_e = 2.9\times10^{-6}$, $\alpha$ comes from the electroweak couplings, and the pion and nucleon masses come from QCD. The two entries nearest to the unit read

```math
m_e \simeq \tfrac12\,\alpha\,m_\pi = 0.509\ \mathrm{MeV}, \qquad m_e \simeq \tfrac{2}{27}\,\alpha\,m_N = 0.5075\ \mathrm{MeV}, \qquad \text{measured } 0.5110\ \mathrm{MeV} .
```

Either form pins the electron Yukawa coupling in units of $\Lambda_\mathrm{QCD}/v$, in the way R3 pins the charm Yukawa coupling. With it the list of pinned parameters becomes $v/\Lambda_\mathrm{QCD}$, $\lambda$, $y_c$ and $y_e$, with the same missing host. The work of Mac Gregor supplies integers and units for this grid and no dynamics; in the terms of section 6 of the unified discussion it has the first of the three things that carry weight.

## 3. The lepton formula of Barut

Barut (1979) proposed $m_N = m_e\big(1 + \tfrac{3}{2\alpha}\sum_{n=0}^{N} n^4\big)$. It gives 105.5 MeV for the muon, 1786.2 MeV for the tau (measured 1776.9), and continues with 10.29, 37.2, 102.8 and 239.0 GeV. The fourth member falls in the bottom region, between $\Upsilon(2S)$ and $\Upsilon(3S)$ and next to the mass of $^{11}\mathrm{B}$ (10.25 GeV), in the stretch of alpha-cluster nuclei of section 1.2 of the unified discussion. The seventh lies 3% below $v$.

## 4. The number 27/2 and the exponent 2/27

The exponent of a heavy-quark mass in the QCD scale is $2/27$ (section 4.2 of the unified discussion). Its inverse has a direct meaning: the three-flavour beta coefficient is $b_0 = 9$, each heavy quark contributes $\tfrac23$, and

```math
\frac{b_0(n_f = 3)}{2/3} = \frac{27}{2} = \frac{33}{2} - 3 .
```

In the trace anomaly the mass term of a heavy quark is worth one such unit of the gluon term. In the chiral limit and at leading order the nucleon mass is therefore $m_N = \tfrac{27}{2}\,\sigma_Q$, where $\sigma_Q = \langle N|m_Q\bar Q Q|N\rangle$ is the contribution of one heavy quark. Nambu's rule assigns the nucleon the half-integer $27/2$. The two statements coincide if

```math
\sigma_Q = \frac{m_e}{\alpha} : \qquad \tfrac{2}{27}\,m_N = 69.5\ \mathrm{MeV} \quad \text{against} \quad \frac{m_e}{\alpha} = 70.0\ \mathrm{MeV} .
```

With the light-quark sigma terms included, $\sigma_Q = \tfrac{2}{27}\big(1 - \sum_{uds} f_{Tq}\big)\,m_N$ is 61 to 64 MeV. Equivalently $m_p/m_e$ would be $27/2\alpha = 1850$, against the measured 1836. The half-integer of the nucleon is the one entry of the grid with a derivation behind it; the QCD identity contains neither the electron mass nor $\alpha$.

## 5. The electroweak value of $\alpha$

The fine-structure constant is a derived quantity of the electroweak sector: $e = g\sin\theta_W$. With $g = 2M_W/v$ and $\sin^2\theta_W = 1 - M_W^2/M_Z^2$, the tree-level value in terms of $G_F$, $M_W$ and $M_Z$ is

```math
\alpha_\mathrm{ew} = \frac{M_W^2\,\sin^2\theta_W}{\pi\,v^2} = \frac{\sqrt2\,G_F\,M_W^2}{\pi}\left(1 - \frac{M_W^2}{M_Z^2}\right) .
```

| Input or comparison | $1/\alpha$ |
| --- | --- |
| PDG 2025 masses ($M_W = 80.3692 \pm 0.0133$ GeV) | $132.10 \pm 0.11$ |
| PDG 2026 masses ($M_W = 80.3625 \pm 0.0077$ GeV) | $132.05 \pm 0.06$ |
| pole masses of W and Z | 132.16 |
| $v/m_{D^0}$ | 132.03 |
| $v/(M_\alpha/2)$ | 132.11 |
| the nuclear integer $50 + 82$ | 132 |
| $1/\alpha$ at zero momentum transfer | 137.04 |

The low-energy value follows from the electroweak one through radiative corrections of 3.6%. The contact with the conversation is that $1/\alpha_\mathrm{ew}$ equals the integer of the unit form (section 1.3 of the unified discussion). Three statements follow.

* The charm relation reads $m_{D^0} = \alpha_\mathrm{ew}\,v$. The right side is $1863.9 \pm 1.5$ MeV with the PDG 2025 W mass and $1864.6 \pm 0.9$ MeV with PDG 2026, against 1864.84 MeV for the $D^0$ and 1863.69 MeV for half an alpha particle.
* The unit is $m_\ast = \tfrac12\,\alpha_\mathrm{ew}\,v = M_W^2\sin^2\theta_W/(2\pi v)$, between 931.9 and 932.3 MeV: the unit of the three relations written with electroweak quantities alone.
* The tin relation becomes $1/\alpha_\mathrm{ew} = 132$, a statement inside the electroweak sector. It corresponds to $M_W = 80.3568$ GeV; $1/\alpha_\mathrm{ew} = v/m_{D^0}$ corresponds to 80.3608 GeV. The Standard Model fit quoted in the 2026 review of the W mass gives $80.357 \pm 0.006$ GeV, and the measured average is $80.3625 \pm 0.0077$ GeV. The slope is 8.1 units of $1/\alpha$ per GeV of $M_W$.

In this reading the three relations are $v = 132$, $M_Z + M_H = 116$ and $m_{D^0} = 1$ in units of $\alpha_\mathrm{ew}\,v$. The Nambu grid belongs to the low-energy $\alpha$: with $\alpha_\mathrm{ew}$ its unit becomes 67.5 MeV and the nucleon moves to 13.9 units.

## 6. The 9.6 GeV unit

One power of $\alpha$ above the Nambu unit lies the bottom scale, and the heavy electroweak states fall near half-integers of it.

| State | Mass in units of $m_e/\alpha^2$ | Nearest half-integer |
| --- | --- | --- |
| $\Upsilon(1S)$ | 0.986 | 1 (-1.4%) |
| W | 8.375 | 17/2 (-1.5%) |
| Z | 9.503 (pole mass 9.499) | 19/2 (+0.03%, pole -0.01%) |
| Higgs | 13.04 to 13.05 | 13 (+0.3% to +0.4%) |
| top | 17.98 | 18 (-0.1%) |
| $v$ | 25.66 | 51/2 (+0.6%) |
| $M_Z + M_H$ | 22.54 to 22.55 | 45/2 (+0.2%) |
| $M(^{100}\mathrm{Sn}) + M(^{132}\mathrm{Sn})$ | 22.51 | 45/2 (+0.03%) |

The pair sum can therefore be read on two rulers: 232 nucleon units, or 45/2 units of $m_e/\alpha^2$ (215.91 GeV).

## 7. One power of $\alpha$ between the sectors

With the low-energy $\alpha$: $m_\tau/\alpha = 243.5$ GeV, 1.1% below $v$; $m_p/\alpha = 128.6$ GeV and $m_\ast/\alpha = 127.8$ GeV, 2% to 3% above the Higgs mass; $v\,\alpha = 1796.8$ MeV, between the tau and the $D^0$. The ratios $v/m_\tau = 138.6$, $1/\alpha = 137.0$ and $v/m_{D^0} = 132.0$ are neighbours, and section 5 identifies the last with the electroweak $\alpha$.

## 8. Status

* Sections 2, 3, 6 and 7 are numerology of the classical kind: lists of near-coincidences without a host. Much of it is already in print (section 9).
* Section 4 contains one exact QCD statement, $m_N = \tfrac{27}{2}\sigma_Q$ in the chiral limit, placed next to an empirical rule.
* Section 5 rewrites two of the three relations of the conversation in electroweak terms. It carries a measurable handle: a W mass known to 2 or 3 MeV distinguishes $1/\alpha_\mathrm{ew} = 132.00$, 132.03 and 132.11.

## 9. Prior literature

A search of arXiv and publisher pages (about 25 lookups, 13 November 2026) gives the following picture. Entries marked "not found" may still exist in print.

| Relation of this note | Prior publication |
| --- | --- |
| masses as multiples of $\tfrac12\,m_e/\alpha$ (section 2) | Nambu 1952. Secondary sources give the muon as $N = 3$ and the pion as $N = 4$ (Palazzi, arXiv:physics/0301074; the rule is restated in Varlamov, arXiv:1705.02227). The assignment $N = 27$ for the nucleon was not confirmed from the 1952 text. |
| nucleon at 27/2 units of $m_e/\alpha$ (section 4) | Mac Gregor (arXiv:hep-ph/0603201, hep-ph/0607233): $p = m_e + 9\,m_f$ with the fermion quantum $m_f = \tfrac32\,m_e/\alpha = 105.04$ MeV, which is 13.5 units of 70 MeV; also $\tau = m_e + 17\,m_f$. |
| the link of 27/2 with the three-flavour beta coefficient and the heavy-quark sigma term (section 4) | not found |
| lepton formula (section 3) | Barut 1979. A comparison of its 10.29 GeV member with the $\Upsilon$ region was not found. |
| top at 18 units of $m_e/\alpha^2$ (section 6) | Mac Gregor 2006 (arXiv:hep-ph/0603201): $m_t = m_e(1 + 18/\alpha^2) = 172.73$ GeV, built from a second-order quantum $\tfrac32\,m_e/\alpha^2 = 14.394$ GeV. |
| W and Z in units of $m_e/\alpha^2$ (section 6) | Mac Gregor 2006: the average of W and Z at 9 units, $m_e(2 + 9/\alpha^2) = 86.365$ GeV against 85.8 GeV observed, and $M_W + M_Z = 171.6$ GeV against the top mass. The single entry $Z = 19/2$ was not found. |
| Higgs at 13 units and $M_Z + M_H$ at 45/2 units (section 6) | not found in the 2006 papers, which precede the measurement. A 2011 meeting abstract by Mac Gregor on "Higgs constants" was not read. |
| $1/\alpha_\mathrm{ew} = 132$ against $50 + 82$, $v/m_{D^0}$ or the alpha particle (section 5) | not found |
| $m_\tau/\alpha$ against $v$, $m_p/\alpha$ against the Higgs mass (section 7) | not found |

The scheme of Mac Gregor also contains $\Upsilon(1S)$ at 9454 MeV and a state near 260 GeV. Sections 2, 3 and part of section 6 of this note therefore repeat published observations, and the entries of sections 4 and 5 marked "not found" are recorded here with the date of this note.

References: Nambu, Prog. Theor. Phys. 7 (1952) 595; Barut, Phys. Rev. Lett. 42 (1979) 1251; Mac Gregor, Int. J. Mod. Phys. A 20 (2005) 719 and 2893, arXiv:hep-ph/0506033; arXiv:hep-ph/0603201; arXiv:hep-ph/0607233; The Power of Alpha (World Scientific, 2007); Palazzi, arXiv:physics/0301074; Varlamov, arXiv:1705.02227; Particle Data Group, Review of Particle Physics 2026, review of the W-boson mass. The assignments of the table in section 2 are computed here and were not compared with the tables of the 1952 paper. The literature search was made by a subagent; the three Mac Gregor preprints were read in full text there, and the other sources through abstracts and citing papers.
