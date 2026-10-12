# Dual QCD and a vectorlike Kaluza–Klein route on CP² × S¹

This note develops the two additional avenues proposed in the current conversation. The user clarified that “non-Dirac” was a typo: the intended quarks are **non-chiral in their gauge representation, Dirac quarks**. The target is initially the strong and electromagnetic sector; a chiral weak theory need not be constructed at this stage.

That changes the model-building priorities. A vectorlike compactification is acceptable, and the short-distance fermion need not be a flat-space Ramond excitation of the same effective string used for mesons. Both avenues merit investigation. They provide concrete ingredients, although neither is a complete construction of the proposed meson/pointlike-fermion relation yet.

## 1. Vectorlike Dirac quarks retain the chiral symmetry needed for pions

There are three different meanings of “chiral” here:

| Meaning | What is required at this stage? |
| --- | --- |
| Chiral gauge representations, as in the weak interactions | Can be deferred. Left- and right-handed quarks can have identical color and electromagnetic charges |
| Approximate global chiral flavor symmetry of light-quark QCD | Needed if the bosonic state is to reproduce the physical pion's Goldstone mechanism |
| Internal chirality of a compact-space Dirac zero mode | Useful for finding zero modes; it does not automatically imply a chiral four-dimensional gauge theory |

For two massless Dirac flavors, with electromagnetism temporarily switched off,

\[
\mathcal L=\bar q_L i\!\not D q_L+\bar q_R i\!\not D q_R
\]

has the global symmetry \(SU(2)^{\rm flavor}_L\times SU(2)^{\rm flavor}_R\), even though the color gauge theory is vectorlike. A condensate \(\langle\bar q_R q_L\rangle\) breaks it to the diagonal subgroup, producing three Goldstone pions. Small Dirac masses give

\[
m_\pi^2=B_0(m_u+m_d)+\cdots,
\]

with additional electromagnetic contributions when electromagnetism is restored, particularly for the charged pion. The axial flavor symmetry in this statement is not the gauged weak \(SU(2)_L\).

**Consequently, Dirac quarks are fully compatible with a pion that is massless in a symmetry limit and acquires a small mass later.** What would remove this mechanism is a large explicit Dirac mass, not a vectorlike gauge assignment. A KK construction must therefore explain light quark modes as well as their representation content.

## 2. A dual strong sector changes which scale the fermion probes

The flat-string argument assumed that the observed fermion's hard amplitude was governed by the same slope that fits hadronic Regge trajectories. A dual gauge-theory construction need not satisfy that assumption.

A useful target would be

\[
\Lambda_{\rm conf}\ll E\ll\Lambda_{\rm dual},M_{\rm KK},
\]

where the mesonic string is an infrared description of confinement, while an appropriate dual fermionic variable is weakly coupled or otherwise has the required partonic hard behavior in that window. Its effective size corrections would then be controlled by the upper scales, not automatically by \(\Lambda_{\rm conf}\).

This is a statement about which fields and operators describe the process. Exact duality must preserve observables and fermion parity: it cannot turn a particular bosonic meson operator into a fermion, or erase a measured form factor by renaming the state. A viable dictionary would identify **two distinct physical sectors**, bosonic and fermionic, and explain their relation. An electric description of the fermion may involve a disorder operator, a charged defect, or other nonlocal structure rather than a local \(\bar q Wq\) operator.

### A controlled precedent, and its limitations

Supersymmetric QCD gives a calculable framework for exploring this possibility. Electric \(SU(N_c)\) with \(N_f\) vectorlike flavors has a magnetic \(SU(N_f-N_c)\) description with magnetic quark superfields and a meson superfield, schematically

\[
W_{\rm magnetic}=h\,\widetilde q Mq.
\]

For example,

\[
SU(7),\ N_f=10\quad\longleftrightarrow\quad SU(3)_{\rm magnetic},\ N_f=10.
\]

The supersymmetric one-loop coefficients are

\[
b_{0,e}=3(7)-10=11,\qquad b_{0,m}=3(3)-10=-1.
\]

