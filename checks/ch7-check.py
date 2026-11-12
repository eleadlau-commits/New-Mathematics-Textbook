# Checks for Chapter 6 (polynomials). Polynomials are lists of coefficients, lowest first.
from fractions import Fraction as F
import random
def trim(p):
    p=list(p)
    while p and p[-1]==0: p.pop()
    return p
def add(p,q):
    n=max(len(p),len(q)); return trim([(p[i] if i<len(p) else 0)+(q[i] if i<len(q) else 0) for i in range(n)])
def mul(p,q):
    if not p or not q: return []
    r=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): r[i+j]+=a*b
    return trim(r)
def ev(p,t): return sum(a*t**i for i,a in enumerate(p))
def red(p,rule):            # reduce modulo x^2 = rule[0] + rule[1] x  -> pair (a,b)
    a,b=F(0),F(0); pw=(F(1),F(0))
    for c in p:
        a+=c*pw[0]; b+=c*pw[1]
        pw=(pw[1]*rule[0], pw[0]+pw[1]*rule[1])
    return (a,b)
def der(p): return trim([i*a for i,a in enumerate(p)][1:])
random.seed(1)
rp=lambda: trim([F(random.randint(-5,5)) for _ in range(random.randint(1,6))])
ok3=ok4=okC=True
for _ in range(300):
    p,q=rp(),rp(); a=F(random.randint(-4,4))
    # Road 3 (x^2 ~ 0): p(a + x) = p(a) + p'(a) x
    shifted=[]; 
    for i,c in enumerate(p):
        term=[c]
        for _k in range(i): term=mul(term,[a,F(1)])
        shifted=add(shifted,term)
    ok3&= red(shifted,(F(0),F(0)))==(ev(p,a),ev(der(p),a))
    # Road 4 (x^2 ~ 1): bag of p is known by (p(1), p(-1)), and products match place by place
    A,B=red(mul(p,q),(F(1),F(0)))
    ok4&= (A+B, A-B)==(ev(p,1)*ev(q,1), ev(p,-1)*ev(q,-1))
    # Road 2 (x^2 ~ -1): product rule (a+bx)(c+dx) = (ac-bd) + (ad+bc)x
    (a1,b1),(c1,d1)=red(p,(F(-1),F(0))),red(q,(F(-1),F(0)))
    okC&= red(mul(p,q),(F(-1),F(0)))==(a1*c1-b1*d1, a1*d1+b1*c1)
print("Road 3 derivative rule:",ok3,"| Road 4 = pairs:",ok4,"| Road 2 product:",okC)
print("Over Z/7: x^7 and x have the same values:", all((t**7-t)%7==0 for t in range(7)), "(different coefficient lists)")
