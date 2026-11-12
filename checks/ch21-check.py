# Checks for Chapter 21 (Taylor). Needs sympy (pip install sympy).
import sympy as sp, random, math
x = sp.symbols('x')
random.seed(5)
# P5: products of straight bags at rung k = products in R[x]/(x^(k+1)), against sympy series of the product of two maps
funcs = [sp.exp(x), sp.sin(x)+2, sp.cos(3*x), 1/(1-x), sp.log(1+x)+1, sp.sqrt(1+x)]
ok = True
for k in range(0, 6):
    for f in funcs:
        for g in funcs:
            tf = sp.series(f, x, 0, k+1).removeO(); tg = sp.series(g, x, 0, k+1).removeO()
            trunc = sp.expand(sp.series(sp.expand(tf*tg), x, 0, k+1).removeO())
            direct = sp.expand(sp.series(f*g, x, 0, k+1).removeO())
            ok &= sp.simplify(trunc - direct) == 0
print("P5 product of normal forms, truncated at x^(k+1), is the normal form of the product (k<=5, 36 pairs):", ok)
# P6: (f - Taylor_k)/x^k comes near 0: numerically at x = 10^-3, 10^-5 for exp at a = 0.7
a = 0.7
def taylor_exp(a, k, h): return sum(math.exp(a)*h**i/math.factorial(i) for i in range(k+1))
print("P6 exp at a=0.7, k=3: (f - T_3)/h^3 at h=1e-1,1e-2,1e-3:", ["%.1e" % ((math.exp(a+h)-taylor_exp(a, 3, h))/h**3) for h in (1e-1, 1e-2, 1e-3)])
# P8: exp(-1/x^2) glued to 0 at every rung at 0 (limit is 0 for every k), and nonzero for x != 0
f = sp.exp(-1/x**2)
print("P8 limit of exp(-1/x^2)/x^k as x->0, k=1,5,20:", [sp.limit(f/x**k, x, 0) for k in (1, 5, 20)], "| value at x=0.5:", float(f.subs(x, 0.5)))
# T2: Lagrange remainder bound for exp: |exp(h) - T_k(h)| <= exp(|h|) |h|^(k+1)/(k+1)!
okr = all(abs(math.exp(h) - taylor_exp(0, k, h)) <= math.exp(abs(h))*abs(h)**(k+1)/math.factorial(k+1) + 1e-15 for h in (-2.5, -1, -0.3, 0.4, 1.7, 3) for k in range(0, 12))
print("T2 remainder bound for exp at six points, k<=11:", okr)
# T3: Taylor sums of cos at x=10 come near cos(10)
print("T3 cos at x=10: Taylor sums to order 20, 40, 60:", [round(sum((-1)**i*10**(2*i)/math.factorial(2*i) for i in range(n//2+1)), 6) for n in (20, 40, 60)], "cos(10) =", round(math.cos(10), 6))
