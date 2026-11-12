# Building 1, II.11 (extensions) and II.12 (finite fields).
import itertools, math, random, sympy as sp
from sympy import Poly, GF, symbols, minimal_polynomial, sqrt, cbrt, cos, pi, Rational, totient, divisors
from sympy.functions.combinatorial.numbers import mobius
random.seed(11); ok = True
x = symbols('x')
# II.11 minimal polynomials and degrees; tower law examples
def deg(a): return sp.degree(minimal_polynomial(a, x), x)
ok &= deg(cbrt(2)) == 3 and deg(sqrt(2) + sqrt(3)) == 4 and deg(cbrt(2) + sqrt(3)) == 6
ok &= deg(cbrt(2) * sp.exp(2*sp.pi*sp.I/3)) == 3
# splitting field of x^3 - 2: Q(cbrt2, w) has degree 6 = 3 * 2 (w satisfies x^2+x+1, irreducible over Q(cbrt2) since that field is real)
ok &= deg(cbrt(2) + sp.sqrt(-3)) == 6
# trisection: cos(20 deg) has minimal polynomial of degree 3
ok &= minimal_polynomial(cos(pi/9), x) == 8*x**3 - 6*x - 1
# constructible degrees: cos(2pi/17) degree 8 = 2^3; cos(2pi/7) degree 3
ok &= deg(cos(2*pi/17)) == 8 and deg(cos(2*pi/7)) == 3
# K[x]/(f) is a field for irreducible f over Z/p: every nonzero class has an inverse
def is_field(f, p):
    F = Poly(f, x, modulus=p); n = F.degree()
    for coeffs in itertools.product(range(p), repeat=n):
        if not any(coeffs): continue
        g = Poly(list(coeffs), x, modulus=p)
        s, t, h = sp.gcdex(g, F)
        if h.degree() != 0: return False
    return True
ok &= is_field(x**2 + 1, 3) and not is_field(x**2 + 1, 5) and is_field(x**3 + x + 1, 2)
print("II.11:", ok)
# II.12: GF(p^n) by an irreducible f; Frobenius respects + and x; multiplicative group cyclic
def gf_elems(p, n): return [Poly(list(c), x, modulus=p) for c in itertools.product(range(p), repeat=n)]
for p, f in [(2, x**3 + x + 1), (3, x**2 + 1), (2, x**4 + x + 1), (5, x**2 + 2), (3, x**3 + 2*x + 1)]:
    F = Poly(f, x, modulus=p); n = F.degree(); q = p**n
    ok &= F.is_irreducible
    E = [e for e in gf_elems(p, n)]
    red = lambda g: g.rem(F)
    frob = lambda g: red(g**p)
    for _ in range(30):
        a, b = random.choice(E), random.choice(E)
        ok &= frob(red(a + b)) == red(frob(a) + frob(b)) and frob(red(a*b)) == red(frob(a)*frob(b))
    ok &= len({frob(e).as_expr() for e in E}) == q          # one-to-one, so onto
    # every member is a root of x^q - x
    ok &= all(red(e**q) == red(e) for e in E)
    # cyclic: some element has order q-1
    nz = [e for e in E if not e.is_zero]
    def order(e):
        k, g = 1, red(e)
        while not (g - 1).is_zero: g = red(g*e); k += 1
        return k
    ords = [order(e) for e in nz]
    ok &= (q - 1) in ords and all((q - 1) % o == 0 for o in ords)
    ok &= all(ords.count(d) == totient(d) for d in divisors(q - 1))
    # Frobenius has order exactly n
    for k in range(1, n):
        ok &= any(red(e**(p**k)) != red(e) for e in E)
print("II.12 fields:", ok)
# count of monic irreducibles of degree n over Z/p = (1/n) sum mu(d) p^(n/d)
for p in (2, 3):
    for n in range(1, 6 if p == 2 else 4):
        cnt = 0
        for c in itertools.product(range(p), repeat=n):
            if Poly([1] + list(c), x, modulus=p).is_irreducible: cnt += 1
        ok &= cnt == sum(mobius(d) * p**(n//d) for d in divisors(n)) // n
# x^(p^n) - x is the product of monic irreducibles of degree dividing n (degree count)
for p, n in [(2, 4), (3, 2), (2, 6)]:
    tot = sum(d * sum(mobius(e) * p**(d//e) for e in divisors(d)) // d for d in divisors(n))
    ok &= tot == p**n
print("ALL", ok)
