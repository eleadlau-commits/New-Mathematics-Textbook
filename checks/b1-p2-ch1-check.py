# Building 1, II.1 check: the table of move systems (finite rows by brute force).
from itertools import permutations, product
def comp(a, b): return tuple(a[b[i]] for i in range(len(b)))
def closure(gens, n):
    e = tuple(range(n)); G = {e}; fr = [e]
    while fr:
        new = []
        for g in fr:
            for h in gens:
                x = comp(h, g)
                if x not in G: G.add(x); new.append(x)
        fr = new
    return G
S3 = set(permutations(range(3)))
D4 = closure([(1, 2, 3, 0), (3, 2, 1, 0)], 4)   # rotation and a flip of corners 0,1,2,3 in order
def tests(G, op, e):
    G = list(G)
    comm = all(op(a, b) == op(b, a) for a in G for b in G)
    def power(g, k):
        x = e
        for _ in range(k): x = op(x, g)
        return x
    cyc = any(len({power(g, k) for k in range(len(G) + 1)}) == len(G) for g in G)
    tf = all(g == e or all(power(g, k) != e for k in range(1, len(G) + 1)) for g in G)
    div = all(any(power(h, n) == g for h in G) for g in G for n in range(1, len(G) + 1))
    return dict(comm=comm, fin=True, cyc=cyc, tf=tf, div=div)
Z6 = tests(range(6), lambda a, b: (a + b) % 6, 0)
U8 = tests([1, 3, 5, 7], lambda a, b: a*b % 8, 1)
s3 = tests(S3, comp, (0, 1, 2)); d4 = tests(D4, comp, (0, 1, 2, 3))
print("|D4| =", len(D4))
for name, r in (("Z/6", Z6), ("(Z/8)x", U8), ("S3", s3), ("D4", d4)): print(name, r)
print("P1 S3 and D4 same answers:", s3 == d4)
# T5 matchings: Z/6 ~ Z/2 x Z/3 via x -> (x mod 2, x mod 3); (Z/8)x ~ Z/2 x Z/2
print("T5 Z/6 -> Z/2 x Z/3 is one-to-one and respects +:", len({(x % 2, x % 3) for x in range(6)}) == 6 and all(((x + y) % 6 % 2, (x + y) % 6 % 3) == ((x % 2 + y % 2) % 2, (x % 3 + y % 3) % 3) for x in range(6) for y in range(6)))
m = {1: (0, 0), 3: (1, 0), 5: (0, 1), 7: (1, 1)}
print("T5 (Z/8)x -> Z/2 x Z/2 respects x/+:", all(m[a*b % 8] == ((m[a][0] + m[b][0]) % 2, (m[a][1] + m[b][1]) % 2) for a in m for b in m))
print("E3 S3 has an element of order 2 count:", sum(1 for g in S3 if g != (0,1,2) and comp(g, g) == (0,1,2)), "vs D4:", sum(1 for g in D4 if g != (0,1,2,3) and comp(g, g) == (0,1,2,3)))
