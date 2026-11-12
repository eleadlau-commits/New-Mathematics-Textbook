# Building 0, II.6: normed spaces.
import numpy as np
rng = np.random.default_rng(6); ok = True
xs = np.linspace(0, 1, 20001); dx = xs[1] - xs[0]
sup = lambda f: np.max(np.abs(f))
L1 = lambda f: np.sum(np.abs(f)) * dx
L2 = lambda f: np.sqrt(np.sum(f**2) * dx)
par = lambda n, f, g: n(f + g)**2 + n(f - g)**2 - 2*n(f)**2 - 2*n(g)**2
# P2: sup fails the parallelogram law with 1 and x; L1 fails with the two half indicators; L2 passes
one, x = np.ones_like(xs), xs
ok &= abs(par(sup, one, x) - 1.0) < 1e-9
h1, h2 = (xs < 0.5).astype(float), (xs >= 0.5).astype(float)
ok &= abs(par(L1, h1, h2) - 1.0) < 1e-3
for _ in range(20):
    f = np.polyval(rng.normal(size=5), xs); g = np.polyval(rng.normal(size=5), xs)
    ok &= abs(par(L2, f, g)) < 1e-6 * (L2(f)**2 + L2(g)**2)
# ell^2 passes; ell^1 and ell^inf fail
for _ in range(20):
    a, b = rng.normal(size=50), rng.normal(size=50)
    ok &= abs(par(np.linalg.norm, a, b)) < 1e-9
e1, e2 = np.eye(2)
ok &= par(lambda v: np.sum(np.abs(v)), e1, e2) != 0 and par(lambda v: np.max(np.abs(v)), e1, e2) != 0
# T2 (finite dim): max and euclid on R^n within factors 1 and sqrt n
n = 7
for _ in range(2000):
    v = rng.normal(size=n)
    ok &= np.max(np.abs(v)) <= np.linalg.norm(v) + 1e-12 <= np.sqrt(n) * np.max(np.abs(v)) + 1e-9
# P4 dies in infinite dim: tents of height 1, width 2/k: sup 1, L1 -> 0
for k in (10, 100, 1000):
    tent = np.maximum(0, 1 - k*np.abs(xs - 0.5))
    ok &= abs(sup(tent) - 1) < 1e-6 and L1(tent) < 1.1 / k
# P5: continuous maps with the L2 distance are not complete: steep ramps come near themselves, near the step
ramps = [np.clip((xs - 0.5) * k + 0.5, 0, 1) for k in (10, 100, 1000, 10000)]
ok &= all(L2(ramps[i] - ramps[i+1]) < 0.5 / np.sqrt(10**(i+1)) for i in range(3))
step = (xs >= 0.5).astype(float); ok &= L2(ramps[-1] - step) < 1e-2
# P6: in ell^2 the unit vectors are sqrt2 apart: the closed ball is not compact
E = np.eye(30); ok &= all(abs(np.linalg.norm(E[i] - E[j]) - np.sqrt(2)) < 1e-12 for i in range(30) for j in range(i))
# T3 polarisation recovers the dot product on R^n
for _ in range(20):
    a, b = rng.normal(size=5), rng.normal(size=5)
    pol = (np.linalg.norm(a + b)**2 - np.linalg.norm(a - b)**2) / 4
    ok &= abs(pol - a @ b) < 1e-9
# T4 (Riesz) on R^n with a skew inner product <u,v> = u^T S v: phi = <., y> with y = S^{-1} c
A = rng.normal(size=(5, 5)); S = A @ A.T + 5*np.eye(5); c = rng.normal(size=5)
y = np.linalg.solve(S, c); u = rng.normal(size=5); ok &= abs(c @ u - u @ S @ y) < 1e-9
print("ALL", ok)
