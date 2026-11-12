# Checks for Chapter 11 (the derivative) by comparing the slope of the line in each bag with small-step quotients.
import math, random
random.seed(4)
def slope(f, a, h=1e-6): return (f(a+h)-f(a-h))/(2*h)
fs = [lambda x: x**3-2*x, math.exp, lambda x: math.cos(2*math.pi*x), lambda x: math.sin(x)*x]
ok_prod = ok_chain = True
for _ in range(200):
    f, g = random.choice(fs), random.choice(fs); a = random.uniform(-1.5,1.5)
    ok_prod &= abs(slope(lambda x: f(x)*g(x), a) - (slope(f,a)*g(a)+f(a)*slope(g,a))) < 1e-5
    ok_chain &= abs(slope(lambda x: g(f(x)), a) - slope(g, f(a))*slope(f, a)) < 1e-4
ok_exp = all(abs(slope(math.exp,a)-math.exp(a))<1e-6 for a in [random.uniform(-2,2) for _ in range(100)])
ok_cos = all(abs(slope(lambda t: math.cos(2*math.pi*t),a)+2*math.pi*math.sin(2*math.pi*a))<1e-5 for a in [random.uniform(-2,2) for _ in range(100)])
# touch: e(x)=|x|^1.5 fades faster than x at 0; |x| does not
fast = max(abs(h)**1.5/abs(h) for h in [10**-k for k in range(5,9)]) < 1e-2
slow = min(abs(h)/abs(h) for h in [10**-k for k in range(4,9)]) == 1
# dual-number product matches product rule
dual = lambda p,q: (p[0]*q[0], p[0]*q[1]+p[1]*q[0])
ok_dual = all(dual((f(a),slope(f,a)),(g(a),slope(g,a)))[1]-slope(lambda x:f(x)*g(x),a) < 1e-5 for f in fs for g in fs for a in [0.3,-0.7])
print("product rule:",ok_prod,"| chain rule:",ok_chain,"| exp'=exp:",ok_exp,"| cos 2πt slope:",ok_cos,"| |x|^1.5 touches 0, |x| does not:",fast and slow,"| dual numbers carry the rule:",ok_dual)
