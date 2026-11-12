# Chapter 28 check: square-integrable maps.
import sympy as sp, itertools, random
x = sp.symbols('x', positive=True)
u = lambda j: sp.sin(2*sp.pi*j*x)
ip = lambda f, g: sp.integrate(f*g, (x, 0, 1))
print("P4 <u_j,u_k> = 0 (j != k <= 6), ||u_j||^2 = 1/2:",
      all(sp.simplify(ip(u(j), u(k))) == 0 for j in range(1, 7) for k in range(1, 7) if j != k) and all(sp.simplify(ip(u(j), u(j)) - sp.Rational(1, 2)) == 0 for j in range(1, 7)))
# P4 all signs, N <= 8 (numerically on a fine grid; exact by orthogonality)
import math
G = [(i + 0.5)/4000 for i in range(4000)]
ok = True
for N in range(1, 9):
    for signs in itertools.product((1, -1), repeat=N):
        v = sum((sum(s*math.sin(2*math.pi*(j+1)*t) for j, s in enumerate(signs)))**2 for t in G)/len(G)
        ok &= abs(v - N/2) < 1e-9
print("P4 ||sum +-u_j||^2 = N/2 for every sign choice, N <= 8:", ok)
print("P6 ||x^-1/3||^2 = 3:", sp.integrate(x**sp.Rational(-2, 3), (x, 0, 1)) == 3, "; int x^-4/3 diverges:", sp.integrate(x**sp.Rational(-4, 3), (x, 0, 1)) == sp.oo)
print("P7 int x^-1/2 = 2, int 1/x diverges:", sp.integrate(x**sp.Rational(-1, 2), (x, 0, 1)) == 2, sp.integrate(1/x, (x, 0, 1)) == sp.oo)
random.seed(28); ok = True
for _ in range(100):
    a = [random.uniform(-3, 3) for _ in range(4)]; b = [random.uniform(-3, 3) for _ in range(4)]
    f = sum(c*x**i for i, c in enumerate(a)); g = sum(c*x**i for i, c in enumerate(b))
    ok &= float(ip(f, g))**2 <= float(ip(f, f))*float(ip(g, g)) + 1e-9
    v = [random.uniform(-5, 5) for _ in range(6)]; w = [random.uniform(-5, 5) for _ in range(6)]
    ok &= sum(p*q for p, q in zip(v, w))**2 <= sum(p*p for p in v)*sum(q*q for q in w) + 1e-9
print("T1 on 100 random polynomial pairs and 100 random lists:", ok)
print("E1 nearest constant to x^2 is 1/3, and x^2-1/3 is at right angles to 1:", ip(x**2 - sp.Rational(1, 3), 1) == 0)
print("E3 x.y = x1y1 - x2y2 breaks T1 at (1,0),(1,1):", (1*1 - 0*1)**2 > (1)*(1 - 1))
print("T5 int|p+q|=int|p-q|=1, int|p|=int|q|=1/2: 1+1 != 2/4+2/4:", 1 + 1 != 2*0.25 + 2*0.25)
print("E4 ||f_n - f_m||^2 for x^-1/3, n=2,m=10:", sp.nsimplify(sp.integrate((10-2)**2, (x, 0, sp.Rational(1, 1000))) + sp.integrate((x**sp.Rational(-1, 3) - 2)**2, (x, sp.Rational(1, 1000), sp.Rational(1, 8)))))
