"""One literal B0 fixture, geometry/source discretizations and full s quadrature."""
import argparse
import datetime as dt
import gc
import json
import os
from pathlib import Path
import time

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.linalg import expm
from threadpoolctl import threadpool_limits

from reconstruct4d import Reconstruction,link_diagnostics
from comparison4d import Comparison


def atomic(path,data):
    path=Path(path);tmp=path.with_suffix(path.suffix+'.tmp')
    with tmp.open('w') as f:
        json.dump(data,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
    tmp.replace(path)


def fixture(seed=261009093, amplitude=.4, a=0., b=0.):
    rng=np.random.default_rng(seed)
    def generator():
        m=rng.normal(size=(5,5))+1j*rng.normal(size=(5,5));m=(m+m.conj().T)/2
        m-=np.trace(m)*np.eye(5)/5
        return 1j*m/np.linalg.norm(m)
    U=np.array([expm(amplitude*generator()) for _ in range(4)])
    tx,ty,g=generator(),generator(),generator()
    U[0]=expm(a*tx) @ U[0];U[1]=expm(b*ty) @ U[1]
    return U,tx,ty,g


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--config',required=True,type=Path);p.add_argument('--output',required=True,type=Path)
    args=p.parse_args();config=json.loads(args.config.read_text());out=args.output;out.mkdir(parents=True,exist_ok=True)
    U,tx,ty,g=fixture(config['seed'],config['amplitude'],config.get('a',0),config.get('b',0))
    mesh=config['mesh'];h=config.get('source_step',.01)
    start=time.monotonic()
    progress=dict(config=config,started_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
                  completed=False,stage='geometry',nodes=[],geometry=[],
                  scientific_scope='Literal finite first comparison B0 in 4D, approximate spatial transport and original-link derivatives; no infinite-current tail bound or full theorem.')
    def save():
        progress['elapsed_seconds']=time.monotonic()-start
        atomic(out/'progress.json',progress)
    def reconstruct(original,label,frozen=None):
        r=Reconstruction(original,weight_nodes=config.get('weight_nodes',96))
        fine,inherited=r.sample_fine(mesh,frozen_inherited=frozen)
        diag=link_diagnostics(fine)
        if max(diag['max_link_unitarity'],diag['max_link_determinant_error'])>1e-10:
            raise ValueError('reconstructed links lost SU(5) normalization')
        progress['geometry'].append(dict(label=label,metrics=r.metrics,links=diag))
        save()
        return fine,inherited,r
    with threadpool_limits(limits=1):
        fine,inherited,_=reconstruct(U,'base')
        derivatives={}
        for name,mu,tangent,step in [('x',0,tx,h),('x_half',0,tx,h/2),('y_half',1,ty,h/2)]:
            pair=[];frozen_pair=[]
            for sign in [1,-1]:
                varied=U.copy();varied[mu]=expm(sign*step*tangent) @ U[mu]
                v,_,geom=reconstruct(varied,f'{name}_{sign:+d}')
                pair.append(v)
                if name=='x_half':
                    frozen,_=geom.sample_fine(mesh,frozen_inherited=inherited)
                    frozen_pair.append(frozen)
            dc=np.zeros_like(U);dc[mu]=tangent @ U[mu]
            derivatives[name]=(dc,(pair[0]-pair[1])/(2*step))
            if name=='x_half':
                derivatives['x_half_frozen_inherited']=(dc,(frozen_pair[0]-frozen_pair[1])/(2*step))
        # Whole-pipeline original gauge covariance, not just a fermion identity.
        rotation=expm(.37*g)
        rotated=np.einsum('ab,mbc,cd->mad',rotation,U,rotation.conj().T)
        rotated_fine,_,_=reconstruct(rotated,'gauge_covariance')
        expected=rotation @ fine @ rotation.conj().T
        cov=float(np.max(abs(rotated_fine-expected)))
        progress['geometry_gauge_covariance_error']=cov
        if cov>2e-10:
            raise ValueError(f'reconstruction/inherited-frame covariance failed: {cov}')
        progress['source_derivative_difference_norm']=float(np.linalg.norm(derivatives['x'][1]-derivatives['x_half'][1]))
        progress['inherited_frame_derivative_effect_norm']=float(np.linalg.norm(derivatives['x_half'][1]-derivatives['x_half_frozen_inherited'][1]))
        arrays={'original':U,'fine':fine,'inherited':inherited}
        for name,(dc,df) in derivatives.items():arrays['coarse_'+name]=dc;arrays['fine_'+name]=df
        np.savez_compressed(out/'fields.npz',**arrays)
        progress['stage']='comparison';save()
    q,w=leggauss(config['quadrature']);q=(q+1)/2;w=w/2
    progress['quadrature_nodes']=q.tolist();progress['quadrature_weights']=w.tolist()
    progress['representations']={}
    with threadpool_limits(limits=2):
        for rep in ['anti5','10']:
            comp=Comparison(U,fine,derivatives,rep,gauge_generator=g)
            rep_result=dict(complete=False,nodes=[],endpoint_moments=None,endpoint_curvatures=None)
            progress['representations'][rep]=rep_result
            for index,(s,weight) in enumerate(zip(q,w)):
                node=comp.node(float(s));node.update(index=index,weight=float(weight),representation=rep)
                atomic(out/f'node-{rep}-{index:03d}.json',node)
                rep_result['nodes'].append(node);progress['nodes'].append(dict(rep=rep,index=index))
                save()
            rep_result['endpoint_moments']=comp.endpoint_moments();save()
            rep_result['endpoint_curvatures']=comp.endpoint_curvatures();save()
            rep_result['integrals']={name:float(sum(n['weight']*n['currents'][name] for n in rep_result['nodes']))
                                     for name in derivatives}
            rep_result['right_integrals']={name:float(sum(n['weight']*n['right_currents'][name] for n in rep_result['nodes']))
                                           for name in derivatives}
            rep_result['gauge_integral']=float(sum(n['weight']*n['gauge_integrand'] for n in rep_result['nodes']))
            rep_result['gauge_ward_residual']=rep_result['gauge_integral']-rep_result['endpoint_moments']['difference']
            rep_result['complete']=True
            save();del comp;gc.collect()
    reps=progress['representations']
    progress['chiral_integrals']={name:sum(reps[r]['integrals'][name] for r in reps) for name in derivatives}
    progress['vectorlike_integrals']={name:sum(reps[r]['integrals'][name]+reps[r]['right_integrals'][name] for r in reps) for name in derivatives}
    progress['chiral_endpoint_curvature_difference']=sum(reps[r]['endpoint_curvatures']['difference'] for r in reps)
    progress['chiral_gauge_ward_residual']=sum(reps[r]['gauge_ward_residual'] for r in reps)
    progress['completed']=True;progress['stage']='finished';save()
    atomic(out/'result.json',progress)
    print(json.dumps({k:progress[k] for k in ['config','elapsed_seconds','chiral_integrals','vectorlike_integrals','chiral_gauge_ward_residual']},indent=2),flush=True)


if __name__=='__main__':
    main()
