from itertools import combinations
rows = {
 'Z':      dict(comm=1, fin=0, cyc=1, tf=1, div=0),
 'Z/6':    dict(comm=1, fin=1, cyc=1, tf=0, div=0),
 'T':      dict(comm=1, fin=0, cyc=0, tf=0, div=1),
 'Qx':     dict(comm=1, fin=0, cyc=0, tf=0, div=0),
 '(Z/8)x': dict(comm=1, fin=1, cyc=0, tf=0, div=0),
 'S3':     dict(comm=0, fin=1, cyc=0, tf=0, div=0),
 'D4':     dict(comm=0, fin=1, cyc=0, tf=0, div=0),
 'GL2R':   dict(comm=0, fin=0, cyc=0, tf=0, div=0),
 'F2':     dict(comm=0, fin=0, cyc=0, tf=1, div=0),
 'Z2':     dict(comm=1, fin=0, cyc=0, tf=1, div=0),
}
tests = ['comm','fin','cyc','tf','div']
classes = set()
for r in range(len(tests)+1):
    for T in combinations(tests, r):
        classes.add(frozenset(k for k,v in rows.items() if all(v[t] for t in T)))
print("classes:", len(classes))
for c in sorted(classes, key=len, reverse=True): print(sorted(c))
sig = {k: tuple(v[t] for t in tests) for k,v in rows.items()}
from collections import Counter
print("bags under all tests:", Counter(sig.values()))
# implications a=>b true in table
for a in tests:
    for b in tests:
        if a!=b and all(v[b] for v in rows.values() if v[a]): print(a,"=>",b)
for a,b in combinations(tests,2):
    if not any(v[a] and v[b] for v in rows.values()): print("never together:",a,b)
