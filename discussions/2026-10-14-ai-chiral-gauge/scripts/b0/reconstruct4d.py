"""Craig Appendix A reconstruction for a one-site, four-dimensional SU(5) torus.

Lifted vertices remain distinct. Spatial transport is approximated by products
of polar-normalized overlaps of the prescribed determinant-corrected frames.
Its path-mesh error must be measured; it is not an exact ODE solution.
"""
import itertools
import time
from functools import lru_cache

import numpy as np
from numpy.polynomial.legendre import leggauss

SITE_INDICES = np.array(list(itertools.product(range(3), repeat=4)), dtype=int)
SITES = (SITE_INDICES - 1) / 3
RADIX = np.array([343, 49, 7, 1])


def polar(a):
    u, _, vh = np.linalg.svd(a, full_matrices=False)
    return u @ vh


def special(a):
    v = polar(a)
    return v * np.exp(-1j * np.angle(np.linalg.det(v))[..., None, None] / 5)


def invsqrt(a):
    e, v = np.linalg.eigh((a + a.conj().T) / 2)
    if e.min() <= 0:
        raise ValueError('nonpositive frame Gram matrix')
    return (v / np.sqrt(e)) @ v.conj().T


@lru_cache(maxsize=65536)
def kappa(t, nodes=96):
    # Integrate each polynomial piece of the triple-box convolution separately.
    # Subtract the peak exponent 64 before normalizing the narrow bump.
    t = abs(t)
    if t >= 1.625:
        return 0.0
    q, w = leggauss(nodes)
    delta = .125
    def beta(x):
        return np.exp(64 - 1 / (delta * delta - x * x))
    norm = delta * np.dot(w, beta(delta * q))
    breaks = sorted(set([-delta, delta] +
                        [t - x for x in [-1.5, -.5, .5, 1.5]
                         if -delta < t - x < delta]))
    answer = 0.0
    for lo, hi in zip(breaks, breaks[1:]):
        u = (lo + hi) / 2 + (hi - lo) * q / 2
        x = abs(t - u)
        box3 = np.where(x < .5, .75 - x*x,
                        np.where(x < 1.5, .5 * (1.5-x)**2, 0))
        answer += (hi-lo) / 2 * np.dot(w, beta(u) * box3) / norm
    return float(answer)


