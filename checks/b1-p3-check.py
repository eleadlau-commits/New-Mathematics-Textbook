# Building 1, Part III: the group law of a cubic (III.1), the torus (III.2), counts over Z/p (III.3).
import itertools, math, random
from fractions import Fraction as Fr
import numpy as np
random.seed(5); ok = True
O = 'O'
def add(P, Q, p, A):                       # P (+) Q: mirror of the third point (III.1 D3)
    if P == O: return Q
    if Q == O: return P
    (x1, y1), (x2, y2) = P, Q
    if x1 == x2 and (y1 + y2) % p == 0: return O
    if P == Q: m = (3*x1*x1 + A) * pow(2*y1, p-2, p) % p
    else:      m = (y2 - y1) * pow(x2 - x1, p-2, p) % p
    x3 = (m*m - x1 - x2) % p; y3 = (y1 + m*(x3 - x1)) % p
    return (x3, (-y3) % p)
def pts(p, A, B):
    return [O] + [(x, y) for x in range(p) for y in range(p) if (y*y - x**3 - A*x - B) % p == 0]
def legendre(c, p):
    c %= p
    return 0 if c == 0 else (1 if pow(c, (p-1)//2, p) == 1 else -1)
def structure(S, p, A):
    # orders of points; group is Z/e1 x Z/e2, e1 | e2, e2 = exponent
    def order(P):
        n, Q = 1, P
        while Q != O: Q = add(Q, P, p, A); n += 1
        return n
    e2 = max(order(P) for P in S); e1 = len(S) // e2
    return e1, e2, order
# III.1: commutative, O neutral, mirror inverse, associative (all triples), collinear triples sum to O
for p in (5, 7, 11, 13):
    for A, B in itertools.product(range(p), repeat=2):
        if (4*A**3 + 27*B**2) % p == 0: continue
        S = pts(p, A, B)
        for P in S:
            ok &= add(P, O, p, A) == P
            if P != O: ok &= add(P, (P[0], (-P[1]) % p), p, A) == O
        for P, Q in itertools.product(S, repeat=2): ok &= add(P, Q, p, A) == add(Q, P, p, A)
        T = S if len(S) <= 12 else random.sample(S, 12)
        for P, Q, R in itertools.product(T, repeat=3):
            ok &= add(add(P, Q, p, A), R, p, A) == add(P, add(Q, R, p, A), p, A)
print("III.1 group laws over Z/p:", ok)
# III.1 over Q: y^2 = x^3 + 1 has the 6 points O, (-1,0), (0,+-1), (2,+-3), and (2,3) has order 6
def addQ(P, Q, A):
    if P == O: return Q
    if Q == O: return P
    (x1, y1), (x2, y2) = P, Q
    if x1 == x2 and y1 + y2 == 0: return O
    m = (3*x1*x1 + A) / (2*y1) if P == Q else (y2 - y1) / (x2 - x1)
    x3 = m*m - x1 - x2; y3 = y1 + m*(x3 - x1); return (x3, -y3)
P = (Fr(2), Fr(3)); Q = P; seen = [P]
for _ in range(5): Q = addQ(Q, P, 0); seen.append(Q)
ok &= seen[-1] == O and len(set(seen)) == 6
# y^2 = x^3 - 2, P = (3,5): 2P = (129/100, -383/1000)
ok &= addQ((Fr(3), Fr(5)), (Fr(3), Fr(5)), 0) == (Fr(129, 100), Fr(-383, 1000))
print("III.1 over Q:", ok)
# III.3: count formula, Lagrange, structure e1 | e2, e1 | p-1, Hasse, for p < 60 all (A,B)
worst = 0
for p in [q for q in range(5, 60) if all(q % d for d in range(2, q))]:
    for A, B in itertools.product(range(p), repeat=2):
        if (4*A**3 + 27*B**2) % p == 0: continue
        S = pts(p, A, B); N = len(S)
        ok &= N == p + 1 + sum(legendre(x**3 + A*x + B, p) for x in range(p))
        e1, e2, order = structure(S, p, A)
        ok &= all(N % order(P) == 0 for P in S) and e2 % e1 == 0 and (p - 1) % e1 == 0 and e1 * e2 == N
        worst = max(worst, abs(N - p - 1) / (2*math.sqrt(p)))
print("III.3 counts, Lagrange, structure; worst |N-p-1|/(2 sqrt p) =", round(worst, 4), ok)
ok &= worst <= 1
# III.2: the torus. z1 + z2 + z3 in Lambda  <=>  images collinear.
w1, w2 = 1.0 + 0j, 0.3 + 1.1j
Nn = 120
I, J = np.meshgrid(np.arange(-Nn, Nn+1), np.arange(-Nn, Nn+1))
L = (I*w1 + J*w2).ravel(); L = L[L != 0]
wp  = lambda z: 1/z**2 + np.sum(1/(z - L)**2 - 1/L**2)
wpd = lambda z: -2/z**3 - 2*np.sum(1/(z - L)**3)
rng = np.random.default_rng(7); dets = []; nondets = []
for _ in range(8):
    z1 = complex(rng.uniform(.1, .9))*w1 + complex(rng.uniform(.1, .9))*w2
    z2 = complex(rng.uniform(.1, .9))*w1 + complex(rng.uniform(.1, .9))*w2
    z3 = -z1 - z2 + w1 + w2
    M = np.array([[wp(z), wpd(z), 1] for z in (z1, z2, z3)])
    dets.append(abs(np.linalg.det(M)) / np.prod([np.linalg.norm(r) for r in M]))
    z3b = z3 + 0.13
    Mb = np.array([[wp(z), wpd(z), 1] for z in (z1, z2, z3b)])
    nondets.append(abs(np.linalg.det(Mb)) / np.prod([np.linalg.norm(r) for r in Mb]))
print("III.2 collinear when sum in Lambda: max det", max(dets), " min det otherwise", min(nondets))
ok &= max(dets) < 1e-4 and min(nondets) > 1e-3
print("ALL", ok)
