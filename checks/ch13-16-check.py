# Checks for Chapters 13-16 (several variables, signed area, the arrow d, Stokes and the holes).
import sympy as sp, numpy as np, itertools, math, random
x,y,z,t = sp.symbols('x y z t', real=True)
random.seed(6); np.random.seed(6)
# ---- Chapter 13
f = x*y/(x**2+y**2)
print("12 P: partials of xy/(x^2+y^2) at 0 are 0 (f=0 on both axes); along y=x the value is", sp.simplify(f.subs(y,x)), "so not continuous, not straight")
g = x*y*(x**2-y**2)/(x**2+y**2)
gx = sp.diff(g,x); gy = sp.diff(g,y)
gxy0 = sp.limit(sp.simplify(gx.subs(x,0))/y, y, 0); gyx0 = sp.limit(sp.simplify(gy.subs(y,0))/x, x, 0)
print("12 R: mixed partials at 0 of xy(x^2-y^2)/(x^2+y^2):", gxy0, gyx0)
h = sp.exp(x*y)*sp.sin(x+y**2)+x**3*y
print("12 T5: mixed partials agree for a smooth map:", sp.simplify(sp.diff(h,x,y)-sp.diff(h,y,x))==0)
F = sp.Matrix([x**2-y, sp.sin(x*y)]); G = sp.exp(x)*y   # g∘F
comp = G.subs({x:F[0], y:F[1]}, simultaneous=True)
lhs = sp.Matrix([[sp.diff(comp,x), sp.diff(comp,y)]])
dG = sp.Matrix([[sp.diff(G,x), sp.diff(G,y)]]).subs({x:F[0], y:F[1]}, simultaneous=True)
print("12 T2: chain rule d(g∘f) = dg·Df:", sp.simplify(lhs - dG*F.jacobian([x,y])) == sp.zeros(1,2))
# ---- Chapter 14: exterior algebra as normal forms (sorted index tuples)
def wedge_basis(I,J):
    L=list(I)+list(J)
    if len(set(L))<len(L): return 0,None
    sign=1; L2=L[:]
    for i in range(len(L2)):
        for j in range(len(L2)-1-i):
            if L2[j]>L2[j+1]: L2[j],L2[j+1]=L2[j+1],L2[j]; sign=-sign
    return sign,tuple(L2)
def wedge(a,b):
    out={}
    for I,ca in a.items():
        for J,cb in b.items():
            s,K=wedge_basis(I,J)
            if s: out[K]=out.get(K,0)+s*ca*cb
    return {k:v for k,v in out.items() if abs(v)>1e-12}
vec = lambda v: {(i,):float(c) for i,c in enumerate(v)}
ok_sq=ok_anti=ok_det=True
for n in [2,3,4]:
    for _ in range(50):
        u,v=np.random.randn(n),np.random.randn(n)
        ok_sq &= wedge(vec(u),vec(u))=={}
        a,b=wedge(vec(u),vec(v)),wedge(vec(v),vec(u))
        ok_anti &= all(abs(a.get(k,0)+b.get(k,0))<1e-9 for k in set(a)|set(b))
        M=np.random.randn(n,n); w={():1.0}
        for r in M: w=wedge(w,vec(r))
        ok_det &= abs(w.get(tuple(range(n)),0)-np.linalg.det(M))<1e-9
dims=[[math.comb(n,k) for k in range(n+1)] for n in [1,2,3,4]]
print("13: v^v=0:",ok_sq,"| u^v=-v^u:",ok_anti,"| v1^...^vn = det:",ok_det,"| dims C(n,k):",dims)
# n=1: (c+m e)(d+k e) = cd + (ck+md) e
p={():2.0,(0,):3.0}; q={():5.0,(0,):7.0}
print("13 T: Λ(R) is the dual numbers:", wedge(p,q)=={():10.0,(0,):29.0})
# ---- Chapter 15: d in R^3, grad curl div
X=[x,y,z]
grad=lambda f: sp.Matrix([sp.diff(f,v) for v in X])
curl=lambda F: sp.Matrix([sp.diff(F[2],y)-sp.diff(F[1],z), sp.diff(F[0],z)-sp.diff(F[2],x), sp.diff(F[1],x)-sp.diff(F[0],y)])
div=lambda F: sum(sp.diff(F[i],X[i]) for i in range(3))
f0=sp.exp(x*y)*sp.cos(z)+x**2*z; F1=sp.Matrix([x*y*z, sp.sin(x)+z**2, sp.exp(y*z)])
print("14: curl grad = 0:", sp.simplify(curl(grad(f0)))==sp.zeros(3,1), "| div curl = 0:", sp.simplify(div(curl(F1)))==0)
# Leibniz for 0-forms: d(fg) = g df + f dg
g0=x+y*z**2
print("14: d(fg) = g df + f dg:", sp.simplify(grad(f0*g0)-(g0*grad(f0)+f0*grad(g0)))==sp.zeros(3,1))
# ---- Chapter 16
P,Q=-y/(x**2+y**2), x/(x**2+y**2)
print("15: the angle form is closed:", sp.simplify(sp.diff(Q,x)-sp.diff(P,y))==0)
loop=lambda k: (sp.cos(k*t), sp.sin(k*t))
def line_int(P,Q,c,a=0,b=2*sp.pi):
    cx,cy=c; return sp.integrate(sp.simplify(P.subs({x:cx,y:cy})*sp.diff(cx,t)+Q.subs({x:cx,y:cy})*sp.diff(cy,t)),(t,a,b))
print("15: angle form around the circle once, twice:", line_int(P,Q,loop(1)), line_int(P,Q,loop(2)))
fx=sp.exp(x)*sp.sin(y); print("15: an exact form around the circle (numeric):", round(float(sp.N(line_int(sp.diff(fx,x),sp.diff(fx,y),loop(1)))),12))
# Stokes on the unit square for a random polynomial 1-form
a=[random.randint(-3,3) for _ in range(6)]
Pw=a[0]*x*y+a[1]*y**2+a[2]*x; Qw=a[3]*x**2+a[4]*x*y+a[5]*y
inside=sp.integrate(sp.integrate(sp.diff(Qw,x)-sp.diff(Pw,y),(x,0,1)),(y,0,1))
edge=sp.integrate(Pw.subs(y,0),(x,0,1))+sp.integrate(Qw.subs(x,1),(y,0,1))-sp.integrate(Pw.subs(y,1),(x,0,1))-sp.integrate(Qw.subs(x,0),(y,0,1))
print("15: Stokes on the unit square:", sp.simplify(inside-edge)==0)
