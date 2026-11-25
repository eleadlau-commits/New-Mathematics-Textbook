# Pre-registration v1: the Ladder rule (frozen 25 Nov 2026, before any scoring)

E (22:02 25 Nov): "how would we have found that object ourselves? Could we have in RH? how many moves would it take? try forward testing if we find out why".

This file is written and committed **before** the rule is scored on anything. It is not edited after the commit. Any change is a new version (v2, v3...) and counts as in-sample for every episode already scored.

## 1. The rule (Ladder rule, L1 to L5)

Use it when a target inequality has a known proof in an **analogue** (function field, finite field, toy model) and that proof needs a **budget** B(X) of some unit that grows with the size parameter X (vanishing order, moments, degree, number of variables), while every single object available for the target supplies O(1) units.

- **L1 Bill.** Name the unit and B(X), read off the analogue proof.
- **L2 Home group.** Name G0, the smallest symmetry group (or object family) the target quantity is a representation of.
- **L3 Ladders.** List ladders that start at G0, each with its canonical move between rungs: rank (G0 ⊂ G1 ⊂ ...), powers (tensor or symmetric powers), field towers, number of variables.
- **L4 Prune.** Keep a ladder only if its move (a) keeps the measured quantity (the blur respects it), (b) adds at least one unit per rung, and (c) costs a bounded amount per rung (the H5 rung-supply audit).
- **L5 Endgame.** Rewrite the target in a one-sided form (H7) that the accumulated units can feed.

**Output:** at most 3 candidate ladders, ranked. **Silent** if L1 finds no analogue with a budget.

## 2. Backtest episodes (list fixed now)

Each is used with the problem as stated before its proof, and only literature older than the proof. I have read all these proofs, so every backtest score is **contaminated by lookahead**. Scores are therefore graded strictly: a hit needs the decisive new object or move inside the top 3, named as specifically as the proof names it.

| # | problem | proof | reason it is on the list |
|---|---|---|---|
| E1 | RH (claimed) | Alpöge 2026, unverified | the case the rule was built from: in-sample by construction, reported separately |
| E2 | Weil conjectures, RH part | Deligne 1974 | budget-type |
| E3 | Ramanujan–Petersson | Deligne 1974 | budget-type |
| E4 | Fermat | Wiles–Taylor 1995 | coordinator's list |
| E5 | Schinzel–Zassenhaus | Dimitrov 2019 | coordinator's list, Lehmer neighbour |
| E6 | Kakeya over finite fields | Dvir 2008 | coordinator's list |
| E7 | Duffin–Schaeffer | Koukoulopoulos–Maynard 2019 | coordinator's list |
| E8 | bounded gaps between primes | Zhang 2013, Maynard 2013 | budget-type |
| E9 | cap sets in F_3^n | Ellenberg–Gijswijt 2016 | control: one-object proof |
| E10 | sensitivity conjecture | Huang 2019 | control: no analogue |

## 3. Scoring

- **Hit:** the decisive new object or move is in the top 3.
- **False lead:** the rule fires but its top 3 misses. Record what it pointed to.
- **Silent:** L1 finds no budget. Correct if the proof has no budget-type step, a miss otherwise.
- **Null to beat:** "the three most-used tools in the neighbouring area at the time". A rule that does no better than the null adds nothing.

## 4. Forward test

The forward test runs on problems that are still open, with predictions committed to git before any solution. It is in FORWARD-v*.md. Only the forward test can count as evidence under E's rule ("hugely positive only if it raises confidence").
