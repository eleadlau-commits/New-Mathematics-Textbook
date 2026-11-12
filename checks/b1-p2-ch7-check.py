# Building 1, II.7: divisibility in any ring.
import random, math, itertools, sympy as sp
random.seed(7); ok = True
# Dies in Z[sqrt-5]: no element of size 2 or 3; 2,3,1+-sqrt-5 irreducible, not associates
N = lambda a, b: a*a + 5*b*b
sizes = {N(a, b) for a in range(-10, 11) for b in range(-5, 6)}
ok &= 2 not in sizes and 3 not in sizes
ok &= N(2, 0) * N(3, 0) == N(1, 1) * N(1, -1) == 36
# units are +-1 (size 1), so 2 ~ 1+sqrt-5 would need equal sizes: 4 vs 6
ok &= N(2, 0) != N(1, 1)
# Z[i] Euclidean: remainder size <= half the divisor's size
for _ in range(2000):
    a = complex(random.randint(-99, 99), random.randint(-99, 99)); b = complex(random.randint(-30, 30), random.randint(-30, 30))
    if b == 0: continue
    q = a / b; q = complex(round(q.real), round(q.imag)); r = a - q*b
    ok &= abs(r)**2 <= abs(b)**2 / 2 + 1e-9
# two squares: p = 1 mod 4 is a^2 + b^2; Wilson: ((p-1)/2)!^2 = -1 mod p
for p in sp.primerange(5, 2000):
    if p % 4 == 1:
        x = math.factorial((p - 1)//2) % p
        ok &= (x*x + 1) % p == 0
        ok &= any(int(math.isqrt(p - a*a))**2 == p - a*a for a in range(1, int(math.isqrt(p)) + 1))
    else:
        ok &= not any(int(math.isqrt(p - a*a))**2 == p - a*a for a in range(0, int(math.isqrt(p)) + 1))
# Gauss lemma: content(fg) = content(f) content(g)
X = sp.symbols('x')
for _ in range(200):
    f = sp.Poly([random.randint(-9, 9) for _ in range(random.randint(1, 5))] + [random.randint(1, 9)], X)
    g = sp.Poly([random.randint(-9, 9) for _ in range(random.randint(1, 5))] + [random.randint(1, 9)], X)
    if f.is_zero or g.is_zero: continue
    ok &= (f*g).content() == f.content() * g.content()
# Eisenstein examples irreducible over Q
for f in (X**5 - 4*X + 2, sp.expand(((X + 1)**7 - 1) / X), X**4 + 6*X**2 + 3*X + 3):
    ok &= sp.Poly(f, X).is_irreducible
# CRT: Z/(ab) = Z/a x Z/b for gcd 1, and in Q[x]
for a, b in [(4, 9), (5, 12), (7, 8)]:
    ok &= len({(n % a, n % b) for n in range(a*b)}) == a*b
f1, f2 = sp.Poly(X**2 + 1, X, domain='QQ'), sp.Poly(X - 3, X, domain='QQ')
s, t, h = sp.gcdex(f1, f2); ok &= h == sp.Poly(1, X, domain='QQ')
print("ALL", ok)
