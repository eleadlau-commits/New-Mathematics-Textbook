# Checks for Chapter 18 (divisibility and primes).
from math import gcd
def divides(a, b): return b == 0 if a == 0 else b % a == 0
# P3: + dies
print("P3: 1|2, 1|1, but 2|3?", divides(1,2), divides(1,1), divides(2,3))
# P5, P8: forced blur from -1~1 respecting x, and the blur kept by div_d in every context, on a window
W = range(-60, 61)
par = {x: x for x in W}
def find(x):
    while par[x] != x: par[x] = par[par[x]]; x = par[x]
    return x
def union(x, y): par[find(x)] = find(y)
union(-1, 1)
changed = True
while changed:
    changed = False
    for x in W:
        for z in W:
            for y in W:
                if find(x) == find(y) and x*z in par and y*z in par and find(x*z) != find(y*z):
                    union(x*z, y*z); changed = True
ok5 = all((find(a) == find(b)) == (b == a or b == -a) for a in W for b in W)
ok8 = all((all(divides(d, a*z) == divides(d, b*z) for d in W for z in range(-6, 7))) == (b == a or b == -a) for a in W for b in W)
print("P5 bags are {a,-a} (window |a|<=60):", ok5, "| P8 kept-by-div blur is the same:", ok8)
# factorisation
def factor(n):
    f, p = {}, 2
    while p*p <= n:
        while n % p == 0: f[p] = f.get(p, 0)+1; n //= p
        p += 1
    if n > 1: f[n] = f.get(n, 0)+1
    return f
M = 2000
F = [None] + [factor(n) for n in range(1, M+1)]
def v(p, n): return F[n].get(p, 0)
ok5v = True
for a in range(1, M+1):
    fa = F[a]
    for b in range(1, M+1):
        if divides(a, b) != all(e <= F[b].get(p, 0) for p, e in fa.items()): ok5v = False
print("T5 a|b iff v_p(a)<=v_p(b) for all p, 1<=a,b<=2000:", ok5v)
ok6 = True
for a in range(1, 301):
    for b in range(1, 301):
        g, l = gcd(a, b), a*b//gcd(a, b)
        ps = set(F[a]) | set(F[b])
        ok6 &= all(v(p, g) == min(v(p, a), v(p, b)) for p in ps) and all(factor(l).get(p, 0) == max(v(p, a), v(p, b)) for p in ps)
print("T6 gcd/lcm are min/max place by place (a,b<=300):", ok6)
# T7, T8: blurs mod n on a window of integers
X = range(-150, 151)
def blurrier(n, m):   # x =_m y  =>  x =_n y, on the window (n,m >= 1)
    return all((x - y) % n == 0 for x in X for y in X if (x - y) % m == 0)
ok7 = all(blurrier(n, m) == (m % n == 0) for n in range(1, 61) for m in range(1, 61))
def join_blur(n, m):  # least blur containing both, on residues mod n*m (a blur respecting + is periodic): generated subgroup
    N = n*m; reach = {0}; todo = [0]
    while todo:
        x = todo.pop()
        for s in (n, m, -n, -m):
            y = (x+s) % N
            if y not in reach: reach.add(y); todo.append(y)
    return min(r for r in reach if r > 0) if len(reach) > 1 else N
ok8 = all(all(((x-y) % n == 0 and (x-y) % m == 0) == ((x-y) % (n*m//gcd(n, m)) == 0) for x in range(0, 120) for y in (0, 1, 7))
          and join_blur(n, m) == gcd(n, m) for n in range(1, 61) for m in range(1, 61))
print("T7 blurrier iff divides (n,m<=60):", ok7, "| T8 meet = lcm, join = gcd:", ok8)
# T3 unique factorisation: count multisets of primes with product n
isprime = lambda n: n > 1 and all(n % d for d in range(2, int(n**0.5)+1))
P = [p for p in range(2, 5001) if isprime(p)]
from functools import lru_cache
@lru_cache(None)
def count(n, i):   # factorisations of n into primes >= P[i], nondecreasing
    if n == 1: return 1
    c = 0
    for j in range(i, len(P)):
        p = P[j]
        if p > n: break
        if n % p == 0: c += count(n//p, j)
    return c
print("T3 exactly one factorisation for 2<=a<=5000:", all(count(n, 0) == 1 for n in range(2, 5001)))
