# Checks for Chapter 22 (the exponential, selected). Numerical illustrations.
import cmath, math, random
random.seed(11)
def E(c, x, N=80):   # the one construction of T2: the series of (c x)^n / n!
    s, t = 0j, 1+0j
    for n in range(N):
        s += t; t = t*c*x/(n+1)
    return s
h = 1e-6
pts = [(complex(random.uniform(-1, 1), random.uniform(-1, 1)), random.uniform(-2, 2)) for _ in range(200)]
print("D1 the series meets the rule f' = c f, f(0) = 1 (200 random c, x):",
      all(abs((E(c, x+h) - E(c, x-h))/(2*h) - c*E(c, x)) < 1e-6 for c, x in pts) and all(E(c, 0) == 1 for c, _ in pts))
print("T1 step: f(x) f(-x) = 1:", all(abs(E(c, x)*E(c, -x) - 1) < 1e-9 for c, x in pts))
print("T3 f(s+t) = f(s) f(t):", all(abs(E(c, x+y) - E(c, x)*E(c, y)) < 1e-9 for (c, x), (_, y) in zip(pts, pts[1:])))
print("T4 E_c(x) = E_{cx}(1), and E_z(1) E_w(1) = E_{z+w}(1):", all(abs(E(c, x) - E(c*x, 1)) < 1e-9 for c, x in pts),
      all(abs(E(z, 1)*E(w, 1) - E(z+w, 1)) < 1e-9 for (z, _), (w, _) in zip(pts, pts[1:])))
print("T5 |E_i(t)| = 1:", all(abs(abs(E(1j, t)) - 1) < 1e-9 for t in [random.uniform(-10, 10) for _ in range(200)]))
# R1: a second construction gives the same map: (1 + x/n)^n
print("R1 (1 + x/n)^n at x = 1.7, n = 10^3, 10^6:", [round((1 + 1.7/n)**n, 6) for n in (10**3, 10**6)], "| series:", round(E(1, 1.7).real, 6))
# R2: the rule f' = f without f(0) = 1 has many solutions: c e^x
print("R2 without f(0) = 1: 3 e^x also has f' = f:", abs((3*math.exp(1+h) - 3*math.exp(1-h))/(2*h) - 3*math.exp(1)) < 1e-5)
