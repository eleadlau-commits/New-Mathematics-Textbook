# Chapter 36: a cubic in the plane.
import itertools, random, sympy as sp
random.seed(2); ok = True
x, y, m, x1, y1, x2, a, b, X = sp.symbols('x y m x1 y1 x2 a b X')
# T1 symbolic: on y = y1 + m(x - x1), the cubic g - y^2 has roots summing to m^2
g = x**3 + a*x + b
cub = sp.expand(g - (y1 + m*(x - x1))**2)
P = sp.Poly(cub, x)
ok &= sp.simplify(-P.coeff_monomial(x**2) / P.coeff_monomial(x**3) - m**2) == 0
# T2: discriminant of g is -(4a^3 + 27b^2)
ok &= sp.simplify(sp.discriminant(g, x) + (4*a**3 + 27*b**2)) == 0
def pts(p, A, B):
    S = [(u, v) for u in range(p) for v in range(p) if (v*v - u**3 - A*u - B) % p == 0]
    return S
def third(P, Q, p, A, B):
    (u1, v1), (u2, v2) = P, Q
    if P != Q and u1 == u2: return 'O'
    if P == Q:
        if v1 == 0: return 'O'
        mm = (3*u1*u1 + A) * pow(2*v1, p-2, p) % p
    else:
        mm = (v2 - v1) * pow(u2 - u1, p-2, p) % p
    u3 = (mm*mm - u1 - u2) % p; v3 = (v1 + mm*(u3 - u1)) % p
    return (u3, v3)
for p in (5, 7, 11, 13):
    for A, B in itertools.product(range(p), repeat=2):
        D = (4*A**3 + 27*B**2) % p
        S = pts(p, A, B)
        # T2: smooth iff D != 0 (singular affine point: y=0, g=g'=0)
        sing = [(u, v) for (u, v) in S if v == 0 and (3*u*u + A) % p == 0]
        ok &= (len(sing) == 0) == (D != 0)
        if D == 0: continue
        Sset = set(S)
        for P_ in S:
            for Q_ in S:
                R = third(P_, Q_, p, A, B)
                if R == 'O': continue
                ok &= R in Sset                                   # T1: third point on C
                # P2: the line meets C in exactly these (with count) -- check collinear
                (u1, v1), (u2, v2), (u3, v3) = P_, Q_, R
                if P_ != Q_:
                    ok &= ((u2-u1)*(v3-v1) - (v2-v1)*(u3-u1)) % p == 0
                    # P2: no other affine point on the line
                    on = [s for s in S if ((u2-u1)*(s[1]-v1) - (v2-v1)*(s[0]-u1)) % p == 0]
                    ok &= len(on) <= 3
print("T1, T2, P2 over Z/p:", ok)
# P5-P9 on random elements with a,b rational
A0, B0 = sp.Rational(-1), sp.Rational(1)
g0 = x**3 + A0*x + B0
def red(f):
    f = sp.expand(f)
    q, r = sp.div(sp.Poly(f, y), sp.Poly(y**2 - g0, y))
    return sp.expand(r.as_expr())
def w(f):
    f = red(f)
    if f == 0: return -1
    pp = sp.Poly(f, y)
    p0 = pp.coeff_monomial(1); q0 = pp.coeff_monomial(y)
    cands = []
    if p0 != 0: cands.append(2*sp.degree(p0, x))
    if q0 != 0: cands.append(2*sp.degree(q0, x) + 3)
    return max(cands)
def N(f):
    f = red(f); return sp.expand(red(f * f.subs(y, -y)))
for _ in range(30):
    f = sum(random.randint(-3, 3)*x**i for i in range(random.randint(0, 4))) + y*sum(random.randint(-3, 3)*x**i for i in range(random.randint(0, 3)))
    h = sum(random.randint(-3, 3)*x**i for i in range(random.randint(0, 4))) + y*sum(random.randint(-3, 3)*x**i for i in range(random.randint(0, 3)))
    if red(f) == 0 or red(h) == 0: continue
    ok &= w(f*h) == w(f) + w(h)                                     # P9
    Nf = N(f); ok &= not Nf.has(y) and sp.degree(Nf, x) == w(f)     # P7, P8
ws = set()
for i in range(21):
    ws.add(2*i); ws.add(2*i + 3)
ok &= 1 not in ws and all(n in ws for n in [0] + list(range(2, 40)))  # P10
print("ALL", ok)
