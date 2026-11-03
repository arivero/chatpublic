#!/usr/bin/env python3
"""Reproducible fixed-integer and continuous-coefficient scans of Kritov v13.
Inputs from manuscript Tables 1 and 3, PDG 2026 tau central value as stated there.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from scipy.optimize import brentq

OUT=Path(__file__).parent
alpha_inv=137.035999177
sigma_alpha_inv=2.1e-8
alpha=1/alpha_inv
kappa=3*alpha_inv/2
me=.51099895069
rho_mu_obs=206.7682827
sigma_mu=4.6e-6
tau_obs_MeV=1776.93
sigma_tau_MeV=.09
rho_tau_obs=tau_obs_MeV/me
sigma_tau=sigma_tau_MeV/me
rho_p_obs=1836.152673426
sigma_p=3.2e-8

def lepton(lam,eta,n=17):
    x=kappa/lam
    return x+eta*n/14., n*(x-eta)

def koide(m,t):
    return (1+m+t)/(1+np.sqrt(m)+np.sqrt(t))**2

def k_ppm(m,t):
    return 1e6*(koide(m,t)/(2/3)-1)

def lambda_mu(eta,n=17):
    return kappa/(rho_mu_obs-eta*n/14.)

def tau_mu(eta,n=17):
    return lepton(lambda_mu(eta,n),eta,n)[1]

def exact_fit_n(n):
    x=(rho_tau_obs+14*rho_mu_obs)/(n+14)
    return kappa/x, 14*(rho_mu_obs-x)/n

def proton_integer(u,q,ainv=alpha_inv):
    aa=1/ainv
    return 27/(2*aa)-83/6 + u*u*aa*aa/(3*(1-q*aa))

def proton_beta(beta,ainv=alpha_inv):
    return proton_integer(beta,beta,ainv)

n0=17
mu0,tau0=lepton(1,1,17)
K0=k_ppm(mu0,tau0)
lambda_exact,eta_exact=exact_fit_n(17)
# Physical heavy-tau branch of Koide's quadratic at fixed observed muon ratio:
sqrtmu=np.sqrt(rho_mu_obs)
sqrt_tau_K=2*(1+sqrtmu)+np.sqrt(3*(1+4*sqrtmu+rho_mu_obs))
rho_tau_koide=sqrt_tau_K**2
eta_koide=brentq(lambda e:tau_mu(e,17)-rho_tau_koide,.9,1.1)
lambda_koide=lambda_mu(eta_koide)
beta_fit=brentq(lambda b:proton_beta(b)-rho_p_obs,.8,1.2)
# d(rho_p)/d(alpha_inv) analytic
x=alpha_inv
dpdx=27/2 - (2*x-1)/(3*x*x*(x-1)**2)
sigma_p_input=abs(dpdx)*sigma_alpha_inv
sigma_p_indep=np.hypot(sigma_p,sigma_p_input)

plt.rcParams.update({
 'font.family':'DejaVu Sans','font.size':10,'axes.labelsize':10.5,
 'axes.titlesize':12,'axes.spines.top':False,'axes.spines.right':False,
 'xtick.labelsize':9,'ytick.labelsize':9,'legend.fontsize':8.7,
 'figure.dpi':140,'savefig.dpi':210,'pdf.fonttype':42,
})
INK='#19364c'; BLUE='#27699b'; GOLD='#ad7026'; RED='#a43b35'; GREEN='#36775b'

def finish(path):
    plt.tight_layout(pad=1.6)
    plt.savefig(OUT/path,bbox_inches='tight')
    plt.close()

# Figure 1: adjacent integer weights dramatically fail even after recalibrating the radius.
ns=np.arange(13,22,dtype=int)
tau_pred=np.array([tau_mu(1,n)*me for n in ns])
delta=tau_pred-tau_obs_MeV
fig,ax=plt.subplots(figsize=(7.25,3.48))
ax.axhspan(-sigma_tau_MeV,sigma_tau_MeV,color=GREEN,alpha=.12,label='PDG 2026: ±1 SD')
ax.axhline(0,color=INK,lw=1.2)
ax.plot(ns,delta,color=BLUE,lw=1.7,alpha=.6)
ax.scatter(ns,delta,color=BLUE,s=39,zorder=3)
ax.scatter([17],[delta[list(ns).index(17)]],color=GOLD,s=80,zorder=4,label='n = 17')
for n,d in zip(ns,delta):
    if n in (16,17,18): ax.annotate(f'{d:+.3f} MeV', (n,d),xytext=(0,14 if n!=18 else -20),textcoords='offset points',ha='center',fontsize=9)
ax.set_xlabel('Integer response weight n = 1 + 16 g (exploratory)')
ax.set_ylabel('Predicted tau energy − PDG target  [MeV]')
ax.set_title('Discrete response weights: muon fitted, correction complete (η = 1)')
ax.set_xticks(ns)
ax.legend(loc='upper left')
finish('fig1_integer_weight.pdf')

# Figure 2: changing n requires large eta to simultaneously match both masses.
ns2=np.arange(14,21)
lams,etas=np.array([exact_fit_n(n) for n in ns2]).T
fig,ax=plt.subplots(figsize=(7.25,3.42))
ax.axhspan(.95,1.05,color=GREEN,alpha=.10,label='Illustrative η near 1 (±5%)')
ax.axhline(1,color=INK,ls='--',lw=1)
ax.plot(ns2,etas,'o-',color=BLUE,lw=1.7)
ax.scatter([17],[eta_exact],color=GOLD,s=85,zorder=4)
for n,e in zip(ns2,etas): ax.annotate(f'{e:.3f}',(n,e),xytext=(0,8),textcoords='offset points',ha='center',fontsize=8)
ax.set_xticks(ns2)
ax.set_xlabel('Integer weight n')
ax.set_ylabel('η required to fit muon and tau central values')
ax.set_title('Exact two-mass fits exist for each integer n, but only 17 has η near 1')
ax.legend(loc='lower right')
finish('fig2_integer_eta.pdf')

# Figure 3: measured likelihood in (eta, offset from the muon-matching lambda curve).
e=np.linspace(.981,1.021,620)
dlambda_ppm=np.linspace(-.075,.075,380)
E,DEL=np.meshgrid(e,dlambda_ppm)
LAMB=lambda_mu(E)+DEL*1e-6
M,T=lepton(LAMB,E,17)
CHI=((M-rho_mu_obs)/sigma_mu)**2+((T-rho_tau_obs)/sigma_tau)**2
fig,ax=plt.subplots(figsize=(7.25,4.0))
levels=[0,2.30,6.18,12,25,50,120]
cf=ax.contourf(E,DEL,np.minimum(CHI,120),levels=levels,cmap='Blues',extend='max')
ct=ax.contour(E,DEL,CHI,levels=[2.30,6.18],colors=[GREEN,GOLD],linewidths=1.65)
ax.clabel(ct,fmt={2.30:'68% (2D)',6.18:'95% (2D)'},fontsize=8)
orig_dl=1e6*(1-lambda_mu(1))
ax.scatter([1],[orig_dl],color=RED,marker='x',s=82,lw=2.3,zorder=5,label='Manuscript (1,1)')
ax.scatter([eta_exact],[0],color=INK,s=45,zorder=5,label='Exact central-value fit')
ax.set_xlabel('η : real mass-calibration factor')
ax.set_ylabel('10⁶ × [λ − λμ(η)]  [ppm]')
ax.set_title('n = 17: joint muon–tau residual after resolving the thin λ direction')
ax.legend(loc='upper right')
fig.colorbar(cf,ax=ax,label='χ² = (Δμ/σμ)² + (Δτ/στ)²',shrink=.94)
finish('fig3_lepton_local_chi2.pdf')

# Figure 4: Koide on muon-matched curve: exact Q and reference Q are different conditions.
eta_range=np.linspace(.985,1.015,700)
T=tau_mu(eta_range,17)
Kppm=k_ppm(rho_mu_obs,T)
fig,ax=plt.subplots(figsize=(7.25,3.62))
ax.plot(eta_range,Kppm,color=BLUE,lw=2,label='Koide along exact muon-fit curve')
ax.axhline(0,color=INK,lw=1.25,ls='--',label='Exact Koide Q = 2/3')
ax.axhline(k_ppm(rho_mu_obs,rho_tau_obs),color=GREEN,lw=1.4,ls=':',label='Muon + PDG tau central target')
ax.axvline(eta_koide,color=GOLD,ls='--',lw=1.25)
ax.axvline(eta_exact,color=GREEN,ls='--',lw=1.05,alpha=.8)
ax.scatter([eta_koide],[0],s=72,color=GOLD,zorder=4,label='η for exact Koide')
ax.scatter([eta_exact],[k_ppm(rho_mu_obs,rho_tau_obs)],s=55,color=GREEN,zorder=4,label='η for tau central value')
ax.scatter([1],[k_ppm(rho_mu_obs,tau_mu(1))],s=43,color=RED,zorder=4,label='η = 1, muon matched')
ax.set_xlabel('η (with λ chosen to fit muon exactly; n = 17)')
ax.set_ylabel('10⁶ × [Q/(2/3) − 1]  [ppm]')
ax.set_title('Koide does not impose a new integer: it selects a continuous calibration')
ax.legend(loc='upper right',ncol=2,fontsize=7.5)
finish('fig4_koide.pdf')

# Figure 5: 2D lattice for truly integer coefficients u, q in the colour ansatz.
us=np.arange(0,4)
qs=np.arange(-3,6)
U,Q=np.meshgrid(us,qs)
Z=(proton_integer(U,Q)-rho_p_obs)/sigma_p_indep
fig,ax=plt.subplots(figsize=(7.25,4.35))
from matplotlib.colors import Normalize
vals=np.log10(1+np.abs(Z))
im=ax.imshow(vals,origin='lower',aspect='auto',extent=[-.5,3.5,-3.5,5.5],cmap='YlGnBu',vmin=0,vmax=5)
ax.set_xticks(us); ax.set_yticks(qs)
for i,q in enumerate(qs):
    for j,u in enumerate(us):
        if u==1: label=f'{Z[i,j]:+.2f}'
        elif u==0: label=f'{Z[i,j]:+.0f}'
        else: label='>> 1'
        ax.text(u,q,label,ha='center',va='center',fontsize=8,color='black' if vals[i,j]<2 else 'white')
ax.plot(1,1,'s',ms=23,mfc='none',mec=RED,mew=2,transform=ax.transData)
ax.set_xlabel('Integer cross-coupling coefficient u (nonnegative)')
ax.set_ylabel('Integer return-diagonal coefficient q')
ax.set_title('Integer-only colour ansatz: annotated combined-uncertainty residual')
fig.colorbar(im,ax=ax,label='log10(1 + |combined z|)',shrink=.85)
finish('fig5_proton_integer_lattice.pdf')

# Figure 6: integer q near original, compare reference-only and illustrative combined errors.
qplot=np.arange(-2,6)
res=np.array([proton_integer(1,q)-rho_p_obs for q in qplot])
fig,ax=plt.subplots(figsize=(7.25,3.52))
ax.axhspan(-1,1,color=GREEN,alpha=.12,label='±1 SD')
ax.axhline(0,color=INK,lw=1.1)
ax.plot(qplot,res/sigma_p,'o-',color=BLUE,lw=1.5,label='Reference-only standard deviation')
ax.plot(qplot,res/sigma_p_indep,'s--',color=GOLD,lw=1.5,label='Including α input; independent approximation')
ax.scatter([1],[(proton_integer(1,1)-rho_p_obs)/sigma_p],color=RED,s=60,zorder=5)
ax.set_xticks(qplot)
ax.set_xlabel('Integer q, with u = 1 fixed')
ax.set_ylabel('Proton prediction residual / uncertainty')
ax.set_title('An integer coefficient can be selected by a narrow reference-only test')
ax.legend(loc='upper left')
finish('fig6_proton_q_uncertainty.pdf')

# Figure 7: vary a genuinely continuous strength beta, keeping integer counts fixed.
betas=np.linspace(.97,1.03,700)
residual=proton_beta(betas)-rho_p_obs
fig,ax=plt.subplots(figsize=(7.25,3.55))
ax.axhspan(-1,1,color=GREEN,alpha=.11)
ax.plot(betas,residual/sigma_p_indep,color=BLUE,lw=1.95,label='Combined-uncertainty z (indicative)')
ax.plot(betas,residual/sigma_p,color=GOLD,lw=1,alpha=.7,label='Reference-only z')
ax.axhline(0,color=INK,lw=1.1)
ax.axvline(1,color=RED,ls='--',lw=1.35,label='Original β = 1')
ax.axvline(beta_fit,color=GREEN,ls=':',lw=1.35,label='Central exact-fit β')
ax.set_ylim(-36,38)
ax.set_xlabel('Real return-strength multiplier β')
ax.set_ylabel('Proton residual / uncertainty')
ax.set_title('Continuous interaction-strength deformation: colour integers unchanged')
ax.legend(loc='upper left')
finish('fig7_proton_beta.pdf')

# Reproducibility summary data in plain text.
summary=(
 f'alpha_inv={alpha_inv}\n'
 f'kappa={kappa}\n'
 f'lepton manuscript mu={mu0:.13f}, tau={tau0:.13f}, Koide relative ppm={K0:.8f}\n'
 f'lepton exact mu+tau n17: lambda={lambda_exact:.13f}, eta={eta_exact:.13f}\n'
 f'lepton exact mu+Koide n17: lambda={lambda_koide:.13f}, eta={eta_koide:.13f}, tau_MeV={rho_tau_koide*me:.12f}\n'
 f'proton manuscript rho={proton_beta(1):.13f}, target={rho_p_obs}\n'
 f'proton beta fit={beta_fit:.13f}\n'
 f'proton sigma_input={sigma_p_input:.13g}, combined={sigma_p_indep:.13g}\n'
)
(OUT/'numerics.txt').write_text(summary)
print(summary)
