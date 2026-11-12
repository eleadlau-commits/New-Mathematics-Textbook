# Checks for Chapter 10 (functions): exp by its series, 2*pi as the least turn, the wrapping map.
from fractions import Fraction
import math, random
def exp_series(z, terms=300):
    s, t = 0j, 1+0j
    for k in range(terms):
        s += t; t = t*z/(k+1)
    return s
random.seed(3)
ok_add = all(abs(exp_series(complex(a,b)+complex(c,d)) - exp_series(complex(a,b))*exp_series(complex(c,d))) < 1e-9
             for a,b,c,d in [[random.uniform(-2,2) for _ in range(4)] for _ in range(200)])
ok_unit = all(abs(abs(exp_series(1j*t))-1) < 1e-12 for t in [random.uniform(-10,10) for _ in range(200)])
# (float rounding in the series grows with |z|, so the wrapping checks use a 1e-5 tolerance)
# least t>0 with exp(it)=1: first t>0 where the second place returns to 0 from below, found by scanning then bisection
f = lambda t: exp_series(1j*t).imag
t, step = 0.1, 0.01
while not (f(t) < 0 and f(t+step) >= 0): t += step
lo, hi = t, t+step
for _ in range(60):
    mid = (lo+hi)/2
    if f(mid) < 0: lo = mid
    else: hi = mid
two_pi = (lo+hi)/2
print("exp(z+w)=exp(z)exp(w):", ok_add, "| |exp(it)|=1:", ok_unit, "| least turn =", round(two_pi,12), "matches 2*pi:", abs(two_pi-2*math.pi)<1e-9)
w = lambda t: exp_series(1j*two_pi*t)
ok_hom = all(abs(w(s+t)-w(s)*w(t))<1e-5 for s,t in [(random.uniform(-2,2),random.uniform(-2,2)) for _ in range(200)])
ok_ker = all(abs(w(n)-1)<1e-5 for n in range(-4,5)) and all(abs(w(k/7)-1)>1e-3 for k in range(1,7))
ok_quarter = abs(w(0.25)-1j) < 1e-9
print("w respects +:", ok_hom, "| w(t)=1 at whole t only (checked on sevenths):", ok_ker, "| w(1/4) = i:", ok_quarter)
