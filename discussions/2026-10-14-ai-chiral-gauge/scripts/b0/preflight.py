"""Independent small controls before authorizing a bounded B0 campaign."""
import json
from pathlib import Path
import time
import numpy as np
from scipy.linalg import eigh,expm
from threadpoolctl import threadpool_limits
from reconstruct4d import Reconstruction,SITE_INDICES
from comparison4d import Comparison,representation,represented_tangent,GAMMA,G5
from worker import fixture,atomic

start=time.monotonic();results={}
with threadpool_limits(limits=1):
    U,tx,ty,g=fixture()
    eps=1e-5
    for rep in ['anti5','10']:
        numeric=(representation(expm(eps*tx) @ U[0],rep)-
                 representation(expm(-eps*tx) @ U[0],rep))/(2*eps)
        analytic=represented_tangent(U[0],tx @ U[0],rep)
        error=float(np.max(abs(numeric-analytic)))
        assert error<1e-8,(rep,error)
        results['representation_derivative_'+rep]=error
    clifford=max(np.max(abs(a @ b+b @ a-(2*np.eye(4) if i==j else 0)))
                 for i,a in enumerate(GAMMA+[G5]) for j,b in enumerate(GAMMA+[G5]))
    assert clifford<1e-14
    results['clifford_error']=float(clifford)
    # Independently differentiate projectors of a generic small Hermitian toy.
    rng=np.random.default_rng(42)
    def hermitian():
        a=rng.normal(size=(8,8))+1j*rng.normal(size=(8,8));return (a+a.conj().T)/2
    H=np.diag([-4,-3,-2,-1,1,2,3,4])+.02*hermitian();A=hermitian();B=hermitian()
    ev,v=eigh(H);p=v[:,4:];n=v[:,:4]
    spectral=float(-2*np.sum(((p.conj().T @ A @ n)*
                             (p.conj().T @ B @ n).conj()/(ev[4:,None]-ev[None,:4])**2).imag))
    def projector(h):
        _,q=eigh(h);return q[:,4:] @ q[:,4:].conj().T
    P=projector(H);dA=(projector(H+eps*A)-projector(H-eps*A))/(2*eps)
    dB=(projector(H+eps*B)-projector(H-eps*B))/(2*eps)
    direct=float((1j*np.trace(P @ (dA @ dB-dB @ dA))).real)
    results['spectral_vs_direct_projector_curvature_error']=abs(spectral-direct)
    assert abs(spectral-direct)<1e-8
    geom=Reconstruction(U);labels,C=geom.frame([.17,-.21,.08,.12])
    rotation=expm(.37*g)
    rotated=Reconstruction(rotation @ U @ rotation.conj().T)
    labels2,C2=rotated.frame([.17,-.21,.08,.12])
    assert np.array_equal(labels,labels2)
    error=float(np.max(abs(C2-rotation @ C @ rotation.conj().T)))
    results['geometric_frame_gauge_covariance_error']=error
    assert error<2e-11
    results['generic_geometry']=geom.metrics
    commuting=np.array([expm(1j*np.diag(np.array([1,2,3,-2,-4])*(mu+1)*.03)) for mu in range(4)])
    flat=Reconstruction(commuting);links,_=flat.sample_fine(2)
    expected=np.broadcast_to(np.eye(5,dtype=complex),links.shape).copy()
    for i,idx in enumerate(SITE_INDICES):
        for mu in range(4):
            if idx[mu]==2:expected[i,mu]=commuting[mu]
    error=float(np.max(abs(links-expected)))
    results['flat_nontrivial_holonomy_error']=error
    assert error<1e-10
with threadpool_limits(limits=2):
    ident=np.broadcast_to(np.eye(5,dtype=complex),(4,5,5)).copy()
    fine=np.broadcast_to(ident,(81,4,5,5)).copy()
    c=Comparison(ident,fine,{'zero':(np.zeros_like(ident),np.zeros_like(fine))},'anti5',periodic=True)
    node=c.node(.5)
    assert abs(node['minimum_gap']-np.sqrt(3)/2)<1e-10,node
    assert abs(node['currents']['zero'])<1e-14,node
    results['free_comparison']=node
results.update(passed=True,seconds=time.monotonic()-start)
atomic(Path(__file__).parent/'preflight.json',results)
print(json.dumps(results,indent=2))
