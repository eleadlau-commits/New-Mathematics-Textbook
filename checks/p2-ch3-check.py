# Checks for Chapter II.3 (vector spaces): over Z/2 and Z/3, search all partitions of K^n
# for blurs respecting + and every scaling, and compare with the number of subspaces.
from itertools import product
def partitions(items):
    if not items: yield []; return
    first, rest = items[0], items[1:]
    for p in partitions(rest):
        for i in range(len(p)):
            yield p[:i] + [[first] + p[i]] + p[i+1:]
        yield [[first]] + p
def count(p, n):
    V = list(product(range(p), repeat=n))
    add = lambda x,y: tuple((a+b)%p for a,b in zip(x,y))
    sc = lambda r,x: tuple((r*a)%p for a in x)
    blurs = 0; zero_bags = set()
    for part in partitions(V):
        cls = {v:i for i,b in enumerate(part) for v in b}
        ok = all(cls[add(x,z)]==cls[add(y,z)] for b in part for x in b for y in b for z in V) and \
             all(cls[sc(r,x)]==cls[sc(r,y)] for b in part for x in b for y in b for r in range(p))
        if ok:
            blurs += 1; zero_bags.add(frozenset(next(b for b in part if (0,)*n in b)))
    subspaces = sum(1 for S in zero_bags)  # each zero bag is checked to be a subspace below
    allsub = all(all(add(x,y) in S and sc(r,x) in S for x in S for y in S for r in range(p)) for S in zero_bags)
    return blurs, len(zero_bags), allsub
for p,n,expected in [(2,2,5),(3,2,6),(2,3,16)]:
    b,z,s = count(p,n)
    print(f"(Z/{p})^{n}: blurs = {b}, distinct zero bags = {z}, all zero bags subspaces: {s}, subspaces by formula = {expected}")
