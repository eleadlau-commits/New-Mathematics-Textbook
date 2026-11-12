# Chapter 32 check: loops around a holomorphic map.
import sympy as sp, numpy as np, cmath, random
x, y = sp.symbols('x y', real=True); z = x + sp.I*y
def closed(fz):
    u, v = sp.re(sp.expand_complex(fz)), sp.im(sp.expand_complex(fz))
    return sp.simplify(sp.diff(v, x) + sp.diff(u, y)) == 0 and sp.simplify(sp.diff(u, x) - sp.diff(v, y)) == 0
print("T1 f dz closed for z^3-2z, exp, 1/z; not for conj:", closed(z**3 - 2*z), closed(sp.exp(z)), closed(1/z), not closed(sp.conjugate(z)))
def cint(f, a=0, r=1.0, n=1, K=4096):
    t = (np.arange(K) + 0.5)/K; zz = a + r*np.exp(2j*np.pi*n*t); dz = 2j*np.pi*n*r*np.exp(2j*np.pi*n*t)/K
    return np.sum(f(zz)*dz)
print("P1 int z^n:", all(abs(cint(lambda s: s**k) - (2j*np.pi if k == -1 else 0)) < 1e-9 for k in range(-5, 6)))
print("P2 int conj z dz = 2 pi i r^2 (r=1.5):", abs(cint(np.conj, r=1.5) - 2j*np.pi*1.5**2) < 1e-9)
res = [(lambda s: 1/(s**2 + 1), 1j, 1/(2j)), (lambda s: np.exp(s)/(s - 0.3), 0.3, np.exp(0.3)), (lambda s: 1/(s*(s - 2)), 0, -0.5)]
print("T4 residues same on radii .1,.3,.6:", all(abs(cint(f, a, r)/(2j*np.pi) - c) < 1e-8 for f, a, c in res for r in (0.1, 0.3, 0.6)))
random.seed(32); ok = True
for f in (np.exp, np.cos, lambda s: 1/(s - 3)):
    for _ in range(10):
        a = complex(random.uniform(-1, 1), random.uniform(-1, 1)); r = random.uniform(0.2, 1.0)
        ok &= abs(cint(lambda s: f(s)/(s - a), a, r)/(2j*np.pi) - f(a)) < 1e-9
        ok &= abs(cint(lambda s: f(s)/(s - a), a, r, n=3)/(2j*np.pi) - 3*f(a)) < 1e-8
print("T5 Cauchy formula (and 3 turns) for exp, cos, 1/(z-3):", ok)
# T3: squashed loops around 0 for exp(z)/z: ellipses with different axes, all give 2 pi i
def ell(f, A, B, K=8192):
    t = (np.arange(K) + 0.5)/K; zz = A*np.cos(2*np.pi*t) + 1j*B*np.sin(2*np.pi*t)
    dz = (-A*np.sin(2*np.pi*t) + 1j*B*np.cos(2*np.pi*t))*2*np.pi/K
    return np.sum(f(zz)*dz)
print("T3 ellipses around 0, exp(z)/z: integral 2 pi i each:", all(abs(ell(lambda s: np.exp(s)/s, A, B) - 2j*np.pi) < 1e-8 for A, B in ((1, 1), (2, .3), (.2, 3))))
print("E1 int exp/(z-1) on |z|=2 = 2 pi i e:", abs(cint(lambda s: np.exp(s)/(s - 1), 0, 2) - 2j*np.pi*np.e) < 1e-8)
print("E4 int dz/(z^2+1) on |z|=2 = 0:", abs(cint(lambda s: 1/(s**2 + 1), 0, 2)) < 1e-9)
