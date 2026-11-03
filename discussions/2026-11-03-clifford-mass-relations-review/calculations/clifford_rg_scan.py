"""One-loop QED+effective-threshold diagnostic of Kritov v13 mass relations.

- Spacelike alpha_eff: exact one-loop lepton vacuum-polarization, on-shell subtraction.
- Mass RG: one-loop QED MSbar with threshold-matched charged-fermion beta,
  and leading pole-to-MSbar matching at each lepton mass.
- Effective u,d,s threshold fixed only to reproduce PDG-ish alpha_MS(mtau);
  not a precision hadronic treatment.
"""
import numpy as np
from scipy.optimize import brentq, minimize_scalar
from numpy.polynomial.legendre import leggauss
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.backends.backend_pdf import PdfPages
from pathlib import Path

OUT=Path('/mnt/data')
x0=137.035999177
alpha0=1/x0
me=0.51099895069/1000 # GeV
mm=105.6583755/1000 # GeV
mt=1.77693  # GeV
mp_ratio=1836.152673426
mu_target=206.7682827
tau_target=mt/me
mu_sigma=0.0000046
tau_sigma=.09/me/1000
p_sigma=3.2e-8

# exact spacelike one-loop leptonic vacuum polarization with on-shell subtraction
nodes, w=leggauss(96)
t=(nodes+1)/2; w=w/2
xx=t*(1-t)
def x_eff(Q):
    Q=np.asarray(Q,dtype=float)
    inv_delta=np.zeros_like(Q)
    for m in [me,mm,mt]:
        inv_delta+=(2/np.pi)*np.sum(w*xx*np.log1p((Q[...,None]/m)**2*xx),axis=-1)
    return x0-inv_delta

def lepton_formula_mu(x):return 1.5*x+17/14
def lepton_formula_tau(x):return 25.5*x-17
def proton_formula(x):return 13.5*x-83/6+1/(3*x*(x-1))
def koide(rmu,rtau):return (1+rmu+rtau)/(1+np.sqrt(rmu)+np.sqrt(rtau))**2

x_mu=2/3*(mu_target-17/14)
x_tau=2/51*(tau_target+17)
x_p=brentq(lambda x:proton_formula(x)-mp_ratio,130,140,xtol=1e-13)
x_koide=brentq(lambda x:koide(lepton_formula_mu(x),lepton_formula_tau(x))-2/3,130,145)
roots={name:brentq(lambda Q:float(x_eff(Q))-x,1e-12,.5,xtol=1e-16) for name,x in [('proton',x_p),('muon',x_mu),('tau',x_tau)]}
print('effective alpha required')
for name,x in [('proton',x_p),('muon',x_mu),('tau',x_tau),('exact Koide',x_koide)]:
 print(f'{name:12s}: x={x:.12f}  x0-x={x0-x:+.12g}  Q={roots.get(name,float("nan"))*1e6:.6f} keV')

# Approximate MS QED charge running, hadron threshold is an effective surrogate
# NF weights = N_c Q^2. 3 light quarks sum 2, charm 4/3, bottom 1/3.
def run_x_with_thresholds(mu, light_quark_threshold):
    events=[(me,1.),(mm,1.),(light_quark_threshold,2.),(1.27,4/3),(mt,1.),(4.18,1/3),(172.7,4/3)]
    events=sorted(events)
    x=x0; S=0.; last=me
    for threshold,weight in events:
        if mu <= threshold:
            x-=2*S/(3*np.pi)*np.log(mu/last)
            return x
        if threshold>last:x-=2*S/(3*np.pi)*np.log(threshold/last)
        S+=weight;last=threshold
    x-=2*S/(3*np.pi)*np.log(mu/last)
    return x

mh=brentq(lambda h: run_x_with_thresholds(mt,h)-133.471,.05,.25)
thresholds=sorted([(me,1.),(mm,1.),(mh,2.),(1.27,4/3),(mt,1.),(4.18,1/3),(172.7,4/3)])

def x_MS(scale): return run_x_with_thresholds(scale,mh)

def integrate_alpha(lo,hi):
    """Integral from lo to hi dlog(mu) * alpha(mu), piecewise exact one loop."""
    assert hi>=lo
    brk=[lo]+[a for a,s in thresholds if lo<a<hi]+[hi]
    val=0
    for a,b in zip(brk,brk[1:]):
        xa=x_MS(a); xb=x_MS(b)
        S=sum(s for th,s in thresholds if th<=a)
        if S:
            slope=2*S/(3*np.pi)
            val+=np.log(xa/xb)/slope
        else:
            val+=np.log(b/a)/xa
    return val

def m_MS_from_pole(M,mu):
    """Matched at mu=M, one loop, evolved to common mu>M."""
    m_at_own=M/(1+1/(np.pi*x_MS(M)))
    return m_at_own*np.exp(-3/(2*np.pi)*integrate_alpha(M,mu))

