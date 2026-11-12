# Checks for Chapter II.4 (metric spaces). Most of the chapter is not machine-checkable; this checks what is.
import math, itertools, random
def tests_finite(pts, d):
    dist = all(d[x][y] >= 0 and (d[x][y] == 0) == (x == y) and d[x][y] == d[y][x] for x in pts for y in pts) and \
           all(d[x][z] <= d[x][y] + d[y][z] for x, y, z in itertools.product(pts, repeat=3))
    chains = all(d[x][z] <= max(d[x][y], d[y][z]) for x, y, z in itertools.product(pts, repeat=3))
    # onepiece: no split into two non-empty parts with every cross distance >= r for some r > 0 (finite: always cut if >= 2 points)
    cut = len(pts) >= 2 and min(d[x][y] for x in pts for y in pts if x != y) > 0
    return dist, chains, not cut
three = {a: {b: (0 if a == b else 1) for b in 'abc'} for a in 'abc'}
odd = {a: {b: 0 for b in 'abc'} for a in 'abc'}
for (a, b), v in {('a', 'b'): 1, ('b', 'c'): 1, ('a', 'c'): 1.5}.items(): odd[a][b] = odd[b][a] = v
print("three points, all distances 1: dist, chains, onepiece =", tests_finite('abc', three))
print("three points, distances 1, 1, 1.5: dist, chains, onepiece =", tests_finite('abc', odd))
def v(x, p):
    if x == 0: return math.inf
    k = 0
    while x % p == 0: x //= p; k += 1
    return k
dp = lambda x, y, p: 0 if x == y else p ** (-v(x - y, p))
random.seed(2)
for p in (2, 3, 5):
    S = [random.randint(-10**6, 10**6) for _ in range(150)] + [p**j for j in range(8)] + [0, 1, -1]
    ok = all(dp(x, z, p) <= max(dp(x, y, p), dp(y, z, p)) for x, y, z in itertools.product(S[:60], repeat=3))
    print("p = %d: p-adic distance chains (60^3 triples):" % p, ok)
for p in (2, 3):
    s = [sum((-p)**j for j in range(i + 1)) for i in range(12)]
    print("p = %d: sums 1 - p + p^2 - ...: d_p between term i and i+1 =" % p, [round(dp(s[i], s[i+1], p), 6) for i in range(5)],
          "| v_p((1+p)*term - 1) =", [v(t*(1+p) - 1, p) for t in s[:6]], "(comes near 1/(1+p), not in Z)")
p = 3
x = 0.3
for _ in range(60): x = math.cos(x)
print("Contraction: cos on 0<=x<=1 (factor sin 1 = %.3f): fixed point %.10f, cos of it %.10f" % (math.sin(1), x, math.cos(x)))
M = p**12; x = 0
for _ in range(14): x = (p*x + 1) % M
print("Contraction on Z_3: x -> 3x + 1 (factor 1/3), after 14 steps (1-3)*x = 1 mod 3^12:", ((1-p)*x) % M == 1)
f = lambda x: 1/(1 + math.exp(-x)); g = lambda t: math.log(t/(1 - t))
print("Logistic map R -> (0,1) and back: round trips", all(abs(g(f(x)) - x) < 1e-9 for x in [i/7 for i in range(-100, 101)]),
      "| image of [-30, 30] stays inside (0,1):", 0 < f(-30) and f(30) < 1, "| f increases:", all(f(i/10) < f((i+1)/10) for i in range(-300, 300)))
print("Inverse not uniform: g(t) - g(t/2) near 0 for t = 1e-3, 1e-6:", [round(g(t) - g(t/2), 4) for t in (1e-3, 1e-6)], "(gap of the inputs falls, gap of the outputs stays near log 2)")
