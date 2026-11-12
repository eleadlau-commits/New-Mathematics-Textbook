# Checks for Part II Chapter 2: blurs respecting + and x of small rings = ideals; the N counterexample.
from itertools import product
def congruences(elems, ops):
    elems=list(elems); idx={e:i for i,e in enumerate(elems)}
    def close(pairs):
        R=set(pairs)|{(e,e) for e in elems}
        while True:
            new={(b,a) for a,b in R}|{(a,d) for a,b in R for c,d in R if b==c}
            for a,b in R:
                for z in elems:
                    for op in ops: new.add((op(a,z),op(b,z))); new.add((op(z,a),op(z,b)))
            if new<=R: return frozenset(R)
            R|=new
    base=close([]); seen={base}; todo=[base]
    while todo:
        R=todo.pop()
        for a in elems:
            for b in elems:
                if (a,b) not in R:
                    S=close(list(R)+[(a,b)])
                    if S not in seen: seen.add(S); todo.append(S)
    return seen
def Zn(n): return range(n), [lambda a,b:(a+b)%n, lambda a,b:(a*b)%n]
def ideals(n):
    E=range(n); out=set()
    for g in E:
        out.add(frozenset((g*k)%n for k in E))
    return out
for n in (6,7,12):
    E,ops=Zn(n); C=congruences(E,ops)
    zero_bags={frozenset(b for a,b in R if a==0) for R in C}
    print(f"Z/{n}: blurs respecting + and x = {len(C)}, distinct zero bags = {len(zero_bags)}, ideals = {len(ideals(n))}")
# (Z/3)^2 with place-by-place operations, the finite stand-in for R^2
E=list(product(range(3),repeat=2))
ops=[lambda a,b:((a[0]+b[0])%3,(a[1]+b[1])%3), lambda a,b:((a[0]*b[0])%3,(a[1]*b[1])%3)]
print("(Z/3)^2:", len(congruences(E,ops)), "blurs")
# N counterexample (checked on 0..N-1 with truncation-free test): x~y iff x==y or both >= 2
sim=lambda x,y: x==y or (x>=2 and y>=2)
ok=all(sim(x+z,y+z) and sim(x*z,y*z) for x in range(30) for y in range(30) if sim(x,y) for z in range(30))
print("N: 'equal or both >= 2' respects + and x:", ok, "| zero bag = {0}, same as equality's")
