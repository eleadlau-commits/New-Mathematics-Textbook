# Building 1, II.4 check: Smith form.
import random, itertools
from math import gcd
from functools import reduce
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form
from sympy.utilities.iterables import partitions
from sympy import factorint
random.seed(44)
def dk(A, k):
    m, n = A.shape; g = 0
    for rows in itertools.combinations(range(m), k):
        for cols in itertools.combinations(range(n), k):
            g = gcd(g, int(A.extract(list(rows), list(cols)).det()))
    return abs(g)
def unimodular(n):
    U = Matrix.eye(n)
    for _ in range(6):
        i, j = random.sample(range(n), 2); E = Matrix.eye(n); E[i, j] = random.randint(-3, 3); U = E*U
    return U
ok = True
for _ in range(200):
    A = Matrix(3, 3, [random.randint(-9, 9) for _ in range(9)]); B = unimodular(3)*A*unimodular(3)
    ok &= all(dk(A, k) == dk(B, k) for k in (1, 2, 3))
print("P1 d_k kept under 200 random moves:", ok)
ok = True
for _ in range(100):
    A = Matrix(3, 4, [random.randint(-12, 12) for _ in range(12)]); S = smith_normal_form(A, domain=ZZ)
    e = [abs(S[i, i]) for i in range(3)]
    nz = [x for x in e if x]
    ok &= all(nz[i+1] % nz[i] == 0 for i in range(len(nz) - 1))
    prod = 1
    for k in range(1, 4):
        prod *= e[k-1]
        ok &= prod == dk(A, k)
print("P4/P5 Smith form diagonal divides, e1...ek = d_k (100 random 3x4):", ok)
print("P3 diag(2,3) ~ diag(1,6):", smith_normal_form(Matrix([[2, 0], [0, 3]]), domain=ZZ))
def count_ab(n):
    c = 1
    for p, a in factorint(n).items(): c *= sum(1 for _ in partitions(a))
    return c
print("T3 counts: n=8 ->", count_ab(8), "; n=72 ->", count_ab(72), "; n=36 ->", count_ab(36))
# T3 by listing chains e1|e2|...|er (all >1) with product n
def chains(n, low=2):
    if n == 1: yield []; return
    for d in range(low, n + 1):
        if n % d == 0:
            for rest in chains(n // d, d):
                if all(r % d == 0 for r in rest): yield [d] + rest
print("T3 listing invariant-factor chains agrees for n <= 200:", all(len(list(chains(n))) == count_ab(n) for n in range(2, 201)))
print("T4 Smith of diag(m,n) = diag(gcd,lcm):", all(list(map(abs, smith_normal_form(Matrix([[m, 0], [0, n]]), domain=ZZ).diagonal())) == [gcd(m, n), m*n//gcd(m, n)] for m in range(1, 15) for n in range(1, 15)))
print("E1:", smith_normal_form(Matrix([[2, 4, 4], [-6, 6, 12], [10, -4, -16]]), domain=ZZ).diagonal(), " E2 chains for 36:", list(chains(36)))
