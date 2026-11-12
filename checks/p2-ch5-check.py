# Chapter II.5 check: fractions, polynomials, determinants over any ring.
import sympy as sp, random, itertools
rel = lambda p, q, n: (p[0]*q[1] - p[1]*q[0]) % n == 0
print("P2 Z/6: (2,1)~(0,3), (0,3)~(0,1), not (2,1)~(0,1):", rel((2, 1), (0, 3), 6), rel((0, 3), (0, 1), 6), not rel((2, 1), (0, 1), 6))
x = sp.symbols('x')
print("P5 Z/4: (2x+1)^2 = 1:", sp.Poly((2*x + 1)**2, x, modulus=4).as_expr() == 1)
print("P6 Z[x]: x = q*2x + r has no integer q, r constant:", sp.div(x, 2*x, domain='ZZ'))
print("P7 roots of x^2-1 in Z/8:", [t for t in range(8) if (t*t - 1) % 8 == 0], "; most roots for n<=30:", max((sum(1 for t in range(n) if (t*t - 1) % n == 0), n) for n in range(2, 31)))
for n in (2, 3):
    A = sp.Matrix(n, n, sp.symbols('a0:%d' % (n*n))); B = sp.Matrix(n, n, sp.symbols('b0:%d' % (n*n)))
    ok1 = sp.expand((A*B).det() - A.det()*B.det()) == 0
    ok2 = sp.simplify(A*A.adjugate() - A.det()*sp.eye(n)) == sp.zeros(n)
    chi = (x*sp.eye(n) - A).det()
    cp = sp.Poly(chi, x).all_coeffs()
    M = sp.zeros(n)
    for c in cp: M = M*A + c*sp.eye(n)
    ok3 = sp.expand(M) == sp.zeros(n)
    print("P10/P12 symbolic n=%d: det(AB)=detA detB %s, A adj A = det I %s, Cayley-Hamilton %s" % (n, ok1, ok2, ok3))
random.seed(5); ok = True
for _ in range(200):
    m = random.choice([4, 6, 8, 9, 12]); A = sp.Matrix(3, 3, [random.randrange(m) for _ in range(9)]); B = sp.Matrix(3, 3, [random.randrange(m) for _ in range(9)])
    ok &= ((A*B).det() - A.det()*B.det()) % m == 0
print("P10 random 3x3 over Z/m:", ok)
inv_count = 0; ok = True
for a, b, c, d in itertools.product(range(4), repeat=4):
    det = (a*d - b*c) % 4
    has_inv = any(((a*e + b*g) % 4, (a*f + b*h) % 4, (c*e + d*g) % 4, (c*f + d*h) % 4) == (1, 0, 0, 1) for e, f, g, h in itertools.product(range(4), repeat=4))
    ok &= has_inv == (det in (1, 3)); inv_count += has_inv
print("P11 over Z/4: invertible iff det is a unit:", ok, "(", inv_count, "invertible of 256 )")
print("E1 (3x+1)(-3x+1) = 1 - 9x^2 = 1 in Z/9:", sp.Poly((3*x + 1)*(-3*x + 1), x, modulus=9).as_expr() == 1)
print("E2 divide x^3+2x+1 by x^2+1 over Z/3:", sp.div(sp.Poly(x**3 + 2*x + 1, x, modulus=3), sp.Poly(x**2 + 1, x, modulus=3)))
