# Chapter 33 check: rigidity.
import numpy as np, math, random
def coef(f, a, n, r=0.5, K=4096):
    t = (np.arange(K) + 0.5)/K; z = a + r*np.exp(2j*np.pi*t)
    return np.mean(f(z)*(r*np.exp(2j*np.pi*t))**(-n))
ok = True
for f, R in ((np.exp, 10), (lambda s: 1/(1 - s), 1), (np.cos, 10)):
    c = [coef(f, 0, n) for n in range(40)]
    for zz in (0.3, 0.2 + 0.4j, -0.45j):
        ok &= abs(sum(c[n]*zz**n for n in range(40)) - f(zz)) < 1e-8
print("T1 the list from the circle integral gives back exp, 1/(1-z), cos inside the disc:", ok)
print("T2 c_n = f^(n)(0)/n! for exp:", all(abs(coef(np.exp, 0, n, r=1.0) - 1/math.factorial(n)) < 1e-13 for n in range(15)))
c = [coef(lambda s: np.sin(s)**2*s, 0, n) for n in range(8)]
print("T5 sin(z)^2 z: first non-zero c_n at n = 3:", [n for n in range(8) if abs(c[n]) > 1e-10][0] == 3)
ok = True
for f in (np.exp, np.cos, lambda s: s**5 - 2*s):
    for r in (0.5, 1, 2):
        t = (np.arange(2048) + 0.5)/2048; B = np.abs(f(r*np.exp(2j*np.pi*t))).max()
        ok &= all(abs(coef(f, 0, n, r)) <= B/r**n + 1e-9 for n in range(12))
print("T6 Cauchy bound:", ok)
random.seed(33); ok = True
g = np.linspace(-1, 1, 201); X, Y = np.meshgrid(g, g); Z = X + 1j*Y; inside = np.abs(Z) <= 1
for _ in range(50):
    cs = [complex(random.gauss(0, 1), random.gauss(0, 1)) for _ in range(5)]
    p = lambda s: sum(ci*s**k for k, ci in enumerate(cs))
    t = np.linspace(0, 1, 40001); edge = np.abs(p(np.exp(2j*np.pi*t))).max()
    ok &= np.abs(p(Z[inside])).max() <= edge*(1 + 1e-6)
print("T8 largest |p| on the closed disc is on the edge (50 random polynomials):", ok)
c = [coef(lambda s: 1/(1 + s*s), 0, n, r=0.95) for n in range(60)]
print("P2 1/(1+z^2): sums settle at z=0.9, grow at z=1.1:", abs(sum(c[n]*0.9**n for n in range(60)) - 1/(1 + 0.81)) < 0.01, abs(c[58]*1.1**58) > 1)
u = lambda x, y: np.real(np.exp(x + 1j*y)); h = 1e-3; x0, y0 = 0.3, -0.2
lap = (u(x0 + h, y0) + u(x0 - h, y0) + u(x0, y0 + h) + u(x0, y0 - h) - 4*u(x0, y0))/h**2
t = (np.arange(4096) + 0.5)/4096; avg = np.mean(u(x0 + 0.4*np.cos(2*np.pi*t), y0 + 0.4*np.sin(2*np.pi*t)))
print("P3 Re exp: Laplacian ~ 0 and circle average = centre:", abs(lap) < 1e-4, abs(avg - u(x0, y0)) < 1e-12)
print("E2 sin(z)-z: first c_n at n=3:", [n for n in range(8) if abs(coef(lambda s: np.sin(s) - s, 0, n)) > 1e-10][0] == 3)
print("E4 max |z^2+1| on |z|<=1 is 2 at z = +-1:", abs(np.abs(Z[inside]**2 + 1).max() - 2) < 1e-9)
