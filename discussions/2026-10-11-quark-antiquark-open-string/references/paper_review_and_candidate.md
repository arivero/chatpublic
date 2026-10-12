# Paper review and candidate

*Exported Claude conversation (claude.ai/chat/233790ec-a8f5-442e-828d-13652e1c8411) — 7 exchanges. Exported 2026-10-11. Collapsed tool-use/thinking steps are shown only by their summary line; files Claude produced are listed by name.*

---

## 1. User

> review both papers.

*Attachments: `fermionic_string_scattering_prl.pdf`, `fermionic_string_scattering_prd.pdf`*

### Claude

> *[Confirming citation details and planning a numeric verification script.]*

I’ll check the algebra and numerics in both papers, verify the references that can be checked, and then write the review.

> *[Creó un archivo, leyó 10 páginas, y 11 pasos más]*

Most comments apply to both papers, because the PRL is a condensed subset of the PRD: the same equations, numbers and table. Equation numbers are given as PRL / PRD.

### What I checked and found correct

- **Algebra and numerics:**

  - Massless Møller benchmark: PRL 5–6; PRD 6–8 and A3–A6, including the 1/2! convention.
  - Low-energy expansion of V: PRL 18–19; PRD 27–31. A symbolic series of Γ(1−α′a)Γ(1−α′b)/Γ(1−α′(a+b)) to O(α′⁴) matches (B2) term by term.
  - The |V₉₀|² table.
  - The reach formula, PRL 21 / PRD 72: 3.01 and 5.36.
  - The Stirling form: exact/asymptotic is 1.025 at z = 10 and 1.003 at z = 90.
  - Hadronic numbers: M_s = 1.054 GeV, and z = 90 at 10 GeV.
- **Representation and field-theory steps:**

  - Chan–Paton trace selection.
  - δM (PRD 33).
  - Propagator expansion and auxiliary-field integration (PRD 46–49).
  - SU(5) branchings (PRD 64–67).
  - Anti-diquark charges (PRD 59) and the Pauli argument for the scalar anti-diquark.
- **References spot-checked:**

  - CMS arXiv:2603.25458: 17/37 TeV, 138 fb⁻¹.
  - STAR, Science 393, 727 (2026).
  - Lucini–Teper, Aguilar-Saavedra–Teixeira, Bourilkov.

### Errors

1. **PRL Eq. (11), sign.** With c = −(a+b), Γ(1−α′(a+b)) = α′c Γ(−α′(a+b)). So V(a,b) = (α′ab/c) B(−α′a, −α′b). As printed, V → −1 as α′ → 0.
2. **PRD Eq. (36), spurious (−1)ⁿ⁻¹.** The residue at α′s = n is ∏ₖ₌₀ⁿ⁻¹(α′b+k) / [(n−1)! α′(s − nM_s²)], which is PRL Eq. (12).

   - Numerically, at α′b = −0.37, the residues for n = 1…4 are −0.370, −0.233, −0.190, −0.167.
   - PRD (36) gives the opposite sign at n = 2 and n = 4.
   - The caveat “up to a convention-dependent overall sign” does not cover a sign that depends on the level. Residue signs are fixed by unitarity.
   - The two papers currently disagree on this formula.
3. **PRL reference numbering is shifted by one from [8] on.**

   - Text [9] (same-stack dimension-eight vs intersecting dimension-six) should be [8], Antoniadis–Benakli–Laugier, which is otherwise never cited.
   - Text [10] should be [9].
   - [11] is cited twice but does not exist. PDG is [10], and the CMS 2026 dijet paper is missing from the PRL list.
4. **Sign between the mediator amplitude and its operator (PRL 26–28; PRD 45–47).**

   - With iM equal to the product of vertices and propagator, M = −g₁g₂\* ū₂(q̸+M)/(q²−M²)u₁.
   - Its low-energy limit is +g₁g₂\*/M ū₂u₁, which matches the stated L_eff.
   - As printed, (27) and (28) differ by a sign. It is an overall phase, but the text says the operator reproduces the amplitude.
5. **PRD reference order.** [32] and [33] are cited before [30] and [31]. With order-of-citation numbering this points to a hand-made list.

### Major issues

**1. Prior work on the central amplitude.** Cullen, Perelstein and Peskin [PRD 62, 055012 (2000)] built this model.

- QED sits inside N=4 U(N) SYM on D3-branes.
- The electron is the gaugino with SU(2) Chan–Paton generators t^±, and the photon is A³.
- A Z₂×Z₃ orbifold projection removes the extra massless states.
- Every ordered amplitude is multiplied by Γ(1−α′s)Γ(1−α′t)/Γ(1−α′s−α′t).
- They computed Bhabha scattering and e⁺e⁻→γγ, and compared with KK graviton exchange.

Bourilkov’s 0.631 TeV bound, which PRD Sec. XI.A describes as coming from “a specific TeV-string model”, is a fit of exactly this construction to LEP Bhabha data. He takes the model from CPP and compares |S(s,t)|² × SM with the data.

Your U(2) assignment (λ± = E₁₂, E₂₁; Q = diag(1,−1)/2) is the same embedding, and Møller is the crossing of their Bhabha. Consequences:

- The abstract claims “we show that the Møller-like amplitude is…” (PRL) and “we derive” (PRD) need to be presented as a re-derivation in the same-sign channel.
- CPP should be cited at Eq. (14)/(21).
- Lüst–Stieberger–Taylor [NPB 808 (2009) 1], which gives four-fermion amplitudes for intersecting-brane matter, belongs next to [17].

**2. Which realization the quark application assumes.**

- The dimension-eight statement holds for the same-stack (adjoint) sector, including orbifold projections of it, where the parent V factor survives (as in CPP).
- For chiral matter at brane intersections, ABL find dimension-six operators, and LST find amplitudes that depend on intersection angles and the compactification.
- Both papers acknowledge this. PRD Sec. XI.B nevertheless quotes LHC sensitivities (2.1%, 0.67%) using the same-stack form, without saying why quarks would belong to that class.
- Either state the assumed realization, or present the dijet numbers as conditional on it.

**3. The common-slope obstruction has a published escape.**

