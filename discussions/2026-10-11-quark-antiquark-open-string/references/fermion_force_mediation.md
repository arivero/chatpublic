# Fermion Force Mediation

*Exported ChatGPT conversation — 11 exchanges. Source: chatgpt.com/c/6ac98231-a860-83ed-9d55-32f580f220b7. Exported 2026-10-11.*

---

## 1. User

> I asked this question in https://physics.stackexchange.com/questions/142061/is-there-some-special-case-where-a-fermion-can-mediate-a-force and really 
>   I havent got a satisfactory answer, particularly to possible zero range.

### ChatGPT

Yes. After looking again at your 2014 question, I think the answers missed the most interesting case. In particular, **zero range does admit a very clean construction**.

A useful modern reference is the 2025 *Reviews of Modern Physics* review on exotic spin-dependent interactions. It now states explicitly that a single fermion cannot generate an ordinary potential **between two fermions**, because a vertex with the two external fermions plus one fermionic mediator would contain three fermion fields and cannot be a Lorentz scalar. [DOI+1](https://doi.org/10.1103/RevModPhys.97.025005) But that statement is narrower than your original question.

### 1. What is actually forbidden

A local relativistic Lagrangian must be Grassmann-even. Consequently every interaction term contains an even number of fermionic fields.

Thus

$$
\phi\,\bar\chi\psi
$$

is perfectly legal: one boson, **two fermions**.

What is illegal is schematically

$$
\bar\psi\psi\chi ,
$$

because it contains three fermionic fields.

Therefore a single fermion cannot mediate

$$
\psi_1+\psi_2\longrightarrow\psi_1+\psi_2
$$

as an ordinary $t$-channel elastic potential: at either end one would need three fermion legs.

But it **can** mediate something such as

$$
\psi_1+\phi_2\longrightarrow\phi_1+\psi_2 .
$$

At each end, a fermionic state turns into a bosonic state while emitting/absorbing the exchanged fermion. Total fermion parity remains conserved.

This is not exotic diagrammatically. SUSY gives concrete examples: $e^-e^-\to\tilde e^-\tilde e^-$ occurs through $t$-channel Majorana neutralino exchange. [arXiv](https://arxiv.org/abs/hep-ph/0307001) So the categorical statement “a fermion cannot mediate an interaction” is simply false.

---

### 2. A minimal Lorentz-invariant model

Take two scalar fields $\phi_{1,2}$, two Dirac fields $\psi_{1,2}$, and a fermionic mediator $\chi$:

$$
\mathcal L_\chi
=
\bar\chi(i\!\not\!\partial-M)\chi
-\left(
g_1\phi_1^\dagger\bar\chi\psi_1
+
g_2\phi_2^\dagger\bar\chi\psi_2
+\text{h.c.}
\right).
$$

Every term is Lorentz scalar and Grassmann-even.

Then

$$
\psi_1(p_1)+\phi_2(p_2)
\rightarrow
\phi_1(p_3)+\psi_2(p_4)
$$

has a single-$\chi$ $t$-channel contribution

$$
{\cal M}\sim
g_1g_2^*
\bar u_2(p_4)
\frac{\not q+M}{q^2-M^2}
u_1(p_1),
\qquad
q=p_1-p_3.
$$

That is literally a force-carrier diagram with a fermion as the internal exchanged particle.

The catch is that it is an **off-diagonal interaction in species/statistics space**, rather than

$$
|1\rangle\rightarrow |1\rangle
$$

at each source.

---

## 3. And now your zero-range case

This is where I think your intuition in the question was particularly good.

For momentum transfers $q\ll M$,

$$
\frac{\not q+M}{q^2-M^2}
=
-\frac1M
-\frac{\not q}{M^2}
-\frac{q^2}{M^3}
+\cdots .
$$

So integrating out the fermion gives

$$
\boxed{
\mathcal L_{\rm eff}
\supset
\frac{g_1g_2^*}{M}\,
\phi_1^\dagger\phi_2\,
\bar\psi_2\psi_1
+\text{h.c.}
}
$$

plus derivative corrections.

That is a completely local, Lorentz-invariant **contact interaction**.

And it contains two fermionic fields, so there is no spin/statistics or Lorentz-invariance problem whatsoever.

In the nonrelativistic spatial description,

$$
\frac{M}{\mathbf q^2+M^2}
\simeq
\frac1M-\frac{\mathbf q^2}{M^3}+\cdots
$$

becomes

$$
\frac1M\delta^{(3)}(\mathbf r)
+
\frac1{M^3}\nabla^2\delta^{(3)}(\mathbf r)
+\cdots .
$$

So yes: **fermion exchange naturally has a zero-range/contact limit.**

Notice what happened. Zero range did not somehow permit a three-fermion Lorentz scalar. Instead, the permissible process has

$$
(\text{fermion}\leftrightarrow\text{boson})
$$

at both ends.

---

## 4. There is an even sharper exact zero-range construction

You can make the mediator an **auxiliary fermion with no kinetic term**.

Define the fermionic current

$$
J=g_1\phi_1\psi_1+g_2\phi_2\psi_2 .
$$

Consider

$$
\boxed{
\mathcal L_{\rm aux}
=
-M\bar\chi\chi
+\bar\chi J+\bar J\chi
}
$$

with **no**

$$
\bar\chi i\!\not\!\partial\chi.
$$

Completing the square,

$$
\mathcal L_{\rm aux}
=
-M
\left(\bar\chi-\frac{\bar J}{M}\right)
\left(\chi-\frac{J}{M}\right)
+
\frac1M\bar J J .
$$

Integrating out $\chi$ therefore gives exactly

$$
\mathcal L_{\rm eff}
=
\frac1M\bar J J .
$$

The cross term contains

$$
\frac{g_1^*g_2}{M}
\phi_1^\dagger\phi_2\bar\psi_1\psi_2
+\text{h.c.}
$$

The “propagator” of the auxiliary fermion is just

$$
S_\chi(q)=\frac{i}{M},
$$

independent of $q$, hence

$$
S_\chi(x-y)
=
\frac{i}{M}\delta^{(4)}(x-y).
$$

**That is literally a zero-range fermionic mediator.**

Fermionic Hubbard–Stratonovich transformations using auxiliary Grassmann fields are a standard mathematical device; there are explicit examples in the literature. [ResearchGate](https://www.researchgate.net/publication/330218275_Phase_transitions_in_the_binary-alloy_Hubbard_model_Insights_from_strong-coupling_perturbation_theory)

But there is an important semantic point: with no kinetic term, $\chi$ is not a propagating particle. It is an auxiliary fermionic degree of freedom used to factorize the contact interaction.

So there are really three cases:

| process | single fermion? | range |
| --- | --- | --- |
| $\psi\psi\to\psi\psi$, unchanged sources | **No** | — |
| $\psi_1\phi_2\to\phi_1\psi_2$ | **Yes** | Yukawa-like $1/M$ range |
| same conversion via auxiliary $\chi$ | **Yes, algebraically** | exactly zero |

---

### 5. Can the off-diagonal interaction deserve to be called a “force”?

More than the old answers suggest.

Suppose the two asymptotic configurations

$$
|F_1B_2\rangle,\qquad |B_1F_2\rangle
$$

are degenerate. Fermion exchange produces an effective two-state Hamiltonian

$$
H(r)=
\begin{pmatrix}
E_0 & K(r)\\
K^*(r)&E_0
\end{pmatrix}.
$$

Its eigenstates are approximately

$$
\frac{|FB\rangle\pm |BF\rangle}{\sqrt2},
$$

with energies

$$
E_\pm(r)=E_0\pm |K(r)|.
$$

Therefore

$$
F_\pm(r)=-\frac{dE_\pm}{dr}
=\mp\frac{d|K(r)|}{dr}.
$$

So a single exchanged fermion really **can generate position-dependent Born–Oppenheimer potentials and forces**, provided the physical eigenstates are coherent combinations of two channels with the *same total fermion parity*. There is no conflict with the fermion-parity superselection rule.

For massive $\chi$, schematically,

$$
K(r)\sim
g_1g_2^*
\left[
M\frac{e^{-Mr}}{4\pi r}
+\text{spin/gradient terms}
\right].
$$

As $M$ becomes large this collapses onto the contact kernel above.

This, I think, is the answer your Stack Exchange question was actually reaching for.

One amusing development is that the 2025 RMP now contains almost exactly the question “why cannot a potential be mediated by a single fermion?”, but answers only the restricted **fermion–fermion elastic-potential** version. [Zentraler Informatikdienst](https://homepage.univie.ac.at/filip.ficek/papers/Cong_2025_RMP.pdf) Your zero-range loophole does not rescue that particular process, but it **does** expose the broader missing class: off-diagonal Bose↔Fermi exchange interactions, with the auxiliary-fermion construction giving an exact zero-range realization.

---

## 2. User

> Our motivational idea here was my conjectural usage of superstring with quarks in the extremes, the bosonic version is just a pion so somehow the string codes the force field that joins both quarks and its lenghts should be meson size; but the superpartner would be two quartks at the extremes of a spin 1/2 string. Muy conjecture was that this has the same scattering properties that a point particle and then the bootstrap program had a concrete realisation: a quark was just a composite of two (anti-)quarks.

### ChatGPT

Yes — stated that way, I think the conjecture is considerably sharper than the original “can a fermion mediate a force?” question.

Your proposed chain is roughly

$$
q\bar q+\text{bosonic flux tube}
\quad\longleftrightarrow\quad
qq+\text{fermionic flux tube},
$$

with the first member giving the mesonic/pion sector, while the second is a fermionic extended object. Then the stronger bootstrap hypothesis is that

$$
(qq)_{\bar{\mathbf3}}+\text{fermionic string}
\;\simeq\; \bar q,
$$

or, with orientations conjugated,

$$
(\bar q\bar q)_{\mathbf3}+\text{fermionic string}
\;\simeq\; q.
$$

That is much more interesting than ordinary quark–diquark phenomenology.

### The group theory works almost embarrassingly well

For color,

$$
3_c\otimes3_c=\bar3_c\oplus6_c,
$$

so the antisymmetric $qq$ channel has exactly the color representation of an antiquark. Conversely,

$$
\bar3_c\otimes\bar3_c=3_c\oplus\bar6_c,
$$

so an antisymmetric pair of antiquarks transforms exactly as a quark.

And for three light flavours the same thing happens:

$$
\bar3_f\otimes\bar3_f=3_f\oplus\bar6_f.
$$

Explicitly,

$$
u\quad\leftrightarrow\quad [\bar d\bar s],
\qquad
d\quad\leftrightarrow\quad [\bar s\bar u],
\qquad
s\quad\leftrightarrow\quad [\bar u\bar d].
$$

Even the electric charges agree:

$$
Q_{\bar d\bar s}=+\frac13+\frac13=+\frac23=Q_u,
$$

and similarly for $d,s$.

So the antisymmetric two-antiquark object has the same

$$
SU(3)_c\times SU(3)_f\times U(1)_{\rm em}
$$

quantum numbers as a quark.

This is exactly the algebraic observation behind Miyazawa hadronic supersymmetry and the later Catto–Gürsey quark–diquark construction. Catto and Gürsey even obtained the symmetry from an effective **string interaction**, with meson and baryon Regge trajectories becoming parallel. [OUP Academic+1](https://academic.oup.com/ptp/article/36/6/1266/1821704) Modern light-front superconformal QCD says almost verbatim that a supercharge transforms a quark into an anti-diquark in the same color representation. [ResearchGate](https://www.researchgate.net/publication/323443983_Hadronic_superpartners_from_a_superconformal_and_supersymmetric_algebra)

But they stop one step before you: their diquark is a **boson**, and the supersymmetry relates it to a fermionic quark. You are proposing to attach a fermionic string degree of freedom so that the whole composite is itself a fermion:

$$
0_{\rm diquark}\otimes\frac12_{\rm string}
=\frac12.
$$

That gives the candidate the correct spin-statistics directly.

## The one missing quantum number is extraordinarily informative

There is one immediate mismatch:

$$
B(q)=+\frac13,
\qquad
B(\bar q\bar q)=-\frac23.
$$

They differ by exactly

$$
\Delta B=1.
$$

Thus the proposed fermionic string must carry one unit of baryon number:

$$
B_{\rm string}=+1
$$

for

$$
[\bar q\bar q]+\text{string}\sim q.
$$

That might have sounded artificial ten years ago. It sounds much less artificial **this week**.

The STAR result published in *Science* in August 2026, and highlighted by *Nature* on October 6, finds evidence disfavoring the picture in which baryon number simply follows the valence quarks, and favoring transport by a **gluonic baryon junction**. [Icahn School of Medicine at Mount Sinai+1](https://scholars.mssm.edu/en/publications/tracking-the-baryon-number-with-nuclear-collisions/) The whole baryon-junction literature going back to Artru and Rossi–Veneziano associates baryon number with the topology of the confining field rather than simply summing $1/3$ labels attached to the quarks. [Springer Nature+1](https://link.springer.com/article/10.1140/epjc/s10052-024-13702-9)

That is remarkably close in spirit to what your construction requires:

$$
\boxed{\text{the missing integer quantum number lives in the string/flux configuration.}}
$$

There is an important geometrical difference: the conventional baryon-number carrier is a **three-pronged junction**, whereas your object initially sounds like an ordinary open string. An ordinary $q\bar q$ flux tube has no obvious integer baryon charge. So a serious implementation probably requires the fermionic string state to carry a junction/topological sector, not merely a Ramond excitation of the mesonic string.

### Now the difficult claim: “same scattering as a point particle”

Here I would weaken your original conjecture in one precise way.

It is almost automatic that it has the **same long-wavelength scattering** as a point quark.

Suppose the composite has size $R$. Its color-current matrix element has the general form

$$
\langle Q(p')|J_A^\mu|Q(p)\rangle
=
g_s\,\bar u(p')\gamma^\mu T_Au(p)\,
F(q^2)+\cdots .
$$

Because the total object transforms as a $3_c$,

$$
F(0)=1.
$$

Thus for

$$
|q|R\ll1
$$

the gluon literally cannot distinguish it from an elementary triplet:

$$
F(q^2)
=
1+c_1 q^2R^2+\cdots .
$$

The same applies to electromagnetic and flavour currents if the representation assignments above hold.

This is an exact analogue of the equivalence between a point charge and an extended charge distribution in the multipole limit.

But **exact equality of the S-matrix at arbitrary momentum is much harder**.

A genuine finite string has internal excitations. Consequently its current correlator generically contains additional poles,

$$
q^2=M_n^2,
$$

and its form factor cannot remain

$$
F(q^2)=1
$$

at all $q^2$. For an actual string this is even more explicit: one expects a Regge tower with

$$
M_n^2\sim\frac{n}{\alpha'}.
$$

Thus a physically extended object of mesonic size cannot have literally the same all-energy S-matrix as a structureless Dirac particle unless something very nontrivial happens: all internal excitations must decouple from the relevant amplitudes, or the “composite description” must be a dual description rather than a conventional bound state.

That second possibility is, I think, where your **bootstrap** interpretation becomes interesting.

You should not require

> a little extended bag of two antiquarks accidentally looks pointlike.

Rather, require

$$
q
\quad\equiv\quad
[\bar q\bar q]\otimes{\cal J}_{B=1}
$$

as **two descriptions of the same state/operator sector**.

Then no compositeness form factor need appear. It would be more like a nonperturbative operator identity/duality than a constituent model.

And this is much closer philosophically to the old S-matrix bootstrap: the particle appearing as an exchanged elementary state in one channel is a bound/composite state in another. Veneziano duality was precisely what made that idea concrete for hadrons before QCD displaced the original bootstrap programme. [Arpi+1](https://arpi.unipi.it/handle/11568/881408)

## There is also a striking string-history precedent

Bars and Hanson wrote *Quarks at the ends of the string* in 1976. They explicitly constructed relativistic strings with spin-$\frac12$ endpoint degrees of freedom; one formulation gave an algebra resembling supersymmetry, and they constructed meson and baryon quark-string models. [APS Journals](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.13.1744)

Then Catto–Gürsey showed that a quark–diquark supersymmetry emerges when the confining interaction becomes effectively stringlike. [ResearchGate](https://www.researchgate.net/publication/225413846_Algebraic_treatment_of_effective_supersymmetry)

And present-day superconformal light-front QCD goes further: meson and baryon superpartners can have related light-front wavefunctions and, in some versions, identical predicted form factors. [SLAC National Accelerator Laboratory+1](https://www.slac.stanford.edu/pubs/slacpubs/16250/slac-pub-16453.pdf)

So three quarters of your mechanism exist separately in the literature:

$$
\begin{array}{ccl}
qq_{\bar3}&\sim&\bar q\quad\text{as color source},\\[2mm]
\text{meson}&\leftrightarrow&\text{baryon via hadronic SUSY},\\[2mm]
\text{confining field}&\sim&\text{string},\\[2mm]
B&\sim&\text{topological/junction degree of freedom}.
\end{array}
$$

What I do **not** see in these constructions is your final identification

$$
\boxed{
q
\equiv
(\bar q\bar q)_{\mathbf3}
+\text{a spin-}\frac12,\ B=1\text{ string configuration}
}
$$

as a genuine bootstrap equivalence.

One curiosity: the modern Brodsky–de Téramond–Dosch superconformal construction actually makes the **pion exceptional**: the $L=0$ pion is the supersymmetric ground state and has no baryon superpartner. [SLAC National Accelerator Laboratory](https://www.slac.stanford.edu/pubs/slacpubs/16250/slac-pub-16397.pdf) So your proposal cannot simply be identified with their supersymmetry. Your “pion → fermionic string” operation would be a different, stronger worldsheet supersymmetry.

The cleanest version of your conjecture, therefore, is not “a quark is a conventional composite”. It is

$$
\boxed{
\text{quark}
\;\longleftrightarrow\;
\text{two antiquark endpoints}
+\text{fermionic/topological QCD string}
}
$$

with the nontrivial requirements

$$
(3_c,3_f,Q,\tfrac12,B)
$$

all reproduced by the complete object, and with **S-matrix duality**, rather than ordinary low-energy compositeness, explaining why the result is pointlike.

That formulation also connects your original fermion-mediated-force question directly back to the model: the fermionic “particle” being exchanged can literally be the supersymmetric flux-tube configuration itself.

---

## 3. User

```text
I got this feedback from Fable 5.1   Summary. The object you describe exists in string theory. In the Ramond–Neveu–Schwarz open string with Chan-Paton factors, the Ramond ground state is
  a spin-1/2 particle with one flavor label at each end, and its Neveu–Schwarz partner carries the same two labels. Your conjecture holds for it in a
  precise form: it scatters as a point fermion below the string scale, with the first deviation at fourth order in energy over string scale, and above
  that scale it shows the Regge tower. What the string refuses is a sector-dependent size. The fermionic and bosonic sectors share the position
  oscillators, so the fermionic partner of a hadron-sized boson is hadron-sized. The electron and the pion differ in size by more than three orders of
  magnitude, so the pairing with QCD mesons and diquarks has to be a symmetry acting on quantum numbers, with no shared string. The zero-range version
  of your picture survives as a Lorentz-invariant spinor with two flavor indices, and in that version the fermionic-mediator question becomes empty in
  exactly the way my previous answer described.

  What the string carries and what the labels carry

  - A Chan-Paton label carries charge and flavor. It carries no spin, no statistics, and no position beyond the string endpoint. Spin and statistics of
    a state come entirely from the worldsheet. The Neveu–Schwarz sector gives the scalar and vector strings, the Ramond sector gives the spinor. So "a
    quark composed of two antiquarks" can mean one thing: the state carries the additive quantum numbers of two antiquark labels. That is what your
    counting uses, and it is consistent. Both label structures you need exist: an oriented string gives N ⊗ N̄, your mesonic 24 ⊕ 1, and a string between
    a stack and its orientifold image gives N ⊗ N, your diquark 15 ⊕ 10.
  - The tension is the same in both sectors. The force field joining the two labels is identical for the pion-like string and for its spinor partner.
    The Ramond zero modes add spin and statistics and leave the tension and the position oscillators unchanged. The transverse spread of the ground
    state, ⟨X²⟩ ∝ α' Σ 1/n, comes from the same oscillators in both sectors, which is the Karliner–Klebanov–Susskind result, so the two partners have
    the same size. This dissolves the premise of your Stack Exchange question: in the string, the fermionic partner carries a bosonic force field plus
    fermionic zero modes. A fermion mediates a force in the string in one way, as a whole Ramond string exchanged between other strings.
  - The string three-vertices are NS–NS–NS and NS–R–R with cyclically matched labels. That is the even-fermion-number rule from my previous answer in
    string form. A Ramond string exchanged between a boson with labels (a,b) and a fermion with labels (b,c) swaps which label pair sits on the fermion,
    and the exchange is dual to the s-channel fermion with labels (a,c). Ramond's 1971 model is the bootstrap realization of fermion exchange.
    Aharonov, Casher and Susskind showed in 1971 that the Ramond sector arises from an odd number of partons, which is the constituent form of the same
    rule. The attempts to read those fermions as bare baryons or as quarks are the history you discussed on PhysicsOverflow.
  - QCD's flux tube has no Ramond sector. The effective QCD string is bosonic. QCD's fermionic strings are baryons in the quark–diquark picture, with
    the color-antitriplet diquark playing the antiquark's role; they have the same Regge slope and the same size scale as mesons. That is the empirical
    form of the same statement, and it is where Miyazawa's quark–diquark supersymmetry lives.

  Point-like scattering, with numbers

  The tree-level four-point amplitude of massless open-string states factorizes:

  A_string(s,t) = A_SYM(s,t) * V(s,t)
  V(s,t) = Gamma(1 - a s) Gamma(1 - a t) / Gamma(1 - a s - a t),    a = alpha'
         = 1 - (pi^2/6) a^2 s t + O(a^3)

  The spinor string scatters as the point fermion of super-Yang–Mills with corrections starting at dimension eight. No dimension-six contact term
  appears at tree level. In that sense a fermionic open string is more point-like than a generic composite fermion, and the same holds for its bosonic
  partner. The departure is the pole tower at α' s = n.

  ┌──────────────────────────────────────────┬──────────────────────────────────────┐
  │                 Quantity                 │                Value                 │
  ├──────────────────────────────────────────┼──────────────────────────────────────┤
  │ pion charge radius                       │ 0.66 fm                              │
  ├──────────────────────────────────────────┼──────────────────────────────────────┤
  │ electron radius, LEP Bhabha, 95% CL      │ < 2.8 × 10⁻¹⁹ m                      │
  ├──────────────────────────────────────────┼──────────────────────────────────────┤
  │ hadronic Regge slope                     │ α' ≈ 0.9 GeV⁻², string scale ≈ 1 GeV │
  ├──────────────────────────────────────────┼──────────────────────────────────────┤
  │ string resonances excluded by CMS dijets │ M_s < 7.4 TeV                        │
  └──────────────────────────────────────────┴──────────────────────────────────────┘

  One string cannot carry both the first row and the second. A fermionic string that is a Standard Model fermion needs a string scale above the CMS
  bound, and then its Neveu–Schwarz partner is a point-like scalar with the same labels. That is the structure of intersecting-brane realizations of the
  Standard Model, where quarks and leptons are strings between brane stacks with the stack labels at the ends. Your identification differs in making
  the labels light-quark flavors and the partners actual hadrons.

  The zero-range version

  Send the string scale to infinity. The Ramond string with labels (i,j) becomes a spinor field ψ_ij, the Neveu–Schwarz string becomes a scalar φ_ij,
  and both are Lorentz invariant with no further input. The labels become flavor indices. The force between the labels is unobservable, for the reason
  in my previous answer: a contact term acts on L = 0, where the swap operator is the identity. In this version the content of the sBootstrap is the
  representation content of ψ_ij under flavor SU(5), in your 2009 notation:

  15 = (3,1)(6) + (2,3)(1) + (1,6)(-4)                              diquarks
  24 = (1,1)(0) + (3,1)(0) + (2,3)(-5) + (2,3bar)(5) + (1,8)(0)      mesons

  with (2,3)(1) and (1,6)(−4) the quark partners and (2,3)(∓5) the charged-lepton partners. Everything below the string scale is this label algebra plus
  the mass relations. The string adds nothing observable there, and at the string scale it adds the tower.
```

### ChatGPT

Fable has found a genuinely relevant historical/string-theoretic structure, but I would not accept the summary as written. The important part is real; two of its strongest conclusions are not.

The cleanest assessment is:

| Claim | Verdict |
| --- | --- |
| RNS open strings have fermionic Ramond states carrying Chan–Paton labels at their ends | **Yes** |
| Their bosonic partners carry the same endpoint labels and same $\alpha'$ | **Yes, with an important qualification** |
| Therefore your proposed two-endpoint spin-$\tfrac12$ string “exists” | **A close analogue exists, not yet your object** |
| Low-energy four-point amplitudes can first deviate at $O(\alpha'^2E^4)$ | **Yes in the standard supersymmetric open-string amplitude** |
| NS and R partners necessarily have the same physical size | **Too strong / badly phrased** |
| Ordinary QCD flux tubes categorically have no Ramond sector | **Too strong** |
| The zero-range limit makes the endpoint interaction unobservable because $L=0$ makes exchange trivial | **No — this is wrong** |
| $15$ vs $24$ SU(5) endpoint algebra | **Yes; and it actually gives a counterexample to the previous claim** |

The details matter.

## 1. The biggest correction: the NS partner of the Ramond ground state is not generically a pion-like scalar

For the ordinary GSO-projected open RNS superstring,

$$
\alpha'M^2_{\rm NS}=N-\frac12,\qquad
\alpha'M^2_{\rm R}=N.
$$

The Ramond ground state is a massless spacetime spinor. But the NS **ground state is a tachyon and is removed by GSO**. The surviving massless NS state is

$$
\psi^\mu_{-1/2}|0;k\rangle_{\rm NS},
$$

a **vector**. Thus the standard massless supermultiplet is

$$
A_\mu \oplus \lambda ,
$$

ten-dimensional super-Yang–Mills, not scalar + spinor. [Fermilab+1](https://lss.fnal.gov/archive/other/kul-tf-89-35.pdf)

So this sentence from Fable,

> “the Ramond ground state is a spin-1/2 particle ... and its Neveu-Schwarz partner carries the same two labels”

is broadly right, but if “partner” is being used to support your **pion ↔ quark/string** construction, it hides the central difficulty: in the standard critical open superstring the partner is a vector.

Scalars certainly occur after compactification, from internal vector components, branes at angles, etc. But then the statement becomes construction-dependent.

Historically, the **old hadronic RNS model** is actually closer to your motivation than modern critical superstring theory: Ramond's 1971 construction really was an attempt to put fermionic hadrons on dual Regge trajectories. [APS Journals](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.3.2415)

---

## 2. Chan–Paton algebra: this part is genuinely useful

Here Fable has identified something important.

An oriented open string carries endpoint labels, and schematically

$$
N\otimes\bar N.
$$

Strings involving an orientifold image can give

$$
N\otimes N
=
\operatorname{Sym}^2N\oplus\wedge^2N.
$$

For $SU(5)$,

$$
5\otimes\bar5=1\oplus24,
$$

and

$$
5\otimes5=15\oplus10.
$$

So your old $24$ meson versus $15$ diquark bookkeeping does fit extremely naturally into open-string endpoint algebra.

But Chan–Paton labels are **gauge/internal indices**, not physical constituent particles sitting at the endpoints. Saying

$$
\psi_{ij}
$$

carries two labels is not yet saying

$$
\psi_{ij}=[\bar q_i\bar q_j]+\text{string}.
$$

That latter statement is your additional bootstrap interpretation.

This is where I would distinguish:

$$
\boxed{\text{two endpoint quantum numbers}}
$$

from

$$
\boxed{\text{two constituent antiquarks}}.
$$

String theory supplies the former automatically. Your conjecture needs the latter identification.

---

## 3. The $E^4/M_s^4$ claim is real — but model-specific

For the standard tree-level open-superstring four-point amplitude one indeed gets a Yang–Mills amplitude multiplied by the Veneziano form factor,

$$
{\cal A}_{\rm string}
=
{\cal A}_{\rm YM}
V(s,t),
$$

with

$$
V(s,t)=
\frac{\Gamma(1-\alpha's)\Gamma(1-\alpha't)}
{\Gamma(1-\alpha'(s+t))}.
$$

Expanding,

$$
\log V
=
-\zeta(2)\alpha'^2st
-\zeta(3)\alpha'^3st(s+t)
+\cdots,
$$

hence

$$
V
=
1-\frac{\pi^2}{6}\alpha'^2st+O(\alpha'^3).
$$

So there is indeed **no $O(\alpha')$** correction in this amplitude. The leading local correction is dimension eight:

$$
\Delta{\cal L}\sim\alpha'^2 F^4+\cdots.
$$

And the same supersymmetric disk amplitudes include Ramond fermions. The low-energy limit gives the expected gaugino–gauge-boson interactions of super-Yang–Mills. [AdS/CFT Duality+1](https://adscft.org/string-ii/10-tree-amplitudes-chan-paton/)

So Fable's striking statement

$$
\frac{\Delta{\cal A}}{{\cal A}}
\sim
\left(\frac{E}{M_s}\right)^4
$$

is essentially correct **for that particular open-superstring setup**.

But it shouldn't be promoted into:

> every fermionic string is pointlike through dimension six.

Generic compactified/intersecting-brane models can have additional heavy states and effective operators. The simple universal Veneziano factor is a special virtue of the maximally simple massless open-string amplitude.

Still, this is highly relevant to your bootstrap idea: a string can look **much more pointlike** at low energy than an ordinary two-body bound state with

$$
F(q^2)=1-\frac16r^2q^2+\cdots .
$$

That part of Fable's answer is useful.

---

## 4. “Same size” is not quite what Karliner–Klebanov–Susskind showed

Fable's underlying argument is sound:

the target-space coordinate field $X^\mu$ is common to NS and R sectors, and the bosonic oscillator algebra and $\alpha'$ are the same. Therefore you cannot simply decree

$$
R_{\rm NS}\sim1\ {\rm fm},
\qquad
R_{\rm R}\sim10^{-19}\ {\rm m}
$$

for two states of the same fundamental open string while retaining the same $\alpha'$.

That's a genuine obstruction.

But invoking Karliner–Klebanov–Susskind as establishing a common finite “size” is misleading. Their striking result is precisely that the transverse mean-square size of a fundamental string has a logarithmic ultraviolet divergence:

$$
\langle R_\perp^2\rangle
\sim
\alpha'\sum_{n=1}^{n_{\rm max}}\frac1n
\sim
\alpha'\log n_{\rm max}.
$$

They emphasize the **divergent average size**, not a finite radius $\sqrt{\alpha'}$. [ResearchGate+1](https://www.researchgate.net/publication/241350232_Size_and_Shape_of_Strings)

At a common observational resolution, NS and R states inherit the same $X^\mu$ fluctuations. That's the defensible statement.

And the more physical obstruction is actually simpler:

$$
\boxed{\text{same }\alpha'\Rightarrow\text{same Regge/string scale}.}
$$

A hadronic string with

$$
\alpha'_{\rm had}\simeq0.9\ {\rm GeV}^{-2}
$$

has excitations around the GeV scale. It cannot simultaneously describe a Standard-Model fermion for which no such tower has appeared up to multi-TeV energies.

The quoted CMS “string resonance” limit is also model-dependent: CMS excluded the particular benchmark string-resonance model below about $7.6$ TeV, not “all possible strings below 7.6 TeV.” [CMS Results](https://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/EXO-17-026/)

Likewise $r_e<2.8\times10^{-19}\,\mathrm m$ comes from a particular phenomenological electron form-factor parametrization in LEP Bhabha scattering. It is not a model-independent geometric radius. [CERN Document Server+1](https://cds.cern.ch/record/427261?ln=en&utm_source=chatgpt.com)

---

# 5. The zero-range paragraph is where Fable goes seriously wrong

This:

> “a contact term acts on $L=0$, where the swap operator is the identity”

confuses **spatial exchange** with **internal exchange**.

For relative orbital angular momentum $L$,

$$
P_{\rm spatial}=(-1)^L.
$$

Thus at $L=0$,

$$
P_{\rm spatial}=+1.
$$

Fine.

But the full exchange operator is

$$
P=P_{\rm spatial}
P_{\rm spin}
P_{\rm flavor}
P_{\rm color}\cdots .
$$

At $L=0$, only the first factor becomes $+1$. The internal exchange operators remain extremely observable.

Consider precisely Fable's $SU(5)$ example:

$$
5\otimes5=15_s\oplus10_a.
$$

The label-swap operator has

$$
P_{12}|15\rangle=+|15\rangle,
$$

while

$$
P_{12}|10\rangle=-|10\rangle.
$$

Therefore an exactly zero-range interaction

$$
\boxed{
H_{\rm contact}
=
g\,\delta^{(3)}(\mathbf r)\,P_{12}
}
$$

gives

$$
V_{15}=+g\,\delta^{(3)}(\mathbf r),
\qquad
V_{10}=-g\,\delta^{(3)}(\mathbf r).
$$

It **maximally distinguishes** the two endpoint representations.

More generally,

$$
V(\mathbf r)
=
\delta^{(3)}(\mathbf r)
\left[
c_0
+c_s\,\boldsymbol\sigma_1\!\cdot\!\boldsymbol\sigma_2
+c_f\,T_1^aT_2^a
+c_P P_{\rm flavor}
+\cdots
\right]
$$

contains plenty of observable spin/flavour/color physics despite having exactly zero range.

This is standard atomic/nuclear/QFT physics: S-wave contact interactions are often *where internal-state dependence is strongest*.

So the conclusion

> “in the zero-range version the fermionic-mediator question becomes empty”

does **not** follow.

It is almost the opposite: once the spatial structure collapses, the problem reduces very cleanly to an **operator acting on the internal endpoint Hilbert space**.

And your $15/10$ algebra is an especially nice demonstration.

---

## 6. Also, $\alpha'\to0$ isn't itself the same thing as a zero-range fermion mediator

There are two limits being mixed.

The string zero-slope limit

$$
\alpha'\rightarrow0
$$

decouples the massive Regge tower and leaves the low-energy field theory. For the standard open superstring that is super-Yang–Mills:

$$
A_\mu,\lambda .
$$

The Ramond fermion $\lambda$ remains a **propagating field**. It does not automatically turn into a contact interaction.

To obtain an actual zero-range fermionic exchange you need something like

$$
M_\chi\rightarrow\infty,
$$

so

$$
\frac{\not q+M_\chi}{q^2-M_\chi^2}
\longrightarrow
-\frac{1}{M_\chi}+\cdots ,
$$

giving a local operator.

Or, exactly, use an auxiliary Grassmann field with no kinetic term, as in the construction we discussed before.

Thus there are two independent limits:

$$
\boxed{\alpha'\to0:\quad \text{string}\rightarrow\text{point-particle QFT}}
$$

versus

$$
\boxed{M_{\rm mediator}\to\infty:\quad
\text{finite-range exchange}\rightarrow\text{contact operator}.}
$$

Fable has implicitly identified them. They need not coincide.

---

## 7. “QCD's flux tube has no Ramond sector” should be softened

For ordinary confining $3+1$-dimensional QCD, the empirically successful effective string at long distances certainly does **not presently exhibit a known massless worldsheet fermion paired supersymmetrically with the transverse Goldstones**.

Current effective-QCD-string work describes the transverse Nambu–Goldstone modes plus, notably, a massive pseudoscalar worldsheet axion. [arXiv](https://arxiv.org/abs/2606.06668)

So:

> “there is no established Ramond sector of the ordinary QCD flux tube”

is fair.

But “QCD's flux tube has no Ramond sector” as a theorem is not. There is literature explicitly considering fermionic degrees of freedom and possible worldsheet supersymmetry in confining strings; the allowed worldsheet theories with fermions have been studied systematically. [arXiv+1](https://arxiv.org/abs/hep-th/0010166)

And once physical quarks live at the endpoints, there are additional fermionic **boundary** degrees of freedom anyway.

---

## 8. The Aharonov–Casher–Susskind connection is real and perhaps more important than Fable realizes

Their 1971 dual-parton paper explicitly took spin-$\tfrac12$ partons with nearest-neighbour interactions and found:

- even number of partons $\rightarrow$ Neveu–Schwarz mesonic model;
- odd number $\rightarrow$ baryonic half-integer-spin model.

They actually computed a meson–baryon amplitude. [INSPIRE+1](https://inspirehep.net/literature/69202)

Their 1972 treatment states even more explicitly that even parton number produces the NS theory while odd parton number produces half-integer-spin baryonic states. [Tel Aviv University](https://cris.tau.ac.il/en/publications/spin-12-partons-in-a-dual-model-of-hadrons/)

That is remarkably close to the **spirit** of what you had in mind.

I would nevertheless not write

> “Ramond's 1971 model is the bootstrap realization of fermion exchange.”

Ramond's original paper was a construction of a dual theory for free fermionic states on Regge trajectories. [APS Journals](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.3.2415) Interaction vertices and mixed boson/fermion amplitudes were developed around it. Fable has compressed several historical steps into one sentence.

---

# What survives for your conjecture

After stripping away the overstatements, I think Fable has actually strengthened the interesting part.

You have three logically distinct objects:

$$
\begin{array}{lll}
\text{NS/RNS string theory} &
:& \text{bosonic and fermionic strings with common endpoint labels};\\[1mm]
\text{Chan--Paton algebra} &
:&
5\bar5=1+24,\quad
55=10+15;\\[1mm]
\text{your bootstrap interpretation} &
:&
\text{fermionic }(ij)\text{ string}\equiv\text{pointlike quark/lepton state}.
\end{array}
$$

The first two really exist.

Your nontrivial conjecture is the third equality.

And the standard open-string amplitude gives a much better motivation for it than I initially gave: a genuinely extended fermionic string can have

$$
{\cal A}
=
{\cal A}_{\rm point}
\left[
1+O\!\left(\frac{E^4}{M_s^4}\right)
\right],
$$

rather than the generic composite-particle expectation

$$
1+O\!\left(\frac{E^2}{\Lambda^2}\right).
$$

So **the pointlike-scattering part of your old intuition has a concrete string realization**.

What does *not* follow is that the fermionic partner of a physical pion can simultaneously be a pointlike quark if they are literally NS/R states of the same fundamental string: common $\alpha'$ ties their Regge scales together.

And, importantly, the zero-range version does **not** evaporate. It becomes an especially transparent internal-state problem:

$$
\boxed{
5\otimes5
\;\xrightarrow{\;\delta^3(r)\,{\cal O}_{\rm internal}\;}
15\oplus10 ,
}
$$

with contact interactions perfectly capable of distinguishing the two representations.

So on the point you originally cared about on Physics.SE, I think Fable inadvertently gives you the ingredients for a better answer and then draws the wrong conclusion from them.

---

## 4. User

> can you calculate a scattering of two fermionic strings and compare with the diagram for two electrons scatter via photon exchange? Draw diagrams, calculate, etc.

### ChatGPT

![Generated image: Tree-level scattering — fermionic open strings vs e⁻e⁻ scattering](image1.png)

---

## 5. User

> can you calculate a scattering of two fermionic strings and compare with the diagram for two electrons scatter via photon exchange? all the math.

### ChatGPT

**[Analizado]**

```python
import sympy as sp
c=sp.symbols('c')
t=-(1-c)/2
u=-(1+c)/2
F=(1+u**2)/t**2+(1+t**2)/u**2+2/(t*u)
sp.simplify(F)
```

**[Resultado]**

```text
2*(c**4 + 6*c**2 + 9)/(c**4 - 2*c**2 + 1)
```

**[Analizado]**

```python
import mpmath as mp
for z in [0.1,0.25,0.5,1,2]:
    V=mp.gamma(1+z/2)**2/mp.gamma(1+z)
    print(z,float(V),float(V**2),float(1-mp.pi**2/12*z**2))
```

**[STDOUT/STDERR]**

```text
0.1 0.9961736355156747 0.9923619120965164 0.9917753296657589
0.25 0.9784608219532953 0.9573855800975183 0.948595810410993
0.5 0.9270373386506858 0.8593982272525463 0.7943832416439717
1 0.7853981633974484 0.616850275068085 0.1775329665758868
2 0.5 0.25 -2.289868133696453
```

Yes. There is a particularly clean calculation if we use a massless Ramond open-string state carrying a charge under a Cartan $U(1)\subset U(2)$. Then the tree-level process has exactly the same $t$- and $u$-channel structure as Møller scattering, and for the simplest same-brane open superstring the result is

$$
\boxed{\mathcal M_{\rm string}
=
V(t,u)\,\mathcal M_{\rm M\o ller}}
$$

with an explicit Veneziano form factor $V$. This is essentially the precise version of Fable's “looks pointlike up to $E^4/M_s^4$” statement.

I will take the electron mass to zero, because that is the appropriate comparison with a massless Ramond ground state.

---

# 1. Point particles: $e^-e^-\to e^-e^-$

Take

$$
e^-(p_1)+e^-(p_2)\longrightarrow e^-(p_3)+e^-(p_4),
$$

with

$$
s=(p_1+p_2)^2,\qquad
t=(p_1-p_3)^2,\qquad
u=(p_1-p_4)^2,
$$

and, for $m_e=0$,

$$
s+t+u=0.
$$

There are two diagrams because the final fermions are identical:


```text
t channel                      u channel

p1 ─────●──── p3              p1 ─────●──── p4
        │ γ                            │ γ
        │                              │
p2 ─────●──── p4              p2 ─────●──── p3
```


The amplitudes are

$$
i\mathcal M_t
=
(-ie)^2
\left[
\bar u(p_3)\gamma^\mu u(p_1)
\right]
\frac{-ig_{\mu\nu}}{t}
\left[
\bar u(p_4)\gamma^\nu u(p_2)
\right],
$$

and

$$
i\mathcal M_u
=
(-ie)^2
\left[
\bar u(p_4)\gamma^\mu u(p_1)
\right]
\frac{-ig_{\mu\nu}}{u}
\left[
\bar u(p_3)\gamma^\nu u(p_2)
\right].
$$

Because we exchange identical external fermions,

$$
\boxed{
\mathcal M_{\rm QED}
=
e^2\left[
\frac{J_t}{t}
-
\frac{J_u}{u}
\right]
}
$$

up to an irrelevant overall phase, where

$$
J_t=
(\bar u_3\gamma^\mu u_1)
(\bar u_4\gamma_\mu u_2),
$$

$$
J_u=
(\bar u_4\gamma^\mu u_1)
(\bar u_3\gamma_\mu u_2).
$$

The relative minus sign is Fermi statistics. [Physics Stack Exchange](https://physics.stackexchange.com/questions/645128/factor-of-1-2-in-the-cross-section-of-m%C3%B8ller-scattering)

---

# 2. Squaring the QED amplitude

Average over initial spins and sum over final spins:

$$
\overline{|\mathcal M|^2}
=
\frac14\sum_{\rm spins}|\mathcal M|^2 .
$$

Use

$$
\sum_s u(p,s)\bar u(p,s)=\not p
$$

for massless fermions, and

$$
\operatorname{Tr}
(\not a\gamma^\mu\not b\gamma^\nu)
=
4\left(
a^\mu b^\nu+a^\nu b^\mu
-g^{\mu\nu}a\cdot b
\right).
$$

For the $t$-channel,

$$
\frac14\sum |\mathcal M_t|^2
=
\frac{e^4}{4t^2}
\operatorname{Tr}
(\not p_3\gamma^\mu\not p_1\gamma^\nu)
\operatorname{Tr}
(\not p_4\gamma_\mu\not p_2\gamma_\nu),
$$

which gives

$$
\boxed{
\frac14\sum |\mathcal M_t|^2
=
2e^4\frac{s^2+u^2}{t^2}.
}
$$

Likewise,

$$
\boxed{
\frac14\sum |\mathcal M_u|^2
=
2e^4\frac{s^2+t^2}{u^2}.
}
$$

The interference trace gives

$$
\frac14\sum
2\operatorname{Re}
(\mathcal M_t(-\mathcal M_u)^*)
=
4e^4\frac{s^2}{tu}.
$$

Thus

$$
\boxed{
\overline{|\mathcal M_{\rm QED}|^2}
=
2e^4
\left[
\frac{s^2+u^2}{t^2}
+
\frac{s^2+t^2}{u^2}
+
\frac{2s^2}{tu}
\right].
}
$$

This is the standard ultrarelativistic Møller result.

---

# 3. Centre-of-mass form

For CM scattering angle $\theta$,

$$
t=-\frac{s}{2}(1-\cos\theta),
$$

$$
u=-\frac{s}{2}(1+\cos\theta).
$$

Hence

$$
tu
=
\frac{s^2}{4}\sin^2\theta.
$$

One finds

$$
\frac{s^2+u^2}{t^2}
+
\frac{s^2+t^2}{u^2}
+
\frac{2s^2}{tu}
=
2\frac{(3+\cos^2\theta)^2}{\sin^4\theta}.
$$

Since the final electrons are identical,

$$
\frac{d\sigma}{d\Omega}
=
\frac{1}{2!}
\frac{\overline{|\mathcal M|^2}}
{64\pi^2s}.
$$

With

$$
e^2=4\pi\alpha,
$$

this gives

$$
\boxed{
\frac{d\sigma_{\rm QED}}{d\Omega}
=
\frac{\alpha^2}{2s}
\frac{(3+\cos^2\theta)^2}
{\sin^4\theta}.
}
$$

---

# 4. Now replace the electrons by Ramond open strings

The massless Ramond vertex operator in the $-1/2$ picture is

$$
V_R^{(-1/2)}(k,u;x)
=
g_o\,\lambda\,
u^A S_A(x)
e^{-\phi(x)/2}
e^{ik\cdot X(x)}.
$$

Here

- $u^A$ is the spacetime spinor polarization,
- $S_A$ is the worldsheet spin field,
- $e^{-\phi/2}$ supplies superghost charge,
- $\lambda$ is the Chan–Paton matrix.

Four Ramond vertices already have total picture

$$
4\times\left(-\frac12\right)=-2,
$$

which is exactly what is required on the disk.

The disk amplitude is

$$
\mathcal A_4
=
\int
\frac{\prod_i dx_i}
{\operatorname{vol} PSL(2,\mathbb R)}
\,
\left\langle
V_{R,1}V_{R,2}V_{R,3}V_{R,4}
\right\rangle.
$$

Use the conformal symmetry to fix

$$
x_1=0,\qquad x_3=1,\qquad x_4=\infty,
$$

and write

$$
x_2=x,\qquad 0<x<1.
$$

The plane-wave correlator produces the Koba–Nielsen factor

$$
\left\langle
\prod_i e^{ik_iX(x_i)}
\right\rangle
\propto
\prod_{i<j}
|x_i-x_j|^{2\alpha' k_i\cdot k_j}.
$$

The spin-field and superghost correlators supply the fermionic numerator.

The remarkable simplification is that the final ordered four-gaugino amplitude is simply

$$
\boxed{
A_{\rm string}(1,2,3,4)
=
A_{\rm SYM}(1,2,3,4)
V(s_{12},s_{23})
}
$$

where

$$
V(a,b)
=
\frac{
\Gamma(1-\alpha'a)
\Gamma(1-\alpha'b)
}{
\Gamma(1-\alpha'(a+b))
}.
$$

The explicit field-theory four-gaugino partial amplitude consists of the two adjacent gauge-boson poles. This exact factorization is a standard open-superstring result. [Uppsala Universitet+1](https://www.uu.se/download/18.6bc4da6b190a20a519b1ef5f/1721035965616/String%20Theory%20I%20and%20II.pdf)

Schematically the worldsheet is not two separate Feynman diagrams:


```text
              R
             ●
          .-' '-.
       R ●       ● R
          '-. .-'
             ●
              R
```


It is one disk integral.

The Feynman diagrams emerge from different **degeneration limits of the disk modulus**.

For example,

$$
x\rightarrow0
$$

makes two vertex insertions approach one another and produces one factorization channel; while

$$
x\rightarrow1
$$

produces the other.

So the point-particle diagrams are literally boundaries of string moduli space.

---

# 5. Make the Ramond string electrically charged

There is an important subtlety.

A $U(1)$ gaugino is neutral. Therefore four ordinary $U(1)$ gauginos do **not** reproduce electron scattering.

A very simple exact toy realization uses

$$
U(2)
$$

and takes the charged Ramond state to be an off-diagonal Chan–Paton state.

Define

$$
\lambda_+
=
E_{12}
=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix},
$$

$$
\lambda_-
=
E_{21}
=
\begin{pmatrix}
0&0\\
1&0
\end{pmatrix}.
$$

Under the Cartan generator

$$
Q=\frac12
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix},
$$

we have

$$
[Q,E_{12}]=+E_{12},
$$

$$
[Q,E_{21}]=-E_{21}.
$$

So $\lambda_+$ carries charge $+1$, exactly like an electron-like charged field with respect to this Cartan gauge boson.

For scattering

$$
R^+R^+\rightarrow R^+R^+
$$

we cross the outgoing particles to incoming antiparticles. Thus in the all-incoming string amplitude take

$$
\lambda_1=\lambda_2=E_{12},
$$

$$
\lambda_3=\lambda_4=E_{21}.
$$

Now look at the Chan–Paton traces.

An ordering containing the two incoming charges adjacent vanishes:

$$
\operatorname{Tr}
(E_{12}E_{12}E_{21}E_{21})
=0
$$

because

$$
E_{12}E_{12}=0.
$$

Thus the $s$-channel ordering is absent.

But

$$
\operatorname{Tr}
(E_{12}E_{21}E_{12}E_{21})
=
1.
$$

Likewise for the ordering obtained by interchanging the two outgoing states.

Thus only the alternating boundary orderings survive:

$$
+,-,+,-.
$$

This is exactly what we want: no charge-$+2$ $s$-channel object, but $t$- and $u$-channel neutral exchange.

---

# 6. Identification of the invariants

Use all-incoming string momenta

$$
k_1=p_1,\qquad
k_2=p_2,\qquad
k_3=-p_3,\qquad
k_4=-p_4.
$$

For the alternating ordering

$$
(1,3,2,4)
$$

the adjacent Mandelstam variables are

$$
(k_1+k_3)^2
=
(p_1-p_3)^2=t,
$$

and

$$
(k_3+k_2)^2
=
(p_2-p_3)^2=u.
$$

Therefore the open-string form factor is

$$
\boxed{
V(t,u)
=
\frac{
\Gamma(1-\alpha't)
\Gamma(1-\alpha'u)
}{
\Gamma(1-\alpha'(t+u))
}.
}
$$

But

$$
t+u=-s,
$$

so

$$
\boxed{
V(t,u)
=
\frac{
\Gamma(1-\alpha't)
\Gamma(1-\alpha'u)
}{
\Gamma(1+\alpha's)
}.
}
$$

The two identical-fermion orderings have the same $V(t,u)$, because it is symmetric under

$$
t\leftrightarrow u.
$$

Therefore it factors completely out of the antisymmetrized fermion amplitude.

The result is

$$
\boxed{
\mathcal M_{\rm string}
=
e^2V(t,u)
\left[
\frac{
(\bar u_3\gamma^\mu u_1)
(\bar u_4\gamma_\mu u_2)
}{t}
-
\frac{
(\bar u_4\gamma^\mu u_1)
(\bar u_3\gamma_\mu u_2)
}{u}
\right].
}
$$

Hence

$$
\boxed{
\mathcal M_{\rm string}
=
V(t,u)\,
\mathcal M_{\rm QED}.
}
$$

That is the result you were looking for.

It is exact at disk/tree level for this simple same-brane Ramond realization, after identifying the Cartan coupling with $e$.

---

# 7. String cross section

Since $t,u<0$ in the physical Møller region, the Gamma functions are real, and

$$
\overline{
|\mathcal M_{\rm string}|^2
}
=
|V(t,u)|^2
\overline{
|\mathcal M_{\rm QED}|^2
}.
$$

Thus

$$
\boxed{
\frac{d\sigma_{\rm string}}{d\Omega}
=
|V(t,u)|^2
\frac{d\sigma_{\rm QED}}{d\Omega}.
}
$$

Explicitly,

$$
\boxed{
\frac{d\sigma_{\rm string}}{d\Omega}
=
\frac{\alpha^2}{2s}
\frac{(3+\cos^2\theta)^2}
{\sin^4\theta}
\left|
\frac{
\Gamma(1-\alpha't)
\Gamma(1-\alpha'u)
}{
\Gamma(1+\alpha's)
}
\right|^2.
}
$$

Now substitute

$$
t=-\frac{s}{2}(1-\cos\theta),
$$

$$
u=-\frac{s}{2}(1+\cos\theta).
$$

Define

$$
z\equiv\alpha's=\frac{s}{M_s^2},
\qquad
M_s^2=\frac1{\alpha'}.
$$

Then

$$
-\alpha't
=
\frac{z}{2}(1-\cos\theta),
$$

$$
-\alpha'u
=
\frac{z}{2}(1+\cos\theta).
$$

Therefore

$$
\boxed{
V(z,\theta)
=
\frac{
\Gamma\!\left(
1+\frac z2(1-\cos\theta)
\right)
\Gamma\!\left(
1+\frac z2(1+\cos\theta)
\right)
}{
\Gamma(1+z)
}.
}
$$

So the full differential cross section is

$$
\boxed{
\frac{d\sigma_{\rm string}}{d\Omega}
=
\frac{\alpha^2}{2s}
\frac{(3+\cos^2\theta)^2}
{\sin^4\theta}
\left[
\frac{
\Gamma\!\left(
1+\frac z2(1-\cos\theta)
\right)
\Gamma\!\left(
1+\frac z2(1+\cos\theta)
\right)
}{
\Gamma(1+z)
}
\right]^2.
}
$$

That is an explicit closed form.

---

# 8. Low-energy expansion: why the string looks pointlike

Use

$$
\log\Gamma(1-z)
=
\gamma z
+
\sum_{n=2}^\infty
\frac{\zeta(n)}{n}z^n.
$$

Hence

$$
\log V(t,u)
=
\sum_{n=2}^{\infty}
\frac{\zeta(n)}{n}
\alpha'^n
\left[
t^n+u^n-(t+u)^n
\right].
$$

At $n=2$,

$$
t^2+u^2-(t+u)^2
=
-2tu,
$$

therefore

$$
-\zeta(2)\alpha'^2tu.
$$

At $n=3$,

$$
t^3+u^3-(t+u)^3
=
-3tu(t+u),
$$

so

$$
-\zeta(3)\alpha'^3tu(t+u)
=
+\zeta(3)\alpha'^3stu.
$$

Thus

$$
\boxed{
V(t,u)
=
1
-\zeta(2)\alpha'^2tu
+\zeta(3)\alpha'^3stu
+O(\alpha'^4).
}
$$

Since

$$
\zeta(2)=\frac{\pi^2}{6},
$$

$$
\boxed{
\mathcal M_{\rm string}
=
\mathcal M_{\rm QED}
\left[
1-
\frac{\pi^2}{6}
\frac{tu}{M_s^4}
+
\zeta(3)
\frac{stu}{M_s^6}
+\cdots
\right].
}
$$

There is **no**

$$
O(M_s^{-2})
$$

term.

The first deviation is

$$
O\left(\frac{E^4}{M_s^4}\right).
$$

So on this precise point Fable was correct for this same-brane superstring construction.

The cross-section ratio is

$$
\frac{d\sigma_{\rm string}}
{d\sigma_{\rm QED}}
=
|V|^2
$$

and therefore

$$
\boxed{
\frac{d\sigma_{\rm string}}
{d\sigma_{\rm QED}}
=
1
-\frac{\pi^2}{3}
\frac{tu}{M_s^4}
+
2\zeta(3)
\frac{stu}{M_s^6}
+\cdots .
}
$$

Since

$$
tu=\frac{s^2}{4}\sin^2\theta,
$$

we obtain

$$
\boxed{
\frac{d\sigma_{\rm string}}
{d\sigma_{\rm QED}}
=
1-
\frac{\pi^2}{12}
\left(\frac{s}{M_s^2}\right)^2
\sin^2\theta
+
\frac{\zeta(3)}2
\left(\frac{s}{M_s^2}\right)^3
\sin^2\theta
+\cdots .
}
$$

So the leading observable compositeness correction is genuinely quartic in $E/M_s$.

---

# 9. At $90^\circ$

This becomes particularly simple.

For

$$
\theta=\frac\pi2,
$$

we have

$$
t=u=-\frac s2.
$$

Then

$$
\boxed{
V_{90^\circ}(z)
=
\frac{
\Gamma(1+z/2)^2
}{
\Gamma(1+z)
}.
}
$$

For $z\ll1$,

$$
V_{90^\circ}
=
1-\frac{\pi^2}{24}z^2+\cdots,
$$

and

$$
\frac{\sigma_{\rm string}}
{\sigma_{\rm QED}}
=
1-\frac{\pi^2}{12}z^2+\cdots.
$$

Some exact numerical values are illuminating:

$$
\begin{array}{c|c|c}
z=s/M_s^2 & V(90^\circ) & |V|^2\\
\hline
0.10 &0.99617&0.99236\\
0.25 &0.97846&0.95739\\
0.50 &0.92704&0.85940\\
1.00 &\pi/4=0.78540&\pi^2/16=0.61685\\
2.00 &0.50000&0.25000
\end{array}
$$

At $E\ll M_s$, it really is almost indistinguishable from a point fermion.

---

# 10. What is actually being exchanged?

This is important for your original Physics.SE question.

In QED,

$$
e^-+e^-\rightarrow e^-+e^-
$$

has a photon at the internal line.

For the Ramond strings,

$$
R+R\rightarrow R+R,
$$

the allowed worldsheet cubic vertex is

$$
R-R-NS.
$$

Therefore the degeneration of the four-Ramond disk factorizes through **Neveu–Schwarz states**:

$$
R+R
\longrightarrow
NS
\longrightarrow
R+R.
$$

At low energy, the $N=0$ exchanged NS state is precisely the massless gauge boson.

At finite string scale,

$$
\mathcal A(t)
\sim
\frac{R_0}{t}
+
\sum_{N\ge1}
\frac{R_N(u)}
{t-M_N^2},
$$

with

$$
M_N^2\simeq\frac{N}{\alpha'}
=N M_s^2.
$$

Likewise in the $u$-channel.

So graphically the string version is


```text
                 Ramond
                   \
                    \
                     ●
                     │
            NS tower│
       γ + massive string states
                     │
                     ●
                    /
                   /
                 Ramond
```


but the internal line should really be understood as a degeneration of the disk worldsheet.

The factorization is

$$
\boxed{
\mathcal A_4
\underset{t\to M_N^2}{\longrightarrow}
\sum_I
\frac{
\mathcal A_3(R_1,R_3,\Phi_{N,I})
\mathcal A_3(\Phi_{N,I},R_2,R_4)
}{
t-M_N^2
}.
}
$$

All $\Phi_{N,I}$ in this channel have NS statistics.

Thus:

$$
\boxed{
\text{two fermionic strings do not exchange a fermionic string here.}
}
$$

They exchange the bosonic NS tower.

This is exactly the string implementation of the ordinary even-fermion rule.

---

# 11. Where the “size” finally reveals itself

At small $s/M_s^2$,

$$
V\simeq1,
$$

so the extended Ramond string is experimentally indistinguishable from the point fermion.

At large fixed-angle energy, set

$$
x=\frac{1-\cos\theta}{2},
\qquad
1-x=\frac{1+\cos\theta}{2},
$$

so

$$
V=
\frac{
\Gamma(1+zx)
\Gamma(1+z(1-x))
}{
\Gamma(1+z)
}.
$$

Using Stirling,

$$
\Gamma(1+y)
\sim
\sqrt{2\pi y}
\left(\frac{y}{e}\right)^y,
$$

we obtain

$$
V
\sim
\sqrt{
2\pi z\,x(1-x)
}
\,
\exp
\left\{
z[
x\ln x+
(1-x)\ln(1-x)
]
\right\}.
$$

Because

$$
0<x<1
$$

implies

$$
x\ln x+(1-x)\ln(1-x)<0,
$$

the amplitude becomes exponentially soft.

At $90^\circ$,

$$
x=\frac12,
$$

and

$$
\boxed{
V
\sim
\sqrt{\frac{\pi z}{2}}\,
2^{-z}.
}
$$

QED remains power-law; the string amplitude becomes exponentially suppressed.

That is the cleanest possible high-energy signature of the extended object.

---

# 12. Effective contact interaction

The leading string correction is

$$
\delta\mathcal M
=
-\zeta(2)\alpha'^2tu\,
\mathcal M_{\rm QED}.
$$

Using

$$
\mathcal M_{\rm QED}
=
e^2
\left(
\frac{J_t}{t}
-
\frac{J_u}{u}
\right),
$$

we get

$$
\boxed{
\delta\mathcal M
=
-\zeta(2)e^2\alpha'^2
\left[
uJ_t-tJ_u
\right].
}
$$

The poles have disappeared: this is a local contact contribution.

Because $J\sim E^2$ and $t,u\sim E^2$,

$$
\delta\mathcal M
\sim
\frac{e^2E^4}{M_s^4}.
$$

Correspondingly the EFT contains dimension-eight operators schematically of the form

$$
\boxed{
\Delta\mathcal L
\sim
\frac{e^2}{M_s^4}
(\bar\psi\gamma^\mu\partial^\nu\psi)
(\bar\psi\gamma_\mu\partial_\nu\psi)
+\cdots .
}
$$

No dimension-six

$$
\frac{1}{M_s^2}
(\bar\psi\gamma^\mu\psi)^2
$$

is generated in this simple same-brane supersymmetric case.

This is exactly the distinction that Fable's summary was implicitly using. But it is **not universal for realistic string electrons**: fermions localized at intersections of different D-branes can generate dimension-six four-fermion contact operators already at tree level. Antoniadis, Benakli and Laugier explicitly found this distinction: same-stack matter gives dimension-eight string-oscillator corrections, while intersecting-brane matter can give dimension-six corrections. [arXiv+1](https://arxiv.org/abs/hep-th/0011281)

---

# 13. The comparison in one equation

For an ordinary electron,

$$
\boxed{
\mathcal M_{e^-e^-}
=
e^2
\left[
\frac{J_t}{t}
-
\frac{J_u}{u}
\right].
}
$$

For the simple charged Ramond open string,

$$
\boxed{
\mathcal M_{RR}
=
e^2
\left[
\frac{J_t}{t}
-
\frac{J_u}{u}
\right]
\frac{
\Gamma(1-\alpha't)
\Gamma(1-\alpha'u)
}{
\Gamma(1+\alpha's)
}.
}
$$

Therefore

$$
\boxed{
\lim_{\alpha'\to0}
\mathcal M_{RR}
=
\mathcal M_{e^-e^-}.
}
$$

And, much more strongly,

$$
\boxed{
\mathcal M_{RR}
-
\mathcal M_{e^-e^-}
=
O(\alpha'^2E^4),
}
$$

not $O(\alpha' E^2)$.

So your original intuition has a rather striking precise realization: **a genuinely extended spin-$\frac12$ open string can scatter exactly like a point fermion through the first nontrivial order one might naively expect, with its string nature first entering at dimension eight.** The price is equally precise: in fermion–fermion elastic scattering the exchanged long-range object is still the bosonic NS gauge string, not a fermionic mediator.

---

## 6. User

> what does it mean experimentally, is the question

### ChatGPT

Experimentally, the statement is much simpler than the string formalism makes it look:

> **If an electron were such a Ramond open string, Møller scattering would look exactly like pointlike QED at low energy, but large-angle scattering would gradually be suppressed by a very specific $E^4/M_s^4$ correction.**

For the toy model we just calculated,

$$
\frac{d\sigma_{\rm string}}{d\Omega}
=
|V(t,u)|^2\,\frac{d\sigma_{\rm QED}}{d\Omega},
$$

and at $E_{\rm cm}\ll M_s$,

$$
\boxed{
\frac{\sigma_{\rm string}}{\sigma_{\rm QED}}
\simeq
1-\frac{\pi^2}{12}
\left(\frac{E_{\rm cm}}{M_s}\right)^4
\sin^2\theta+\cdots
}
$$

So experimentally you would measure the **angular distribution** of

$$
e^-e^-\to e^-e^-
$$

and ask whether

$$
R(\theta)\equiv
\frac{(d\sigma/d\Omega)_{\rm measured}}
{(d\sigma/d\Omega)_{\rm QED}}
$$

has the characteristic form

$$
\boxed{
R(\theta)-1
\simeq
-0.822\,
\left(\frac{E_{\rm cm}}{M_s}\right)^4
\sin^2\theta .
}
$$

That is the direct observable.

### It is *not* an ordinary electron-radius effect

This is perhaps the most interesting experimental consequence of the calculation.

For an ordinary composite fermion you expect a form factor

$$
F(q^2)=1-\frac16r^2q^2+\cdots
$$

and consequently corrections of order

$$
\frac{E^2}{\Lambda^2}.
$$

Those are dimension-six/compositeness effects.

But our open-string fermion gives

$$
\boxed{\delta{\cal A}/{\cal A}\propto E^4/M_s^4}
$$

with no $E^2/M_s^2$ term.

So an experimental statement like

$$
r_e<10^{-19}\ {\rm m}
$$

obtained by fitting a conventional $q^2r_e^2$ form factor does **not directly constrain this model in the same way**. It is fitting the wrong functional dependence.

In EFT language the distinction is

$$
\underbrace{\frac1{\Lambda^2}
(\bar e\gamma_\mu e)^2}_{\text{ordinary compositeness}}
$$

versus something schematically like

$$
\boxed{
\frac1{M_s^4}
(\bar e\gamma_\mu\partial_\nu e)
(\bar e\gamma^\mu\partial^\nu e)
}
$$

for the string.

The PDG's standard compositeness limits are overwhelmingly limits on the former class of dimension-six operators, often reaching tens of TeV. [Particle Data Group](https://pdg.lbl.gov/2025/reviews/rpp2025-rev-searches-quark-lep-compositeness.pdf) They therefore cannot simply be read as $M_s>30$ TeV for our particular dimension-eight amplitude.

## Numerically, what precision corresponds to what $M_s$?

At the optimal angle,

$$
\theta=90^\circ,
$$

we have

$$
|\delta|
\simeq
0.822
\left(\frac{E_{\rm cm}}{M_s}\right)^4.
$$

Therefore a null result with fractional precision $\epsilon$ implies approximately

$$
\boxed{
M_s
\gtrsim
E_{\rm cm}
\left(\frac{0.822}{\epsilon}\right)^{1/4}.
}
$$

For example:

| experimental accuracy | sensitivity to $M_s/E_{\rm cm}$ |
| --- | --- |
| $10\%$ | $1.69$ |
| $1\%$ | $3.01$ |
| $0.1\%$ | $5.35$ |
| $0.01\%$ | $9.52$ |

Notice the brutal fourth-root law. Increasing precision buys rather little compared with increasing collision energy.

Thus at a hypothetical $1$ TeV $e^-e^-$ collider:

$$
1\%\quad\Rightarrow\quad M_s\gtrsim3.0\ {\rm TeV},
$$

while

$$
0.1\%\quad\Rightarrow\quad M_s\gtrsim5.4\ {\rm TeV}.
$$

At $3$ TeV and $1\%$,

$$
M_s\gtrsim9\ {\rm TeV}.
$$

That is what “pointlike below the string scale” means quantitatively.

---

### The angular dependence is diagnostic

There is another nice feature.

Since

$$
tu=\frac{s^2}{4}\sin^2\theta,
$$

the leading deviation vanishes for forward scattering:

$$
\theta\to0:
\qquad
R(\theta)\to1.
$$

It is maximum near $90^\circ$.

So you don't primarily search for a uniform rescaling of the Møller cross section. You search for a deformation

$$
\text{forward: almost QED}
$$

but

$$
\text{central scattering: depleted}.
$$

For example, if

$$
E_{\rm cm}=0.5 M_s,
$$

then at $90^\circ$,

$$
R\simeq
1-0.822(0.5)^4
=
0.9486
$$

at leading order: about a **5% deficit**.

For

$$
E_{\rm cm}=0.2M_s,
$$

it is only

$$
\delta\simeq-0.00132,
$$

or **0.13%**.

That illustrates how suddenly the object starts to become visible as you approach the string scale.

## Something I should correct from the previous discussion: no resonance in physical Møller scattering

This is an important experimental distinction.

For physical

$$
e^-e^-\to e^-e^-,
$$

we have

$$
s>0,\qquad t<0,\qquad u<0.
$$

Our amplitude is

$$
V(t,u)
=
\frac{\Gamma(1-\alpha't)\Gamma(1-\alpha'u)}
{\Gamma(1+\alpha's)}.
$$

There are therefore **no physical $t$- or $u$-channel Regge poles** in Møller scattering, because $t,u$ are negative.

And our Chan–Paton assignment killed the $s$-channel, for the simple physical reason that two equal charges cannot annihilate into a neutral gauge-string state.

So the experimental signature in $e^-e^-$ is

$$
\boxed{\text{smooth angular distortion/suppression, not a resonance tower.}}
$$

The Regge tower appears in a crossed channel such as an allowed

$$
e^-e^+\rightarrow X,
$$

where

$$
s=M_s^2,\;2M_s^2,\;3M_s^2,\ldots
$$

can become physical poles.

That's a useful distinction between the two experiments:

$$
e^-e^-:
\quad\text{precision test of the string form factor},
$$

$$
e^+e^-:
\quad\text{potential direct production of string excitations}.
$$

---

# And for your actual quark-bootstrap hypothesis

This is where it becomes experimentally more interesting.

Suppose your effective “quark”

$$
q_{\rm observed}
\sim
\bar q\,\bar q+\text{fermionic string}
$$

really has the same open-string scattering property.

Then partonic

$$
qq\to qq
$$

would acquire

$$
\boxed{
{\cal M}_{qq}^{\rm string}
\simeq
{\cal M}_{qq}^{\rm QCD}
\left[
1-
\frac{\pi^2}{6}
\frac{tu}{M_s^4}
+\cdots
\right].
}
$$

So before resolving the string directly one should see a distortion of the **high-$p_T$ dijet angular distribution**.

The qualitative fingerprint would be:

$$
\text{low }p_T:\quad\text{ordinary QCD},
$$

$$
\text{very large }p_T,\text{ central jets}:
\quad\text{deficit/deformation},
$$

and eventually, in crossed channels which admit them,

$$
\sqrt{\hat s}\sim M_s:
\quad\text{Regge excitations}.
$$

CMS has explicitly searched for benchmark low-scale string resonances in dijets; the classic Run-2 benchmark exclusion reached roughly $7.6\!-\!7.7$ TeV. That number is model-dependent—it is **not** a universal lower bound on the $M_s$ in our amplitude—but it tells us immediately the scale at which collider data already attack literal TeV-scale QCD-colored open strings. [CMS Results+1](https://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/EXO-17-026/)

The most striking conceptual result, though, is this:

$$
\boxed{
\text{“pointlike” experimentally does not imply geometrically pointlike.}
}
$$

A conventional extended two-constituent object advertises its size through an $O(q^2R^2)$ form factor. This particular fermionic string does **not**. Its first tree-level scattering fingerprint is

$$
O(q^4\alpha'^2).
$$

So if your original conjecture was that the two-endpoint fermionic string could **scatter for a surprisingly long energy range as though it were the point particle that the bootstrap identifies it with**, the calculation says yes: there is a precise open-superstring mechanism by which that happens.

---

## 7. User

> Ok write a physics review letter on it, use the full four pages in the PRL tex format.

### ChatGPT

**[Analizado]**

```python
import mpmath as mp
for z in [0.1,0.25,0.5,1,2]:
    V=mp.gamma(1+z/2)**2/mp.gamma(1+z)
    print(z, float(V), float(V**2))
```

**[STDOUT/STDERR]**

```text
0.1 0.9961736355156747 0.9923619120965164
0.25 0.9784608219532953 0.9573855800975183
0.5 0.9270373386506858 0.8593982272525463
1 0.7853981633974484 0.616850275068085
2 0.5 0.25
```

Done. I wrote and compiled it in **REVTeX 4.2 PRL reprint format**, tuned to **exactly four pages**.

The Letter contains the full Møller calculation, four-Ramond disk amplitude, Chan–Paton projection, exact Veneziano factor, $E^4/M_s^4$ experimental correction, Regge factorization, zero-range fermion-exchange construction, and the quark/anti-diquark bootstrap interpretation.

A useful conclusion emerged while making the experimental argument sharper: if the Ramond quark literally shared the ordinary hadronic slope

$$
\alpha'_{\rm had}\simeq0.9\ {\rm GeV}^{-2},
$$

then already at $10$ GeV and $90^\circ$ the naive string amplitude would suppress the cross section by roughly $2^{-180}$. Thus **the literal common-tension pion/quark RNS identification is experimentally impossible**. The bootstrap can survive only as a dual/operator identification, or with a mechanism separating the QCD flux-tube scale from the Ramond hard-scattering scale. I made that negative result prominent rather than hiding it.

---

## 8. User

> Now go for the larger Physica Review D on the topic, well detailled, bibliography covered, 12 pages

### ChatGPT

Done. I expanded the Letter into a **12-page Physical Review D manuscript in REVTeX 4.2**, with the bibliography and derivations substantially enlarged rather than padded.

It now includes the complete Møller calculation; four-Ramond disk amplitude and Chan–Paton projection; exact string/QED form-factor relation; dimension-eight EFT matching; Regge/fixed-angle limits; genuinely fermionic exchange and its zero-range limit; contact interactions with internal swap operators; the $qq/\bar q\bar q$ representation algebra; Miyazawa–Catto–Gürsey and modern light-front hadronic supersymmetry; the Aharonov–Casher–Susskind/Ramond history; baryon-junction considerations including the 2026 STAR result; QCD effective-string caveats; and current collider/compositeness constraints.

A central negative result is made explicit: a **literal common-tension pion/quark RNS pairing is excluded phenomenologically**. With the hadronic Regge slope, hard quark scattering would become enormously string-soft already at modest energies. What remains viable is the stronger bootstrap/duality interpretation in which the extended representation and the apparently pointlike quark are alternative descriptions rather than ordinary superpartners sharing the same physical $\alpha'$.

---

## 9. User

> the main idea was to compare fermionic string scattering both in quark diquark and in lepton meson. Elaborate the similar lepton meaon formalism and compare with experimental limits on compositeness

### ChatGPT

I have re-centered the paper around the actual **two-sided sBootstrap**, rather than treating the lepton sector as an afterthought. It is again exactly **12 pages in PRD REVTeX format**, and I recompiled and visually checked the PDF.

The central construction is now

$$
\boxed{\mathrm{diquark\ NS}\longleftrightarrow \mathrm{quark\ R}},
\qquad
\boxed{\mathrm{meson\ NS}\longleftrightarrow \mathrm{lepton\ R}} .
$$

For the lepton side I spell out the five-light-flavour algebra explicitly. With

$$
U=(u,c),\qquad D=(d,s,b),
$$

the meson matrix

$$
5\otimes\bar5=1\oplus24
$$

contains

$$
U\bar D:\quad 2\times3=6,\quad Q=+1,
$$

and

$$
D\bar U:\quad 3\times2=6,\quad Q=-1.
$$

Those six $Q=-1$ bosonic endpoint states can be put in one-to-one correspondence with

$$
e_L,e_R,\mu_L,\mu_R,\tau_L,\tau_R,
$$

and similarly for the conjugates. This is precisely the charged-sector observation in your 2005 paper; the neutral sector is deliberately treated as less constrained because $5\bar5$ gives 13 neutral states before further projections. [arXiv+1](https://arxiv.org/abs/hep-ph/0512065)

I have made the quark side genuinely parallel. The symmetric flavor $15$ gives

$$
UU:3\times Q=4/3,\qquad
UD:6\times Q=1/3,\qquad
DD:6\times Q=-2/3,
$$

so the two six-dimensional nonexotic sectors reproduce the charged multiplicities of the quark Weyl states. I also inserted an important caveat which the earlier manuscript glossed over: **the flavor $15$ counting and the color-$\bar3_c$ diquark statement are separate representation-theory facts**. Fermi statistics means the whole $15_F$ cannot simply be called one scalar color-antitriplet S-wave multiplet.

The experimental comparison is now the main phenomenology section. It distinguishes:

- the **direct string/Veneziano test** from LEP Bhabha scattering, giving $M_s>0.631$ TeV in the Cullen–Perelstein–Peskin string-QED model; [ResearchGate+1](https://www.researchgate.net/publication/1994631_Search_for_TeV_strings_and_new_phenomena_in_Bhabha_scattering_at_CERN_LEP2)
- ordinary $D=6$ four-electron compositeness, where the PDG quotes a representative $\Lambda_{eeee}\gtrsim8.3$ TeV; [Grupo de Datos de Partículas](https://pdgprod.lbl.gov/pdgprod/pdgLive/Particle.action?home=&node=S054)
- excited-electron searches, with $m_{e^*}>5.6$ TeV for $m_{e^*}=\Lambda$, and dedicated analyses reaching compositeness parameters around $25$ TeV for lighter excited leptons; [CERN Document Server+1](https://cds.cern.ch/record/2706282/files/2001.04521.pdf)
- $qq\ell\ell$ contact interactions, crucial if one tries to interpret the mesonic endpoints as ordinary quark constituents: ATLAS reaches $35.8$ TeV in the constructive LL benchmark; [ResearchGate](https://www.researchgate.net/publication/346081146_Search_for_new_non-resonant_phenomena_in_high-mass_dilepton_final_states_with_the_ATLAS_detector)
- quark compositeness, where the 2026 CMS dijet-angular result gives $17$ TeV destructive and $37$ TeV constructive for the benchmark LL operator. [arXiv](https://arxiv.org/abs/2603.25458)

The paper now emphasizes that these numbers are **not competing measurements of the same $\Lambda$**. The string prediction is

$$
\delta {\cal M}_{\rm string}\sim \frac{E^4}{M_s^4},
$$

whereas conventional compositeness fits use

$$
\delta {\cal M}_{\rm CI}\sim \frac{E^2}{\Lambda^2}.
$$

That is exactly why the historical electron-radius and contact-interaction limits cannot simply be translated into $M_s$.

The strongest common conclusion of the two branches is also now made explicit. A literal physical QCD meson/diquark string has

$$
\alpha'_{\rm had}\simeq0.9\ {\rm GeV}^{-2},
\qquad M_{s,\rm had}\simeq1.05\ {\rm GeV}.
$$

For the **lepton-meson** branch, LEP already requires the Ramond hard scale to exceed that by about a factor $600$ in mass,

$$
\frac{0.631\ {\rm TeV}}{1.05\ {\rm GeV}}\simeq 601,
$$

or roughly

$$
\frac{\alpha'_{\rm had}}{\alpha'_{\rm hard}}
\gtrsim3.6\times10^5.
$$

For the **quark-diquark** branch, multi-TeV dijet scattering gives the same conclusion even more strongly. Thus both sides independently say

$$
\boxed{\alpha'_{\rm hard}\ll\alpha'_{\rm had}},
$$

which turns the viable conjecture into a genuine **dual/operator bootstrap**, rather than a literal statement that the observed fermion and its physical QCD bosonic partner share one ordinary string tension.

---

## 10. User

> the small masses  of electron up and down, as well as the nonzero mass of pion, signala we are missing some effect that could contribute to the scattering size too. Research.

### ChatGPT

**[Analizado]**

```python
import math
hbarc_m_per_GeVinv=1.973269804e-16
Ms=631.0
mpi=0.13957
me=0.000510999
mu=0.00216
md=0.00470
for m,name in [(mpi,'pi'),(me,'e'),(mu,'u'),(md,'d')]:
    r=m/Ms**2 # GeV^-1 if r^2~m^2/Ms^4 => r~m/Ms^2
    print(name, r, r*hbarc_m_per_GeVinv)
# effective Lambda=M_s^2/m
for m,name in [(mpi,'pi'),(me,'e'),(mu,'u'),(md,'d')]:
    print(name, Ms**2/m/1e3, 'TeV')
# B0
mpi0=0.1349768
B0=mpi0**2/(mu+md)
print("B0",B0)
# chiral epsilon m_pi^2/1GeV^2
print("epsilon pi",mpi**2)
# yuks
v=246.22
for m,name in [(me,'e'),(mu,'u'),(md,'d')]:
    y=math.sqrt(2)*m/v
    print(name,y, Ms/math.sqrt(y)/1e3) # if C6 y/M
```

**[STDOUT/STDERR]**

```text
pi 3.5053659198163557e-07 6.9170327215443e-23
e 1.2833979219461475e-09 2.532490365892682e-25
u 5.424941167015353e-09 1.0704872593347918e-24
d 1.1804270131931555e-08 2.3293009809599633e-24
pi 2852.769219746364 TeV
e 779181.5639560937 TeV
u 184333.7962962963 TeV
d 84715.10638297872 TeV
B0 2.6557924982857144
epsilon pi 0.0194797849
e 2.935024434079641e-06 368.3184706833348
u 1.2406389792567159e-05 179.14580720829238
d 2.6995385196789648e-05 121.44638578845789
```

Yes. The literature strongly suggests that the **massless four-Ramond calculation is too special** for the phenomenology you want. Once one asks why $m_e,m_u,m_d\neq0$ and why the pion is only pseudo-Goldstone rather than massless, there are new operators which can carry information about size. But there are two quite different effects, and they should not be conflated.

The most interesting result I found is that **string theory already contains an explicit example of exactly this phenomenon**: same-stack open-string fermions have the dimension-eight Veneziano correction we calculated, whereas chiral matter living at brane intersections generically acquires **dimension-six four-fermion contact terms**. In the same intersecting-brane framework, Yukawa couplings—and therefore fermion masses after symmetry breaking—come from worldsheet geometry/instantons. [arXiv+2](https://arxiv.org/abs/hep-th/0011281)

So there is a credible mechanism by which

$$
\boxed{\text{the effect which makes the fermion massive also destroys the exceptional }E^4/M_s^4\text{ pointlikeness}.}
$$

## 1. First, the masses are symmetry-breaking parameters

For the light quarks, current PDG values are roughly

$$
m_u(2{\rm\ GeV})=2.16\ {\rm MeV},\qquad
m_d(2{\rm\ GeV})=4.70\ {\rm MeV}.
$$

They explicitly break

$$
SU(2)_L\times SU(2)_R.
$$

In their absence the pion is a true Goldstone boson. At leading order,

$$
m_\pi^2=B_0(m_u+m_d),
$$

up to electromagnetism. [Particle Data Group+1](https://pdg.lbl.gov/2025/tables/rpp2025-sum-quarks.pdf)

Numerically,

$$
B_0\simeq
\frac{(135\ {\rm MeV})^2}{6.86\ {\rm MeV}}
\simeq 2.7\ {\rm GeV}.
$$

Thus a few-MeV explicit breaking produces a $135$-MeV pseudo-Goldstone because it enters **mass squared**.

The electron is analogous only at the abstract chiral level:

$$
m_e=\frac{y_e v}{\sqrt2},
$$

with

$$
y_e\simeq2.94\times10^{-6}.
$$

In the Standard Model these are unrelated sources of symmetry breaking: $y_e,y_u,y_d$ are independent Yukawas and the pion mass is then generated by QCD. So the numerical similarity is not evidence for your bootstrap by itself.

But in your construction, all of them tell us that the putative exact NS/R identification must be deformed.

---

# 2. And masses do indeed produce additional probes of size

For a spin-$\tfrac12$ object the electromagnetic vertex is

$$
\Gamma^\mu(q)=
F_1(q^2)\gamma^\mu
+
\frac{i\sigma^{\mu\nu}q_\nu}{2m}F_2(q^2).
$$

The two fundamental compositeness observables are

$$
F_1(q^2)
=
1+\frac16\langle r_1^2\rangle q^2+\cdots ,
$$

and

$$
F_2(0)=a=\frac{g-2}{2}.
$$

The important distinction is:

$$
\langle r^2\rangle:
\quad\text{chirality preserving},
$$

whereas

$$
F_2:
\quad\text{chirality flipping}.
$$

Therefore a chiral symmetry which makes $m_f$ small also naturally suppresses the anomalous magnetic moment.

This is actually old compositeness lore. The current PDG says explicitly that chiral invariance explains how a composite fermion can have

$$
m_f\ll \Lambda_{\rm comp}
$$

despite having a finite inverse size $\Lambda_{\rm comp}$. It also notes that the small lepton masses and $g-2$ measurements motivate chirality-conserving excited-fermion couplings. [Particle Data Group+1](https://pdg.lbl.gov/2025/reviews/rpp2025-rev-searches-quark-lep-compositeness.pdf)

Brodsky and Drell made the connection to form factors more quantitative. In a generic relativistic composite system one finds schematically

$$
a_f\sim m_f R,
$$

while when the chiral-breaking mass scale is itself small,

$$
\boxed{
a_f\sim \mu\,m_f\,R^2 .
}
$$

If $\mu\sim m_f$,

$$
\boxed{
a_f\sim m_f^2R^2
\sim\frac{m_f^2}{\Lambda_{\rm comp}^2}.
}
$$

This is precisely why an extremely small fermion mass can coexist with sizeable underlying compositeness without immediately producing a huge magnetic moment. [Scribd+1](https://www.scribd.com/document/909142824/9705477v1)

That mechanism belongs in our paper.

---

# 3. Our previous Veneziano result is an exceptionally symmetric limit

We had

$$
{\cal M}_{RR}
=
{\cal M}_{\rm QED}
V(t,u),
$$

with

$$
V(t,u)
=
1-\zeta(2)\frac{tu}{M_s^4}
+O(M_s^{-6}).
$$

Thus

$$
\boxed{\delta{\cal M}\sim E^4/M_s^4}
$$

and there was no dimension-six term

$$
\frac{1}{M_s^2}
(\bar\psi\gamma_\mu\psi)^2.
$$

That absence is *not* a generic property of composite fermions.

It is a special property of the supersymmetric same-stack open-string amplitude. The open-superstring effective action indeed begins its nontrivial four-field corrections at $\alpha'^2$. [arXiv+1](https://arxiv.org/abs/hep-th/0310015)

Once we introduce the symmetry breaking necessary to explain the observed spectrum, the correct generic EFT is instead

$$
{\cal L}_{\rm eff}
=
{\cal L}_{SM}
+
\frac{c_6}{M_s^2}{\cal O}_6
+
\frac{c_8}{M_s^4}{\cal O}_8+\cdots .
$$

Our previous calculation corresponds to

$$
c_6=0,\qquad c_8\ne0.
$$

The real question for the bootstrap model becomes:

$$
\boxed{\text{does the same deformation that generates }m_f,m_\pi
\text{ also generate }c_6\ne0?}
$$

And string theory says: **it certainly can.**

---

# 4. Intersecting D-branes are almost exactly the counterexample we need

Antoniadis, Benakli and Laugier calculated four-fermion scattering when matter lives at D-brane intersections.

After subtracting the ordinary massless exchanges, they find

$$
\boxed{
{\cal L}_{4f}
\sim
\frac{c_{ijkl}}{M_s^2}
(\bar\psi_i\gamma^\mu\psi_j)
(\bar\psi_k\gamma_\mu\psi_l)
}
$$

already at dimension six.

The contributions come from:

$$
\text{massive string oscillators},
\qquad
\text{KK states},
\qquad
\text{winding states}.
$$

This is explicitly contrasted with strings whose two endpoints are on the same brane stack, for which the leading oscillator effect is dimension eight. [arXiv](https://arxiv.org/abs/hep-th/0011281)

Even better, in intersecting-brane models the Yukawa couplings arise geometrically from worldsheet instantons,

$$
Y_{ijk}\sim
e^{-A_{ijk}/2\pi\alpha'}
\times(\text{theta functions}),
$$

where $A_{ijk}$ is an appropriate area between intersections. [arXiv](https://arxiv.org/abs/hep-th/0302105)

So there is a concrete string framework with

$$
\boxed{
\text{geometry}
\rightarrow
\begin{cases}
\text{small Yukawa/mass},\\
\text{four-fermion contact interactions}.
\end{cases}}
$$

That is almost precisely your suspicion.

There is no universal algebraic relation

$$
m_f\longleftrightarrow r_f
$$

because the Yukawa and four-point amplitudes depend differently on the geometry. But they arise from the **same deformation away from the simple universal RNS string**.

---

# 5. A useful phenomenological parametrization

We can therefore write your fermionic string amplitude as

$$
{\cal M}
=
{\cal M}_{SM}
+
{\cal M}_{6}^{\rm break}
+
{\cal M}_{8}^{\rm string}
+\cdots ,
$$

where

$$
{\cal M}_{8}^{\rm string}
\sim
\frac{E^4}{M_s^4},
$$

and

$$
{\cal M}_{6}^{\rm break}
\sim
c_6^{\rm break}
\frac{E^2}{M_s^2}.
$$

If the dimension-six term itself vanishes with some symmetry-breaking spurion $\epsilon$,

$$
c_6^{\rm break}=\kappa\epsilon .
$$

There are several possibilities.

For a soft NS/R mass splitting,

$$
\epsilon
\sim
\frac{\Delta m^2}{M_s^2},
$$

so

$$
{\cal M}_{6}^{\rm break}
\sim
\kappa
\frac{\Delta m^2 E^2}{M_s^4}.
$$

Compare this with

$$
{\cal M}_{8}
\sim
\frac{E^4}{M_s^4}.
$$

Their ratio is simply

$$
\boxed{
\frac{{\cal M}_{6}^{\rm break}}
{{\cal M}_{8}}
\sim
\kappa\frac{\Delta m^2}{E^2}.
}
$$

At collider energies this particular soft-breaking correction would be negligible.

But this scaling is **not compulsory**. Intersecting-brane amplitudes demonstrate that breaking/localization can instead give

$$
c_6=O(1),
$$

in which case

$$
\frac{{\cal M}_{6}}{{\cal M}_{8}}
\sim
\frac{M_s^2}{E^2},
$$

and dimension six dominates far below $M_s$.

That is experimentally an enormous distinction.

---

# 6. What does the pion teach us about “size”?

Here there is a nice surprise.

The pion's nonzero mass certainly reflects the missing explicit-breaking physics, but its effect on the pion radius is **not** simply

$$
r_\pi\sim1/m_\pi.
$$

Chiral perturbation theory gives

$$
F_\pi(q^2)
=
1+\frac16\langle r_\pi^2\rangle q^2+\cdots,
$$

and schematically

$$
\langle r_\pi^2\rangle
=
\text{LEC}
-
\frac{1}{16\pi^2F_\pi^2}
\ln m_\pi^2+\cdots.
$$

Therefore

$$
\boxed{
\langle r_\pi^2\rangle\to\infty
\quad\text{logarithmically as}\quad
m_\pi\to0.
}
$$

Lattice calculations explicitly have to include this chiral logarithm; the pion radius becomes increasingly sensitive as one approaches the physical light-quark masses. [APS Journals+1](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.93.054503)

This means the pion has at least two notions of size:

$$
R_{\rm core}\sim\Lambda_{\rm QCD}^{-1},
$$

and a long-distance chiral cloud controlled by

$$
m_\pi^{-1}.
$$

The finite pion mass **cuts off** that infrared cloud.

This is conceptually important for the bootstrap. The physical $0.66$ fm pion radius is not simply the geometrical width of a fundamental open string. It contains low-energy QCD dressing.

So the statement

> pion-sized NS string $\Rightarrow$ equally pion-sized Ramond partner

was too naive even independently of compositeness limits.

The measured pion radius contains physics that need not map onto the hard scattering form factor of the Ramond state.

---

# 7. That may help the lepton–meson side considerably

Suppose

$$
M_{ij}^{NS}\sim q_i\bar q_j
$$

and

$$
L_{ij}^{R}\sim \text{lepton}.
$$

An exact worldsheet theory may give the same bare string tension and oscillator coordinates, but the physical meson obtains enormous additional IR dressing:

$$
|M_{\rm phys}\rangle
=
Z^{1/2}|M_{\rm string}\rangle
+
|\pi\pi\rangle+
|\rho\pi\rangle+\cdots .
$$

Then its measured electromagnetic form factor is

$$
F_M(q^2)
=
F_{\rm core}(q^2)
+
F_{\rm chiral}(q^2)+\cdots .
$$

The lepton need not have the QCD chiral cloud.

Therefore

$$
R_{\rm physical\ pion}
\gg
R_{\rm hard\ Ramond}
$$

does **not necessarily require two different fundamental $\alpha'$'s**.

This is subtler than our previous conclusion.

It does not save a literal hadronic $M_s\sim1$ GeV string from the high-energy Veneziano suppression—that problem remains. But it does invalidate the simple argument

$$
r_\pi\simeq0.66{\rm fm}
\quad\Rightarrow\quad
r_e\simeq0.66{\rm fm}.
$$

The pion's observed radius is substantially an IR hadronic observable.

---

# 8. Massive endpoints produce another correction

There is also a more literal string effect.

For a string with endpoint masses,

$$
S=
-T\int d^2\sigma\sqrt{-h}
-\sum_i m_i\int ds_i,
$$

the boundary conditions change from pure Neumann to

$$
T\,\partial_\sigma X^\mu
\sim
m_i\frac{d}{d\tau}
\left(
\frac{\dot X^\mu}
{\sqrt{-\dot X^2}}
\right).
$$

This changes:

- the rotating-string length,
- endpoint velocities,
- Regge trajectories,
- quantum fluctuation frequencies.

Massive-endpoint string phenomenology indeed produces nonlinear Regge trajectories and mass-dependent spectra. [arXiv+1](https://arxiv.org/abs/1801.00798)

For

$$
m_{u,d}\ll\sqrt T\sim\Lambda_{\rm QCD},
$$

these are perturbatively small for long excited strings.

But the pion is the worst possible state to analyze with a classical rotating string—it is a pseudo-Goldstone ground state. Its small mass is mostly chiral dynamics, not the classical energy

$$
E\simeq TL+m_1+m_2.
$$

So endpoint masses matter, but they are probably not the principal missing physics for the pion.

---

# 9. What the small fermion masses imply experimentally

For the fermionic states, the additional most sensitive observable is probably not ordinary scattering first, but the dipole.

A chirally protected compositeness contribution behaves naturally as

$$
\delta a_f
\sim
\frac{m_f^2}{\Lambda^2}.
$$

For the electron,

$$
m_e=5.11\times10^{-4}\ {\rm GeV}.
$$

Taking sensitivity to new physics in $a_e$ at roughly $10^{-12}$,

$$
\Lambda
\sim
\frac{m_e}{\sqrt{\delta a_e}}
\sim500\ {\rm GeV}.
$$

Interestingly this is of the same rough order as the old direct string-Bhabha limit

$$
M_s>0.631\ {\rm TeV}.
$$

The electron $g-2$ interpretation is currently complicated by the $5.5\sigma$ disagreement between the independent Cs and Rb determinations of $\alpha$, so one should not turn this into a precision modern bound without specifying which $\alpha$ is used. [Particle Data Group](https://pdg.lbl.gov/2025/reviews/rpp2025-rev-standard-model.pdf)

Still, parametrically it is exactly the observable expected to reveal a **mass-induced departure from the massless Ramond limit**.

---

# 10. But ordinary scattering can be much more restrictive if dimension six appears

PDG parameterizes fermion compositeness as

$$
{\cal L}_{CI}
=
\frac{g_*^2}{2\Lambda^2}
\eta_{XY}
(\bar\psi_X\gamma^\mu\psi_X)
(\bar\psi_Y\gamma_\mu\psi_Y).
$$

Current quark contact-interaction bounds are typically

$$
\Lambda\sim9-30\ {\rm TeV},
$$

depending on chirality/sign, while combined quark-lepton operators are constrained around

$$
\Lambda\simeq24-36\ {\rm TeV}.
$$

Thus the experimental hierarchy is:

$$
\boxed{
\begin{array}{c|c}
\text{leading correction}&\text{sensitivity}\\
\hline
E^4/M_s^4 & M_s\sim{\rm TeV}\\
E^2/\Lambda^2 & \Lambda\sim10-30{\rm\ TeV}
\end{array}}
$$

roughly.

So whether the mass-generating deformation restores a dimension-six term is **the phenomenologically decisive question**.

---

# 11. An instructive numerical estimate

Suppose, conservatively, that breaking enters only through the NS/R mass splitting:

$$
C_6
\sim
\frac{\Delta m^2}{M_s^4}.
$$

For the pion/electron pair,

$$
\Delta m^2
\simeq m_\pi^2-m_e^2
\simeq0.0195\ {\rm GeV}^2.
$$

At the direct Bhabha string bound

$$
M_s=631\ {\rm GeV},
$$

this corresponds to an effective dimension-six scale

$$
\Lambda_{\rm eff}
=
\frac{M_s^2}{\sqrt{\Delta m^2}}
\simeq
2.9\times10^3\ {\rm TeV}.
$$

Equivalently, an associated length scale would be only

$$
r_{\rm break}\sim
\frac{m_\pi}{M_s^2}
\simeq
7\times10^{-23}\ {\rm m}.
$$

So **soft mass-splitting breaking by itself is completely safe experimentally**.

For the electron mass spurion,

$$
r_e^{\rm break}
\sim
\frac{m_e}{M_s^2}
\simeq2.5\times10^{-25}\ {\rm m}.
$$

Far below the traditional Bhabha “electron radius” limit

$$
r_e<2.8\times10^{-19}\ {\rm m}.
$$

The dangerous case is not mass-suppressed soft breaking.

It is a deformation like brane localization/intersection which generates

$$
C_6\sim\frac{O(1)}{M_s^2}.
$$

Then the tens-of-TeV contact limits apply immediately.

---

# 12. I think this changes the conceptual picture of the paper

We should really distinguish three layers:

$$
\boxed{\text{exact string/bootstrap core}}
$$

with

$$
m_f=m_{\rm NS}=0,
\qquad
c_6=0,
\qquad
\delta{\cal A}\sim E^4/M_s^4;
$$

then

$$
\boxed{\text{mass/chiral breaking}}
$$

producing

$$
m_e,m_u,m_d,\quad m_\pi^2\sim m_u+m_d,
$$

dipoles and potentially mass-suppressed $q^2$ form factors;

and finally

$$
\boxed{\text{geometrical/string breaking}}
$$

which may generate unsuppressed

$$
\frac{1}{M_s^2}(\bar\psi\gamma\psi)^2
$$

contact interactions.

The pion is especially informative because its measured size contains a **chiral infrared contribution which actually grows when its mass is reduced**. The electron/up/down small masses, on the other hand, tell us that chirality is an excellent approximate symmetry and therefore strongly suppress helicity-flipping compositeness effects.

So your suspicion is correct, but in a more interesting form than “finite mass gives the string a little radius”:

$$
\boxed{
\text{mass generation is a symmetry-breaking deformation, and that deformation can introduce an entirely new }q^2/M^2\text{ scattering structure absent from the ideal RNS amplitude.}
}
$$

The intersecting-D-brane calculations are the concrete precedent showing that this can actually happen in string theory, while the pion chiral logarithm shows that the bosonic partner's physical radius cannot be identified directly with the microscopic string radius.

---

## 11. User

> also I wonder if the quarks in the extreme of the strings, while being somehow the same, have different mass properties or even massless

### ChatGPT

Yes. After checking the string-hadron and QCD literature, I think this is more than a possible loophole: there are established frameworks in which **“the mass of the quark at the end of the string” is not the mass ordinarily assigned to that quark**, and it may consistently be zero.

The key is to keep four different quantities apart:

$$
\boxed{
m_q^{\overline{\rm MS}}(\mu),\qquad
M_q(p^2),\qquad
m_q^{\rm end},\qquad
M_{\rm whole\ string}
}
$$

They need not coincide.

### QCD itself already does this

The Lagrangian/current mass $m_q(\mu)$ is a short-distance parameter. For $u,d$ it is only a few MeV. But the dressed propagator is

$$
S(p)=
\frac{Z(p^2)}
{\not p-M(p^2)},
$$

with

$$
M(p^2)=\frac{B(p^2)}{A(p^2)}.
$$

Dynamical chiral symmetry breaking makes $M(p^2)$ large at small momentum even in the exact chiral limit

$$
m_q(\mu)=0.
$$

At infrared momenta the light quark behaves roughly constituent-like, $M(0)\sim O(300\ {\rm MeV})$; at high momentum it evolves back toward the small running current mass. This is standard DSE/lattice QCD phenomenology. [MDPI+1](https://www.mdpi.com/2073-8994/12/9/1468)

So the same fundamental $u$ quark can legitimately be

$$
\boxed{
\text{almost massless when probed hard}
\quad\leftrightarrow\quad
\text{strongly dressed and apparently massive in a hadron}.
}
$$

That is already remarkably close to what we need.

And the pion makes the point even sharper. In the chiral limit one has the exact relation

$$
f_\pi^0 E_\pi(k;0)=B(k^2).
$$

Thus the same nonzero $B(k^2)$ which makes the dressed quark massive is precisely what guarantees a **massless pion**. [MDPI](https://www.mdpi.com/2073-8994/12/9/1468)

So QCD itself tells us:

$$
\boxed{
M_q^{\rm dressed}\neq0,
\qquad
m_\pi=0
}
$$

in the chiral limit.

There is therefore no elementary rule saying that endpoint quark mass + string energy must add naively to the meson mass.

---

## The string endpoint mass is a fifth notion of mass

This is perhaps the most relevant literature result for us.

Sonnenschein and Weissman explicitly distinguish the mass parameter attached to the end of a phenomenological QCD string from both current and constituent quark masses:

$$
m_{\rm end}\neq m_q^{\rm current},
\qquad
m_{\rm end}\neq m_q^{\rm constituent}.
$$

In their holographic interpretation, $m_{\rm end}$ is the energy of a **vertical string segment in the holographic direction** mapped to a point mass in four dimensions. [Springer Nature+1](https://link.springer.com/article/10.1140/epjc/s10052-019-6828-y)

For $u,d$, their spectroscopy fits allow

$$
0\lesssim m_{u,d}^{\rm end}\lesssim100\ {\rm MeV},
$$

and their conventional fitted value is

$$
m_{u,d}^{\rm end}\simeq60\ {\rm MeV}.
$$

They explicitly note that the light endpoint masses are poorly determined and may be essentially zero. [Springer Nature](https://link.springer.com/article/10.1140/epjc/s10052-019-6828-y)

Compare:

$$
m_u^{\overline{\rm MS}}\sim2\ {\rm MeV},
$$

$$
m_d^{\overline{\rm MS}}\sim5\ {\rm MeV},
$$

$$
m_{u,d}^{\rm end}\sim0-100\ {\rm MeV},
$$

$$
M_{u,d}^{\rm dressed}(0)\sim300\ {\rm MeV}.
$$

These are genuinely different objects.

That distinction is almost tailor-made for our construction.

---

## And there are string-QCD models with literally massless quarks

The Witten–Sakai–Sugimoto model is even cleaner.

The fundamental chiral quarks arise as massless modes of open strings stretching between color D4 and flavor D8/$\overline{\rm D8}$ branes. In the standard model the light quarks are **exactly massless**, while confinement and spontaneous chiral symmetry breaking still generate the hadronic scale. [SpringerLink+1](https://springerlink.fh-diploma.de/article/10.1140/epjc/s10052-018-5926-6)

Thus string theory already has the configuration

$$
\boxed{
m_{\rm endpoint\ quark}=0
}
$$

while

$$
\boxed{
M_{\rm generic\ hadron}\sim\Lambda_{\rm QCD}\neq0.
}
$$

The pion alone remains massless in the exact chiral limit, because it is the Goldstone state.

Switching on explicit quark masses then makes

$$
m_\pi^2\propto m_u+m_d.
$$

So this gives almost exactly the hierarchy you were wondering about.

---

# What does an endpoint mass actually do?

For a Nambu–Goto string with endpoint masses,

$$
S=
-T\int d^2\sigma\sqrt{-\det h}
-\sum_i m_i\int d\tau
\sqrt{-\dot X_i^2}.
$$

Variation gives the modified boundary condition

$$
T\,\partial_\sigma X^\mu
+
m_i\frac{d}{d\tau}
\frac{\dot X^\mu}
{\sqrt{-\dot X^2}}
=0
$$

(up to orientation signs).

For a uniformly rotating straight string the endpoint velocity $\beta_i$ obeys

$$
\boxed{
\frac{T}{\omega}
=
\frac{m_i\beta_i}{1-\beta_i^2}.
}
$$

Consequently,

$$
m_i\rightarrow0
\quad\Longrightarrow\quad
\beta_i\rightarrow1.
$$

The ordinary open string is therefore precisely the **massless-endpoint limit**.

The endpoint still carries flavor/charge information. It just carries no independent inertial mass.

This makes your phrase “somehow the same quark” rather natural: the endpoint can be a quark **label/boundary state**, not a little point particle with the full effective quark mass glued onto it.

---

# This is especially interesting for the quark–diquark branch

HISH baryons are described by

$$
q-\text{string}-[qq].
$$

Their fitted spectra actually do **not** require the diquark endpoint mass to equal the sum of two ordinary constituent masses. Holographically, it contains vertical string pieces plus a baryonic vertex. Sonnenschein and Weissman say the effective diquark endpoint mass can range roughly between the single-quark value and twice it, and potentially more depending on the baryonic vertex. [Springer Nature](https://link.springer.com/article/10.1140/epjc/s10052-019-6828-y)

More strikingly, in some heavy-light baryons the short strings and baryonic vertex associated with light quarks appear to contribute essentially no measurable endpoint mass. They explicitly mention that this may indicate nearly massless light quarks at the ends. [Springer Nature](https://link.springer.com/article/10.1140/epjc/s10052-019-6828-y)

So

$$
m^{\rm end}_{[ud]}
\neq
m_u^{\rm constituent}+m_d^{\rm constituent}
$$

is not only allowed; existing string-hadron models already encounter it.

That helps your identification

$$
q
\;\longleftrightarrow\;
[\bar q\bar q]+\text{fermionic string},
$$

because the two antiquark endpoints need not inject

$$
2\times300\ {\rm MeV}
$$

into the mass of the resulting object.

They could be effectively **massless boundary degrees of freedom**.

---

## This suggests a cleaner version of the bootstrap

Instead of saying

$$
q=\bar q+\bar q+\text{string}
$$

as an additive constituent-mass formula, write

$$
\boxed{
|q\rangle_R
\;\simeq\;
|\bar q_i,\bar q_j;\,R\text{-string}\rangle .
}
$$

The endpoint objects carry

$$
\text{color},\quad
\text{flavor},\quad
Q,
$$

but potentially

$$
m_{\rm endpoint}=0.
$$

The mass of the complete Ramond state is then an eigenvalue of the complete interacting system,

$$
M_R^2
=
M_R^2(T,\text{boundary interactions},
\text{worldsheet breaking},\ldots),
$$

not

$$
M_R=2m_{\bar q}+TL.
$$

Likewise the bosonic member would be

$$
|M\rangle_{NS}
=
|q_i,\bar q_j;\,NS\text{-string}\rangle.
$$

Again the endpoint masses could vanish.

Then the striking spectrum

$$
m_u,m_d,m_e\ll\Lambda_{\rm QCD},
$$

$$
m_\pi\ll\Lambda_{\rm QCD}
$$

could all originate from small departures from an exact chiral/worldsheet-symmetric limit rather than from constituent endpoint masses.

---

# There is also a direct connection with the scattering question

Massive endpoints do change the Veneziano amplitude.

Sever and Zhiboedov studied precisely the leading correction produced by giving the ends of a string a small point mass. They found a universal high-energy correction to the Veneziano asymptotics. [Springer Nature+1](https://link.springer.com/article/10.1007/JHEP06%282018%29054)

Schematically,

$$
\delta\log {\cal A}
\propto
-\alpha' m_{\rm end}^{3/2}
\left(\frac{st}{s+t}\right)^{1/4}
\times
\{\text{elliptic functions}\}.
$$

The important thing is the very unusual dependence

$$
\boxed{
\delta{\cal A}\propto m_{\rm end}^{3/2}.
}
$$

The corresponding leading Regge trajectory becomes

$$
j(t)
=
\alpha'
\left[
t-
\frac{8\sqrt{\pi}}{3}
m_{\rm end}^{3/2}t^{1/4}
+\cdots
\right].
$$

So endpoint mass is not merely a correction to the rest energy. It gives a characteristic deformation of the **scattering amplitude itself**.

And in the limit

$$
m_{\rm end}\to0
$$

that entire correction disappears.

This now gives us three conceptually separate sources for departure from ideal pointlike Ramond scattering:

$$
\boxed{
\begin{aligned}
\text{finite }\alpha' &: &&
\delta{\cal A}\sim \alpha'^2 E^4,\\
\text{endpoint mass} &: &&
\delta\log{\cal A}\sim
\alpha' m_{\rm end}^{3/2}E^{1/2},
\\
\text{boundary/chiral breaking} &: &&
\delta{\cal A}\sim c_6 E^2/M_s^2
\quad\text{if allowed}.
\end{aligned}}
$$

That separation seems physically much better than treating “quark mass” as a single input.

---

## What I think is the most economical interpretation

The same $u$ label can appear in all three regimes without contradiction:

$$
\begin{array}{ccl}
\text{fundamental/chiral endpoint}
&:&m_{\rm end}\simeq0,\\[2mm]
\text{hard quark}
&:&m_u(\mu)\simeq {\rm few\ MeV},\\[2mm]
\text{soft dressed quark}
&:&M_u(p\sim0)\sim300\ {\rm MeV}.
\end{array}
$$

These aren't three particles.

They are three different answers to three different questions about the **same quark degree of freedom**.

That is probably the correct conceptual language for your string picture as well. The quarks at the two ends need not be miniature on-shell versions of the asymptotic quark. They can be essentially massless color/flavor boundary degrees of freedom, while both the hadronic constituent mass and the small observed explicit quark mass arise from different kinds of dressing or symmetry breaking.

And there is a rather beautiful QCD precedent: in the exact chiral limit,

$$
\boxed{
m_{u,d}^{\rm current}=0,\qquad
M_{u,d}^{\rm dressed}\neq0,\qquad
m_\pi=0.
}
$$

That three-way distinction looks much closer to the structure your bootstrap construction needs than the naive constituent-quark picture does.
