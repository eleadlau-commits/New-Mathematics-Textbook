# Backtest of the Ladder rule v1 (25 Nov 2026, scored after PREREG-v1.md was committed)

Rule and episode list: PREREG-v1.md, commit 55f1814 (22:05 UTC). **All scores below are contaminated by lookahead**, because I have read every proof. I graded strictly, but strictness does not remove the bias. This file can falsify the rule. It cannot confirm it.

## 1. RH: how we could have found the object, and in how many moves (E1, in-sample)

Our state on 13 Nov, from map/STEPANOV-Z.md, FROBENIUS-HUNT.md and riemann/LOOP-RULE.md:

| move | content | status on 13 Nov |
|---|---|---|
| 1 Bill (L1) | Stepanov needs free vanishing order √X over ℤ | **had it** (STEPANOV-Z keeper: free/paid ratio √q over F_q, 1 over ℤ) |
| 2 Single-object audit | no one map on one ring supplies it (≤ 1, 0.71·π(X)·log log X, t^0.23) | **had it** (FROBENIUS-HUNT) |
| 3 Split the bill | ask for √X objects, one unit each | **rule existed, not applied** (Z11 Amplify; LOOP-RULE "keep the moves") |
| 4 Home group (L2) | ζ and Dirichlet χ are automorphic forms of the smallest kind (GL1, unitary U(1)) | new, one standard fact |
| 5 Ladders (L3) | rank ladder U(1) ⊂ U(2) ⊂ … with theta lifts as the move; power ladder Sym^k; cyclotomic field tower | new, **needs literature we never opened** (Weil representation, which we had already named as the joint +/× object) |
| 6 Prune (L4) | theta lifts exist and keep the character data (Howe, Rallis); Sym^k lifts are not known to exist, so that ladder fails; the cyclotomic tower plays Stepanov's step 7 (Iwasawa ↔ F_{qⁿ}) | new, literature |
| 7 Endgame (L5) | one-sided form: upper bound on a series with coefficients ≥ 0, then Landau | new, but H7 would give it at once |

**Seven moves. Two we had, one was our own unused rule, four were new, and two of those four needed literature.** The output is hit@2: the theta ladder, plus Sym^k (the famous Langlands–Serre route, blocked by functoriality). The architecture was reachable. The proof was not: it took 20 dated steps, three repairs and about 180 named theorems.

## 2. The other nine episodes

| # | problem | what v1 outputs | decisive object in the proof | score |
|---|---|---|---|---|
| E2 | Weil conjectures (Deligne) | power ladder Xᵏ / tensor powers, from the defect ½ in the trivial bound | Rankin squaring with tensor powers (plus monodromy via Lefschetz pencils) | **hit**, half: the monodromy half is not in the output |
| E3 | Ramanujan–Petersson | Sym^m ladder (Langlands 1970), Rankin–Selberg ladder | Kuga–Sato varieties, which move the problem into Weil | **false lead** (the Sym^m route is real but was finished in 2021, Newton–Thorne) |
| E4 | Fermat | silent: no analogue with a budget | Taylor–Wiles patching over growing sets of auxiliary primes | **miss** (a dial was there, and v1 did not look) |
| E5 | Schinzel–Zassenhaus | ladder of primes p (α ↦ α^p), Dobrowolski-type | one rationality criterion: a Hankel determinant of growing size, plus capacity | **false lead** (it points to the old route) |
| E6 | Kakeya over F_q | multiscale ladder (Wolff, Bourgain) | one polynomial of degree q − 1, by dimension count | **false lead** |
| E7 | Duffin–Schaeffer | silent | GCD graphs with iterated compression | **miss** |
| E8 | bounded gaps | number-of-variables ladder for sieve weights, supply M_k ≈ log k | Maynard's k-dimensional weights | **hit** (Zhang's route, level of distribution, not in the output) |
| E9 | cap sets | density-increment ladder (Meshulam, Bateman–Katz) | slice rank: one polynomial object, by dimension count | **false lead** |
| E10 | sensitivity | silent | signed hypercube matrix plus interlacing | correctly silent |

**Score: 2 hits (one of them half), 4 false leads, 2 misses, 1 correctly silent, plus RH in-sample.**

**Null** ("three most-used tools next door at the time"): E2 contains Rankin's trick and Lefschetz pencils; E8 contains Selberg's sieve. So the null also scores about 2. **v1 does no better than the null, even on contaminated data.**

## 3. What the failures share (in-sample, so this only suggests v2)

- **All four false leads have one shape.** The old route was a ladder with a **fixed** gain per rung (Dobrowolski's primes, density increments, multiscale induction). The breakthrough replaced it with **one object whose size is a free dial** (degree, determinant size, slice rank), so supply comes from a dimension count.
- **Both misses had a dial too.** Taylor–Wiles uses growing sets of auxiliary primes; Koukoulopoulos–Maynard iterate compression.
- **Both hits are dials** (tensor power k, number of variables k), and so is RH (√X rungs).

**Common reason:** in every decisive step, the supply scales with **a parameter the prover chooses**, and grows faster than the bill. The routes that stall have supply fixed by the problem. A ladder is one way to get that, not the only one. That is the rule v2 (PREREG-v2.md). Because it was read off these ten episodes, v2 is **in-sample on all of them**, and only the forward test can score it.