- The argument in the PRL’s “Bootstrap interpretation and its obstruction” and in PRD Sec. X is the historical reason dual models failed as theories of hard scattering.
- Polchinski and Strassler [PRL 88, 031601 (2002)] showed the escape. In a warped background, the local string scale at the scattering point is redshifted relative to the 4D Regge scale. Fixed-angle amplitudes then fall as powers, following the QCD counting rules, while the hadronic Regge slope is kept. The DIS version is hep-th/0209211.
- PRD option (ii), “strong warping”, is this mechanism.
- The hadronic supersymmetry the papers lean on (Brodsky, de Téramond, Dosch) is formulated in light-front holography, an AdS framework, so the obstruction section should engage PS directly.
- As written, the conclusion holds in flat space but is presented as the main limitation, without noting that a known mechanism evades it.

**4. The quantum-number matching is narrower than stated.** PRD Sec. VIII says the anti-diquark reproduces “the entire non-Abelian and electromagnetic label content of a light quark”. This holds for SU(3)_c × SU(3)_f × U(1)_em, with three restrictions.

- **(a) Electroweak SU(2)_L × U(1)_Y.**

  - A Lorentz-scalar antiquark pair is built either from two left-handed Weyl fields (u^c, d^c, s^c, all SU(2)_L singlets) or from two right-handed ones (Q†Q†, giving (3, 1 or 3)₋₁/₃). Mixed pairs are Lorentz vectors.
  - None of these options gives Q_L = (3,2)₁/₆.
  - For right-handed quarks the full SM charges do match: [d^c s^c] = (3,1)₂/₃ = u_R, [s^c u^c] = d_R, [u^c d^c] = s_R.
  - So unless the string sector carries SU(2)_L, the identification covers right-handed quarks only.
- **(b) Flavor numbers.**

  - [d̄s̄] has (N_u, N_d, N_s) = (0,−1,−1), against (1,0,0) for u. Its strangeness is +1 against 0.
  - The difference (1,1,1) is the same unit of baryon number (S = Y − B), so it adds no new constraint.
  - Still, “light-flavor quantum numbers” should read “SU(3)_f weights”.
- **(c) Number of flavors.**

  - Λ²(N̄) ≅ N only for N = 3, so Eq. (58) does not extend to c, b, t.
  - With three generations, the down-type pairs [s^c b^c], [b^c d^c], [d^c s^c] carry (3,1)₂/₃, the charges of u_R, c_R, t_R. This is a different assignment from Eq. (58), and may deserve a remark.

### Moderate issues

5. **4D internal quantum numbers.**

   - “Suppressing compactification-dependent internal operators” hides a choice that determines M_gauge.
   - In 4D N=4, gauginos carry an SU(4)_R index and couple to scalars through φ^{AB}λ_Aλ_B, with φ antisymmetric.
   - Eq. (3) holds for external states with equal R-index. Otherwise scalar exchange contributes.
   - With coincident branes, the massless W± also make the “charged” fermion part of an unbroken U(2) multiplet.
   - CPP’s orbifold projection handles both points. Adopting it, or stating the choices explicitly, fixes this.
6. **Description of the two orderings.**

   - (1,3,2,4) and (1,4,2,3) are reflections of each other.
   - Each color-ordered amplitude contains both the t- and u-channel poles. The full amplitude is 2A(1,3,2,4)V(t,u), up to sign.
   - The phrase “the same factor multiplies both exchange terms” reads as if one ordering supplies the t-exchange and the other the u-exchange.
   - The factorization does not require V to be symmetric.
7. **The sign of the effect depends on the channel.**

   - For an ordering with a timelike invariant, V(s,t) = 1 − ζ(2)α′²st + … is greater than 1 for t < 0. For example, V = 1.0021 at z = 0.05, θ = 90°.
   - Bhabha, qq̄ and gluon-containing orderings therefore get an enhancement in those color structures.
   - Table I (“central suppression”) and the dijet “deficits” in Sec. XI.B apply only to the same-sign channel. For color-summed dijets the sign has to be computed.
8. **Leading-order versus exact values.** PRD Sec. XI quotes 6.7×10⁻³, 2.1% and 0.67%. The exact 1 − |V₉₀|² values are 6.2×10⁻³, 1.87% and 0.62%. Since Eq. (70) is available in closed form, quote the exact values or label the others as leading order.
9. **KK graviton exchange.**

   - In large-volume realizations, cylinder-level KK graviton exchange gives a dimension-eight operator with a different angular dependence.
   - CPP estimate that it is suppressed by g² relative to the string form factor.
   - State this, because the claim that the observable is |V|² at O(s²/M_s⁴) depends on it.
10. **A quantitative version of the form-factor remark.**

    - At fixed s, ∂_t V(t, −s−t)|ₜ₌₀ = α′[ψ(1+α′s) + γ] = ζ(2)α′²s − ζ(3)α′³s² + ….
    - Matching J_t F(t)²/t with F(t) = 1 + r²t/6 (t < 0) gives r²_eff = (π²/2) s/M_s⁴ + O(s²/M_s⁶).
    - The apparent radius grows with s and vanishes as s → 0. This puts “no static radius at tree level” into a formula. It could replace the qualitative paragraphs (PRL “A caution about terminology”; PRD after Eq. 34).
    - Separately, PRD Eqs. (1) and (C1) use F = 1 − r²q²/6. That has the wrong sign for spacelike q² < 0 in the mostly-minus metric used elsewhere; write it in terms of Q² = −q².
11. **Polarization and choice of machine (PRD XI.A).**

    - In the Møller-like channel, V multiplies every helicity amplitude identically. It therefore cancels in all polarization asymmetries at tree level, while a chiral contact operator generally changes them. That is a more specific claim than “can help distinguish”.
    - No 3 TeV e⁻e⁻ machine is proposed; CLIC at 3 TeV is e⁺e⁻.
    - Recasting the estimate for Bhabha would connect it to an existing proposal and to the CPP/Bourilkov analysis, at the cost of the s-channel ordering V(s,t).

### Minor and editorial

- **Overlap between the papers.** The PRL does not cite the PRD. For companion submissions it should, and the PRL needs content that the PRD does not simply repeat.
- **PRL space.**

  - The fermionic-mediator section (Eqs. 24–28) and the SU(5) bookkeeping (Eq. 31) are tangential to the letter’s claim.
  - The mediator result is standard: u-channel fermion exchange, as in e⁺e⁻ → γγ.
  - PRD Secs. VI–VII are textbook material; shorten them or move them to an appendix.
  - Labelling the views addressed as “misconceptions” needs a citation showing that someone holds them.
