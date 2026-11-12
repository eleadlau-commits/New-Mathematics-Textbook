# Chapter 37: the torus and the map selected by its pole.
import numpy as np, mpmath as mp
ok = True
w1, w2 = 1.0 + 0j, 0.3 + 1.1j
N = 160
I, J = np.meshgrid(np.arange(-N, N+1), np.arange(-N, N+1))
L = (I*w1 + J*w2).ravel(); L = L[L != 0]
G4 = np.sum(L**-4.0); G6 = np.sum(L**-6.0)
g2, g3 = 60*G4, 140*G6
def wp(z):  return 1/z**2 + np.sum(1/(z - L)**2 - 1/L**2)
def wpd(z): return -2/z**3 - 2*np.sum(1/(z - L)**3)
rng = np.random.default_rng(3)
errs = []
for _ in range(6):
    z = complex(rng.uniform(0.1, 0.9)) * w1 + complex(rng.uniform(0.1, 0.9)) * w2
    # T4: the cubic
    lhs, rhs = wpd(z)**2, 4*wp(z)**3 - g2*wp(z) - g3
    errs.append(abs(lhs - rhs) / abs(lhs))
    # periodicity of wp' (truncation hurts wp' least)
    errs.append(abs(wpd(z + w1) - wpd(z)) / abs(wpd(z)))
    errs.append(abs(wp(-z) - wp(z)) / abs(wp(z)))
print("max relative error (T4, period, even):", max(errs)); ok &= max(errs) < 1e-3
# T5: e1, e2, e3 are the three roots and they differ (Delta != 0)
e = [wp(w1/2), wp(w2/2), wp((w1+w2)/2)]
roots = np.roots([4, 0, -g2, -g3])
ok &= all(min(abs(r - ei) for r in roots) < 1e-3*abs(ei) + 1e-3 for ei in e)
ok &= abs(g2**3 - 27*g3**2) > 1e-3
print("half periods are the roots, distinct:", ok)
# T2 / T3 on an elliptic map built from wp: f = wp - c has 2 zeros per bag, sum in Lambda.
# Count zeros of wp - c in the cell by the argument principle along the edge of a shifted cell.
c = 0.7 + 0.2j
s0 = -0.37*w1 - 0.41*w2       # shift so no zero or pole on the edge
def edge(t):
    if t < 1:  return s0 + t*w1, w1
    if t < 2:  return s0 + w1 + (t-1)*w2, w2
    if t < 3:  return s0 + w1 + w2 - (t-2)*w1, -w1
    return s0 + w2 - (t-3)*w2, -w2
M = 4000; tot = 0; tot_z = 0; res = 0
for k in range(4*M):
    t = (k + 0.5) / M
    z, dz = edge(t)
    fz = wp(z) - c; f1 = wpd(z)
    tot += f1/fz * dz / M
    tot_z += z * f1/fz * dz / M
    res += (wp(z) * dz / M)          # residues of wp in the cell: 0 (T2)
nz = tot / (2j*np.pi); sz = tot_z / (2j*np.pi)
print("zeros minus poles in a cell:", nz, " integral of wp on edge:", abs(res))
ok &= abs(nz) < 1e-2 and abs(res) < 1e-2
# sum of zeros minus sum of poles lies in Lambda: solve sz = m w1 + n w2
A = np.array([[w1.real, w2.real], [w1.imag, w2.imag]]); mn = np.linalg.solve(A, [sz.real, sz.imag])
print("sum zeros - sum poles in lattice coords:", mn); ok &= np.allclose(mn, np.round(mn), atol=1e-2)
print("ALL", ok)
