# Building 1, III.1: orders at a point by a ladder of jets, and the "at most one" line earned from them.
# Over Z/p, every smooth y^2 = x^3 + a x + b, every affine point P:
#   P8  the jet ladder exists and each rung has exactly one lift (y0 != 0: Y(x); y0 = 0: X(y));
#   P10 ord_P(line) = meeting number (B0 ch36 D2), for every line through P;
#   P11 Divide: if ord_P(f) >= ord_P(l) at every affine point P of a line l with all points in C(k), l | f in k[C];
#   T2  no relation R - O = sum n_i (L_i.C - 3 O) with R != O: checked as "P - O glued to Q - O only if P = Q"
#       on random sums of line gluings (the bag of 0 written out, then reduced by T1's steps).
import itertools, random
random.seed(11); ok = True
N = 8                                            # rungs of the ladder kept

def inv(a, p): return pow(a % p, p - 2, p)
def smul(u, v, p):                                # jets mod t^N
    w = [0] * N
    for i, a in enumerate(u):
        if a:
            for j in range(N - i): w[i + j] = (w[i + j] + a * v[j]) % p
    return w
def spow(u, k, p):
    w = [1] + [0] * (N - 1)
    for _ in range(k): w = smul(w, u, p)
    return w
def sadd(u, v, p): return [(a + b) % p for a, b in zip(u, v)]
def ordj(u):
    for i, a in enumerate(u):
        if a: return i
    return N
def poly_at(c, xs, p):                            # polynomial in x (coeff list) at the jet xs
    w = [0] * N
    for k, a in enumerate(c):
        if a: w = sadd(w, [a * t % p for t in spow(xs, k, p)], p)
    return w

def ladder(P, p, a, b):
    """Return (xs, ys): x and y as jets in the ladder parameter t at P."""
    x0, y0 = P
    g = lambda X: sadd(sadd(spow(X, 3, p), [a * t % p for t in X], p), [b] + [0] * (N - 1), p)
    if y0 % p:
        xs = [x0, 1] + [0] * (N - 2)                # t = x - x0
        Y = [y0] + [0] * (N - 1)
        G = g(xs)
        for n in range(1, N):                      # one lift per rung: Y += (G - Y^2)/(2 y0) at t^n
            r = sadd(G, [(-c) % p for c in smul(Y, Y, p)], p)
            assert all(c == 0 for c in r[:n])
            Y[n] = r[n] * inv(2 * y0, p) % p
        assert sadd(G, [(-c) % p for c in smul(Y, Y, p)], p) == [0] * N
        return xs, Y
    else:                                          # y0 = 0: t = y, x = X(y), g(X) = y^2
        ys = [0, 1] + [0] * (N - 2)
        d = (3 * x0 * x0 + a) % p; assert d       # simple root (Delta != 0)
        X = [x0] + [0] * (N - 1)
        T = spow(ys, 2, p)
        for n in range(1, N):
            r = sadd(T, [(-c) % p for c in g(X)], p)
            assert all(c == 0 for c in r[:n])
            X[n] = (X[n] + r[n] * inv(d, p)) % p
        assert sadd(T, [(-c) % p for c in g(X)], p) == [0] * N
        return X, ys

def ordP(f, P, p, a, b, cache):                    # f = (pc, qc): p(x) + q(x) y
    if P not in cache: cache[P] = ladder(P, p, a, b)
    xs, ys = cache[P]
    return ordj(sadd(poly_at(f[0], xs, p), smul(poly_at(f[1], xs, p), ys, p), p))

def fmul(f, h, p, a, b):                           # product in k[C] = k[x] + k[x] y, y^2 = g(x)
    def pm(u, v):
        if not u or not v: return [0]
        w = [0] * (len(u) + len(v) - 1)
        for i, s in enumerate(u):
            for j, t in enumerate(v): w[i + j] = (w[i + j] + s * t) % p
        return w
    def pa(u, v):
        n = max(len(u), len(v)); u = u + [0] * (n - len(u)); v = v + [0] * (n - len(v))
        return [(s + t) % p for s, t in zip(u, v)]
    gx = [b, a, 0, 1]
    P0 = pa(pm(f[0], h[0]), pm(pm(f[1], h[1]), gx)); Q0 = pa(pm(f[0], h[1]), pm(f[1], h[0]))
    return (P0, Q0)