This lies in the free-magnetic range \(N_c+1<N_f<3N_c/2\): the magnetic description becomes weak toward the infrared below its matching scale. It is an explicit example of a strongly interacting electric description having more elementary-looking dual variables.

It is **not ordinary three-color QCD**. There are superpartners and ten flavors, and the magnetic beta-function sign is different from that of asymptotically free few-flavor QCD. A realistic confining deformation must be specified and followed through the duality; simply dropping four flavors is not a derivation. Also, an elementary magnetic meson superfield is not automatically a physical pion with its observed form factor. The example establishes a useful mechanism and laboratory, not the desired spectrum.

Seiberg–Witten monopole condensation provides another controlled precedent for dual variables and confining strings. Separately, charge–monopole systems can carry field angular momentum

\[
J_{\rm field}=\frac{eg}{4\pi}=\frac n2,
\qquad eg=2\pi n.
\]

With suitable quantization, topological charged sectors can thus support half-integer spin. This identifies another possible source of fermionic structure beyond Ramond oscillators. It is not a claim that an ordinary QCD flux tube carries such a monopole, or that a resulting soliton is light and pointlike: its mass, core size, statistics, and coupling to the probe would all need calculation.

## 3. What CP² × S¹ supplies

The geometric motivation is concrete:

\[
\mathbb{CP}^2=SU(3)/U(2).
\]

Its connected isometry algebra is \(\mathfrak{su}(3)\), while a circle supplies \(\mathfrak u(1)\). In a metric KK construction, surviving isometries can produce gauge vectors. The global effective isometry group of CP² is \(PSU(3)=SU(3)/\mathbb Z_3\), so obtaining fundamental triplets requires attention to bundles and the lift of this action. The Lie algebra alone is insufficient.

Ordinary scalar functions on CP² have harmonics in \((p,p)\) representations,

\[
\dim(p,p)=(p+1)^3=1,8,27,64,\ldots.
\]

They have zero triality and do not provide a color triplet. In contrast, holomorphic sections of the line bundle \(\mathcal O(k)\), for \(k\ge0\), have

\[
\dim H^0(\mathbb{CP}^2,\mathcal O(k))
=\binom{k+2}{2}=1,3,6,10,\ldots.
\]

At \(k=1\) this is a fundamental or conjugate-fundamental triplet, depending on the convention for the group action. A bundle can therefore supply precisely the representation absent from ordinary scalar harmonics. The triplet is a color representation if this SU(3) is identified with color; its three components are not automatically three generations.

### The non-spin obstruction has a spinᶜ remedy

Let \(H\) be the integral generator of \(H^2(\mathbb{CP}^2,\mathbb Z)\), normalized by \(\int H^2=1\). Then

\[
c_1(T\mathbb{CP}^2)=3H,\qquad
w_2(T\mathbb{CP}^2)=H\pmod2\ne0.
\]

CP² is not spin. Taking its direct product with \(S^1\) does not change this: the pullback of \(w_2\) is still nonzero. Choosing periodic or antiperiodic boundary conditions around the circle cannot fix it.

But CP² is spinᶜ. A spinᶜ structure combines the spinor transition functions with a line-bundle connection. For determinant bundle \(\mathcal O(d)\), with \(d\) odd, the four-dimensional internal index is

\[
\operatorname{ind}D_{\rm spin^c}
=\int_{\mathbb{CP}^2}e^{dH/2}\widehat A
=\frac{d^2-1}{8}.
\]

Equivalently, twist the canonical spinᶜ structure by \(\mathcal O(k)\). Its determinant is \(\mathcal O(2k+3)\), giving

\[
\operatorname{ind}D_k=\frac{(k+1)(k+2)}2.
\]

With the standard compatible complex geometry and connection, for \(k\ge0\) the relevant zero modes are the holomorphic sections just described. In particular, **a triplet of internal spinᶜ zero modes is available at \(k=1\)**. This is a concrete starting point for vectorlike quark modes. It requires the connection/flux, not merely the metric of CP².

