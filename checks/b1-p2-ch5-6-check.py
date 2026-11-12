# Building 1, II.5 (actions) and II.6 (counting bags mod p, Cauchy, Sylow).
import itertools, math
from sympy.combinatorics import Permutation, PermutationGroup
from sympy.combinatorics.named_groups import SymmetricGroup, AlternatingGroup, DihedralGroup, CyclicGroup
from sympy import totient, divisors, binomial, factorint
ok = True
# II.5 T1 orbit-stabiliser and T2 Burnside: S4 acting on 2-subsets of {0..3}
G = SymmetricGroup(4); X = [frozenset(s) for s in itertools.combinations(range(4), 2)]
act = lambda g, s: frozenset(g(i) for i in s)
els = list(G.elements)
for x in X:
    orb = {act(g, x) for g in els}; stab = [g for g in els if act(g, x) == x]
    ok &= len(orb) * len(stab) == len(els)
orbits = len({frozenset(act(g, x) for g in els) for x in X})
ok &= orbits * len(els) == sum(sum(act(g, x) == x for x in X) for g in els)
# T3 necklaces: n beads, c colours, up to rotation
def neck_brute(n, c):
    seen = set(); cnt = 0
    for w in itertools.product(range(c), repeat=n):
        if w in seen: continue
        cnt += 1
        for r in range(n): seen.add(w[r:] + w[:r])
    return cnt
for n in range(1, 9):
    for c in (2, 3):
        ok &= neck_brute(n, c) == sum(totient(d) * c**(n//d) for d in divisors(n)) // n
# cube faces, 3 colours, rotations (24): 57
cube = PermutationGroup([Permutation([0,2,3,4,1,5]), Permutation([1,5,2,0,4,3])])
ok &= cube.order() == 24
fix = lambda g: 3**len(g.full_cyclic_form)
ok &= sum(fix(g) for g in cube.elements) // 24 == 57
# P3 class equation; T4 index = smallest prime => normal
for H in (SymmetricGroup(4), DihedralGroup(4), AlternatingGroup(4), DihedralGroup(6), AlternatingGroup(5)):
    E = list(H.elements); Z = [z for z in E if all(z*g == g*z for g in E)]
    classes = H.conjugacy_classes()
    ok &= sum(len(c) for c in classes) == len(E) and sum(1 for c in classes if len(c) == 1) == len(Z)
    ok &= all(len(E) % len(c) == 0 for c in classes)
for H in (SymmetricGroup(4), DihedralGroup(5), DihedralGroup(6), SymmetricGroup(3)):
    n = H.order(); p = min(factorint(n))
    subs = [K for K in [H.subgroup([a, b]) for a in H.elements for b in H.elements] if K.order() == n // p]
    ok &= all(K.is_normal(H) for K in subs)
print("II.5:", ok)
# II.6 T1 counting lemma: D4 (order 8) on colourings of square corners, 2 colours: fixed count = |X| mod 2
D4 = DihedralGroup(4); X = list(itertools.product(range(3), repeat=4))
fixed = [x for x in X if all(tuple(x[g(i)] for i in range(4)) == x for g in D4.elements)]
ok &= (len(fixed) - len(X)) % 2 == 0
# T2 centre of p-groups non-trivial: D4, Q8-like (via D4), C3xC3, a group of order 27 (Heisenberg mod 3)
heis = PermutationGroup([Permutation([[0,1,2],[3,4,5],[6,7,8]]), Permutation([[0,3,6],[1,4,7],[2,5,8]])])
# a non-comm group of order 27 as permutations of Z/3 x Z/3 x Z/3? use upper unitriangular action on F3^2 affine
def aff(a, b, c):  # (x,y) -> (x + a*y + b, y + c) on F3^2
    return Permutation([((x + a*y + b) % 3) * 3 + (y + c) % 3 for x in range(3) for y in range(3)])
H27 = PermutationGroup([aff(1, 0, 0), aff(0, 1, 0), aff(0, 0, 1)])
for H in (D4, H27):
    E = list(H.elements); Z = [z for z in E if all(z*g == g*z for g in E)]
    ok &= len(Z) > 1
ok &= H27.order() == 27 and not H27.is_abelian
# T4 Cauchy and T5-T7 Sylow on several groups
for H in (SymmetricGroup(4), AlternatingGroup(4), AlternatingGroup(5), SymmetricGroup(5), DihedralGroup(6), DihedralGroup(10)):
    n = H.order(); E = list(H.elements)
    for p, a in factorint(n).items():
        ok &= any(g.order() == p for g in E)                    # Cauchy
        P = H.sylow_subgroup(p); ok &= P.order() == p**a        # Sylow I
        # count Sylow p-subgroups via conjugates
        conj = {frozenset((g**-1)*x*g for x in P.elements) for g in E}
        npp = len(conj); m = n // p**a
        ok &= npp % p == 1 and m % npp == 0                      # Sylow III
        # Sylow II: every element of p-power order lies in some conjugate
        for g in E:
            o = g.order()
            if o > 1 and o == p**int(round(math.log(o, p))):
                ok &= any(g in c for c in conj)
    print(" ", H.order(), "ok", ok)
# Wielandt count: binom(p^a m, p^a) not divisible by p
for p in (2, 3, 5):
    for a in (1, 2, 3):
        for m in (1, 2, 3, 4, 5, 6, 7):
            if m % p: ok &= binomial(p**a * m, p**a) % p != 0
# order 15 => cyclic: n3 | 5, n3 = 1 mod 3 -> 1 ; n5 | 3, n5 = 1 mod 5 -> 1
ok &= [d for d in divisors(5) if d % 3 == 1] == [1] and [d for d in divisors(3) if d % 5 == 1] == [1]
print("ALL", ok)
