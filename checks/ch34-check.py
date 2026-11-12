# Chapter 34 check: poles and valuations.
import numpy as np, random, math
def lc(f, a, n, r=0.3, K=4096):
    t = (np.arange(K) + 0.5)/K; e = np.exp(2j*np.pi*t)
    return np.mean(f(a + r*e)*(r*e)**(-n))
def ordr(c, tol=1e-9):
    for n, v in c: 
        if abs(v) > tol: return n
random.seed(34); ok = True
for _ in range(30):
    j, k = random.randint(0, 4), random.randint(0, 4)
    f = lambda s, j=j: s**j*np.exp(s); g = lambda s, k=k: s**k*(2 + np.sin(s))
    of = ordr([(n, lc(f, 0, n)) for n in range(8)]); og = ordr([(n, lc(g, 0, n)) for n in range(8)])
    ofg = ordr([(n, lc(lambda s: f(s)*g(s), 0, n)) for n in range(12)])
    osum = ordr([(n, lc(lambda s: f(s) + g(s), 0, n)) for n in range(8)])
    ok &= of == j and og == k and ofg == j + k and (osum == min(j, k) if j != k else osum >= j)
print("P1 ord(fg)=ord f+ord g, ord(f+g)>=min, = when different (30 cases):", ok)
print("P2 1/(2+sin z) is a germ (no negative terms):", all(abs(lc(lambda s: 1/(2 + np.sin(s)), 0, -n)) < 1e-12 for n in range(1, 6)))
print("P6 exp(1/z): coefficients at -n are 1/n! for n=0..10:", all(abs(lc(lambda s: np.exp(1/s), 0, -n, r=1.0) - 1/math.factorial(n)) < 1e-10 for n in range(11)))
f = lambda s: 1/(s**2*(s - 1))
res0, res1 = lc(f, 0, -1, r=0.3), lc(f, 1, -1, r=0.3)
print("T1/E2 residues of 1/(z^2(z-1)): at 0 =", np.round(res0, 10), "at 1 =", np.round(res1, 10), " sum 0:", abs(res0 + res1) < 1e-10)
print("E3 cot has residue 1 at k pi:", all(abs(lc(lambda s: np.cos(s)/np.sin(s), k*np.pi, -1, r=0.5) - 1) < 1e-10 for k in (-2, 0, 1, 3)))
print("T2 sin(z)/z has no negative terms:", all(abs(lc(lambda s: np.sin(s)/s, 0, -n)) < 1e-12 for n in range(1, 6)))
def cint(f, R, K=8192):
    t = (np.arange(K) + 0.5)/K; z = R*np.exp(2j*np.pi*t); return np.sum(f(z)*2j*np.pi*z/K)
ok = True
for f, poles in ((lambda s: 1/(s**2 + 1), [1j, -1j]), (lambda s: np.exp(s)/(s*(s - 2)), [0, 2]), (lambda s: 1/((s - 0.5)**3*(s + 1.5)), [0.5, -1.5])):
    for R in (0.7, 1.2, 1.8, 3.0):
        inside = [p for p in poles if abs(p) < R]
        ok &= abs(cint(f, R) - 2j*np.pi*sum(lc(f, p, -1, r=0.2) for p in inside)) < 1e-7
print("T3 residues add (3 maps, 4 circles):", ok)
ok = True
for _ in range(30):
    cs = [complex(random.gauss(0, 1), random.gauss(0, 1)) for _ in range(6)]
    p = np.polynomial.Polynomial(cs); dp = p.deriv(); R = random.uniform(0.5, 2.0)
    roots = p.roots()
    if min(abs(abs(roots) - R)) < 0.05: continue
    count = cint(lambda s: dp(s)/p(s), R)/(2j*np.pi)
    ok &= abs(count - sum(abs(roots) < R)) < 1e-6
print("T4 (1/2 pi i) int f'/f counts zeros inside, random polynomials:", ok)
p = np.polynomial.Polynomial([1, 3, 0, 0, 0, 1])
print("E4 z^5+3z+1: zeros inside |z|=1:", round((cint(lambda s: p.deriv()(s)/p(s), 1.0)/(2j*np.pi)).real), "(roots:", sum(abs(p.roots()) < 1), ")")
c = lambda f: ordr([(n, lc(f, 0, n, r=0.5)) for n in range(-4, 8)])
print("E1 ord_0 of sin^3, 1-cos, z/sin^2:", c(lambda s: np.sin(s)**3), c(lambda s: 1 - np.cos(s)), c(lambda s: s/np.sin(s)**2))