- **PRL wording.** “The absence of an O(α′E²) term is the central experimental fact” — it is a prediction, not an experimental fact.
- **PRD after Eq. (33).** “Two additional derivatives on each fermion bilinear in total” is ambiguous. Dimension eight means two derivatives in total, one per bilinear in Eq. (34).
- **Regge residues (PRL after Eq. 12; PRD after Eq. 36).**

  - Spin content is read from the full residue: V’s residue times A_SYM, where the k = 0 factor cancels the massless pole in the other invariant.
  - The leading spin at level n is n+1 for the vector multiplet.
  - “Degree-n polynomial, hence spins at level n”, applied to V alone, is loose.
- **1/2! in dσ/dΩ (PRL 6; PRD 8).** State that the angular integral then runs over 4π.
- **PRL introduction.** “Independently, Miyazawa’s…” — Miyazawa (1966) predates the works listed before it.
- **PRL ref. [7].** The LMU thesis exists under that title (2011). I could not confirm the Fortschr. Phys. 60, 373 entry; check it against INSPIRE.
- **PRD Sec. X on Lucini–Teper.** Their abstract reports consistency with the bosonic string and inconsistency with other simple effective string theories, without naming NS. Cite the specific page or adjust the paraphrase.
- **Intensifiers.** “decisive limitation”, “sharp obstruction”, “fail spectacularly”, “especially simple”, “unusually clean”, “impressive”, “precisely” carry no technical content.

### Assessment

**PRL.**

- CPP covers the amplitude, ABL the dimension-six/eight distinction, and PS the slope problem.
- That leaves the bootstrap framing as the new content, and it ends at an obstruction with a known escape. In its current form I don’t think it meets the letter novelty criterion.
- A letter would need a result outside CPP. Two candidates:

  - the four-Ramond amplitude in a warped background, showing how the hadronic slope and the hard scale separate for the anti-diquark–string state;
  - a worked-out junction mechanism that supplies ΔB = 1.

**PRD.** It is viable as a synthesis paper after:

- repositioning against CPP, LST and PS;
- fixing errors 1–5;
- restricting the quantum-number claim as in Major issue 4;
- specifying the 4D embedding.

Sources:

