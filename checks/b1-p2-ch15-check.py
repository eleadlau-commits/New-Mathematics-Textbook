# Building 1, II.15: colourings up to symmetry (cycle counts).
import itertools, sympy as sp
from sympy.combinatorics import Permutation, PermutationGroup
from sympy.combinatorics.named_groups import SymmetricGroup, DihedralGroup, CyclicGroup
ok = True
def orbits_brute(G, n, c):
    seen = set(); cnt = 0
    els = list(G.elements)
    for w in itertools.product(range(c), repeat=n):
        if w in seen: continue
        cnt += 1
        for g in els: seen.add(tuple(w[g(i)] for i in range(n)))
    return cnt
def cyc(g, n): return len(g.cyclic_form) + (n - sum(len(c) for c in g.cyclic_form))
def polya(G, n, c): return sum(c**cyc(g, n) for g in G.elements) // G.order()
cube = PermutationGroup([Permutation([0,2,3,4,1,5]), Permutation([1,5,2,0,4,3])])
for c in (1, 2, 3, 4):
    ok &= polya(cube, 6, c) == (c**6 + 3*c**4 + 12*c**3 + 8*c**2) // 24 == orbits_brute(cube, 6, c)
for n in range(3, 8):
    for c in (2, 3):
        ok &= polya(DihedralGroup(n), n, c) == orbits_brute(DihedralGroup(n), n, c)
# graphs on 4 points up to relabelling: S4 acting on the 6 pairs; 11 graphs; by number of edges 1,1,2,3,2,1,1
pairs = list(itertools.combinations(range(4), 2))
gens = []
for g in SymmetricGroup(4).generators:
    gens.append(Permutation([pairs.index(tuple(sorted((g(a), g(b))))) for a, b in pairs]))
E = PermutationGroup(gens)
ok &= E.order() == 24 and polya(E, 6, 2) == 11
x = sp.symbols('x')
gf = sp.expand(sum(sp.prod([(1 + x**len(cy)) for cy in g.full_cyclic_form] + [(1 + x)]*(6 - sum(len(cy) for cy in g.full_cyclic_form))) for g in E.elements) / 24)
ok &= sp.Poly(gf, x).all_coeffs()[::-1] == [1, 1, 2, 3, 2, 1, 1]
# weighted: cube faces with 3 red and 3 blue: 2
gfc = sp.expand(sum(sp.prod([(1 + x**len(cy)) for cy in g.full_cyclic_form] + [(1 + x)]*(6 - sum(len(cy) for cy in g.full_cyclic_form))) for g in cube.elements) / 24)
ok &= sp.Poly(gfc, x).coeff_monomial(x**3) == 2
print("ALL", ok)
