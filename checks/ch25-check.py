# Chapter 25 (design) check: inverting a map near a point.
import math, random
random.seed(25)
# P2: x + 2 x^2 sin(1/x) has slope 1 at 0, shares the tangent bag of x, and is one-to-one on no interval around 0
f = lambda x: x + 2 * x * x * math.sin(1 / x) if x != 0 else 0.0
fp = lambda x: 1 + 4 * x * math.sin(1 / x) - 2 * math.cos(1 / x)
print("P2 slope at 0 (difference quotients):", ["%.4f" % (f(h) / h) for h in (1e-2, 1e-4, 1e-6)])
print("P2 slope is -1 at 1/(2 pi m), +3 at 1/((2m+1) pi):", all(abs(fp(1 / (2 * math.pi * m)) + 1) < 1e-2 and abs(fp(1 / ((2 * m + 1) * math.pi)) - 3) < 1e-2 for m in range(50, 2000, 37)))
ok = True
for m in (10, 100, 1000, 10000):       # a place where f falls, inside 0 < x < 1/m: two points with the same value exist
    x0 = 1 / (2 * math.pi * m); ok &= f(x0 + 1e-3 * x0 / m) < f(x0)
print("P2 f falls somewhere in every 0 < x < 1/m:", ok)
# P3: x^3 inverse has no slope at 0; x^2 is not one-to-one near 0
print("P3 cube root difference quotients at 0 grow:", ["%.0f" % ((h ** (1 / 3)) / h) for h in (1e-3, 1e-6, 1e-9)])
# T3: random smooth maps of R^2 with invertible tangent at a; solve F(x) = y by the contraction x -> x - L^{-1}(F(x) - y)
def make():
    c = [random.uniform(-1, 1) for _ in range(12)]
    def F(x, y):
        return (c[0] * x + c[1] * y + c[2] * math.sin(x * y) + c[3] * x * x + c[4] * math.cos(y),
                c[5] * x + c[6] * y + c[7] * math.sin(x + y) + c[8] * y * y + c[9] * math.exp(-x * x))
    return F
def jac(F, x, y, e=1e-6):
    a = F(x + e, y); b = F(x - e, y); c = F(x, y + e); d = F(x, y - e)
    return [[(a[0] - b[0]) / (2 * e), (c[0] - d[0]) / (2 * e)], [(a[1] - b[1]) / (2 * e), (c[1] - d[1]) / (2 * e)]]
def inv(m):
    D = m[0][0] * m[1][1] - m[0][1] * m[1][0]
    return [[m[1][1] / D, -m[0][1] / D], [-m[1][0] / D, m[0][0] / D]], D
okT3 = okDG = True; n = 0; worst_steps = 0
for _ in range(300):
    F = make(); a = (random.uniform(-1, 1), random.uniform(-1, 1)); J = jac(F, *a); Li, D = inv(J)
    if abs(D) < 0.3: continue
    n += 1; b = F(*a)
    def G(y, tol=1e-13):
        x = a; steps = 0
        while steps < 500:
            v = F(*x); r = (v[0] - y[0], v[1] - y[1])
            if abs(r[0]) + abs(r[1]) < tol: break
            x = (x[0] - Li[0][0] * r[0] - Li[0][1] * r[1], x[1] - Li[1][0] * r[0] - Li[1][1] * r[1]); steps += 1
        return x, steps
    d = 1e-3
    y = (b[0] + random.uniform(-d, d), b[1] + random.uniform(-d, d)); x, st = G(y); worst_steps = max(worst_steps, st)
    v = F(*x); okT3 &= abs(v[0] - y[0]) + abs(v[1] - y[1]) < 1e-11 and abs(x[0] - a[0]) + abs(x[1] - a[1]) < 0.1
    e = 1e-5   # tangent of the inverse at b, by difference quotients, against the inverse of the tangent
    gx1, _ = G((b[0] + e, b[1])); gx0, _ = G((b[0] - e, b[1])); gy1, _ = G((b[0], b[1] + e)); gy0, _ = G((b[0], b[1] - e))
    DG = [[(gx1[0] - gx0[0]) / (2 * e), (gy1[0] - gy0[0]) / (2 * e)], [(gx1[1] - gx0[1]) / (2 * e), (gy1[1] - gy0[1]) / (2 * e)]]
    okDG &= all(abs(DG[i][j] - Li[i][j]) < 1e-4 * (1 + abs(Li[i][j])) for i in range(2) for j in range(2))
print("T3 contraction solves F(x) = y near F(a) (", n, "maps, at most", worst_steps, "steps ):", okT3)
print("T3 tangent of the inverse = inverse of the tangent:", okDG)
# T4: the circle x^2 + y^2 = 1 as a graph near (0.6, 0.8); slope -x/y
g = lambda x: math.sqrt(1 - x * x)
print("T4 slope of the graph at 0.6:", "%.6f" % ((g(0.6 + 1e-6) - g(0.6 - 1e-6)) / 2e-6), " -x/y =", -0.6 / 0.8)
# R: exp on C has det e^{2x} != 0 everywhere and is not one-to-one
E = lambda x, y: (math.exp(x) * math.cos(y), math.exp(x) * math.sin(y))
print("R exp: same value at y and y + 2 pi:", all(abs(u - v) < 1e-12 for u, v in zip(E(0.3, 0.5), E(0.3, 0.5 + 2 * math.pi))), "; det at (0.3, 0.5) =", "%.4f" % inv(jac(E, 0.3, 0.5))[1], " e^{0.6} =", "%.4f" % math.exp(0.6))
# T2: contraction on a box has one fixed point: x -> cos(x)/2 on -1 <= x <= 1
x = 1.0
for _ in range(60): x = math.cos(x) / 2
print("T2 fixed point of cos(x)/2:", "%.12f" % x, " check:", abs(x - math.cos(x) / 2) < 1e-14)
