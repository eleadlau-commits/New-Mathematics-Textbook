from itertools import combinations
tests=["semi","neg","nzd","inv","ord","least","lim","fin","dense"]
rows={"N":"101011100","Z":"111011100","Z/6":"110000010","Z/7":"111100010","Q":"111110001","R":"111110101","R^2":"110000000"}
I={k:{t for t,c in zip(tests,v) if c=="1"} for k,v in rows.items()}
def ext(T): return frozenset(k for k in I if set(T)<=I[k])
def intent(E): 
    return frozenset(tests) if not E else frozenset(set.intersection(*[I[k] for k in E]))
concepts={(ext(T),intent(ext(T))) for r in range(len(tests)+1) for T in combinations(tests,r)}
print(len(concepts),"classes")
for e,i in sorted(concepts,key=lambda c:(-len(c[0]),sorted(c[0]))): print(sorted(e),"|",[t for t in tests if t in i])
print("single implications a=>b (a nontrivial):")
for a in tests:
    for b in tests:
        if a!=b and ext([a]) and ext([a])<=ext([b]) and ext([b])!=frozenset(I): print(" ",a,"=>",b)
print("never together:",[(a,b) for a,b in combinations(tests,2) if not ext([a,b])])
print("rows distinct:",len(set(rows.values()))==len(rows))
