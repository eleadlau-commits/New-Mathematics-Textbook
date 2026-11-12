# Building 2, Ch1 (proofs, propositional) and Ch2 (provability, letterless).
import itertools, random
random.seed(21); ok = True
# ---- Ch1: formulas in letters p, q; worlds = arrows letters -> {0,1}
def ev(f, w):
    t = f[0]
    if t == 'v': return w[f[1]]
    if t == 'F': return 0
    if t == 'not': return 1 - ev(f[1], w)
    if t == 'and': return ev(f[1], w) & ev(f[2], w)
    if t == 'or': return ev(f[1], w) | ev(f[2], w)
    if t == 'imp': return (1 - ev(f[1], w)) | ev(f[2], w)
letters = ['p', 'q']
worlds = [dict(zip(letters, v)) for v in itertools.product((0, 1), repeat=2)]
def gen(depth):
    if depth == 0: return [('v', 'p'), ('v', 'q'), ('F',)]
    prev = gen(depth - 1); out = list(prev)
    for a in prev: out.append(('not', a))
    for a in prev:
        for b in prev:
            out += [('and', a, b), ('or', a, b), ('imp', a, b)]
    return out
F = gen(2)  # every formula of depth <= 2
tables = {tuple(ev(f, w) for w in worlds) for f in F}
# close the tables of p, q, F under the connectives: 2^(2^2) = 16 bags
T = set(tables); grow = True
while grow:
    new = {tuple(1 - x for x in a) for a in T} | {tuple(x & y for x, y in zip(a, b)) for a in T for b in T} | {tuple(x | y for x, y in zip(a, b)) for a in T for b in T}
    grow = not new <= T; T |= new
ok &= len(T) == 16
tables = T
# axioms of the proof system are true in every world (soundness, one way of Appears)
A, B, C = ('v', 'p'), ('v', 'q'), ('not', ('v', 'p'))
ax1 = lambda a, b: ('imp', a, ('imp', b, a))
ax2 = lambda a, b, c: ('imp', ('imp', a, ('imp', b, c)), ('imp', ('imp', a, b), ('imp', a, c)))
ax3 = lambda a, b: ('imp', ('imp', ('not', b), ('not', a)), ('imp', a, b))
for a, b, c in itertools.product(random.sample(F, 12), repeat=3):
    ok &= all(ev(ax1(a, b), w) for w in worlds) and all(ev(ax2(a, b, c), w) for w in worlds) and all(ev(ax3(a, b), w) for w in worlds)
# normal form: one disjunction of full rows per table
def dnf(table):
    rows = [w for w, t in zip(worlds, table) if t]
    if not rows: return ('F',)
    terms = []
    for w in rows:
        lit = [('v', l) if w[l] else ('not', ('v', l)) for l in letters]
        terms.append(('and', lit[0], lit[1]))
    f = terms[0]
    for t in terms[1:]: f = ('or', f, t)
    return f
ok &= all(tuple(ev(dnf(t), w) for w in worlds) == t for t in tables)
print("Ch1:", ok)
# ---- Ch2: letterless sentences, read at depth n of the linear frame (GL); first-failure depth = rung
INF = 10**9
def true_at(f, n, memo={}):
    key = (f, n)
    if key in memo: return memo[key]
    t = f[0]
    if t == 'F': r = False
    elif t == 'not': r = not true_at(f[1], n)
    elif t == 'and': r = true_at(f[1], n) and true_at(f[2], n)
    elif t == 'or': r = true_at(f[1], n) or true_at(f[2], n)
    elif t == 'imp': r = (not true_at(f[1], n)) or true_at(f[2], n)
    elif t == 'box': r = all(true_at(f[1], m) for m in range(n))
    memo[key] = r; return r
N = 40
def rung(f):                       # first depth where f fails; INF if never (= provable, on depths < N)
    for n in range(N):
        if not true_at(f, n): return n
    return INF
bot = ('F',); box = lambda a: ('box', a); neg = lambda a: ('not', a)
Con = neg(box(bot))
def equally(a, b): return all(true_at(box(a), n) == true_at(box(b), n) for n in range(N))
ok &= equally(bot, Con) and rung(bot) == 0 and rung(Con) == 0      # bottom and Con on rung 0
ok &= rung(neg(Con)) == 1                                          # not-Con on rung 1
ok &= not equally(bot, neg(Con))
# or dies: bottom ~ Con, but bottom or notCon (rung 1) vs Con or notCon (provable)
ok &= rung(('or', bot, neg(Con))) == 1 and rung(('or', Con, neg(Con))) == INF
# letterless sentences of small size
def gen2(d):
    if d == 0: return [bot]
    prev = gen2(d - 1); out = list(prev)
    for a in prev: out += [neg(a), box(a)]
    s = prev[:14]
    for a in s:
        for b in s: out += [('and', a, b), ('imp', a, b)]
    return list(dict.fromkeys(out))
S = gen2(3)
for a in S:
    ok &= rung(box(a)) == (INF if rung(a) == INF else rung(a) + 1)        # box climbs one rung
    ok &= equally(a, ('imp', box(a), a))                                  # Lob: a ~ (box a -> a)
    k = rung(a)
    if k < INF:
        bk = bot
        for _ in range(k + 1): bk = box(bk)
        ok &= all(true_at(box(a), n) == true_at(bk, n) for n in range(N))   # |- box a <-> box^(k+1) bottom
for a, b in itertools.product(S[:30], repeat=2):
    ok &= rung(('and', a, b)) == min(rung(a), rung(b))                    # and takes the lower rung
    ok &= equally(a, b) == (rung(a) == rung(b))                           # bags = rungs
print("rungs seen:", sorted({rung(a) for a in S}, key=lambda r: r)[:8])
print("ALL", ok)