- [Cullen, Perelstein, Peskin, hep-ph/0001166 (PRD 62, 055012)](https://arxiv.org/abs/hep-ph/0001166v3)
- [Bourilkov, hep-ph/0002172](https://arxiv.org/pdf/hep-ph/0002172)
- [Polchinski, Strassler, hep-th/0109174](https://arxiv.org/abs/hep-th/0109174)
- [Polchinski, Strassler, DIS, hep-th/0209211](https://arxiv.org/abs/hep-th/0209211)
- [CMS, arXiv:2603.25458](https://arxiv.org/abs/2603.25458)
- [STAR, arXiv:2408.15441](https://arxiv.org/pdf/2408.15441)
- [Science publication summary (sci.news)](https://www.sci.news/physics/baryon-junction-14992.html)
- [Lucini, Teper, hep-lat/0107007](https://arxiv.org/abs/hep-lat/0107007)
- [Aguilar-Saavedra, Teixeira, hep-ph/0307001](https://arxiv.org/abs/hep-ph/0307001)
- [Schlotterer thesis, LMU](https://edoc.ub.uni-muenchen.de/13381/)

---

## 2. User

> work in the first outside cpp candidate

### Claude

> *[Deriving the UV constituent twist from asymptotic freedom running.]*

I’ll check the prior literature on string amplitudes in warped backgrounds first, then set up the radial-convolution amplitude for four Ramond states and compute it.

> *[Creó 11 archivos, editó 3 archivos, y 50 pasos más]*

I worked candidate 1 out as a draft PRD section, `warped_ramond_draft.pdf`, with the LaTeX source, figure and scripts in `warped_ramond_section.zip`. Warping does separate the hard Ramond scale from the hadronic slope, but the warped amplitude is pointlike only if the quark state is effectively a single free (twist-one) field. In addition, a colored Ramond string cannot be the QCD flux tube in this kind of construction.

**Setup.** Put the same-sign four-Ramond amplitude in a confining Polchinski–Strassler (PS) background.

- I write z = α′_had s, where α′_had is the Regge slope seen at the infrared wall, and x = (1−cosθ)/2.
- The four-dimensional amplitude is M_gauge × 𝒱(z,x), where 𝒱 is V averaged over the radial direction.
- The radial weight is ∝ y^{2ν−1}, with 2ν = Σᵢ(τᵢ − 1) = Σγᵢ: each state’s twist excess over a free spin-½ field. This follows from PS’s twist counting.
- The same-sign channel has no s-channel ordering, so the local amplitude has no poles along the radial integral. This is the channel where the local approximation can be applied cleanly.

**Results.** All of these are checked numerically by `warped_ramond_checks.py`.

1. **Large z.** 𝒱 → K ν 𝓜(ν;x) z^{−ν}, where 𝓜(ν;x) = ∫₀^∞ dw w^{ν−1} V_w(x).

   - The power z^{−ν} reproduces the PS counting rule.
   - The angular dependence 𝓜(ν;x) does not depend on the infrared region; only the prefactor K does.
   - PS and Armoni et al. (2024) give the power counting only, without the angular function.
2. **Disk-modulus form.** 𝓜(ν;x) = Γ(ν+1) x(1−x) ∫₀¹ dξ/[ξ(1−ξ)] ℓ_x(ξ)^{−ν−1}, with ℓ_x = −x lnξ − (1−x) ln(1−ξ).

   - The radial average turns the Koba–Nielsen factor e^{−wℓ} into a power.
   - Agreement with direct integration is better than 10⁻¹⁸.
   - For a hard wall there is a closed form valid at all z, using an incomplete gamma function.
3. **Low energy, hard wall.** 1 − 𝒱 = ζ(2) [ν/(ν+2)] z² x(1−x) + O(z³). The coefficient depends on the infrared model.
4. **Near-free states, ν → 0⁺.** 𝒱 ≈ [z e^{−κ(x)}]^{−ν}.

   - The hadronic slope enters only through ν ln(α′_had s).
   - κ(½) = 0.599 and κ(χ=16) = 1.606.
   - Near the forward direction, κ(x) ≈ −ln[x ln(1/x)], so the cutoff is set by α′_had|t| ln(s/|t|), the Regge combination.
5. **UV-dominated states, ν = −b < 0, with UV boundary y₀.**

   - For 0 < b < 2: 1 − 𝒱 ≈ b|𝓜(−b;x)| (s/M_\*²)^b, with M_\* = M_had/y₀.
   - The hard scale is therefore set by the UV boundary. For b < 2 the deviation is a non-integer power of s, which no local operator produces.
   - For b > 2 the dimension-eight form returns.
   - 𝓜 has poles at ν = 0, −2, −3, … with residues 1, −ζ(2)x(1−x), ζ(3)x(1−x), …

**Consequences for the bootstrap.**

- **Two hard antiquarks per state** (τ = 2, ν = 2):

  - dσ/dt ∝ s^{−6}, the counting rule for eight constituents.
  - |𝒱|² = 1.3×10⁻⁶ at 10 GeV (the flat-space value is 9×10⁻⁵³) and 1.3×10⁻²² at 1 TeV.
  - Warping removes the exponential suppression, but this power law is still excluded by partonic scaling.
- **Near-twist-one states.**

  - Dijet scaling gives Σγ ≲ 1–1.5×10⁻². This is an order-of-magnitude estimate, not a fit.
  - At fixed s, the angular shape changes by ≈ 1.01 Σγ between χ = 16 and χ = 1, the same in every mass bin.
- **The scattering degree of freedom is a twist-one field.**

  - The spin-½ unitarity bound Δ ≥ 3/2 is saturated only by free fields.
  - So pointlike hard scattering with a hadronic slope requires either ν → 0⁺ (approaching a free field) or ν < 0 (an elementary component).
  - In both cases what scatters hard is a single twist-one field. The anti-diquark–string configuration can be at most its infrared, partially composite component.
- **Color.**

  - Normalizable bulk states of a holographic dual are color singlets of the confining group, and Chan–Paton labels on branes along r are global symmetries of that sector.
  - Putting QCD color on the Ramond strings therefore needs a confining sector in which SU(3)_c is a weakly gauged global symmetry.
  - The throat string is then not the QCD flux tube, and M_had becomes that sector’s infrared string scale (Reece–Wang place it a few times above the lightest Kaluza–Klein mass in Randall–Sundrum).
  - The literal Eq. (63), with the QCD string, is not realized by warping.

**Not done:**

- The ν < 0 regime is parametrized by the radial weight exponent. I have not derived its map to the Randall–Sundrum bulk fermion mass c, including spinor factors.
- The color-summed dijet version, with gg and qg orderings, is not computed.
- Crossed channels with an s-ordering are not treated, because the local continuum approximation smears the discrete Regge spectrum there.
- I found no earlier evaluation of the angular factor or of the modulus representation, but the search was limited to PS, Armoni et al. and the AdS Veneziano literature.

Sources:

- [Polchinski–Strassler, hep-th/0109174](https://arxiv.org/abs/hep-th/0109174)
- [Polchinski–Strassler DIS, hep-th/0209211](https://arxiv.org/abs/hep-th/0209211)
- [Armoni, Pyszkowski, Sugimoto, Weissman, arXiv:2412.17784](https://arxiv.org/abs/2412.17784)
- [Reece–Wang, arXiv:1003.5669](https://arxiv.org/abs/1003.5669)
- [Alday, Chester, Hansen, Zhong, arXiv:2403.13877](https://arxiv.org/abs/2403.13877v1)

**[File produced: Warped ramond draft (PDF)]**

**[File produced: Warped ramond section (ZIP)]**

---

## 3. User

> also propose ideas for delta B =1

### Claude

> *[Creó un archivo, editó un archivo, y 5 pasos más]*

The unit of baryon number cannot be removed by relabelling. It has to be carried by a real object in the string sector R, absorbed by a condensate, or produced by explicit B violation. The ideas below cover these options, with the checks I ran (`wb_6.py`).

### Constraints that apply to every idea

**ΔB = 1 cannot be relabelled away.**

- Take any assignment B = α(N_q − N_q̄)/3 + (1−α)(N_J − N_J̄), with N_J counting junctions. All of them agree on colour singlets.
- In flux terms the anti-diquark side is q̄q̄J̄: the two antiquark lines meet at an anti-junction, leaving one open line, as for a quark.
- The difference between q and q̄q̄J̄ is three quark endpoints plus one junction, which is one baryon. So ΔB = 1 for every α. Attributing baryon number to the junction (Rossi–Veneziano, Kharzeev) moves it around but does not remove it.

**What R must carry.**

- R must have B = 1, be a colour singlet, and have spin ½ (combined with the scalar anti-diquark).
- If a single R serves all three light flavours (u ≅ [d̄s̄]R, d ≅ [s̄ū]R, s ≅ [ūd̄]R), it also needs Q = 0 and Y = 0. These are the quantum numbers of the Λ: B = 1, S = −1, I = 0.

**Electroweak topology cannot supply it.** Standard Model instantons change B by N_g = 3, so B mod 3 is exactly conserved in the SM.

### Ideas

**1. A diquark condensate absorbs ΔB (colour–flavour-locked, CFL, phase).**

- The condensate ⟨qq⟩ ∝ ε^{abI}ε_{ijI} carries B = 2/3. It breaks U(1)_B down to Z₂ = e^{3πiB}, which is −1 on q and +1 on [q̄q̄].
- The condition B(R) = 1 then reduces to “R is odd under this Z₂”, i.e. R is a fermion. A Ramond state satisfies that by construction.
- Under the locked SU(3)_{c+f}, both q and [q̄q̄] decompose as 8 ⊕ 1, so R must be a locked singlet.
- This extends the Schäfer–Wilczek quark–hadron continuity [PRL 82, 3956 (1999)] to anti-diquarks.
- Consequence: the bootstrap holds as an identity in dense quark matter and needs one of the other ideas in vacuum.
- Check to do: in an NJL model of CFL matter, compare the gapped quasiparticle spectrum (octet gap Δ, singlet gap 2Δ) with the [q̄q̄] ⊗ R composites.

**2. R is a topological baryon.**

- In the Skyrme model, B is the winding number. For N_c = 3 the Wess–Zumino term makes the soliton a fermion (Witten 1983), so this also supplies the Ramond statistics.
- 3 ⊗ R contains a 3 only for R = 1 or R = 8. The Witten–Guadagnini condition (allowed representations must contain states with Y = N_c/3 = 1) excludes the singlet. R is therefore the spin-½ octet, with no freedom left.
- The flavour wavefunction is then fixed in the SU(3) limit. For the u quark the weights are:

| Component | Weight |
| --- | --- |
| p[ūd̄] | 3/8 |
| Σ⁺[s̄ū] | 3/8 |
| Σ⁰[d̄s̄] | 3/16 |
| Λ[d̄s̄] | 1/16 |

- Because an octet baryon is q[qq], the identity reduces to q ≅ q ⊗ ([qq]_b[q̄q̄]^b). That is a quark dressed by a flavour-singlet scalar diquark–antidiquark pair, which has B = 0 and vacuum quantum numbers.
- In this version the bootstrap is a dynamical statement about how strongly q mixes with that dressed state.
- **Holographic version.** In the Sakai–Sugimoto model the baryon is an instanton on the D8 flavour branes, with instanton number equal to B (Hata–Sakai–Sugimoto–Yamato 2007). It is the D4 baryon vertex dissolved into the D8, so the junction and soliton pictures coincide.

  - The instanton sits at the infrared tip. That fits the warped-section result, where the anti-diquark–string configuration can only be the quark’s infrared component.
- **Variant with an extended carrier.** In Komargodski’s quantum-Hall-droplet baryon, B is the magnetic symmetry of an η′ sheet and is carried by chiral modes on its boundary. The boundary is then a closed string carrying B = 1. For N_f = 1 the droplet has spin N_c/2, so getting spin ½ requires N_f ≥ 2.

**3. R is a three-pronged string junction.**

- In D-brane models U(1)_B = Q₃/3, where Q₃ is the U(1) charge of the colour stack.
- The charges are: q has Q₃ = +1, the antisymmetric [q̄q̄] (an orientifold-image string) has −2,on.**

- In D-brane models U(1)_B = Q₃/3, where Q₃ is the U(1) charge of the colour stack.
- The charges are: q has Q₃ = +1, the antisymmetric [q̄q̄] (an orientifold-image string) has −2, and a junction with all three prongs on the colour stack has +3, i.e. B = 1.
- It is a colour singlet through the ε contraction, and B is conserved throughout.
- Such junction states become light near exceptional enhancement points (Gaberdiel–Zwiebach, hep-th/9709013).
- R is then a single flavour-singlet state with Λ quantum numbers. If it is lighter than the Λ, it mixes with it. BESIII’s bound BR(Λ → invisible) < 7.4×10⁻⁵ limits that mixing.

**4. Explicit ΔB = 1 violation.**

- **Stringy instanton.** A Euclidean brane that intersects the colour stack once has three colour zero modes λ^a. Integrating them gives ∫d³λ λ^aλ^bλ^c = ε^{abc}, and the instanton violates Q₃ by 3.

  - The junction tensor and the unit of B therefore come from the same object (review: Blumenhagen–Cvetič–Kachru–Weigand, arXiv:0902.3251).
- **Pati–Salam form.** With the lepton as a fourth colour, Λ³(4̄) ≅ 4 gives q ↔ [q̄q̄ℓ̄]. B−L is conserved, while B and L each change by one unit.
- **Experimental constraint.** For u_R ↔ [d^c s^c], the minimal gauge-invariant, B−L-conserving operator is u^c d^c s^c N^c, with N a gauge singlet.

  - Through p → K⁺ + invisible (lifetime limit τ > 5.9×10³³ yr), it requires a scale Λ ≳ 7×10¹⁴ GeV.
  - This route therefore gives only a negligible mixing and cannot make the bootstrap an O(1) identity.

**5. B carried by a duality map.**

- In Seiberg duality, the dual quark’s baryon number is N_c/(N_f − N_c) times the electric quark’s, so B is not additive over constituents.
- For N_c = 3 the dual quark has the electric quark’s B only at N_f = 6.
- This suggests stating the bootstrap as a duality with extra singlet fields fixed by ‘t Hooft anomaly matching. This is speculative; anomaly matching is the test.

### Which to pursue

Ideas 1 and 2 need no B violation and each has a concrete next computation: the CFL quasiparticle comparison for idea 1, and the [q̄q̄] ⊗ octet overlap with the fixed weights for idea 2. Idea 3 is the one with direct phenomenology, through mixing with the Λ. Idea 4 is excluded as an O(1) mechanism.

I have not edited `warped_ramond.tex`; it changed on disk after I delivered it. If you want ideas 1–2 added as a subsection, I’ll write it against the current version.

Sources:

- [Komargodski, Baryons as quantum Hall droplets, arXiv:1812.09253](https://arxiv.org/abs/1812.09253)
- [BESIII dark-sector overview (Λ → invisible limit), arXiv:2410.14982](https://arxiv.org/pdf/2410.14982)

---

## 4. User

> the main idea was to compare fermionic string scattering both in quark diquark and in lepton meson. Elaborate the similar lepton meaon formalism and compare with experimental limits on compositeness

### Claude

> *[Weighing chiral protection needed for light composite lepton masses.]*

I’ll set up the lepton–meson map in parallel to the quark–diquark one, derive its Chan–Paton selection rules and scattering factors, and then compare with current lepton compositeness limits. I’m checking the experimental numbers first.

> *[Creó 4 archivos, editó 2 archivos, y 40 pasos más]*

The lepton–meson construction is worked out as a new PRD section, `lepton_meson.tex`. It is compiled together with the warped section in `prd_addendum_draft.pdf`, and the source plus the script that reproduces every number are in `lepton_meson_section.zip`.

**Quantum numbers.** I scanned, for each Standard Model fermion, which Lorentz-scalar fermion pairs carry exactly its gauge charges.

- **Lepton–meson map.** L_L ≅ (ū_R Q_L) ⊗ R, i.e. ν_L ↔ ūu and e_L ↔ ūd, the charges of (π⁰, π⁻). Equivalent forms are (Q d^c)\* and (L e^c)*.
- **Unpaired states.** e_R and ν_R have no scalar partner. This is the reverse of the quark case, where u_R and d_R have one and Q_L does not.
- **One unit of B−L in every pairing.** The SO(10) charge X = 5(B−L) − 4Y takes the values 1, −3 and 5 on the fermions, so matching all gauge charges forces ΔX = −5.

  - The string state R therefore always carries the B−L of a right-handed neutrino.
  - In the quark–diquark case that unit is ΔB = 1; in the lepton–meson case it is ΔL = 1, and R has exactly the quantum numbers of ν_R.
  - The lepton side needs no junction and has no baryon-number problem.

**Chan–Paton structure.**

- **Lepton–meson.** The lepton is an oriented string with endpoint labels in N⊗N̄. The PRL’s U(2) state E₁₂ is already of this type, so the Møller computation in the papers is a lepton–meson calculation.
- **Quark–diquark.** The quark is an unoriented string from an orientifold. If the endpoint labels carry colour and flavour, the colour- and flavour-antisymmetric anti-diquark needs the symmetric projection, and it brings colour-sextet partners.
- **Colour-octet partners.** If the lepton’s endpoint labels carry colour, 3⊗3̄ = 1⊕8 gives colour-octet partners degenerate with the lepton at tree level.
- **String factors.**

  - The surviving orderings are those where particle and antiparticle labels alternate, and the result is the same for every sector I checked (oriented, bifundamental, antisymmetric and symmetric orientifold).
  - Same-sign scattering gets V(t,u).
  - Particle–antiparticle and annihilation channels get V(s,t), or V(s,u) depending on how the shared label is oriented.
  - A process whose two fermion pairs share no endpoint label vanishes at disk level. So whether e⁺e⁻→μ⁺μ⁻ or Drell–Yan sees a string factor depends on the generation and label map.

**Observables.**

- Same-sign scattering has a deficit, −(π²/3)z²x(1−x); annihilation and Bhabha have an excess, +(π²/3)z²x.
- The string also shifts the forward–backward asymmetry by δA_FB = −(3π²/32)z². A form factor depending only on s cannot produce this.
- The Bhabha reach formula gives 0.65 TeV for LEP2, close to Bourilkov’s fit of 0.631 TeV. His fit used the Cullen–Perelstein–Peskin model, which is this oriented sector.

**Comparison with compositeness limits.**

|  | Dimension-six contact limit (Λ⁺/Λ⁻) | Same-stack string limit |
| --- | --- | --- |
| Leptons, ee→ee (LEP) | 8.3 / 10.3 TeV | M_s > 0.631 TeV (published fit) |
| Leptons, q q̄→ℓℓ (LHC) | 23–40 TeV | ≈ 2–3.5 TeV (my estimate; needs a shared label chain) |
| Quarks, dijets | 17 / 37 TeV | string resonances > 7.7 TeV |

- The string limits sit a factor of about 16 (leptons) and 5 (quarks) below the dimension-six ones, because the leading string correction is dimension eight.
- In length units, a same-stack lepton string can be as large as 3×10⁻¹⁹ m, against 2×10⁻²⁰ m for a generic composite electron.
- Leptons are less constrained than quarks in string scale (12× weaker) than in contact scale (3–4×) because the lepton limit comes from √s = 0.2 TeV.
- With assumed precisions, future lepton colliders reach 2.3 TeV (FCC-ee), 10.7 TeV (CLIC at 3 TeV) and 36 TeV (10 TeV muon collider).

**Lepton–meson with the QCD string is excluded** for three independent reasons:

- Bhabha scattering requires M_s > 0.63 TeV, against about 1 GeV for the QCD string.
- The degenerate colour-octet partners would sit at the lepton mass; LHC recasts exclude colour-octet leptons only up to 1.2–1.55 TeV.
- A hadron-sized electron would shift g−2 by about 3×10⁻⁷, against an allowed 10⁻¹².

As on the quark side, the endpoint labels have to belong to a separate confining sector.

**A test specific to leptons.** If R is lighter than the pion, the map implies the operator (ū_R d_L)(ē_L N_R), whose pseudoscalar part lifts the helicity suppression of π→eν. The PIENU ratio Γ(π→eν)/Γ(π→μν) then requires a scale of about 60 TeV for unit coefficient. This is an estimate and has no quark analogue.

The contact-limit numbers are from PDG 2024, CMS 2021 and the CMS 2026 dijet paper. The entries for μμ/ττ, Drell–Yan, g−2 and π→eν are my estimates and are marked as such in the table.

Sources:

- [PDG 2024, compositeness listings](https://ccwww.kek.jp/pdg/2024/listings/rpp2024-list-quark-lepton-compositeness.pdf)
- [CMS dilepton search, JHEP 07 (2021) 208](https://arxiv.org/abs/2103.02708)
- [Cullen–Perelstein–Peskin, hep-ph/0001166](https://arxiv.org/abs/hep-ph/0001166v3)
- [Almeida et al., arXiv:2212.06178 (leptogluon recasts)](https://ar5iv.labs.arxiv.org/html/2212.06178)
- [Muon g−2 final result, arXiv:2506.03069](https://arxiv.org/pdf/2506.03069)
- [CERN Courier on the g−2 result and WP25](https://cerncourier.com/a/fermilabs-final-word-on-muon-g-2/)
- [Aliberti et al., Phys. Rep. 1143 (2025)](https://vivo.colorado.edu/display/pubid_393250)
- [ZEUS quark-radius limit, arXiv:1604.01280](https://ar5iv.arxiv.org/html/1604.01280)

**[File produced: Prd addendum draft (PDF)]**

**[File produced: Lepton meson section (ZIP)]**

---

## 5. User

> the small masses  of electron up and down, as well as the nonzero mass of pion, signala we are missing some effect that could contribute to the scattering size too. Research.

### Claude

> *[Bounding compositeness scales from form factors and radiative effects.]*

I’ll survey the mass-generation mechanisms that could apply here and, for each, work out what it adds to the scattering amplitude, with numbers against current limits. First the literature.

> *[Creó 3 archivos, compartió 2 archivos, y 34 pasos más]*

You are right that the masses point to a missing sector, and it does change the scattering. Every way I found of generating these masses adds a size effect one order lower than the string’s own correction (dimension six, or a magnetic dipole, instead of dimension eight), at the scale of whatever produces the masses. It is written up as a third section, “Masses and scattering size”, in `prd_addendum_draft.pdf`; sources and check scripts are in `prd_addendum_sources.zip`.

**Why the massless string can’t account for it.** The same-stack Ramond states are massless, and the string factor V multiplies a helicity-conserving amplitude. Putting the masses into the kinematics only shifts V by about m²α′, roughly 10⁻¹³ for the electron at M_s = 1 TeV. So any size effect tied to the masses has to come from the sector that breaks chiral symmetry.

**Five candidate mechanisms:**

1. **Chiral symmetry breaking and the pion multiplet.**

   - The Gell-Mann–Oakes–Renner relation has exactly the form of a supersymmetry-breaking B term, m_φ² = m_ψ² + 2m_ψB. It fits with m_ψ = (m_u + m_d)/2 and B = 2.66 GeV.
   - In the lepton–meson pairing e ↔ π⁻, a common B would need m_e ≈ 3.7 MeV. With the observed 0.511 MeV, B would have to be 19 GeV, so the electron mass is not set by the same explicit breaking as the pion’s.
   - In light-front holographic QCD the supercharge annihilates the pion, so it has no partner. The would-be partner (L_B = −1) sits at M² = 0, an empty massless fermion slot the lepton–meson map would fill.
   - The same dynamics gives a charge radius r² = 3/κ², which reproduces 0.653 fm against the pion’s 0.659 fm. The LEP Bhabha bound then needs κ′ > 1.2 TeV, about 2300 times the QCD value.
2. **Quasi-Nambu–Goldstone fermions** (Buchmüller–Love–Peccei–Yanagida; Kugo–Yanagida).

   - This is the field-theory version of “a fermion is the partner of a Goldstone boson”. Yukawa couplings vanish by the shift symmetry, so light masses come out naturally.
   - The coset geometry adds a four-fermion contact term of order 1/f². Contact limits then require f ≳ 3 TeV (electrons) to 10 TeV (dijets), which is 3×10⁴–10⁵ times f_π.
3. **Yukawa couplings at brane intersections.**

   - Here Y ~ exp(−A/2πα′), where A is the area of the worldsheet triangle joining the intersections. The first generation needs A/2πα′ = 12.7 (e), 11.3 (u) and 10.5 (d).
   - Their masses lie within a factor of nine because these areas agree to 20%.
   - The cost is that matter at intersections has dimension-six contact terms at M_s. Generations sitting at different intersections also produce flavour-changing neutral currents, which require M_s ≳ 10² TeV, or about 10⁴ TeV once dipole moments are included.
4. **Partial compositeness.**

   - Here m_f is proportional to ε_L ε_R, where ε_L and ε_R are the fermion’s composite admixtures, and the contact coefficient goes as ε⁴. The size therefore grows with the mass.
   - For a 3 TeV composite sector, the equivalent contact scale is 3.6×10⁶ TeV for the electron, against 11 TeV for the top.
   - This is the only mechanism where light fermions look pointlike because they are light. It predicts deviations ordered by mass (t > b > τ > …), testable in tt̄, bb̄ and ττ final states.
5. **Radiative masses.**

   - A mass generated at one loop at scale M brings a magnetic-moment shift δa ~ m²/M². The g−2 measurements then require M ≳ 0.5 TeV (electron) and 2.6 TeV (muon).
   - Nambu’s relation m_e ≈ (α/2)m_π± holds to 0.34%. A loop origin at the pion scale, however, would give δa_e ≈ 1.3×10⁻⁵, seven orders above the bound.

**Consequences:**

- The QCD scales (f_π, κ, m_π) are 10³–10⁵ below every bound. The dynamics that makes the pion light cannot also make leptons or quarks the partners of mesons or diquarks.
- Once masses are included, the leading size effect comes from the mass-generating sector, not from the string oscillators.
- Partial compositeness is the one option that gives small masses and small size without a high scale.

The scale bounds carry unknown O(1) coefficients. Two points are qualitative only: how the chiral condensate in a holographic model would change the warped amplitude’s prefactor (I expect the high-energy exponent to stay the same), and the precise map from the partial-compositeness mixing to the warped exponent.

Sources:

- [Abel–Masip–Santiago, flavour-changing neutral currents in intersecting-brane models](https://arxiv.org/abs/hep-ph/0303087v1)
- [Abel–Lebedev–Santiago, flavour bounds on the string scale](https://arxiv.org/abs/hep-ph/0312157)
- [Cremades–Ibáñez–Marchesano, Yukawa couplings at intersections](https://arxiv.org/abs/hep-th/0302105)
- [Dosch–de Téramond–Brodsky, pion with no baryonic partner](https://ar5iv.arxiv.org/html/1501.00959)
- [Erlich–Katz–Son–Stephanov, holographic model of hadrons](https://ar5iv.arxiv.org/html/hep-ph/0501128)
- [Yanagida, quasi-Nambu–Goldstone fermions (slides)](https://indico.ipmu.jp/event/66/contributions/1514/attachments/1202/1438/YANAGIDA_Tsutomu_Quasi_NG_Fermions.pdf)
- [Yanagida–Yin–Yokozaki, arXiv:1608.06618](https://ar5iv.labs.arxiv.org/html/1608.06618)

**[File produced: Prd addendum draft (PDF)]**

**[File produced: Prd addendum sources (ZIP)]**

---

## 6. User

> reconsider the massless string

### Claude

> *[Creó un archivo, editó un archivo, y 9 pasos más]*

I read “reconsider the massless string” as: drop the assumption that the Ramond states are massless and let the string itself carry the light masses. That changes my previous conclusion. The result is a new subsection 17.1 in `prd_addendum_draft.pdf`, with the summary revised to match; the check script `massless_checks.py` is in `prd_addendum_sources.zip`.

**What actually removes the dimension-six term.** Masslessness is not needed. Two things do the work: particle and antiparticle labels must alternate around the disk, and the exchanged gauge trajectory must have the supersymmetric intercept.

- **Massive external states (stretched strings).** In the alternating orderings the stretchings of neighbouring particle and antiparticle cancel. V(t,u) then depends only on the four-dimensional t and u, with t + u = 4m² − s, and still has no O(α′) term.
- **Massive exchanged states.** The factor becomes V(α′(s − m²), α′t) = 1 − ζ(2)α′²(s − m²)t + …. The mass term is −m²/s times the massless one, so it never exceeds the oscillator term in a physical channel.

  - Read as a dimension-six scale, Λ₆ = M_s²/(√ζ(2) m). That is 1.5×10⁹ GeV for m_e at M_s = 1 TeV.
- **Small shifts α₀ of the exchanged trajectory’s intercept.** They give the same structure, with linear coefficient ≈ −ζ(2)α₀.

So light masses carried by the string add nothing to the size at order 1/M_s². My earlier statement that any size effect must come from the mass-generating sector holds only for masses supplied from outside the string.

**What brings dimension six back from inside the string.** An order-one shift of the intercept does. The linear coefficient diverges as α₀ → ½, which is the Lovelace–Shapiro amplitude: ρ trajectory starting at ½, massless pion, Adler zero. At low energy that amplitude is −πα′(s + t), a pure dimension-six term at about 0.6 GeV for the hadronic slope.

- A massless Goldstone pion and the absence of a dimension-six term therefore belong to different strings.
- In the superstring, the massless bosonic (NS) partners of Ramond states are moduli, not Goldstone bosons. A nonzero m_π would then be a modulus mass from supersymmetry breaking.

**Masses as string lengths (m = Δy/2πα′).** The lengths L = 2πα′m come out as:

|  | hadronic slope | M_s = 1 TeV |
| --- | --- | --- |
| e | 5.7×10⁻¹⁹ m | 6.3×10⁻²⁵ m |
| u | 2.4×10⁻¹⁸ m | — |
| d | 5.2×10⁻¹⁸ m | — |

These lie in the transverse space and are not four-dimensional charge radii. This realization fails for two reasons:

- **Degenerate bosonic partners.** In the supersymmetric limit the NS states of the same stretched string have the fermion’s mass. For e ≃ (dū) that includes a charged vector boson at 0.511 MeV.
- **Triangle inequality.** With u ≃ [d̄s̄] and d ≃ [s̄ū] (using orientifold images) and e ≃ (dū), the masses are distances, so m_e ≥ |m_d − m_u| = 2.5 MeV is required. That fails by a factor of five, in any number of transverse dimensions and for any α′.

  - The muon gives m_μ ≤ m_u + m_s = 95.7 MeV against 105.7 MeV, which is within scheme uncertainties.

**The consistent string-internal option: intersecting branes.**

- At a brane intersection the Ramond ground state stays massless and chiral, while the NS scalars are shifted by the intersection angles.
- Giving the scalar partner the pion mass needs an angle combination δ = 2πα′m_π², which is 0.11 at the hadronic slope or 1.2×10⁻⁷ at M_s = 1 TeV.
- The opposite-sign scalar is tachyonic. Its condensation, brane recombination, is the intersecting-brane Higgs mechanism. Fermion masses then come from the worldsheet areas discussed in the intersection subsection, which brings back that subsection’s dimension-six terms at M_s.

One point is untested: whether the dimension-six coefficient at a small-angle intersection vanishes in proportion to δ. If it does, the pion mass would set the size directly, as Λ₆⁻² ∝ m_π²/M_s⁴.

Sources:

- [Cremades–Ibáñez–Marchesano, Higgs mechanism as brane recombination](https://arxiv.org/abs/hep-th/0203160)
- [Abel–Masip–Santiago](https://arxiv.org/abs/hep-ph/0303087v1)
- [Dosch–de Téramond–Brodsky](https://ar5iv.arxiv.org/html/1501.00959)

**[File produced: Prd addendum draft (PDF)]**

**[File produced: Prd addendum sources (ZIP)]**

---

## 7. User

*Attached image `1000024497.jpg` (screenshot of the ChatGPT conversation), no text:*

![1000024497.jpg](1000024497.png)

### Claude

> *[Leyó 4 páginas, buscó en la web, ejecutó un comando]*

Treating the endpoint quarks as separate objects from the quark string states is consistent with the framework, but it does not rescue masses-as-string-lengths. It does change which mass each object should carry.

**Different notions of quark mass in this construction:**

- **Chan–Paton label (the brane).** It carries colour, flavour and charge but has no mass parameter. In the same-stack picture of the PRL it is massless by construction.
- **Endpoint mass in effective strings.** In the rotating-string fits of Sonnenschein–Weissman, the endpoint mass is defined as tension times the vertical string segment in the holographic picture. They state it is neither the QCD (current) mass nor the constituent mass.

  - Their fitted values are m_u/d ≈ 0–60 MeV (the massless fit is often optimal for light trajectories), m_s ≈ 220 MeV, m_c ≈ 1500 MeV and m_b ≈ 4730 MeV, with α′ = 0.884 GeV⁻².
  - They exclude the pion ground state from the fit as too light for the model.
- **Current mass, 2–5 MeV.** In the D3/D7 holographic setup this is the separation of the flavour brane from the colour branes, divided by 2πα′: a stretching in the UV.
- **Constituent mass, ≈ 300 MeV.** This is the dressing from chiral symmetry breaking.
- **The bootstrap quark.** In the bootstrap this is the Ramond string state, a different object from the label at the end of another string.

So “the same quark” means the same quantum numbers attached to a label and to a state. Their masses need not coincide, and massless labels are the natural default.

**Effect on the stretched-string no-go.** I added additive endpoint masses μ ≥ 0 to the stretched-string masses, M_ij = μ_i + μ_j + T·L_ij. The vector identity behind the triangle inequality still holds, and gives:

0.511 − μ_d − μ_u ≥ |−2.54 + μ_u − μ_d| (MeV)

- The best case over all μ ≥ 0 is at μ = 0 and still fails by 2.03 MeV.
- Massless endpoints are just the pure-stretching case, which is already excluded.
- A rescue needs a negative contribution of about −1.0 MeV on the d label, together with about +1.5 MeV on u. Negative constant terms come from string zero-point (Casimir) energies, which cancel in the Ramond sector of the superstring.

The loophole therefore does not save masses as lengths. It is compatible with the brane-intersection option: massless labels, a massless chiral string, and a mass that comes from a coupling.

**What it could change in the scattering size.**

- The photon couples to the charges at the endpoints. For massless endpoints, the endpoints fluctuate as much as the string itself, which is what produces the string’s spread-out charge distribution.
- A heavy endpoint would localize its charge. I expect that to reduce the charge-radius part of the size while leaving the exchanged Regge tower, and so the dimension-eight factor V, in place.
- I have not computed this. An endpoint mass is a boundary interaction that is not a marginal deformation of the critical superstring, so there is no exact disk amplitude to expand. The effective-string fits likewise give spectra, not amplitudes.

**Three masses in one holographic picture.** These notions can coexist without conflict:

- the current mass as the flavour brane’s UV position;
- the endpoint mass as the vertical segment near the infrared wall;
- the constituent mass from the condensate.

The pion fits none of them. Its lightness comes from the Goldstone mechanism, which in the string language is the intercept condition (the Lovelace–Shapiro case), not from endpoint masses. That matches the Sonnenschein–Weissman fit leaving the pion out.

If you want this in the draft, I can add it as a paragraph to section 17.1 after “Masses as separations”, with the endpoint-mass inequality and the HISH values.

Sources:

- [Sonnenschein–Weissman, Rotating strings confronting PDG mesons, arXiv:1402.5603](https://ar5iv.arxiv.org/html/1402.5603)
- [JHEP 08 (2014) 013](https://link.springer.com/article/10.1007/JHEP08(2014)013)
