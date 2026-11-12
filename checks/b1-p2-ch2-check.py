# Building 1, II.2 check: blurs respecting left moves.
from itertools import permutations, combinations
from math import gcd
def comp(a, b): return tuple(a[b[i]] for i in range(len(b)))
def inverse(s):
    r = [0]*len(s)
    for i, v in enumerate(s): r[v] = i
    return tuple(r)
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
def subgroups(G, n):
    G = list(G); subs = set()
    for a in G:
        for b in G:
            subs.add(frozenset(closure([a, b], n)))
    return subs
def left_respecting_blurs(G, op):
    # all partitions respecting x->gx: determined by class of e; check every subset containing e
    G = list(G); e = G[0] if False else None
    return None
S3 = set(permutations(range(3))); S4 = set(permutations(range(4)))
D4 = closure([(1, 2, 3, 0), (3, 2, 1, 0)], 4)
# P1: for S3 and D4, every subset K containing e such that x~y iff x^-1 y in K is an equivalence respecting left moves  <=> K subgroup
for name, G, n in (("S3", S3, 3), ("D4", D4, 4)):
    e = tuple(range(n)); Gl = sorted(G); good = 0; sg = 0
    others = [g for g in Gl if g != e]
    for r in range(len(others) + 1):
        for sub in combinations(others, r):
            K = set(sub) | {e}
            rel = lambda x, y: comp(inverse(x), y) in K
            equiv = all(rel(x, x) for x in Gl) and all(rel(y, x) for x in Gl for y in Gl if rel(x, y)) and all(rel(x, z) for x in Gl for y in Gl for z in Gl if rel(x, y) and rel(y, z))
            issub = all(comp(a, b) in K for a in K for b in K)
            good += equiv; sg += issub
            assert equiv == issub
    print("P1 %s: left-respecting blurs = sub move systems: %d" % (name, good))
# general blurs respecting left mult on Z/12: partitions by x-y in K
print("P1 Z/12: K must be a subgroup:", all((all(((a + b) % 12) in K for a in K for b in K)) for K in [set(range(0, 12, d)) for d in (1, 2, 3, 4, 6, 12)]))
K = {(0, 1, 2), (1, 0, 2)}
a, b = comp((0, 1, 2), (2, 1, 0)), comp((1, 0, 2), (2, 1, 0))
print("P4 e(1 3) and (1 2)(1 3) in different left cosets:", comp(inverse(a), b) not in K)
subs4 = subgroups(S4, 4)
sizes = sorted({len(H) for H in subs4})
ok = True
for H in subs4:
    cos = {frozenset(comp(x, h) for h in H) for x in S4}
    ok &= all(len(c) == len(H) for c in cos) and len(cos)*len(H) == 24
print("T1 all sub move systems of S4: cosets same size, |G| = |K| * #bags:", ok, " sizes that occur:", sizes)
def order(g):
    e = tuple(range(len(g))); x, m = g, 1
    while x != e: x = comp(g, x); m += 1
    return m
print("T2/T3 order divides 24 in S4:", all(24 % order(g) == 0 for g in S4))
phi = lambda n: sum(1 for a in range(1, n + 1) if gcd(a, n) == 1)
print("T4 a^phi(n) = 1 mod n for n <= 200:", all(pow(a, phi(n), n) == 1 for n in range(2, 201) for a in range(1, n) if gcd(a, n) == 1))
A4 = {g for g in S4 if sum(1 for i in range(4) for j in range(i + 1, 4) if g[i] > g[j]) % 2 == 0}
print("T5 A4 has no sub move system of size 6:", not any(len(H) == 6 for H in subgroups(A4, 4)), " (sizes in A4:", sorted({len(H) for H in subgroups(A4, 4)}), ")")
print("E2 3^100 mod 7:", pow(3, 100, 7), "= 3^(100 mod 6) =", pow(3, 100 % 6, 7))
