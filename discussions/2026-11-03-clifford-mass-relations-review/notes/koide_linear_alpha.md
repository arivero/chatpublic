# Koide's ratio for lepton masses linear in 1/α

3 November 2026. This note follows a remark by the user: in Barut-like models with masses linear in 1/α, α simplifies out of Koide's ratio, while second-order terms in α are harder to factor out. Is there a choice of values for which Koide holds identically?

## Setup

Write the heavy-lepton masses in units of the electron mass as

$$\rho_i = \frac{m_i}{m_e} = a_i + w_i\,\kappa,\qquad \kappa = \frac{3}{2\alpha},\qquad i = \mu,\tau,$$

with the electron fixed at $\rho_e = 1$. Barut (1979) has $w = (1, 17)$ and $a = (1, 1)$. Kritov v13 has the same weights and $a = (17/14,\,-17)$. Koide's ratio is

$$Q = \frac{1+\rho_\mu+\rho_\tau}{\bigl(1+\sqrt{\rho_\mu}+\sqrt{\rho_\tau}\bigr)^2}.$$

## Expansion in √α

With $W = w_\mu + w_\tau$, $S = \sqrt{w_\mu}+\sqrt{w_\tau}$ and $T = a_\mu/(2\sqrt{w_\mu}) + a_\tau/(2\sqrt{w_\tau})$,

$$Q = \frac{W}{S^2} \;-\; \frac{2W}{S^3}\,\kappa^{-1/2} \;+\; \frac{W}{S^2}\Bigl[\frac{1+a_\mu+a_\tau}{W} - \frac{1+2ST}{S^2} + \frac{4}{S^2}\Bigr]\kappa^{-1} \;+\; O(\kappa^{-3/2}).$$

- **Leading order.** $Q_\infty = W/S^2$ depends only on the weights: α drops out, as the user says. For $w = (1, 17)$, $Q_\infty = 18/(1+\sqrt{17})^2 = 0.685813$, 2.9% above 2/3. Koide at this order would need $\sqrt{w_\tau/w_\mu} = 2+\sqrt3$, so $w_\tau/w_\mu = 7+4\sqrt3 = 13.93$, which is irrational.
- **Order √α.** The term $-(2W/S^3)\kappa^{-1/2}$ comes from the electron's own $\sqrt{m_e}$ in the denominator. It is independent of the offsets $a_i$. For $w = (1,17)$ its coefficient is $-0.2677$, giving $-0.01867$ at the measured α. This term brings $Q$ from 0.6858 to 0.6671.
- **Order α.** The offsets enter here first. Barut's $(1,1)$ gives $+1.28\times10^{-4}$; Kritov's $(17/14,-17)$ gives $-4.65\times10^{-4}$.

Numerically, the expansion to order α gives 0.667267 (Barut) and 0.666674 (Kritov), against the exact values 0.667279 and 0.666666. The difference is the $O(\alpha^{3/2})$ remainder, about $10^{-5}$.

So the manuscript's Koide value, $Q/(2/3)-1 = -1.0\times10^{-6}$, is the sum of three terms of different orders: $+0.0191$ (weights), $-0.0187$ (electron), $-0.0005$ (offsets), plus a remainder near $10^{-5}$.

## Second-order terms

A correction $c_i/\kappa$ in $\rho_i$, of the kind the proton relation uses ($\alpha^2/(3(1-\alpha))$ and similar), enters $Q$ at order $\kappa^{-2}$, that is $\alpha^2 \approx 5\times10^{-5}$ times an order-one coefficient. That is above the present Koide precision (about $10^{-5}$, set by the τ mass), so such terms are not negligible, but they arrive after the √α and α terms and cannot cancel them.

## Can Koide hold for all α?

Not with the electron as a fixed unit. The coefficient of $\kappa^{-1/2}$, $-2W/S^3$, is nonzero for any positive weights. Offsets and higher-order terms start at order α and cannot remove it. With masses linear in 1/α relative to a fixed electron, $Q = 2/3$ can hold only at isolated values of α:

| Model | $Q/(2/3)-1$ at the measured α | α⁻¹ where $Q = 2/3$ exactly |
| --- | --- | --- |
| Barut 1979, offsets (1, 1) | $+9.2\times10^{-4}$ | 128.34 |
| Kritov v13, offsets (17/14, −17) | $-1.0\times10^{-6}$ | 137.0455 |

Barut's crossing sits near the electroweak-scale coupling, α⁻¹(M_Z) ≈ 128.9 on-shell or 127.93 in MS-bar. Within this framework that is a numerical curiosity, not a derivation: Barut's formula uses Thomson-limit α, and Sec. 3.7 of the review shows that running couplings do not combine well with these relations.

$Q$ becomes independent of α only if the electron scales like the others, with offsets proportional to the weights: $m_i \propto w_i(\kappa+\beta)$ for all three leptons, including $w_e \neq 0$. Then $Q = \sum w/(\sum\sqrt w)^2$ exactly, and Koide is a condition on the weights alone. But then $m_\mu/m_e = w_\mu/w_e$ no longer depends on α. Mass ratios that are 1/α-quantized relative to the electron, and Koide holding identically in α, exclude each other. In these models Koide can only be a coincidence at one value of α.

Section 4.4 of the review gives the geometric alternative that does produce Koide identically: a square-root mass operator with a cyclic Z₃ symmetry and equal norms for its scalar and traceless parts, which is the 45° cone of Foot (1994).
