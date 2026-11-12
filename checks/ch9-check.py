# Checks for Chapter 9 (angles). Complex numbers stand for arrows in R^2.
import random, cmath
random.seed(2)
def q(u,v): w=u.conjugate()*v; return w/abs(w)
def rnd(): 
    while True:
        z=complex(random.uniform(-5,5),random.uniform(-5,5))
        if abs(z)>1e-3: return z
ok_inv=ok_nf=ok_add=ok_cos=ok_swap=True
for _ in range(1000):
    u,v,w,z=rnd(),rnd(),rnd(),rnd(); r=random.uniform(0.01,9)
    ok_inv &= abs(q(z*u,z*v)-q(u,v))<1e-9 and abs(q(u,r*v)-q(u,v))<1e-9
    nf=v/u; nf/=abs(nf)                      # normal form ((1,0), nf)
    ok_nf &= abs(nf-q(u,v))<1e-9
    ok_add &= abs(q(u,v)*q(v,w)-q(u,w))<1e-9   # corners compose
    dot=u.real*v.real+u.imag*v.imag
    ok_cos &= abs(q(u,v).real-dot/(abs(u)*abs(v)))<1e-9
    ok_swap &= abs(q(v,u)-q(u,v).conjugate())<1e-9
roots=[cmath.exp(2j*cmath.pi*k/6) for k in range(6)]
ok_clock=all(abs(roots[(a+b)%6]-roots[a]*roots[b])<1e-9 for a in range(6) for b in range(6))
print("invariant:",ok_inv,"| normal form:",ok_nf,"| angles add:",ok_add,"| real part = cos formula:",ok_cos,"| swap = conjugate:",ok_swap,"| Z/6 inside:",ok_clock)
