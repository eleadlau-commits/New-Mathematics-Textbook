# Building 1, II.3 check: blurs respecting both sides.
from itertools import permutations, combinations, product
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
    return {frozenset(closure([a, b], n)) for a in G for b in G}
def normal(N, G): return all(comp(comp(g, x), inverse(g)) in N for g in G for x in N)
S3 = set(permutations(range(3))); S4 = set(permutations(range(4)))
D4 = closure([(1, 2, 3, 0), (2, 1, 0, 3)], 4)   # corners 0..3: quarter turn and flip (1 3) in 1-based = swap 0<->2? use flip fixing 1 and 3
# P1 on S3, D4: x ~ y iff x^-1 y in K respects both sides iff K is a normal subgroup
for name, G, n in (("S3", S3, 3), ("D4", D4, 4)):
    e = tuple(range(n)); Gl = sorted(G); others = [g for g in Gl if g != e]; cnt = 0; ok = True
    for r in range(len(others) + 1):
        for sub in combinations(others, r):
            K = set(sub) | {e}
            if not all(comp(a, b) in K for a in K for b in K): continue
            rel = lambda x, y: comp(inverse(x), y) in K
            right = all(rel(comp(x, g), comp(y, g)) for x in Gl for y in Gl if rel(x, y) for g in Gl)
            ok &= right == normal(K, G); cnt += right
    print("P1 %s: two-sided blurs = normal sub systems (%d):" % (name, cnt), ok)
# P4 in D4 with corners 1,2,3,4 -> 0,1,2,3: s = (2 4) -> swap 1,3; r = (1 2 3 4) -> 0->1->2->3->0
r = (1, 2, 3, 0); s = (0, 3, 2, 1); e4 = (0, 1, 2, 3)
D4b = closure([r, s], 4); V = {e4, s, (2, 1, 0, 3), comp(s, (2, 1, 0, 3))}
print("P4 |D4|=8, V sub, {e,s} normal in V, V normal in D4, {e,s} not normal in D4:",
      len(D4b) == 8, V <= D4b and all(comp(a, b) in V for a in V for b in V), normal({e4, s}, V), normal(V, D4b), not normal({e4, s}, D4b), comp(comp(r, s), inverse(r)) == (2, 1, 0, 3))
print("P5 index-2 sub systems of S4 are normal:", all(normal(H, S4) for H in subgroups(S4, 4) if len(H) == 12))
# T1 det on GL2(Z/3)
mats = [(a, b, c, d) for a, b, c, d in product(range(3), repeat=4) if (a*d - b*c) % 3]
mul = lambda X, Y: ((X[0]*Y[0] + X[1]*Y[2]) % 3, (X[0]*Y[1] + X[1]*Y[3]) % 3, (X[2]*Y[0] + X[3]*Y[2]) % 3, (X[2]*Y[1] + X[3]*Y[3]) % 3)
det = lambda X: (X[0]*X[3] - X[1]*X[2]) % 3
SL = [X for X in mats if det(X) == 1]
print("T1 GL2(Z/3): size", len(mats), "kernel of det", len(SL), "picture {1,2}: 48/24 = 2:", len(mats)//len(SL) == 2, all(det(mul(X, Y)) == det(X)*det(Y) % 3 for X in mats for Y in mats))
def ab_size(G, n):
    G = list(G); comms = {comp(comp(a, b), comp(inverse(a), inverse(b))) for a in G for b in G}
    Dg = closure(list(comms), n) if comms else {tuple(range(n))}
    return len(G)//len(Dg)
print("T4 |G^ab| for S3, S4, D4:", ab_size(S3, 3), ab_size(S4, 4), ab_size(D4b, 4))
# T5 A5
A5 = [g for g in permutations(range(5)) if sum(1 for i in range(5) for j in range(i + 1, 5) if g[i] > g[j]) % 2 == 0]
seen, sizes = set(), []
for g in A5:
    if g in seen: continue
    cl = {comp(comp(p, g), inverse(p)) for p in A5}; seen |= cl; sizes.append(len(cl))
sizes.sort()
unions = {1 + sum(c) for r in range(5) for c in combinations([x for x in sizes if x != 1] , r)}
print("T5 A5 class sizes:", sizes, " unions holding e that divide 60:", sorted(u for u in unions if 60 % u == 0))
