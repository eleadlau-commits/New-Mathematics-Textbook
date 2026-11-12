# Checks for Chapter 17 (orders of magnitude): ratios on large n.
import math
N=[10**k for k in range(3,8)]
def ratio_bounded(a,b): # a <~ b: a_n/b_n stays bounded on the sample
    r=[a(n)/b(n) for n in N]; return max(r) < 10*r[0]+1
def glued(a,b): return ratio_bounded(a,b) and ratio_bounded(b,a)
print("n+1 ~ n:",glued(lambda n:n+1,lambda n:n), "| n^2+n ~ n^2:", glued(lambda n:n*n+n,lambda n:n*n), "| n+n^2 ~ max:", glued(lambda n:n+n*n, lambda n:max(n,n*n)))
print("log n strictly below n^0.1 (ratio falls):", [round(math.log(n)/n**0.1,3) for n in [10**k for k in (6,12,24,48)]])
print("n^5 strictly below 2^n:", [n**5/2**n for n in (50,100,200)])
print("2^n strictly below n!:", [2**n/math.factorial(n) for n in (10,20,40)])
osc=lambda n: n**((-1)**n)
print("n^((-1)^n) vs 1: ratio along even n", [osc(n) for n in (10,100,1000)], "along odd n", [osc(n) for n in (11,101,1001)])
s=lambda f,M: sum(f(n) for n in range(1,M))
print("sum 1/n grows:", [round(s(lambda n:1/n,M),3) for M in (10**3,10**5,10**6)], "| sum 1/n^2 settles:", [round(s(lambda n:1/n**2,M),6) for M in (10**3,10**5,10**6)])
print("sum 3/n^2+1/n^3 settles too (same bag as 1/n^2):", [round(s(lambda n:3/n**2+1/n**3,M),6) for M in (10**3,10**5,10**6)])
