"""Full position-space 4D finite comparison; no momentum reduction.

Positive spectral projectors and the orientation H_f -> extended H_c follow
Craig's equations (direct-comparison) and (transgression). Sparse application
of derivatives limits memory; all eigenvectors are computed deterministically.
"""
import itertools
import time

import numpy as np
from scipy import linalg, sparse

PAULI = [np.eye(2), np.array([[0,1],[1,0]]),
         np.array([[0,-1j],[1j,0]]), np.diag([1,-1])]
GAMMA = [np.kron(PAULI[1], PAULI[j]) for j in [1,2,3]] + [np.kron(PAULI[2], PAULI[0])]
G5 = np.kron(PAULI[3], PAULI[0])
PAIRS = np.array(list(itertools.combinations(range(5), 2)))


def representation(u, rep):
    if rep == 'anti5':
        return u.conj()
    if rep != '10':
        raise ValueError(rep)
    a, b = PAIRS.T
    return u[...,a[:,None],a[None,:]] * u[...,b[:,None],b[None,:]] - \
           u[...,a[:,None],b[None,:]] * u[...,b[:,None],a[None,:]]


def represented_tangent(u, du, rep):
    if rep == 'anti5':
        return du.conj()
    a,b=PAIRS.T
    return (du[...,a[:,None],a[None,:]] * u[...,b[:,None],b[None,:]] +
            u[...,a[:,None],a[None,:]] * du[...,b[:,None],b[None,:]] -
            du[...,a[:,None],b[None,:]] * u[...,b[:,None],a[None,:]] -
            u[...,a[:,None],b[None,:]] * du[...,b[:,None],a[None,:]])


def generator_rep(g, rep):
    return represented_tangent(np.eye(5, dtype=complex), g, rep)


def wilson(links, periodic=False, derivative=False):
    sites, _, r, _ = links.shape
    L = int(round(sites**.25))
    if L**4 != sites:
        raise ValueError('expected isotropic one- or three-site-per-axis lattice')
    d = 4*r
    blocks = {(i,i): (np.zeros((d,d),complex) if derivative else 3*np.kron(G5,np.eye(r)))
              for i in range(sites)}
    for i, idx in enumerate(itertools.product(range(L),repeat=4)):
        for mu in range(4):
            nxt = list(idx); nxt[mu] = (nxt[mu]+1)%L
            j = np.ravel_multi_index(tuple(nxt),(L,)*4)
            sign = -1 if idx[mu] == L-1 and not periodic else 1
            hop = sign*np.kron((-1j*GAMMA[mu]-G5)/2,links[i,mu])
            blocks[(i,j)] = blocks.get((i,j),0)+hop
            blocks[(j,i)] = blocks.get((j,i),0)+hop.conj().T
    data=[];indices=[];indptr=[0]
    for i in range(sites):
        for (row,col), block in sorted(blocks.items()):
            if row == i:
                data.append(block); indices.append(col)
        indptr.append(len(data))
    result=sparse.bsr_matrix((np.array(data),np.array(indices),np.array(indptr)),
                             shape=(sites*d,sites*d)).tocsr()
    error=sparse.linalg.norm(result-result.conj().T)
    if error > 1e-10:
        raise ValueError(f'non-Hermitian Wilson operator: {error}')
    return result


