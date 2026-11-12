# Chapter 35: the projective plane over Z/p, checked by brute force.
import itertools, random
random.seed(1)
def nf(v, p):
    for i in (2, 1, 0):
        if v[i] % p:
            inv = pow(v[i], p - 2, p); return tuple(x * inv % p for x in v)
    return None
def det(u, v, w, p):
    return (u[0]*(v[1]*w[2]-v[2]*w[1]) - u[1]*(v[0]*w[2]-v[2]*w[0]) + u[2]*(v[0]*w[1]-v[1]*w[0])) % p
ok = True
for p in (2, 3, 5, 7):
    vs = [v for v in itertools.product(range(p), repeat=3) if any(v)]
    pts = sorted({nf(v, p) for v in vs})
    # P4: each bag has exactly one normal form; bag = scalar multiples
    bags = {}
    for v in vs: bags.setdefault(nf(v, p), set()).add(v)
    ok &= all(len(b) == p - 1 for b in bags.values())
    ok &= len(pts) == p*p + p + 1                                   # P5
    on = lambda a, v: sum(x*y for x, y in zip(a, v)) % p == 0
    lines = pts                                                     # P6 duality
    ok &= all(sum(on(a, v) for v in pts) == p + 1 for a in lines)
    ok &= all(sum(on(a, v) for a in lines) == p + 1 for v in pts)
    for P, Q in itertools.combinations(pts, 2):                     # T1
        ok &= sum(on(a, P) and on(a, Q) for a in lines) == 1
    for L, M in itertools.combinations(lines, 2):                   # T2
        ok &= sum(on(L, v) and on(M, v) for v in pts) == 1
    for P, Q, R in itertools.combinations(pts, 3):                  # T3
        col = any(on(a, P) and on(a, Q) and on(a, R) for a in lines)
        ok &= col == (det(P, Q, R, p) == 0)
    for P, Q in itertools.combinations(pts, 2):                     # P3
        ok &= any(on(a, P) != on(a, Q) for a in lines)
    for _ in range(20):                                             # T5
        while True:
            A = [[random.randrange(p) for _ in range(3)] for _ in range(3)]
            if det(*A, p): break
        img = lambda v: nf(tuple(sum(A[i][j]*v[j] for j in range(3)) % p for i in range(3)), p)
        ok &= len({img(v) for v in pts}) == len(pts)
        for P, Q, R in itertools.combinations(pts, 3):
            ok &= (det(P, Q, R, p) == 0) == (det(img(P), img(Q), img(R), p) == 0)
    print("p =", p, "points", len(pts), "ok so far", ok)
print("ALL", ok)
