# Checks for Chapter 20 (sequences of maps).
import math
grid = lambda b, c, m=20001: [b + (c-b)*i/(m-1) for i in range(m)]
G01, G09 = grid(0, 1), grid(0, 0.9)
lim = lambda x: 1.0 if x == 1 else 0.0
print("P5 x^n on 0<=x<=1: largest gap to the jump map on the grid, n=10,100,1000:",
      [round(max(abs(x**n - lim(x)) for x in G01), 3) for n in (10, 100, 1000)], "(stays near 1: for every n some x below 1 has x^n > 1/2)")
print("   on 0<=x<=0.9 the gap is 0.9^n:", [round(max(abs(x**n) for x in G09), 6) for n in (10, 100, 1000)])
print("   integral of x^n on [0,1] = 1/(n+1):", [round(1/(n+1), 4) for n in (10, 100, 1000)])
def tent(n, x):
    if x <= 1/n: return n*n*x
    if x <= 2/n: return 2*n - n*n*x
    return 0.0
def integral(f, b, c, m=200001):
    h = (c-b)/(m-1); return h*(sum(f(b+i*h) for i in range(m)) - (f(b)+f(c))/2)
print("P9 tents: integral on [0,1] for n=10,100,1000:", [round(integral(lambda x: tent(n, x), 0, 1), 4) for n in (10, 100, 1000)],
      "| value at x=0.05 for n=10,100,1000:", [tent(n, 0.05) for n in (10, 100, 1000)])
G = grid(-3, 3)
print("P10 sin(n^2 x)/n: largest size on [-3,3] for n=10,100:", [round(max(abs(math.sin(n*n*x)/n) for x in G), 4) for n in (10, 100)],
      "| derivative n cos(n^2 x) at 0:", [n*math.cos(0) for n in (10, 100)])
def s(N, x): return sum(x**k/math.factorial(k) for k in range(N+1))
print("T5 exp partial sums in M on [-3,3]: largest gap for N=5,10,20,30:", ["%.1e" % max(abs(math.exp(x)-s(N, x)) for x in G[::50]) for N in (5, 10, 20, 30)])
ds = lambda N, x: sum(k*x**(k-1)/math.factorial(k) for k in range(1, N+1))
print("T5 term-by-term derivative of the exp series equals the series (N=30, 61 points):", max(abs(ds(30, x) - s(29, x)) for x in G[::100]) < 1e-12)
print("R2 edge: sums of x^n/n at x=-1 (settle near -log 2 = %.4f):" % -math.log(2), [round(sum((-1)**n/n for n in range(1, M)), 4) for M in (10**3, 10**5)],
      "| at x=1 (grow):", [round(sum(1/n for n in range(1, M)), 2) for M in (10**3, 10**5)])