class Reconstruction:
    def __init__(self, original, weight_nodes=96, projector_tol=2e-13):
        self.U = np.asarray(original, complex)
        if self.U.shape != (4, 5, 5):
            raise ValueError('expected four original fundamental SU(5) links')
        if max(np.linalg.norm(u.conj().T @ u - np.eye(5)) for u in self.U) > 1e-10:
            raise ValueError('input links are not unitary')
        self.nodes = weight_nodes
        self.tol = projector_tol
        self.frames = {}
        self.metrics = dict(frame_count=0, max_projector_residual=0.,
                            max_unselected_norm_bound=0., min_selected_eigenvalue=1.,
                            max_selected_eigenvalue=1., max_weight_error=0.,
                            max_frame_orthogonality=0., min_phase_real=1.,
                            min_overlap_singular_value=1., max_iterations=0)
        displacements = np.array(list(itertools.product(range(-3, 4), repeat=4)))
        powers = np.array([[np.linalg.matrix_power(u, int(k)) for k in range(-3, 4)]
                           for u in self.U])
        m = np.zeros((len(displacements), 5, 5), complex)
        for order in itertools.permutations(range(4)):
            p = np.broadcast_to(np.eye(5), m.shape).copy()
            for mu in order:
                p = p @ powers[mu, displacements[:, mu] + 3]
            m += p / 24
        singular = np.linalg.svd(m, compute_uv=False)
        self.metrics['min_short_average_singular_value'] = float(singular.min())
        if singular.min() < .5:
            raise ValueError('short-path polar normalization is unsafe')
        normalized = polar(m)
        phase = np.angle(np.linalg.det(normalized))
        self.metrics['max_short_determinant_phase'] = float(np.max(abs(phase)))
        if np.max(abs(phase)) > .5:
            raise ValueError('short-path determinant left near-one branch')
        self.short = normalized * np.exp(-1j*phase[:, None, None]/5)
        self._short_symmetry = float(np.max(abs(self.short -
                                               self.short[::-1].conj().transpose(0, 2, 1))))
        if self._short_symmetry > 2e-12:
            raise ValueError('short-transport reversal failed')

    def frame(self, y):
        y = np.asarray(y, float)
        shift = np.floor(y + .5 + 1e-12).astype(int)
        z = y - shift
        key = tuple(np.round(z, 12))
        if key not in self.frames:
            options = [list(range(int(np.ceil(t-1.625)), int(np.floor(t+1.625))+1))
                       for t in z]
            labels = np.array(list(itertools.product(*options)), int)
            weights = np.ones(len(labels))
            for mu in range(4):
                weights *= np.array([kappa(round(float(z[mu]-i), 12), self.nodes)
                                     for i in labels[:, mu]])
            active = weights > 1e-28
            labels, weights = labels[active], weights[active]
            weight_error = abs(weights.sum()-1)
            if weight_error > 2e-11:
                raise ValueError(f'partition of unity error {weight_error}')
            phi = np.sqrt(weights)
            disp = labels[None, :, :] - labels[:, None, :]
            u = self.short[(disp+3) @ RADIX]
            K = (phi[:, None, None, None] * u * phi[None, :, None, None])
            K = K.transpose(0, 2, 1, 3).reshape(len(labels)*5, -1)
            W = (phi[:, None, None] * self.short[(-labels+3) @ RADIX]).reshape(-1, 5)
            Q = W @ invsqrt(W.conj().T @ W)
            for iteration in range(1, 31):
                Z = K @ Q
                Q = Z @ invsqrt(Z.conj().T @ Z)
                KQ = K @ Q
                A = Q.conj().T @ KQ
                residual = np.linalg.norm(KQ-Q @ A)
                if residual < self.tol:
                    break
            else:
                raise ValueError(f'fiber subspace failed to converge: {residual}')
            ev = np.linalg.eigvalsh(A)
            # ||K-Q A Q†||_F bounds every unwanted eigenvalue in modulus.
            # Use the explicit residual matrix to avoid cancellation of norms.
            rest = np.linalg.norm(K-(Q @ A) @ Q.conj().T)
            if ev.min() < .75 or ev.max() > 1.25 or rest > .25:
                raise ValueError(f'geometric spectral clusters not separated: {ev}, {rest}')
            QB = Q.reshape(-1, 5, 5)
            coords = np.einsum('icb,i,ijcd->jbd', QB.conj(), phi, u, optimize=True)
            coords = polar(coords)
            anchor = polar(Q.conj().T @ W)
            transitions = anchor.conj().T @ coords
            r = np.dot(weights, np.linalg.det(transitions))
            if abs(r-1) > .4:
                raise ValueError(f'determinant synchronization left near-one branch: {r}')
            C = (Q @ anchor * np.exp(1j*np.angle(r)/5)).reshape(-1, 5, 5)
            orth = np.linalg.norm(C.reshape(-1, 5).conj().T @ C.reshape(-1, 5)-np.eye(5))
            self.frames[key] = (labels, C)
            met = self.metrics
            met['frame_count'] += 1
            for name, value in [('max_projector_residual', residual),
                                ('max_unselected_norm_bound', rest),
                                ('max_weight_error', weight_error),
                                ('max_frame_orthogonality', orth),
                                ('max_iterations', iteration),
                                ('max_selected_eigenvalue', ev.max())]:
                met[name] = max(met[name], float(value))
            met['min_selected_eigenvalue'] = min(met['min_selected_eigenvalue'], float(ev.min()))
            met['min_phase_real'] = min(met['min_phase_real'], float(r.real))
        labels, C = self.frames[key]
        return labels+shift, C

    def overlap(self, previous, following):
        a, A = previous
        b, B = following
        # Match ambient lifted vertex identities; never merge torus copies.
        lookup = {tuple(x): i for i, x in enumerate(a)}
        pairs = [(lookup[tuple(x)], j) for j, x in enumerate(b) if tuple(x) in lookup]
        if not pairs:
            raise ValueError('no common ambient components in transport step')
        ia, ib = np.array(pairs).T
        overlap = np.einsum('icb,icd->bd', B[ib].conj(), A[ia], optimize=True)
        singular = np.linalg.svd(overlap, compute_uv=False)
        self.metrics['min_overlap_singular_value'] = min(
            self.metrics['min_overlap_singular_value'], float(singular.min()))
        if singular.min() < .5:
            raise ValueError('path step too large for safe frame overlap')
        return special(overlap)

    def transport(self, start, end, steps):
        start, end = np.asarray(start), np.asarray(end)
        result = np.eye(5, dtype=complex)
        old = self.frame(start)
        for j in range(1, steps+1):
            new = self.frame(start+(end-start)*(j/steps))
            result = self.overlap(old, new) @ result
            old = new
        return result

    def inherited_coordinates(self, steps):
        # All centered children have parent zero. Integer translates use the
        # translated original frame and identical component matrices.
        return np.array([self.transport(np.zeros(4), y, steps) for y in SITES])

    def sample_fine(self, steps, frozen_inherited=None):
        inherited = (self.inherited_coordinates(steps) if frozen_inherited is None
                     else frozen_inherited)
        links = np.empty((81, 4, 5, 5), complex)
        for ix, (idx, y) in enumerate(zip(SITE_INDICES, SITES)):
            for mu in range(4):
                nxt = idx.copy(); nxt[mu] = (nxt[mu]+1) % 3
                jx = np.ravel_multi_index(tuple(nxt), (3,)*4)
                z = y.copy(); z[mu] += 1/3
                edge = self.transport(y, z, steps)
                links[ix, mu] = inherited[ix].conj().T @ edge.conj().T @ inherited[jx]
        return links, inherited


