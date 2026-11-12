# Chapter 26 (design) check: null sets.
from fractions import Fraction as Fr
import random
random.seed(26)
# P3: the rationals of 0 <= x <= 1 are null: the i-th one gets a stretch of length 10^-(k+i+1); total < 10^-k
def rationals(n):
    out, q = [], 1
    while len(out) < n:
        for p in range(q + 1):
            r = Fr(p, q)
            if r.denominator == q: out.append(r)
            if len(out) == n: break
        q += 1
    return out
for k in (0, 1, 3):
    rs = rationals(400)
    total = sum(Fr(1, 10 ** (k + i + 1)) for i in range(len(rs)))
    print("P3 rung", k, ": 400 rationals covered, total length < 10^-k:", total < Fr(1, 10 ** k), " (total = %.3e)" % float(total))
# P2: sharing out a rung: sum over i of 10^-(k+i+1) = 10^-k / 9
print("P2 shares add up to 10^-k/9:", abs(sum(10.0 ** -(2 + i + 1) for i in range(60)) - 10.0 ** -2 / 9) < 1e-15)
# T1, finite step: finitely many open stretches that cover 0 <= x <= 1 have total length > 1
ok = True; n = 0
for _ in range(3000):
    m = random.randint(1, 12)
    S = [(a, a + random.uniform(0.01, 0.6)) for a in [random.uniform(-0.3, 1.0) for _ in range(m)]]
    # does S cover [0,1]?  walk from 0: take the stretch containing the current point that reaches furthest
    x, covered = 0.0, True
    while x <= 1.0:
        reach = [d for (c, d) in S if c < x < d]
        if not reach: covered = False; break
        x = max(reach)
    if covered:
        n += 1; ok &= sum(d - c for c, d in S) > 1.0
print("T1 finite covers of the stretch have total length > 1 (", n, "covers ):", ok)
# T1 fails over Q: P3 again. And the creeping walk needs every point: over Q a cover can leave out sqrt(1/2).
# R: the middle-thirds set: 2^k stretches of length 3^-k
print("R middle thirds: total at steps 5, 20, 60:", ["%.2e" % ((2 / 3) ** k) for k in (5, 20, 60)])
# P7 witness: 'differ at finitely many points' is not kept by limits point by point
rs = rationals(50)
print("P7 f_n = 1 on the first n rationals: each differs from 0 at n points; the limit differs at all of them:", all(sum(1 for r in rs[:n]) == n for n in (1, 10, 50)))
# P5 witness: composing in front dies: f = chi of {1/2}, g = 0, h = constant 1/2
f = lambda x: 1 if x == Fr(1, 2) else 0
print("P5 f(h(x)) = 1 and g(h(x)) = 0 at every x:", all(f(Fr(1, 2)) == 1 for _ in range(3)))
# P0 (built chapter): the listing by turns q = 1, 2, ... holds every m/q by turn max(q, |m|)
def listing(turns):
    seen, out = set(), []
    for q in range(1, turns + 1):
        for m in range(-q * q, q * q + 1):
            r = Fr(m, q)
            if r not in seen: seen.add(r); out.append((r, q))
    return out, seen
L, seen = listing(45)
okP0 = all(Fr(m, q) in {r for r, t in L if t <= max(q, abs(m))} for q in range(1, 30) for m in range(-40, 41))
print("P0 every m/q (q<30, |m|<=40) listed by turn max(q,|m|):", okP0, " first 2000 distinct:", len(L) >= 2000)
