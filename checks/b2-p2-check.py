# Building 2, Part II: loops, Amplify, atoms, the missing move.
import itertools, math, cmath, functools
import numpy as np, sympy as sp
ok = True
# ---- Ch3 Loops
# Gauss sums on Z/p: |sum chi(x) e(x/p)|^2 = p for every non-trivial character chi (chi from a generator)
for p in sp.primerange(3, 80):
    g = sp.primitive_root(p)
    log = {pow(g, k, p): k for k in range(p - 1)}
    for j in range(1, p - 1):
        tau = sum(cmath.exp(2j*math.pi*j*log[x]/(p-1)) * cmath.exp(2j*math.pi*x/p) for x in range(1, p))
        ok &= abs(abs(tau)**2 - p) < 1e-8
# one prime: logs of powers of 2 have gap log 2; two primes {2,3}: gaps between a log2 + b log3 (a,b>=0, value <= L) shrink
def gaps(primes, L):
    vals = set()
    def rec(i, v):
        if i == len(primes): vals.add(round(v, 12)); return
        x = v
        while x <= L + 1e-12: rec(i + 1, x); x += math.log(primes[i])
    rec(0, 0.0); v = sorted(vals); return min(b - a for a, b in zip(v, v[1:]))
ok &= abs(gaps([2], 40) - math.log(2)) < 1e-9
g23 = [gaps([2, 3], L) for L in (10, 20, 40, 80)]
ok &= all(a > b for a, b in zip(g23, g23[1:]))
# p-adic units acting by x on Z/p^k: k+1 bags (one per valuation level)
for p, k in [(2, 5), (3, 4), (5, 3)]:
    n = p**k; units = [u for u in range(n) if u % p]
    bags = {frozenset((u*x) % n for u in units) for x in range(n)}
    ok &= len(bags) == k + 1
# Redheffer: det = Mertens M(n)
def mertens(n): return sum(sp.mobius(k) for k in range(1, n + 1))
for n in range(1, 41):
    R = sp.Matrix(n, n, lambda i, j: 1 if (j == 0 or (j + 1) % (i + 1) == 0) else 0)
    ok &= R.det() == mertens(n)
print("Ch3:", ok)
# ---- Ch4 Amplify
# Cauchy-Schwarz by tensor powers: <a^k, b^k> = <a,b>^k, |a^k| = |a|^k
rng = np.random.default_rng(4)
a, b = rng.normal(size=4), rng.normal(size=4)
ak, bk = a.copy(), b.copy()
for k in range(2, 5):
    ak, bk = np.kron(ak, a), np.kron(bk, b)
    ok &= abs(ak @ bk - (a @ b)**k) < 1e-9 and abs(np.linalg.norm(ak) - np.linalg.norm(a)**k) < 1e-9
# Gelfand, trace form: |tr A^m|^(1/m) -> max |eigenvalue|
A = rng.normal(size=(5, 5)); rho = max(abs(np.linalg.eigvals(A)))
tr = [abs(np.trace(np.linalg.matrix_power(A, m)))**(1/m) for m in (50, 100, 200)]
ok &= abs(tr[-1] - rho) / rho < 0.05
# genus-2 curve y^2 = x^5 + 2x + 1 over F_{3^m}: counts predicted from N1, N2
p = 3
def gf(m):
    # F_{p^m} as polynomials mod an irreducible of degree m over Z/p
    x = sp.symbols('x')
    for c in itertools.product(range(p), repeat=m):
        f = sp.Poly([1] + list(c), x, modulus=p)
        if f.is_irreducible: break
    mod = [int(t) % p for t in f.all_coeffs()]
    elems = list(itertools.product(range(p), repeat=m))
    def mul(u, v):
        prod = [0] * (2*m - 1)
        for i, ui in enumerate(u):
            if ui:
                for j, vj in enumerate(v): prod[i + j] = (prod[i + j] + ui*vj) % p
        # reduce, highest degree first; u stored low->high
        for d in range(2*m - 2, m - 1, -1):
            c = prod[d]
            if c:
                for t in range(m + 1):
                    prod[d - m + t] = (prod[d - m + t] - c * mod[m - t]) % p
        return tuple(prod[:m])
    return elems, mul
def count(m):
    E, mul = gf(m); add = lambda u, v: tuple((s + t) % p for s, t in zip(u, v))
    zero = tuple([0]*m); one = tuple([1] + [0]*(m-1)); two = tuple([2] + [0]*(m-1))
    sq = {}
    for y in E: sq.setdefault(mul(y, y), 0); sq[mul(y, y)] += 1
    N = 1   # one point at infinity (odd degree model)
    for x in E:
        x2 = mul(x, x); x4 = mul(x2, x2); x5 = mul(x4, x)
        r = add(add(x5, mul(two, x)), one)
        N += sq.get(r, 0)
    return N
