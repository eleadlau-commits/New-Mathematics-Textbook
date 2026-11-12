# Checks for Chapter 5 (nearness).
import math, random
from fractions import Fraction as F
random.seed(7)
def cell(x,k): return math.floor(x*10**k)
def same_cell(x,y,k): return cell(x,k)==cell(y,k)
def near(x,y,k): return abs(x-y) < F(1,10**k)
rnd=lambda: F(random.randint(-10**6,10**6),10**6)
# P: the cell blur does not respect +
x,y,z=F(1,100),F(8,100),F(5,100)
print("cells k=1: 0.01~0.08:", same_cell(x,y,1), "| after adding 0.05:", same_cell(x+z,y+z,1))
# N_k = "same cell after some shift": exact check with the canonical shift z = -min(x,y) + cell start
ok=True
for _ in range(20000):
    k=random.randint(0,3); a,b=rnd(),rnd()
    if random.random()<0.5: b=a+F(random.randint(-15,15),10**(k+1))
    lo=min(a,b); z=-lo                      # shift the lower point to 0, the start of a cell
    exists = same_cell(a+z,b+z,k)           # if any shift works, this one does
    ok &= (exists == near(a,b,k))
    if near(a,b,k): ok &= same_cell(a+z,b+z,k)
print("within 10^-k  <=>  same cell after some shift:", ok)
# chaining dies; two steps law
print("k=1: 0 N 0.08:", near(F(0),F(8,100),1), "0.08 N 0.16:", near(F(8,100),F(16,100),1), "0 N 0.16:", near(F(0),F(16,100),1))
ok2=all((not(near(a,b,k+1) and near(b,c,k+1))) or near(a,c,k) for a,b,c,k in [(rnd(),)*1+(rnd(),rnd(),random.randint(0,3)) for _ in range(1)]+[(a,a+F(random.randint(-9,9),10**(k+2)),a+F(random.randint(-18,18),10**(k+2)),k) for a,k in [(rnd(),random.randint(0,3)) for _ in range(20000)]])
print("two steps at k+1 make one step at k:", ok2)
# three maps: rung needed for output rung k=2
def rung_needed(f,a,k=2):
    m=0
    while not all(abs(f(a+d)-f(a))<10**-k for d in [s*10**-m*t for s in (-1,1) for t in (0.999,0.5,0.1)]): m+=1
    return m
print("x^2: rung needed near 3:", rung_needed(lambda x:x*x,3.0), "| near 100:", rung_needed(lambda x:x*x,100.0), "| identity:", rung_needed(lambda x:x,100.0))
step=lambda x: 1.0 if x>=0 else 0.0
print("step at 0: any rung m up to 12 works:", any(all(abs(step(d)-step(0))<0.01 for d in (-0.5*10**-m,0.5*10**-m)) for m in range(13)))
