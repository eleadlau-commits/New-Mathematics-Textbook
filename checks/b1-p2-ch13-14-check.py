# Building 1, II.13 (Galois correspondence) and II.14 (solvable ladders, radicals).
import itertools, sympy as sp, numpy as np
from sympy.polys.numberfields.galoisgroups import galois_group
from sympy.combinatorics import Permutation, PermutationGroup
from sympy.combinatorics.named_groups import SymmetricGroup, AlternatingGroup, CyclicGroup, DihedralGroup
x = sp.symbols('x'); ok = True
# |G| = degree of splitting field; G inside A_n iff discriminant is a square
cases = {x**3 - 2: 6, x**3 - 3*x + 1: 3, x**4 - 2: 8, x**4 + x**3 + x**2 + x + 1: 4, x**4 - 10*x**2 + 1: 4, x**5 - 4*x + 2: 120}
for f, order in cases.items():
    G, alt = galois_group(sp.Poly(f, x), by_name=True)
    grp = G.get_perm_group()
    ok &= grp.order() == order
    d = sp.discriminant(f, x)
    ok &= alt == (d > 0 and sp.sqrt(d).is_integer)
# x^3 - 2: middle fields and their degrees = index of the subgroup
r = sp.cbrt(2); w = sp.exp(2*sp.pi*sp.I/3)
deg = lambda a: sp.degree(sp.minimal_polynomial(a, x), x)
ok &= deg(r) == 3 and deg(r*w) == 3 and deg(r*w**2) == 3 and deg(w) == 2   # S3 subgroups of order 2 (index 3) and A3 (index 2)
# Q(zeta_5): G = (Z/5)^x cyclic of order 4; its subgroup of order 2 fixes zeta + zeta^-1, degree 2, = (-1+sqrt5)/2
z = sp.exp(2*sp.pi*sp.I/5)
ok &= sp.minimal_polynomial(z + 1/z, x) == x**2 + x - 1
# normal not transitive: Q(sqrt2)/Q and Q(2^(1/4))/Q(sqrt2) normal, Q(2^(1/4))/Q not (x^4 - 2 has non-real roots)
ok &= len([t for t in sp.Poly(x**4 - 2, x).nroots() if abs(sp.im(t)) < 1e-12]) == 2
print("II.13:", ok)
# II.14: solvable ladders
for n in range(1, 7):
    ok &= SymmetricGroup(n).is_solvable == (n <= 4)
A5 = AlternatingGroup(5)
ok &= A5.derived_subgroup().order() == 60                     # A5 equals its own commutator: no comm rung
S4 = SymmetricGroup(4); ds = S4.derived_series()
ok &= [g.order() for g in ds] == [24, 12, 4, 1]
# Jordan-Holder for Z/12: every composition ladder has rung sizes {2,2,3}
ok &= sorted([2, 2, 3]) == sorted(sp.factorint(12, multiple=True))
# x^5 - 4x + 2: exactly three real roots; a swap and a 5-cycle generate S5
roots = sp.Poly(x**5 - 4*x + 2, x).nroots()
ok &= sum(1 for t in roots if abs(sp.im(t)) < 1e-12) == 3
ok &= PermutationGroup([Permutation([1, 0, 2, 3, 4]), Permutation([1, 2, 3, 4, 0])]).order() == 120
# Kummer rung: over Q(w), x^3 - 2 has group Z/3: the splitting field degree over Q(w) is 3
ok &= sp.degree(sp.minimal_polynomial(r, x, domain=sp.QQ.algebraic_field(w)), x) == 3
print("ALL", ok)
