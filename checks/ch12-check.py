# Checks for Chapter 12 (the integral). The area rule is computed by fine sums only to test the theorems.
import math, random
random.seed(5)
def I(f,b,c,n=20000):
    h=(c-b)/n; return h*sum(f(b+(k+0.5)*h) for k in range(n))
fs=[math.exp, math.cos, lambda x: x**3-x, lambda x: math.sin(3*x)*x]
ok_add=ok_lin=ok_pos=True
for _ in range(30):
    f,g=random.choice(fs),random.choice(fs); b,c,d=sorted(random.uniform(-2,2) for _ in range(3)); r=random.uniform(-3,3)
    ok_add &= abs(I(f,b,c)+I(f,c,d)-I(f,b,d))<1e-6
    ok_lin &= abs(I(lambda x:f(x)+r*g(x),b,c)-(I(f,b,c)+r*I(g,b,c)))<1e-6
    ok_pos &= I(lambda x: f(x)**2,b,c) >= 0
ok_ftc = all(abs(I(math.exp,b,c)-(math.exp(c)-math.exp(b)))<1e-6 for b,c in [(-1,0.5),(0,2)])
# G(x)=I(f,b,x) has slope f(x)
f=math.cos; b=0.0; x=0.7; h=1e-4
ok_slope = abs((I(f,b,x+h,40000)-I(f,b,x-h,40000))/(2*h)-f(x))<1e-4
disc = I(lambda x: 2*math.sqrt(max(0.0,1-x*x)),-1,1,200000)
ok_pi = abs(disc-math.pi)<1e-5
ok_log = abs(I(lambda t:1/t,1,math.e)-1)<1e-8
ok_parts = abs(I(lambda x: x*math.exp(x),0,1)-(1*math.e-0-(math.e-1)))<1e-8
print("adds:",ok_add,"| linear:",ok_lin,"| positive:",ok_pos,"| F(c)-F(b):",ok_ftc,"| slope of G is f:",ok_slope,"| disc area = pi:",ok_pi,"| log e = 1:",ok_log,"| parts:",ok_parts)