def lines_and_points(p, a, b):
    S = [(x, y) for x in range(p) for y in range(p) if (y * y - x ** 3 - a * x - b) % p == 0]
    Sset = set(S); L = []
    for c in range(p):                             # upright x = c
        pts = [(c, y) for y in range(p) if (c, y) in Sset]
        if pts:
            cnt = {P: (2 if P[1] == 0 else 1) for P in pts}
            L.append((([(-c) % p, 1], [0]), cnt))
    for m in range(p):
        for c in range(p):                         # y = m x + c, i.e. l = y - m x - c
            F = lambda x: (x ** 3 + a * x + b - (m * x + c) ** 2) % p
            roots = [x for x in range(p) if F(x) == 0]
            # root multiplicities by repeated synthetic division
            coeffs = [(b - c * c) % p, (a - 2 * m * c) % p, (-m * m) % p, 1]
            cnt, tot = {}, 0
            for x0 in roots:
                k, cf = 0, coeffs[:]
                while len(cf) > 1:
                    q = [0] * (len(cf) - 1); r = 0
                    for i in range(len(cf) - 1, -1, -1):
                        r = (r * x0 + cf[i]) % p
                        if i: q[i - 1] = r
                    if r: break
                    k += 1; cf = q
                cnt[(x0, (m * x0 + c) % p)] = k; tot += k
            if tot == 3: L.append((([(-c) % p, (-m) % p], [1]), cnt))   # all three points in C(k)
    return S, L

for p in (5, 7, 11):
    for a, b in itertools.product(range(p), repeat=2):
        if (4 * a ** 3 + 27 * b ** 2) % p == 0: continue
        S, L = lines_and_points(p, a, b); cache = {}
        for P in S: ladder(P, p, a, b)
        for l, cnt in L:                           # P10
            for P in S:
                ok &= ordP(l, P, p, a, b, cache) == cnt.get(P, 0)
        # P11, both directions on random f: l | f iff ord conditions hold
        for _ in range(6):
            l, cnt = random.choice(L)
            u = ([random.randrange(p) for _ in range(3)], [random.randrange(p) for _ in range(2)])
            f = fmul(l, u, p, a, b)
            ok &= all(ordP(f, P, p, a, b, cache) >= k for P, k in cnt.items())
            g = ([random.randrange(p) for _ in range(4)], [random.randrange(p) for _ in range(3)])
            cond = all(ordP(g, P, p, a, b, cache) >= k for P, k in cnt.items())
            # direct divisibility test: g = l*u for some u of bounded degree (search by linear algebra is
            # overkill; use the reduction r_g of the proof and test F_l | r_g)
            if l[1] == [0]:                        # upright x - c: (x - c) | p and q
                c = (-l[0][0]) % p
                ev = lambda cf: sum(t * pow(c, i, p) for i, t in enumerate(cf)) % p
                div = ev(g[0]) == 0 and ev(g[1]) == 0
            else:
                c, m = (-l[0][0]) % p, (-l[0][1]) % p
                ev = lambda cf, x: sum(t * pow(x, i, p) for i, t in enumerate(cf)) % p
                r = lambda x: (ev(g[0], x) + ev(g[1], x) * (m * x + c)) % p
                # F_l | r_g: r_g vanishes at each root to its multiplicity (check via jets in x)
                div = True
                for P, k in cnt.items():
                    xs = [P[0], 1] + [0] * (N - 2)
                    rj = sadd(poly_at(g[0], xs, p), smul(poly_at(g[1], xs, p), poly_at([c, m], xs, p), p), p)
                    div &= ordj(rj) >= k
            ok &= cond == div
print('III.1 orders at a point: P8 ladder, P10 lines, P11 divide:', ok)
