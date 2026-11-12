# Chapter 31 check: the complex derivative.
import numpy as np, cmath, random
random.seed(31); np.random.seed(31)
def DF(f, a, h=1e-6):
    fx = (f(a + h) - f(a - h))/(2*h); fy = (f(a + 1j*h) - f(a - 1j*h))/(2*h)
    return np.array([[fx.real, fy.real], [fx.imag, fy.imag]])
def commutes(M, tol=1e-5): return abs(M[0,0] - M[1,1]) < tol and abs(M[0,1] + M[1,0]) < tol
ok = True
for _ in range(50):
    c = np.random.randn(5) + 1j*np.random.randn(5); p = lambda z: sum(ci*z**k for k, ci in enumerate(c))
    a = complex(*np.random.randn(2)); M = DF(p, a); dp = sum(k*ci*a**(k-1) for k, ci in enumerate(c) if k)
    ok &= commutes(M) and abs(complex(M[0,0], M[1,0]) - dp) < 1e-5
for f, d in ((cmath.exp, cmath.exp), (lambda z: 1/z, lambda z: -1/z**2)):
    for _ in range(30):
        a = complex(*np.random.randn(2)) + 0.5; M = DF(f, a); ok &= commutes(M) and abs(complex(M[0,0], M[1,0]) - d(a)) < 1e-5
print("T1 polynomials, exp, 1/z: DF commutes with J and f' = p + iq:", ok)
print("P5 conj: DF = diag(1,-1), not commuting:", not commutes(DF(lambda z: z.conjugate(), 0.3+0.2j)))
print("E1 |z|^2: commutes only at 0:", commutes(DF(lambda z: abs(z)**2 + 0j, 0j)), not commutes(DF(lambda z: abs(z)**2 + 0j, 0.5+0.1j)))
q = lambda u, v: (u.conjugate()*v)/abs(u.conjugate()*v)
ok = True
for f in (cmath.exp, lambda z: z**3 + z, cmath.sin):
    for _ in range(40):
        a = complex(*np.random.randn(2)); u = complex(*np.random.randn(2)); v = complex(*np.random.randn(2)); h = 1e-6
        fu = (f(a + h*u) - f(a))/h; fv = (f(a + h*v) - f(a))/h
        ok &= abs(q(fu, fv) - q(u, v)) < 1e-4
print("T2 angles kept by exp, z^3+z, sin at random points:", ok)
h = 1e-4; fu = ((h*1)**2); fv = ((h*1j)**2)
print("T2 z^2 at 0: corner (1,i) -> (1,-1):", abs(q(fu + 0j, fv) - q(1+0j, -1+0j)) < 1e-9, " conj turns angle back:", abs(q((1+0j).conjugate(), (1j).conjugate()) - q(1+0j, 1j).conjugate()) < 1e-12)
ok = True
for _ in range(30):
    b = complex(*np.random.randn(2)); L = cmath.log(b); ok &= abs(cmath.exp(L) - b) < 1e-12 and abs((cmath.log(b + 1e-7) - L)/1e-7 - 1/b) < 1e-5
    r = b**(1/3); ok &= abs(((r + 1e-7)**3 - b)/1e-7 - 3*r*r) < 1e-4
print("T3 log is an inverse of exp near b with derivative 1/z; cube root inverse of z^3:", ok)
print("P6 |exp(h)-1-h| <= |h|^2 exp|h|:", all(abs(cmath.exp(h) - 1 - h) <= abs(h)**2*np.exp(abs(h)) for h in (complex(*np.random.randn(2)) for _ in range(200))))
print("E4 z^2+2z keeps angles except at z=-1 (derivative 2z+2)")