For a nine-dimensional spinᶜ Dirac field on \(M^{3,1}\times\mathbb{CP}^2\times S^1\), a CP² zero mode combined with a periodic circle zero mode can give a four-dimensional Dirac field, assuming a vanishing higher-dimensional mass. Internal chirality does not by itself remove one four-dimensional chirality in this odd-dimensional compactification. Thus the vectorlike target does not require solving the harder problem of a chiral weak spectrum.

An index protects a difference of internal zero-mode counts; it does not forbid an allowed higher-dimensional Dirac mass. Keeping the resulting four-dimensional quark light still needs an appropriate symmetry or specified small mass parameter.

There are also distinct U(1) roles here: the spinᶜ connection, the circle graviphoton, and electromagnetism. They cannot be identified without checking the charge lattice and bundle lift. The spinᶜ charge condition is substantive. For example, ordinary up- and down-quark electric charges have a ratio of \(-2\), so they cannot both be odd integers in one common electromagnetic charge unit; the simplest spinᶜ lift in which every fermion has odd charge under that sole U(1) cannot accommodate both. An additional gauge connection or a more general combined spin/gauge structure may be needed. Vectorlike baryon charge is one possible extra ingredient in a strong-only model, but its four-dimensional gauge dynamics would also have to be addressed.

### A related geometric option: a circle bundle, rather than a product

If the circle is fibered over CP² with first Chern class \(pH\), odd \(p\) kills the pulled-back \(w_2\). At \(p=1\) the total space is the spin manifold \(S^5\), viewed as the Hopf circle bundle over CP². Spinors on the total space then have a geometric relation to charged spinᶜ descriptions on the base.

This is a legitimate nearby avenue, but it changes the topology from CP² × S¹. It also does not automatically produce light quarks: the ordinary Dirac operator on the positively curved round \(S^5\) has no zero modes. Flux or other additional structure would again be needed.

## 4. Charges and masses must be checked together

A color/charge assignment can be written as

\[
\mathcal H_q=\mathbf3\otimes
\bigl(\mathbb C_{n=-1}\oplus\mathbb C_{n=2}\bigr),
\qquad Q_{\rm em}=\frac n3.
\]

For a chosen diagonal \(\mathbb Z_3\) quotient generated by
\((\omega\mathbf1,e^{2\pi i/3})\), \(\omega^3=1\), the descent condition is \(t+n=0\pmod3\), where \(t\) is color triality. Both down-type and up-type triplets satisfy it. Products with conjugates contain color singlets of electric charges \(0,\pm1\), as required for a simple mesonic sector.

This is a representation assignment, **not proof that one specified CP² bundle lift and compactification realize every assigned mode**. In particular, if \(n\) is literally circle momentum, it costs mass. In an unwarped product compactification, schematically,

\[
m_4^2=m_9^2+\lambda_{\rm CP^2}^2
+\frac{(n+\vartheta)^2}{R_1^2},
\]

where \(\lambda_{\rm CP^2}\) is an internal Dirac eigenvalue and \(\vartheta\) includes the applicable circle twist or Wilson-line shift. For two modes of the same parent field with a common shift,

\[
\max\{|2+\vartheta|,|-1+\vartheta|\}\ge\frac32.
\]

Thus at least one has \(m_4\ge3/(2R_1)\). A small circle cannot provide both light quark charges as these simple momentum modes. Different bundle sectors, charge-dependent Wilson lines, or a photon obtained from a different gauge combination are possible modifications, but must be worked out explicitly. The CP² zero-mode result alone does not solve this circle mass issue.

The economical physical target is therefore to obtain vectorlike quarks from genuine internal zero modes and arrange electromagnetism through a consistent gauge/bundle embedding that does not force their light masses to be inverse-radius energies. This requires more than the bare metric product.

## 5. Combining the geometric and dual avenues

The two proposals solve different parts of the problem and can be combined:

1. **Geometric sector:** obtain light Dirac triplets, their conjugates, and the required color/charge lattice from a spinᶜ compactification or a related fibered geometry.
2. **Strong sector:** generate confinement and spontaneous global chiral symmetry breaking below the KK scale, giving an effective mesonic string and pseudo-Goldstone pions.
3. **Dual dictionary:** identify the candidate hard-scattering fermion and explain its relation to the mesonic string without assigning its amplitude the hadronic flat-string slope by assumption.

