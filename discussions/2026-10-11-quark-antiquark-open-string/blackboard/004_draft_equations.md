# 004 — Analytic review of the supplied draft equations

12 October 2026. These are short derivations and an extension of an existing radial ansatz. No numerical scripts were added. PRL page 2, PRD page 4, and addendum page 3 were checked visually against the original PDFs, because native extraction loses mathematical notation.

## 1. PRL Eq. (11): beta-function prefactor

Keep the PDF's conventions `a+b+c=0` and

```math
V(a,b)=\frac{\Gamma(1-\alpha'a)\Gamma(1-\alpha'b)}
{\Gamma(1-\alpha'(a+b))}.
```

Using `Γ(1+z)=zΓ(z)` in numerator and denominator gives

```math
V(a,b)=\frac{\alpha'^2 ab}{-\alpha'(a+b)}
\frac{\Gamma(-\alpha'a)\Gamma(-\alpha'b)}{\Gamma(-\alpha'(a+b))}
=\frac{\alpha'ab}{c}B(-\alpha'a,-\alpha'b).
```

The printed PRL Eq. (11) instead uses denominator `−c`. With the stated definitions it has the wrong sign. The low-energy factor defined by the gamma ratio must tend to +1. This is a correction to the intermediate relation, not a change to the correct gamma-ratio benchmark used elsewhere.

## 2. PRD Eq. (36): no alternating level sign

Let `δ=α'a−n` and `β=α'b`. At integer n≥1,

```math
\Gamma(1-n-\delta)\sim\frac{(-1)^n}{(n-1)!\,\delta},\qquad
\frac{\Gamma(1-\beta)}{\Gamma(1-n-\beta)}
=(-1)^n\prod_{k=0}^{n-1}(\beta+k).
```

The two signs cancel:

```math
V(a,b)\sim
\frac{\prod_{k=0}^{n-1}(\alpha'b+k)}
{(n-1)!\,\alpha'(a-nM_s^2)}.
```

The PRD's extra `(-1)^(n−1)` is incorrect for this defined function. An overall amplitude convention cannot absorb a relative sign that changes from level to level. PRL Eq. (12) already has the corrected residue, so the supplied versions disagree. Spin/positivity statements about physical exchange still require the **full amplitude**, not the scalar factor in isolation.

## 3. Addendum Eq. (111): the PDF already has the correct sign

For `0<b<2`, analytic continuation of the Mellin function can be written as

```math
\mathcal M(-b;x)=\int_0^\infty dw\,w^{-b-1}[V_w(x)-1]<0,
\qquad 0<x<1.
```

The physical deficit is positive. The PDF prints `b |M(−b;x)| (s/M*²)^b`, which is correct within its ansatz. The extracted text drops the absolute-value bars. **There is no sign correction to make to this printed equation.** This is a concrete example of why automatic extraction must not be treated as exact mathematical transcription.

## 4. A useful missing case: the marginal radial exponent b=2

This is an analytic completion of the addendum's toy average, not a derivation of a physical holographic wavefunction. Write `u=y²`, `u0=y0²`, `z=α'had s`, and `δ=z u0=s/M*²`. The normalized UV-weighted average is

```math
\bar V_b(z,x)=\frac{b u_0^b}{1-u_0^b}
\int_{u_0}^{1}du\,u^{-b-1}V(zu,x),\qquad b>0.
```

Consequently its deficit has an explicitly positive, finite-cutoff representation:

```math
1-\bar V_b=
\frac{b\delta^b}{1-u_0^b}
\int_{\delta}^{z}dw\,w^{-b-1}[1-V(w,x)].
```

Set `a(x)=ζ(2)x(1−x)`, so that `1−V(w,x)=a(x)w²+O(w³)` near zero. In the window `δ≪1≪z` at fixed nonforward angle:

```math
1-\bar V_b\sim
\begin{cases}
\dfrac{b|\mathcal M(-b;x)|}{1-u_0^b}\,\delta^b,&0<b<2,\\[6pt]
\dfrac{2a(x)}{1-u_0^2}\,\delta^2\log(1/\delta),&b=2,\\[6pt]
\dfrac{b a(x)}{(b-2)(1-u_0^b)}\,\delta^2,&b>2.
\end{cases}
```

The logarithm follows from integrating `a(x)/w` between δ and order one. At b=2 there are additional nonlogarithmic terms of order δ². Dropping `u0^b` in the normalization recovers the addendum's two displayed regimes and supplies its missing boundary case. The expansion is not uniform near b=2; simply taking b→2 in either neighboring leading formula is invalid. The leading cross-section deficit is twice the amplitude deficit only when the latter is small and the factorization assumed by this toy model holds.

For fixed nonzero u0, the true low-energy expansion `z≪1` is instead analytic:

```math
1-\bar V_b=a(x)z^2\langle u^2\rangle_b+O(z^3),
```

with

```math
\langle u^2\rangle_b=
\frac{b u_0^b}{1-u_0^b}\frac{1-u_0^{2-b}}{2-b}\quad(b\ne2),
\qquad
\langle u^2\rangle_2=\frac{2u_0^2}{1-u_0^2}\log(1/u_0).
```

Thus a fractional power in the intermediate regime does not show that the finite-cutoff model lacks a low-energy local expansion. At b=1 the energy power is integer, but matching one power of s still does not establish a local dimension-six operator: angular dependence and the range of validity must also match.

This b=2 calculation is new to this notebook and follows by standard asymptotic integration. No literature-novelty claim is made. A new numerical study is warranted only if a specified candidate profile or observable needs the finite-energy crossover, not merely to recheck this integral identity.
