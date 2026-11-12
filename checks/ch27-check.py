# Chapter 27 check: integrable maps.
import sympy as sp, random, math
x = sp.symbols('x', positive=True); n, m = 7, 13
# P3: tent height 1 on [1/2-1/n, 1/2+1/n]: integral 1/n
for N in (3, 10, 50):
    tent = sp.Piecewise((1 - N*sp.Abs(x - sp.Rational(1, 2)), sp.Abs(x - sp.Rational(1, 2)) <= sp.Rational(1, N)), (0, True))
    I = sp.integrate(1 - N*(x - sp.Rational(1,2)), (x, sp.Rational(1,2), sp.Rational(1,2)+sp.Rational(1,N)))*2
    print("P3 tent", N, "integral = 1/N:", sp.simplify(I - sp.Rational(1, N)) == 0)
# P6: f_n = min(x^-1/2, n): int |f_n - f_m| <= 2/n ; int f_n^2 = 1 + 2 log n
for (a, b) in ((2, 5), (7, 13), (10, 100)):
    d = sp.integrate(b - a, (x, 0, sp.Rational(1, b*b))) + sp.integrate(x**sp.Rational(-1, 2) - a, (x, sp.Rational(1, b*b), sp.Rational(1, a*a)))
    print("P6 int|f_%d - f_%d| = %s <= 2/%d:" % (a, b, sp.nsimplify(d), a), d <= sp.Rational(2, a))
for a in (2, 7, 30):
    s = sp.integrate(a*a, (x, 0, sp.Rational(1, a*a))) + sp.integrate(1/x, (x, sp.Rational(1, a*a), 1))
    print("P6 int f_%d^2 = 1 + 2 log %d:" % (a, a), sp.simplify(s - 1 - 2*sp.log(a)) == 0)
# E5: int min(x^-1/2, n) = 2 - 1/n
for a in (2, 7, 30):
    s = sp.integrate(a, (x, 0, sp.Rational(1, a*a))) + sp.integrate(x**sp.Rational(-1, 2), (x, sp.Rational(1, a*a), 1))
    print("E5 int f_%d = 2 - 1/%d:" % (a, a), sp.simplify(s - 2 + sp.Rational(1, a)) == 0)
# P8: s_n comes near itself in I: int |s_n - s_m| = 1/(2n) - 1/(2m) roughly; compute numerically
def s(N, t): return 0.0 if t <= 0.5 else min(1.0, N*(t - 0.5))
G = [i/200000 for i in range(200001)]
def intg(f): return sum(f(t) for t in G)/len(G)
print("P8 int|s_10 - s_100| = %.5f (exact 0.045)" % intg(lambda t: abs(s(10, t) - s(100, t))))
# T2(a): for random polynomials g >= 0 on [0,1], length{g > t} <= (1/t) int g
random.seed(27); ok = True
for _ in range(200):
    c = [random.uniform(-2, 2) for _ in range(5)]
    g = lambda t: abs(sum(ci*t**i for i, ci in enumerate(c)))
    vals = [g(i/4000) for i in range(4001)]; ig = sum(vals)/len(vals); t = random.uniform(0.05, 1.5)
    L = sum(1 for v in vals if v > t)/len(vals)
    ok &= L <= ig/t + 1e-3
print("T2(a) length{g>t} <= int g / t on 200 random polynomials:", ok)
# T5.1 witness: tents of ch20 P9 have integral 1, limit 0; T5.2 witness: int_0^1 min(1/x, n) = 1 + log n
for a in (2, 10, 1000):
    s2 = sp.integrate(a, (x, 0, sp.Rational(1, a))) + sp.integrate(1/x, (x, sp.Rational(1, a), 1))
    print("T5.2 int min(1/x,%d) = 1 + log %d:" % (a, a), sp.simplify(s2 - 1 - sp.log(a)) == 0)
print("T5.1 ch20 tents: integral n * (2/n) / 2 = 1 for n = 5, 50:", all(abs(N*(2/N)/2 - 1) < 1e-12 for N in (5, 50)))