The scale separation in step 2 is possible in a four-dimensional effective gauge theory through dimensional transmutation:

\[
\Lambda_{\rm conf}\simeq M_{\rm KK}
\exp\!\left[-\frac{2\pi}{b_0\alpha_s(M_{\rm KK})}\right].
\]

For illustration only, ignoring flavor thresholds, six Dirac flavors give \(b_0=7\). Taking \(M_{\rm KK}=10\) TeV and \(\Lambda_{\rm conf}=0.2\) GeV requires \(\alpha_s(M_{\rm KK})\simeq0.083\). This shows why a high geometric scale and a low string tension need not coincide. It is not a fit to running QCD or a solution of the higher-dimensional gravitational equations. In a pure gravitational KK model, gauge couplings, radii, and the Planck scale are related and cannot all be chosen independently.

The outstanding question in step 3 is essential. With actual Dirac quarks, the local \(\bar q Wq\) meson operator is still bosonic. An exact duality preserves this parity. The corresponding fermionic candidate therefore needs a separately identified odd sector—possibly involving extra fields, fermionic defect modes, or an appropriate topological sector. A duality can change how that sector is represented; it cannot dispense with it.

If the fermion is defined as an ordinary product of a meson and an extra spinor, hard scattering will generally resolve a composite. To obtain the stronger bootstrap claim, the operator/disorder map and the current matrix elements must show why that constituent interpretation fails or has a limited domain of validity.

## 6. What has been established and what should be built next

The earlier flat-Ramond calculation remains valid for its stated model. It should not serve as a general exclusion of this broader program. The new ingredients justify a constructive search:

- Vectorlike Dirac quarks are compatible with the pion's approximate chiral symmetry.
- CP² has suitable triplet bundle and spinᶜ zero-mode structures; its lack of an ordinary spin structure is a problem with a known mathematical remedy.
- A high KK scale can coexist with a much lower dynamically generated confinement scale.
- Gauge dualities provide controlled precedents for changing the useful elementary variables, with important limits on the energy range and field content.

The next concrete model should specify the metric, flux/bundle, higher-dimensional fields, and electromagnetic generator; calculate the light Dirac spectrum; and verify the low-energy axial flavor currents. Then it should identify both the meson operator and the odd-parity candidate fermion, with a dual dictionary and the relevant electromagnetic or color-current correlators. A stable compactification background is also needed: the positively curved CP² product is not by itself a vacuum solution of pure higher-dimensional Einstein gravity with zero cosmological constant.

This is a more promising target than requiring both states to inherit one flat-space Veneziano factor. The geometric proposal can supply the quarks and representations, while a dual confining description can supply the mesonic string. The full meson/pointlike-fermion correspondence remains the dynamical part to establish.

## Calculations and sources

[geometry_checks.py](scripts/geometry_checks.py) checks the index in two forms, representation dimensions, the illustrative center quotient and meson charges, the circle-mass bound's saturation, the free-magnetic example, and the dimensional-transmutation estimate. Its results are in [geometry_results.json](calculations/geometry_results.json). Seven algebraic/numerical check groups pass; none constitutes a constructed KK vacuum or duality for nonsupersymmetric QCD.

The index calculations use \(c_1=3H\), \(c_2=3H^2\), \(p_1=3H^2\), \(\operatorname{Td}=1+3H/2+H^2\), and \(\widehat A=1-H^2/8\). These derivations were checked directly here. The global topology and cohomological interpretation are standard mathematical inputs.

Relevant literature includes Seiberg's [electric–magnetic duality paper](https://arxiv.org/abs/hep-th/9411149), Seiberg–Witten's [monopole-condensation and confinement paper](https://arxiv.org/abs/hep-th/9407087), and Jackiw–Rebbi's [spin-from-isospin paper](https://doi.org/10.1103/PhysRevLett.36.1116). These are reading pointers, not newly retrieved sources; primary-paper access remains unavailable in this environment. No claim of a published construction achieving the full proposal is made.
