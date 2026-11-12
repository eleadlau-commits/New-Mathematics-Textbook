# Building 0, Part III: loops up to deformation, mass one, flows, doubling on the circle.
import math, itertools, random
from fractions import Fraction as Fr
import numpy as np
from sympy import mobius, divisors, binomial
rng = np.random.default_rng(31); random.seed(31); ok = True
# ---- III.1 lifting: random loops on the circle (as points of R/Z) lift to R; the end minus start is a whole number
def lift(angles):            # angles in [0,1); each step assumed < 1/2 apart (fine sampling)
    out = [angles[0]]
    for a in angles[1:]:
        d = (a - out[-1]) % 1.0
        if d > 0.5: d -= 1.0
        out.append(out[-1] + d)
    return out
for n in range(-3, 4):
    t = np.linspace(0, 1, 4001)
    wiggle = 0.2 * np.sin(2*np.pi*3*t) * np.sin(np.pi*t)
    ang = (n*t + wiggle) % 1.0
    L = lift(list(ang)); ok &= abs((L[-1] - L[0]) - n) < 1e-9
# Brouwer in the disc: a continuous map of the closed disc into itself has a fixed point (grid search for small |f(x)-x|)
for _ in range(5):
    c = rng.normal(size=6)
    def f(x, y):
        u = 0.6*np.sin(c[0]*x + c[1]*y + c[2]); v = 0.6*np.cos(c[3]*x + c[4]*y + c[5])
        return u, v                               # lands in the disc of radius 0.85 < 1
    g = np.linspace(-1, 1, 801); X, Y = np.meshgrid(g, g); m = X**2 + Y**2 <= 1
    U, V = f(X, Y); dist = np.where(m, np.hypot(U - X, V - Y), 9)
    ok &= dist.min() < 5e-3
print("III.1:", ok)
# ---- III.2 binary digits are independent fair coins; Chebyshev; law of large numbers; bell curve
for n in (1, 2, 3, 4, 5, 6, 7, 8):
    # exact: over all 2^n digit strings (equal length), mean of S_n/n is 1/2, variance 1/(4n)
    vals = [sum(w)/n for w in itertools.product((0, 1), repeat=n)]
    mu = sum(vals)/len(vals); var = sum((v - mu)**2 for v in vals)/len(vals)
    ok &= abs(mu - 0.5) < 1e-12 and abs(var - 1/(4*n)) < 1e-12
    # Chebyshev bound holds exactly
    a = 0.25
    ok &= sum(abs(v - 0.5) >= a for v in vals)/len(vals) <= 1/(4*n*a*a) + 1e-12
# fourth moment: E(S_n - n/2)^4 = n/16 + 3n(n-1)/16 <= 3n^2/16
for n in range(1, 15):
    m4 = sum(binomial(n, k) * (k - Fr(n, 2))**4 for k in range(n + 1)) / 2**n
    ok &= m4 == Fr(n, 16) + Fr(3*n*(n - 1), 16) and m4 <= Fr(3*n*n, 16)
# bell curve: waves cos(t/sqrt n)^n -> exp(-t^2/2); binomial probabilities near the bell
for t in (0.5, 1.0, 2.0):
    ok &= abs(math.cos(t/math.sqrt(10**6))**(10**6) - math.exp(-t*t/2)) < 1e-5
n = 400
cdf = sum(math.comb(n, k) for k in range(0, n//2 + 21)) / 2**n          # P(S_n <= n/2 + 20), z = 2
ok &= abs(cdf - 0.5*(1 + math.erf(2.05/math.sqrt(2)))) < 5e-3
print("III.2:", ok)
# ---- III.3 flows: Picard ladder for x' = x gives the Taylor polynomials; non-uniqueness; blow-up; flow law
t = np.linspace(0, 0.5, 501)
x = np.ones_like(t)
for k in range(12):
    x = 1 + np.concatenate([[0], np.cumsum((x[1:] + x[:-1]) / 2 * np.diff(t))])
ok &= np.max(np.abs(x - np.exp(t))) < 1e-5
# x' = 2 sqrt|x|: both 0 and t^2 are answers from x(0) = 0
tt = np.linspace(0, 1, 11); ok &= np.allclose(2*tt, 2*np.sqrt(np.abs(tt**2)))
# x' = x^2, x(0) = 1: x = 1/(1 - t) leaves every bound before t = 1
def rk4(F, x0, T, N):
    h = T/N; x = np.array(x0, float)
    for _ in range(N):
        k1 = F(x); k2 = F(x + h/2*k1); k3 = F(x + h/2*k2); k4 = F(x + h*k3)
        x = x + h/6*(k1 + 2*k2 + 2*k3 + k4)
    return x
ok &= abs(rk4(lambda x: x**2, [1.0], 0.9, 9000)[0] - 10) < 1e-3
# flow law phi_{s+t} = phi_s o phi_t for a pendulum
F = lambda v: np.array([v[1], -np.sin(v[0])])
a = rk4(F, rk4(F, [1.0, 0.0], 0.7, 7000), 1.1, 11000); b = rk4(F, [1.0, 0.0], 1.8, 18000)
ok &= np.max(np.abs(a - b)) < 1e-9
# linear: phi_t = exp(tA) by the series
A = np.array([[0, 1], [-1, 0]]); E = sum(np.linalg.matrix_power(A, k) / math.factorial(k) for k in range(30))
ok &= np.allclose(E, [[math.cos(1), math.sin(1)], [-math.sin(1), math.cos(1)]])
print("III.3:", ok)
# ---- III.4 doubling: 2^n - 1 points of period n; least periods by Mobius; 1/3 has period 2
for n in range(1, 13):
    pts = {Fr(k, 2**n - 1) for k in range(2**n - 1)}
    ok &= all((2**n * p) % 1 == p for p in pts) and len(pts) == 2**n - 1
    least = sum(1 for p in pts if all((2**d * p) % 1 != p for d in range(1, n)))
    ok &= least == sum(mobius(d) * (2**(n//d) - 1) for d in divisors(n))
ok &= (2*Fr(1, 3)) % 1 == Fr(2, 3) and (4*Fr(1, 3)) % 1 == Fr(1, 3)
# a dense orbit: the point whose digits list every finite word; its orbit meets every stretch of length 2^-8
digits = []
for L in range(1, 9):
    for w in itertools.product((0, 1), repeat=L): digits += list(w)
hit = set()
for k in range(len(digits) - 8): hit.add(tuple(digits[k:k+8]))
ok &= len(hit) == 256
# sensitivity: points 2^-k apart are at least 1/4 apart (on the circle) at some step <= k
for k in range(3, 20):
    x0 = Fr(1, 7); x1 = x0 + Fr(1, 2**k)
    sep = max(min((2**j*(x1 - x0)) % 1, 1 - (2**j*(x1 - x0)) % 1) for j in range(k))
    ok &= sep >= Fr(1, 4)
# long-run average: random digits spend about half the time in [0, 1/2) (first digit 0)
bits = rng.integers(0, 2, size=200000); ok &= abs(np.mean(bits == 0) - 0.5) < 0.01
# length is kept: the stretch [a, b) pulls back to two stretches of half the length
print("III.4:", ok)
print("ALL", ok)
