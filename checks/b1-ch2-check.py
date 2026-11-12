# Building 1, Chapter 2 check: words.
from itertools import product
from sympy.combinatorics.free_groups import free_group
from sympy.combinatorics.fp_groups import FpGroup
NAMES = ['s', 'S', 't', 'T']; INV = {'s': 'S', 'S': 's', 't': 'T', 'T': 't'}
def reduce(w):
    out = []
    for x in w:
        if out and out[-1] == INV[x]: out.pop()
        else: out.append(x)
    return ''.join(out)
def act(x, r): return r[1:] if r and r[0] == INV[x] else x + r
def act_word(u, r):
    for x in reversed(u): r = act(x, r)
    return r
reduced = [''.join(p) for k in range(0, 6) for p in product(NAMES, repeat=k) if reduce(''.join(p)) == ''.join(p)]
ok = True
for k in range(0, 9):
    for p in product(NAMES, repeat=k):
        u = ''.join(p); ru = reduce(u)
        ok &= all(act_word(u, r) == act_word(ru, r) for r in reduced[:60])
        ok &= act_word(ru, '') == ru
print("P1 B1 keeps the action, every word glued to its reduction, reduced words act differently (length <= 8):", ok)
print("P3 counts 4*3^(k-1):", all(sum(1 for p in product(NAMES, repeat=k) if reduce(''.join(p)) == ''.join(p)) == 4*3**(k - 1) for k in range(1, 9)))
print("P4 sSs ~ s:", reduce('sSs') == 's')
eps = lambda w: w.count('s') - w.count('S')
print("P5 exponent sum and length parity survive reduction (length <= 8):", all(eps(''.join(p)) == eps(reduce(''.join(p))) and len(p) % 2 == len(reduce(''.join(p))) % 2 for k in range(9) for p in product(NAMES, repeat=k)))
F, s, t = free_group('s t')
print("T3 orders: <s|s^5> via <s,t|s^5,t>:", FpGroup(F, [s**5, t]).order(), "; S3:", FpGroup(F, [s**2, t**2, (s*t)**3]).order(),
      "; dihedral n=4,5,6:", [FpGroup(F, [s**2, t**2, (s*t)**n]).order() for n in (4, 5, 6)], "; <s,t|s^2,t^3,(st)^5>:", FpGroup(F, [s**2, t**3, (s*t)**5]).order())
# arrow onto S3: s -> (1 2), t -> (2 3) satisfies the relations
def comp(a, b): return tuple(a[b[i]] for i in range(3))
S, T, e = (1, 0, 2), (0, 2, 1), (0, 1, 2)
st = comp(S, T)
print("T3 relations hold in S3 for s=(1 2), t=(2 3):", comp(S, S) == e and comp(T, T) == e and comp(st, comp(st, st)) == e)
print("E1:", reduce('stTSsTts') or '1', " E4 reduced words of length <= 3:", 1 + 4 + 12 + 36)
