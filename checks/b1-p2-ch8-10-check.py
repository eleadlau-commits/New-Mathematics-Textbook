# Building 1, II.8 (linear maps, tensor), II.9 (similarity), II.10 (forms).
import random, itertools, numpy as np, sympy as sp
from sympy.matrices.normalforms import invariant_factors, smith_normal_form
random.seed(8); ok = True
x = sp.symbols('x')
def rnd(m, n, lo=-3, hi=3): return sp.Matrix(m, n, lambda i, j: random.randint(lo, hi))
def rnd_inv(n):
    while True:
        P = rnd(n, n)
        if P.det() != 0: return P
# II.8: rank kept by PAQ; rank-nullity; row rank = column rank; normal form [I_r 0; 0 0]
for _ in range(40):
    m, n = random.randint(1, 5), random.randint(1, 5)
    A = rnd(m, n) * rnd(n, n, -1, 1)          # often rank-deficient
    B = rnd_inv(m) * A * rnd_inv(n)
    ok &= A.rank() == B.rank() == A.T.rank()
    ok &= A.rank() + len(A.nullspace()) == n
    ok &= list(invariant_factors(A, domain=sp.QQ)).count(1) == A.rank()
# tensor: e1(x)f1 + e2(x)f2 is not v(x)w (its matrix has rank 2); dim V(x)W = mn
T = sp.Matrix([[1, 0], [0, 1]]); ok &= T.rank() == 2
# Z/m (x) Z/n = Z/gcd: presentation matrix diag(m, n) on one generator -> Smith of [[m],[n]]
for m_, n_ in [(2, 3), (4, 6), (12, 18), (5, 10)]:
    S = smith_normal_form(sp.Matrix([[m_], [n_]]), domain=sp.ZZ)
    ok &= abs(S[0, 0]) == sp.gcd(m_, n_)
print("II.8:", ok)
# II.9: similar => same invariant factors of xI - M; char poly does not separate; Jordan
def inv_f(M): return [sp.Poly(f, x).monic() if f != 0 else 0 for f in invariant_factors(x*sp.eye(M.rows) - M, domain=sp.QQ[x])]
for _ in range(15):
    n = random.randint(2, 4); M = rnd(n, n); P = rnd_inv(n)
    N = P * M * P.inv()
    ok &= inv_f(M) == inv_f(N)
    ok &= sp.expand(M.charpoly(x).as_expr() - N.charpoly(x).as_expr()) == 0
    # Cayley-Hamilton: product of invariant factors = char poly
    prod = sp.Integer(1)
    for f in inv_f(M): prod *= f.as_expr()
    ok &= sp.expand(prod - M.charpoly(x).as_expr()) == 0
    # minimal polynomial = last invariant factor kills M
    last = inv_f(M)[-1]
    val = sp.zeros(n, n)
    for k, c in enumerate(reversed(last.all_coeffs())): val += c * M**k
    ok &= val == sp.zeros(n, n)
Z2 = sp.Matrix([[0, 1], [0, 0]])
ok &= Z2.charpoly(x) == sp.zeros(2, 2).charpoly(x) and inv_f(Z2) != inv_f(sp.zeros(2, 2))
# ranks of (M - l)^k separate Jordan types with the same char poly
J1 = sp.Matrix([[2, 1, 0, 0], [0, 2, 0, 0], [0, 0, 2, 1], [0, 0, 0, 2]])
J2 = sp.Matrix([[2, 1, 0, 0], [0, 2, 1, 0], [0, 0, 2, 0], [0, 0, 0, 2]])
ok &= J1.charpoly(x) == J2.charpoly(x) and ((J1 - 2*sp.eye(4))**2).rank() != ((J2 - 2*sp.eye(4))**2).rank()
print("II.9:", ok)
# II.10: Sylvester: signs of eigenvalues kept under P^T M P; completing squares; spectral
rng = np.random.default_rng(10)
for _ in range(50):
    n = rng.integers(2, 6)
    A = rng.integers(-4, 5, (n, n)); M = A + A.T
    P = rng.integers(-3, 4, (n, n))
    if abs(np.linalg.det(P)) < 0.5: continue
    N = P.T @ M @ P
    sig = lambda S: (int(np.sum(np.linalg.eigvalsh(S) > 1e-8)), int(np.sum(np.linalg.eigvalsh(S) < -1e-8)))
    ok &= sig(M) == sig(N)
    w, Q = np.linalg.eigh(M)
    ok &= np.allclose(Q.T @ Q, np.eye(n)) and np.allclose(Q.T @ M @ Q, np.diag(w))
    # highest point of v.Mv on the sphere is the largest eigenvalue (random search lower bound)
    V = rng.normal(size=(4000, n)); V /= np.linalg.norm(V, axis=1)[:, None]
    ok &= np.max(np.einsum('ij,jk,ik->i', V, M, V)) <= w[-1] + 1e-9
# over Z/p: diag(1,1) ~ diag(1,c) iff c is a square; discriminant square class kept
for p in (5, 7, 11):
    sq = {(a*a) % p for a in range(1, p)}
    for c in range(1, p):
        # forms diag(1,1) and diag(1,c): equivalent iff det differ by a square
        reach = set()
        for P in itertools.product(range(p), repeat=4):
            a, b, cc, d = P
            if (a*d - b*cc) % p == 0: continue
            # P^T diag(1,1) P
            M2 = ((a*a + cc*cc) % p, (a*b + cc*d) % p, (b*b + d*d) % p)
            reach.add(M2)
        ok &= ((1, 0, c % p) in reach) == (c in sq)
print("II.10:", ok)
print("ALL", ok)