Ns = [count(m) for m in range(1, 5)]
ok &= Ns == [7, 15, 19, 83]
# from N1, N2: S_m = q^m + 1 - N_m = sum alpha_i^m over 4 alphas with |alpha| = sqrt3
S1, S2 = p + 1 - Ns[0], p**2 + 1 - Ns[1]
# L-polynomial 1 + a1 T + a2 T^2 + q a1 T^3 + q^2 T^4 with a1 = -S1, a2 = (S1^2 - S2)/2
a1 = -S1; a2 = (S1**2 - S2) // 2
roots = np.roots([p**2, p*a1, a2, a1, 1])     # reciprocal roots are alphas
alphas = 1 / roots
ok &= all(abs(abs(al) - math.sqrt(p)) < 1e-9 for al in alphas)
for m in (3, 4):
    ok &= abs(p**m + 1 - sum(al**m for al in alphas).real - Ns[m-1]) < 1e-6
print("Ch4:", ok)
# ---- Ch5 Atoms: factorisation lengths in Z[sqrt-d]
def atoms_lengths(d, Nmax):
    els = [(a, b) for a in range(-40, 41) for b in range(-20, 21) if 1 < a*a + d*b*b <= Nmax]
    nrm = lambda z: z[0]**2 + d*z[1]**2
    def divides(u, z):           # u | z in Z[sqrt-d]
        n = nrm(u); a, b = z; c, e = u
        re, im = a*c + d*b*e, b*c - a*e     # z * conj(u)
        return re % n == 0 and im % n == 0
    def quo(z, u):
        n = nrm(u); a, b = z; c, e = u
        return ((a*c + d*b*e)//n, (b*c - a*e)//n)
    irr = [z for z in els if not any(1 < nrm(u) < nrm(z) and divides(u, z) for u in els if nrm(u) < nrm(z))]
    irr_by = {}
    @functools.lru_cache(None)
    def lengths(z):
        if nrm(z) == 1: return frozenset([0])
        out = set()
        for u in irr:
            if nrm(u) <= nrm(z) and nrm(z) % nrm(u) == 0 and divides(u, z):
                for l in lengths(quo(z, u)): out.add(l + 1)
        return frozenset(out)
    ratios = [max(lengths(z)) / min(lengths(z)) for z in els if lengths(z)]
    return max(ratios)
ok &= atoms_lengths(5, 600) == 1.0          # fair: lengths agree (Z[sqrt-5], class number 2)
ok &= atoms_lengths(1, 600) == 1.0          # free: Z[i]
# unfair: in Z[sqrt-14], 81 = 3^4 = (5 + 2 sqrt-14)(5 - 2 sqrt-14); 3 and 5 +- 2 sqrt-14 are irreducible
nrm14 = lambda a, b: a*a + 14*b*b
small = {nrm14(a, b) for a in range(-30, 31) for b in range(-10, 11)}
ok &= 3 not in small and 27 not in small and (5*5 - 14*(-4)) == 81    # no element of norm 3 or 27
ok &= (5 + 2*sp.sqrt(-14)) * (5 - 2*sp.sqrt(-14)) == 81 or sp.expand((5 + 2*sp.sqrt(-14)) * (5 - 2*sp.sqrt(-14))) == 81
# 3 does not divide 5 + 2 sqrt-14 (5/3 not whole), so 5 + 2 sqrt-14 (norm 81) has no factor of norm 9 other than 3, and none of norm 3, 27
print("Ch5:", ok)
# ---- Ch6: Redheffer char poly = (x-1)^(n-K-1) Q_n(x-1), Q_n(y) = y^(K+1) - sum F_k(n) y^(K-k)
x = sp.symbols('x')
def F(k, n):
    @functools.lru_cache(None)
    def chains(a, k):           # chains starting above a, k more proper steps, all <= n
        if k == 0: return 1
        return sum(chains(b, k - 1) for b in range(2*a, n + 1, a))
    return sum(chains(a1, k - 1) for a1 in range(2, n + 1))
for n in (6, 12, 30, 48):
    R = sp.Matrix(n, n, lambda i, j: 1 if (j == 0 or (j + 1) % (i + 1) == 0) else 0)
    K = int(math.floor(math.log2(n)))
    y = sp.symbols('y')
    Q = y**(K+1) - sum(F(k, n) * y**(K - k) for k in range(1, K + 1))
    target = sp.expand((x - 1)**(n - K - 1) * Q.subs(y, x - 1))
    ok &= sp.expand(R.charpoly(x).as_expr() - target) == 0
print("ALL", ok)