Qgrid=np.geomspace(1e-8,.25,600) # GeV, 10eV to 250MeV
scale=np.geomspace(mt,80.,400) # 1.78 to 80GeV, pure QED omitted weak at high end
alpha_RG=np.array([x_MS(s) for s in scale])
ms_masses=np.array([[m_MS_from_pole(m,s) for m in [me,mm,mt]] for s in scale])
rmu_RG=ms_masses[:,1]/ms_masses[:,0]
rtau_RG=ms_masses[:,2]/ms_masses[:,0]
xmu_RG=2/3*(rmu_RG-17/14)
xtau_RG=2/51*(rtau_RG+17)
Q_RG=koide(rmu_RG,rtau_RG)
print('effective light u/d/s threshold fitted to x_MS(mtau)=133.471:',mh,'GeV')
for mu in [mt,2.,10.,80.]:
 x=x_MS(mu); masses=[m_MS_from_pole(m,mu) for m in [me,mm,mt]]
 rm=masses[1]/masses[0];rt=masses[2]/masses[0]
 print(f'mu={mu:7.3f} GeV; x_MS={x:.6f}, rmu_MS={rm:.6f}, rtau_MS={rt:.6f}, Koide={koide(rm,rt):.9f}, x_needed_mu={(rm-17/14)*2/3:.6f}, x_needed_tau={(rt+17)*2/51:.6f}')

# local logarithmic sensitivities
print('Q(Thomson) =',koide(mu_target,tau_target),'Q_MS=',Q_RG[0])

# create figures
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'figure.dpi':140})
fig1,ax=plt.subplots(figsize=(8.7,4.9))
delta=x0-x_eff(Qgrid)
ax.loglog(Qgrid*1e6,delta,color='C0',lw=2,label=r'$\alpha^{-1}(0)-\alpha_{\mathrm{eff}}^{-1}(Q)$ (lepton VP)')
for name,color in [('proton','C3'),('muon','C2'),('tau','C1')]:
 x={'proton':x_p,'muon':x_mu,'tau':x_tau}[name]
 q=roots[name]*1e6
 ax.scatter([q],[x0-x],s=48,color=color,zorder=4)
 ax.axvline(q,color=color,alpha=.45,ls='--')
 ax.annotate(f'{name}: {q:.3g} keV',xy=(q,x0-x),xytext=(5,0),textcoords='offset points',fontsize=9,color=color)
ax.axhline(x0-x_koide,ls=':',color='0.4',label='exact Koide requires negative shift (inaccessible)') if x0-x_koide>0 else None
ax.set_xlabel('spacelike momentum Q  [keV]')
ax.set_ylabel(r'$\alpha^{-1}(0)-\alpha^{-1}_{\mathrm{eff}}(Q)$')
ax.set_title('If pole masses stay fixed: each relation wants a different Q')
ax.grid(alpha=.18,which='both');ax.legend(loc='upper left',fontsize=8)
fig1.tight_layout();fig1.savefig(OUT/'clifford_rg_1_onshell_scale.png',dpi=170);fig1.savefig(OUT/'clifford_rg_1_onshell_scale.pdf')

fig2,ax=plt.subplots(figsize=(8.7,5.2))
ax.plot(scale,alpha_RG,lw=2.2,label=r'$\alpha_{\overline{MS}}^{-1}(\mu)$ (1-loop QED, matched)',color='C0')
ax.plot(scale,xmu_RG,lw=2,label=r'needed $\alpha^{-1}$ from $m_\mu/m_e$',color='C2')
ax.plot(scale,xtau_RG,lw=2,label=r'needed $\alpha^{-1}$ from $m_\tau/m_e$',color='C1')
ax.axhline(x0,ls=':',color='0.45',label=r'Thomson $\alpha^{-1}(0)$')
ax.set_xscale('log')
ax.set_xlabel(r'common renormalization scale $\mu$  [GeV]')
ax.set_ylabel(r'inverse coupling ($\alpha^{-1}$)')
ax.set_title('Consistent running masses: no common-scale crossing')
ax.legend(fontsize=9,loc='center left');ax.grid(alpha=.18)
fig2.tight_layout();fig2.savefig(OUT/'clifford_rg_2_common_scale.png',dpi=170);fig2.savefig(OUT/'clifford_rg_2_common_scale.pdf')

fig3,ax=plt.subplots(figsize=(8.7,4.7))
ax.plot(scale,1e3*(Q_RG-2/3),lw=2,color='C3',label=r'Koide of running $\overline{MS}$ lepton masses')
ax.axhline(1e3*(koide(mu_target,tau_target)-2/3),color='C2',ls='--',label='Koide of measured pole masses')
ax.axhline(0.,ls=':',color='black',label=r'exact $2/3$')
ax.set_xscale('log');ax.set_xlabel(r'common scale $\mu$  [GeV]')
ax.set_ylabel(r'$10^3\,[K(\mu)-2/3]$')
ax.set_title('Koide does not improve at a higher common renormalization scale')
ax.legend(fontsize=8);ax.grid(alpha=.18)
fig3.tight_layout();fig3.savefig(OUT/'clifford_rg_3_koide.png',dpi=170);fig3.savefig(OUT/'clifford_rg_3_koide.pdf')

# Compose PDF figure sheets for user
with PdfPages(OUT/'clifford_rg_plots.pdf') as pdf:
 for fig in (fig1,fig2,fig3):pdf.savefig(fig)
plt.close('all')
