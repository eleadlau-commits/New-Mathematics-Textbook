# Chapter 23 (design) check: the local step and "far away is large".
import cmath, random
random.seed(23)
def ev(p, z):  # p = [a0, a1, ..., an]
    r = 0
    for c in reversed(p): r = r * z + c
    return r
def recentre(p, a):  # coefficients of p(a + h) in h (exact, by repeated division)
    p = list(p); out = []
    while p:
        q = [0] * (len(p) - 1); r = 0
        for i in range(len(p) - 1, -1, -1):
            r = r * a + p[i]
            if i > 0: q[i - 1] = r
        out.append(r); p = q
    return out
def kth_root(u, k):  # by the wrapping: u = r w(t), root = r^(1/k) w(t/k)
    r, t = abs(u), cmath.phase(u) / (2 * cmath.pi)
    return r ** (1.0 / k) * cmath.exp(2j * cmath.pi * t / k)
ok_desc = ok_far = ok_rec = True; trials = 0
for _ in range(400):
    n = random.randint(1, 7)
    p = [complex(random.uniform(-3, 3), random.uniform(-3, 3)) for _ in range(n + 1)]
    if random.random() < 0.4 and n >= 3: p[1] = 0          # force k > 1 at a = 0 sometimes
    a = 0 if random.random() < 0.4 else complex(random.uniform(-2, 2), random.uniform(-2, 2))
    c = recentre(p, a)
    h = complex(random.uniform(-1, 1), random.uniform(-1, 1))
    ok_rec &= abs(ev(c, h) - ev(p, a + h)) < 1e-8
    if abs(c[0]) < 1e-6: continue
    k = next(i for i in range(1, n + 1) if abs(c[i]) > 1e-12)
    h0 = kth_root(-c[0] / c[k], k)
    K = sum(abs(c[j]) * abs(h0) ** j for j in range(k + 1, n + 1))
    s = min(1.0, abs(c[0]) / (2 * K)) if K > 0 else 1.0
    ok_desc &= abs(ev(p, a + s * h0)) < abs(c[0]) * (1 - s ** k / 2 + 1e-12)
    R = max(1.0, 2 * sum(abs(x) for x in p[:-1]) / abs(p[-1]))
    z = R * random.uniform(1, 5) * cmath.exp(2j * cmath.pi * random.random())
    ok_far &= abs(ev(p, z)) >= abs(p[-1]) * abs(z) ** n / 2 - 1e-9
    trials += 1
print("re-centring exact:", ok_rec)
print("local step lowers |p| (", trials, "trials ):", ok_desc)
print("far away is large:", ok_far)
# the witness over R: x^2 + 1 has a lowest point at 0 that is not a root
print("x^2+1 on R: lowest value", min(x * x + 1 for x in [i / 1000 - 2 for i in range(4001)]))
# the theorem itself, by repeating the local step from a = 0
def descend(p, a=0j, steps=4000):
    for _ in range(steps):
        c = recentre(p, a)
        if abs(c[0]) < 1e-13: break
        k = next(i for i in range(1, len(c)) if abs(c[i]) > 1e-12)
        h0 = kth_root(-c[0] / c[k], k); s = 1.0
        while abs(ev(p, a + s * h0)) >= abs(c[0]) and s > 1e-16: s /= 2
        a = a + s * h0
    return a
bad = 0
for _ in range(100):
    n = random.randint(1, 6)
    p = [complex(random.uniform(-3, 3), random.uniform(-3, 3)) for _ in range(n + 1)]
    if abs(ev(p, descend(p))) > 1e-6: bad += 1
print("descent reached a root in", 100 - bad, "of 100 polynomials")