def link_diagnostics(links):
    ident = np.eye(5)
    unitarity = float(np.max(np.linalg.norm(links.conj().transpose(0, 1, 3, 2) @ links-ident,
                                          axis=(-2, -1))))
    determinant = float(np.max(abs(np.linalg.det(links)-1)))
    plaq = 0.
    for ix, idx in enumerate(SITE_INDICES):
        for mu in range(4):
            for nu in range(mu+1, 4):
                xmu=idx.copy(); xmu[mu]=(xmu[mu]+1)%3
                xnu=idx.copy(); xnu[nu]=(xnu[nu]+1)%3
                im=np.ravel_multi_index(tuple(xmu), (3,)*4)
                inn=np.ravel_multi_index(tuple(xnu), (3,)*4)
                p=links[ix,mu] @ links[im,nu] @ links[inn,mu].conj().T @ links[ix,nu].conj().T
                plaq=max(plaq, float(np.linalg.norm(p-ident, ord=2)))
    return dict(max_link_unitarity=unitarity, max_link_determinant_error=determinant,
                max_plaquette_operator_deviation=plaq)


if __name__ == '__main__':
    import json
    from scipy.linalg import expm
    original = np.array([expm(1j*np.diag(np.array([1,2,3,-2,-4])*(mu+1)*.03))
                         for mu in range(4)])
    start = time.monotonic()
    geom = Reconstruction(original)
    links, _ = geom.sample_fine(2)
    expected = np.broadcast_to(np.eye(5, dtype=complex), links.shape).copy()
    for ix, idx in enumerate(SITE_INDICES):
        for mu in range(4):
            if idx[mu] == 2:
                expected[ix, mu] = original[mu]
    error = float(np.max(abs(links-expected)))
    assert error < 1e-10, error
    print(json.dumps(dict(commuting_seam_gauge_error=error, seconds=time.monotonic()-start,
                          geometry=geom.metrics, links=link_diagnostics(links)), indent=2))