class Comparison:
    def __init__(self, original, fine, variations, rep, gauge_generator=None, periodic=False):
        self.rep=rep
        self.r=5 if rep=='anti5' else 10
        self.d=4*self.r
        self.n=81*self.d
        self.Hc=wilson(representation(original[None],rep),periodic).toarray()
        self.F=wilson(representation(fine,rep),periodic)
        self.g5=np.kron(G5,np.eye(self.r))
        self.diag=np.tile(np.diag(self.g5),81)
        self.variations={name:(wilson(represented_tangent(original[None],dc[None],rep),
                                      periodic,True).toarray(),
                               wilson(represented_tangent(fine,df,rep),periodic,True))
                         for name,(dc,df) in variations.items()}
        self.G=(np.kron(np.eye(4),generator_rep(gauge_generator,rep))
                if gauge_generator is not None else None)
        # Constant centered copying: I†I=1; both fields use inherited coordinates.
        inclusion=np.tile(np.eye(self.d),(81,1))/9
        self.embedding_error=float(np.linalg.norm(inclusion.conj().T @ inclusion-np.eye(self.d)))
        if self.embedding_error>1e-12:
            raise ValueError('coarse inclusion is not isometric')

    def extended_apply(self,v,matrix=None):
        compressed=v.reshape(81,self.d,-1).sum(axis=0)/9
        if matrix is None:
            correction=(self.Hc-self.g5) @ compressed
            return self.diag[:,None]*v + np.tile(correction/9,(81,1))
        return np.tile((matrix @ compressed)/9,(81,1))

    def dense(self,s):
        h=(1-s)*self.F.toarray()
        h += s*np.kron(np.ones((81,81))/81,self.Hc-self.g5)
        h[np.diag_indices(self.n)] += s*self.diag
        return np.asfortranarray(h)

    def node(self,s):
        start=time.monotonic()
        eigenvectors=self.dense(s)
        ev,v=linalg.eigh(eigenvectors,overwrite_a=True,check_finite=False,driver='evd')
        del eigenvectors
        gap=float(np.min(abs(ev)))
        if gap < .05:
            raise ValueError(f'comparison gap unsafe at s={s}: {gap}')
        split=int(np.count_nonzero(ev<0))
        if split!=self.n//2:
            raise ValueError(f'unexpected positive/negative ranks {split}, {self.n}')
        vn=v[:,:split]; vp=v[:,split:]
        # Check one deterministic eigenpair without constructing another dense H.
        j=self.n//3
        residual=np.linalg.norm((1-s)*(self.F @ v[:,j:j+1])+s*self.extended_apply(v[:,j:j+1])-
                                ev[j]*v[:,j:j+1])
        if residual > 1e-9:
            raise ValueError(f'eigenpair residual {residual}')
        A=vp.conj().T @ (self.extended_apply(vn)-self.F @ vn)
        denominator=ev[split:,None]-ev[None,:split]
        result=dict(s=float(s),minimum_gap=gap,dimension=self.n,negative_rank=split,
                    embedding_isometry_error=self.embedding_error,
                    eigenpair_residual=float(residual),currents={},right_currents={})
        for name,(dc,df) in self.variations.items():
            B=vp.conj().T @ ((1-s)*(df @ vn)+s*self.extended_apply(vn,dc))
            terms=A*B.conj()/denominator**2
            result['currents'][name]=float(-2*np.sum(terms.imag,dtype=np.longdouble))
            # Complementary-band trace calculated with the reversed blocks.
            result['right_currents'][name]=float(-2*np.sum(terms.conj().T.imag,
                                                           dtype=np.longdouble))
            del B,terms
        if self.G is not None:
            gv=np.einsum('ab,ibj->iaj',self.G,vn.reshape(81,self.d,-1),optimize=True).reshape(self.n,-1)
            goff=vp.conj().T @ gv
            # d_g H=[G,H] -> off-diagonal block = -(lambda+ - lambda-)G+-.
            result['gauge_integrand']=float(2*np.sum((A*goff.conj()/denominator).imag,
                                                     dtype=np.longdouble))
        result['seconds']=time.monotonic()-start
        return result

    def endpoint_moments(self):
        if self.G is None:
            return None
        answer=[]
        for h,sites in [(self.Hc,1),(self.F.toarray(),81)]:
            ev,v=linalg.eigh(h,overwrite_a=True,check_finite=False,driver='evd')
            vp=v[:,ev>0].reshape(sites,self.d,-1)
            gv=np.einsum('ab,ibj->iaj',self.G,vp,optimize=True)
            # Reference gamma5 projector has zero trace against traceless color G.
            reference=sites*np.trace(self.G[:self.d//2,:self.d//2])
            answer.append(float((1j*(np.vdot(vp,gv)-reference)).real))
        return dict(coarse=answer[0],fine=answer[1],difference=answer[0]-answer[1])

    def endpoint_curvatures(self, first='x_half', second='y_half'):
        answer=[]
        for h,dx,dy in [(self.Hc,self.variations[first][0],self.variations[second][0]),
                         (self.F.toarray(),self.variations[first][1],self.variations[second][1])]:
            ev,v=linalg.eigh(h,overwrite_a=True,check_finite=False,driver='evd')
            split=np.count_nonzero(ev<0);vn=v[:,:split];vp=v[:,split:]
            X=vp.conj().T @ (dx @ vn);Y=vp.conj().T @ (dy @ vn)
            den=ev[split:,None]-ev[None,:split]
            answer.append(float(-2*np.sum((X*Y.conj()/den**2).imag,dtype=np.longdouble)))
        return dict(coarse=answer[0],fine=answer[1],difference=answer[0]-answer[1])


if __name__=='__main__':
    import json
    from threadpoolctl import threadpool_limits
    U=np.broadcast_to(np.eye(5,dtype=complex),(4,5,5)).copy()
    fine=np.broadcast_to(U,(81,4,5,5)).copy()
    zeros=np.zeros_like(U)
    with threadpool_limits(limits=2):
        comparison=Comparison(U,fine,{'zero':(zeros,np.zeros_like(fine))},'anti5',periodic=True)
        result=comparison.node(.5)
    # For periodic one-site coarse momentum zero, each nonzero fine component
    # contributes sin^2=3/4 and Wilson mass increment 3/2. At s=1/2,
    # the smallest added-mode gap is sqrt((3/4)^2+3/16)=sqrt(3)/2.
    assert abs(result['minimum_gap']-np.sqrt(3)/2)<1e-10,result
    assert abs(result['currents']['zero'])<1e-14,result
    print(json.dumps(result,indent=2))
