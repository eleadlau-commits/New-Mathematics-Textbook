# Chapter 24 (design) check: the rung 2 blur at a point of R^n and what it keeps.
import random, math, itertools
random.seed(24)
def Q(q, h):  # symmetric matrix q, arrow h
    n = len(h); return sum(q[i][j] * h[i] * h[j] for i in range(n) for j in range(n))
def rand_sym(n):
    q = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n): q[i][j] = q[j][i] = random.uniform(-2, 2)
    return q
def cube_faces_min_max(q, n, grid=21):
    # lowest and highest value of Q on the faces of the cube max|h_i| = 1 (finitely many closed boxes)
    lo, hi = 1e9, -1e9; pts = [-1 + 2 * i / (grid - 1) for i in range(grid)]
    for i in range(n):
        for s in (-1, 1):
            for rest in itertools.product(pts, repeat=n - 1):
                h = list(rest[:i]) + [s] + list(rest[i:]); v = Q(q, h)
                lo, hi = min(lo, v), max(hi, v)
    return lo, hi
def cubic(c, h):  # a third-order term: what the rung 2 blur glues away
    n = len(h); return sum(c[i][j][k] * h[i] * h[j] * h[k] for i in range(n) for j in range(n) for k in range(n))
okT1 = okT3 = okP = True; nT1 = nT3 = 0
for _ in range(3000):
    n = random.choice([1, 2, 3]); q = rand_sym(n)
    c = [[[random.uniform(-5, 5) for _ in range(n)] for _ in range(n)] for _ in range(n)]
    lo, hi = cube_faces_min_max(q, n)
    K = sum(abs(c[i][j][k]) for i in range(n) for j in range(n) for k in range(n))
    slack = 2 * n * 2 * math.sqrt(n) / 20   # the grid can miss the true lowest value by at most this
    if lo - slack > 0.05:  # positive: P3 bound and T1 (strict lowest point survives the glued-away part)
        lo -= slack; nT1 += 1; r = lo / (2 * K)           # inside max|h_i| < r the cubic part cannot win
        for _ in range(200):
            h = [random.uniform(-r, r) for _ in range(n)]; m = max(abs(x) for x in h)
            if m == 0: continue
            okP &= Q(q, h) >= lo * m * m - 1e-12
            okT1 &= Q(q, h) + cubic(c, h) > 0
    if lo < -0.05 and hi > 0.05:  # both signs: neither. Go along an arrow where Q < 0 and one where Q > 0.
        nT3 += 1
        best = {}
        for _ in range(4000):
            h = [random.uniform(-1, 1) for _ in range(n)]; v = Q(q, h)
            if v < best.get('lo', (0,))[0]: best['lo'] = (v, h)
            if v > best.get('hi', (0,))[0]: best['hi'] = (v, h)
        if 'lo' not in best or 'hi' not in best: nT3 -= 1; continue
        for key, sign in (('lo', -1), ('hi', 1)):
            v, h = best[key]; t = abs(v) / (2 * K)     # for 0 < t' <= t the cubic part cannot win
            for tt in (t, t / 10, t / 1000):
                okT3 &= sign * (Q(q, [tt * x for x in h]) + cubic(c, [tt * x for x in h])) > 0
print("P3 bound Q(h) >= m max|h_i|^2:", okP)
print("T1 strict lowest point kept under glued-away cubic (", nT1, "forms ):", okT1)
print("T3 both signs kept at every scale (", nT3, "forms ):", okT3)
# T2 witnesses: same bag at rung 2, different answers
x = [i / 1000 for i in range(-100, 101) if i != 0]
print("x^4 lowest, -x^4 highest, x^3 neither:", all(t**4 > 0 for t in x), all(-t**4 < 0 for t in x), min(t**3 for t in x) < 0 < max(t**3 for t in x))
print("x^2+y^4 lowest:", all(a*a + b**4 > 0 for a in x[::10] for b in x[::10]), "; x^2-y^4 not: value at (0,0.1) =", 0 - 0.1**4)
# n = 2 test by the determinant: q11 > 0 and q11 q22 - q12^2 > 0 <=> positive
ok = True
for _ in range(2000):
    q = rand_sym(2); d = q[0][0] * q[1][1] - q[0][1] ** 2
    if abs(d) < 1e-3 or abs(q[0][0]) < 1e-3: continue
    pos = all(Q(q, [math.cos(t), math.sin(t)]) > 0 for t in [i * math.pi / 180 for i in range(360)])
    both = d < 0
    signs = [Q(q, [math.cos(t), math.sin(t)]) for t in [i * math.pi / 180 for i in range(360)]]
    ok &= pos == (q[0][0] > 0 and d > 0)
    ok &= both == (min(signs) < 0 < max(signs))
print("n = 2: determinant test agrees:", ok)
# P2: normal form from second slopes, f = exp(x) cos(y) + x y^2 at a = (0.3, -0.2); error / |h|^2 comes near 0
f = lambda x, y: math.exp(x) * math.cos(y) + x * y * y
a, b = 0.3, -0.2
fx = math.exp(a) * math.cos(b) + b * b; fy = -math.exp(a) * math.sin(b) + 2 * a * b
fxx = math.exp(a) * math.cos(b); fxy = -math.exp(a) * math.sin(b) + 2 * b; fyy = -math.exp(a) * math.cos(b) + 2 * a
ratios = []
for s in (1e-1, 1e-2, 1e-3):
    worst = 0
    for _ in range(200):
        t = random.uniform(0, 2 * math.pi); h, k = s * math.cos(t), s * math.sin(t)
        nf = f(a, b) + fx * h + fy * k + 0.5 * (fxx * h * h + 2 * fxy * h * k + fyy * k * k)
        worst = max(worst, abs(f(a + h, b + k) - nf) / (s * s))
    ratios.append(worst)
print("P2 error/|h|^2 at scales 1e-1, 1e-2, 1e-3:", ["%.1e" % r for r in ratios])
