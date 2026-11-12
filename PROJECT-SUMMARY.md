# The Grand Mathematics Theory: where everything stands (12 Nov 2026)

One summary of the whole project, replacing the separate build, algebra, elliptic-curve and reassessment threads. Nothing here has had a specialist check. "Known" means the mathematics is in the literature; "ours" means the placement in the grammar or an unchecked computation.

---

## 1. The aim

A new way to write and discover mathematics, by **Looking Away** (the blur method): make a thing, then decide what to stop seeing, and read off what is kept, what is lost and what appears. Standing rules: stay true to the blur, avoid importing, no traditional textbook layout, Given/Let terseness, one small step at a time, no check questions.

## 2. The method in one page

**Three verbs.** Build (at least one), Select (which one), Blur (at most one, and what is kept).

**Blur.** Glue things that pass the same tests. Two directions must agree:
- from below: name a few gluings, close them up (forget ⟨R⟩);
- from above: keep the answers to some questions (keep ⟪g⟫).
When they agree, the question *appears* (h appears at ◇ iff ◇ = ⟪h⟫). Gluings are choices, never claims. A blur must say what it respects (L7); a one-way blur (L8) is an order.

**Lines.** Every chapter is written as lines: Given, Let/Definitions, Blur (B1 below, B2 above), Bags, Normal form, **Survives**, **Dies** (always with a witness pair), **Appears**, Arrow, Theorems, Remarks. A theorem is a blur line read aloud: IVT and Stokes are Survives lines. A theorem that is not a blur line carries "Imported" or "From Chapter n".

**Rules** live in `textbook/ch0-rules.tex`: Background S; Build M1–M7; Blur L1–L9; Theorems Z1–Z11; Arrows W (W4 = the arrow's own blur); conventions C1–C6; second floor F1–F7 (floor two reads floor one only).
Drafts not in ch0 (E's decision): **F8 Loop** (a later chapter blurs by an action of an earlier system; verdicts closed / changed / wild) and **Z12 Amplify** (a rough bound on every rung of a power ladder forces the sharp bound).

**Rule of thumb (11 Nov).** Blur proves "at most one" and "this is kept". Existence comes from Build, from "closed" (completeness with an estimate), or from the one construction behind a Select. Design each chapter to need existence once.

**Nearness.** Blur unchanged; a ladder of true blurs (first k digits; mod pᵏ). "ℝ cannot be cut" is why ε–δ exists. The one-way form of ch5 T8 is the de-importing tool.

**Moves.** A move is an arrow from a floor to itself that is inside and picture (W2). Not a new verb. Forgetting the "how" of a move system gives a blur. Map of the book = Buildings × Floors: Building 0 Blur (Parts I–II), Building 1 Moves (the algebra path), Building 2 loops. The tower (blur, moves, ways between ways…) has no top.

**Heuristic.** Every Dies line is a build order: it asks for a floor where the lost question survives. The next chapter is the repair.

## 3. The book (`textbook/`)

`building0-blur.pdf`: 37 chapters of Part I plus Part II.1–II.6, 150 pages; `building1-moves.pdf`: 19 chapters, 48 pages, compiled clean on 12 Nov. Repo: github.com/eleadlau-commits/new-mathematics-textbook. `build.py` assembles and checks (and compiles if pdflatex is present).

**Part I** (ch1–25): integers, rationals, congruences, reals, nearness, ℝⁿ, polynomials, circle, angles, maps and germs, derivative, integral, several variables, signed area (det), the arrow d, Stokes, orders of magnitude, divisibility, p-adics, sequences of maps, Taylor, exp, ℂ is closed, highest/lowest points, inverting a map, null sets, integrable maps, square-integrable maps, waves on the circle, the two homes of a wave (L² = ℓ²), the complex derivative, loops around a holomorphic map (Cauchy from Stokes), rigidity, poles and valuations.
**Part II:** II.1 the table, II.2 any ring, II.3 vector spaces, II.4 metric spaces.

**Imports left: three**, all in Remarks only: Weierstrass (ch20), Borel (ch21), Ostrowski (ch19). Ch29's Fejér average (a positive blur of the rungs) now gives Weierstrass, so it can be earned once proofs are written. Ch27 T3 (bags are maps, at most one) and the dominated/monotone lines are marked classical, proof deferred. FTA was de-imported in ch23. MVT became "closed stretches survive" + "rising chains" (ch11).

**Leg 1 (analysis) built 12 Nov:** ch26–30. **Leg 2 (complex analysis):** ch31–34. **Leg 3 (algebra short road):** Building 1 Parts I–II, through the Smith form. **Leg 4 (elliptic curves):** Building 0 ch35–37 (plane, cubic, torus) and Building 1 Part III (group law as a blur, torus carries the law, counts over ℤ/p). **Leg 5 (rest of algebra):** Building 1 II.5–II.14, actions and Sylow through Galois and the quintic (no imports in the core; Hasse, Mordell–Weil, uniformisation reported only). **Leg 6 (logic):** Building 2 Part I, Proofs and Equally provable. **Building 0 II.6:** sizes on vector spaces (normed, Banach, Hilbert). Plans: `WORKPLAN-2.md` (analysis ch26–30, complex analysis C1–C4), `ALGEBRA-PATH.md` (17 chapters), elliptic-curves route (in memory, summarised below).

**Proofs:** deferred by E (statements only, each checked by a script where a computer can).

**Pending small edit:** ch21 Taylor remainder by "≥ 0 is kept, k + 1 times" (non-strict rising chains), dropping continuity of f^(k+1). Proposed, not applied.

## 4. Results so far

**Ours, machine-checked on small cases, not specialist-checked**
- T10–T14: one-way blurs of Mₙ(F_q) number 2n + 1. Blur counts for ℤ/n under ×: a(6) = 27, a(30) = 2039, a(p²) = 2^p + 3 (OEIS A241573 matches 2^p + 3).
- T17: binary operations on matrices respected by × are s·x + t·y.
- T18–T23: "what a floor remembers" (abs/ladder2.py).
- Pigeonhole in three blur lines (proof shortening).
- Graph twin of the Riemann block: size(x) = q|a|² − a·A·b + |b|², BᵀPB = qP (novelty unchecked).
- Cap and 17/19 law in Weil's cut form: positivity caps w_p ≤ log p for p = 2, 3, 5, 7, 11, 13, 19; certified to 50 digits for p = 2, 3, 13 (no interval arithmetic yet). p is capped iff d₋·d₊ ≳ 0.015. The room is paid for by the ζ zeros (resonance). Echo blur proposed. Not found in the literature (modest search).
- Candidate "equally provable" blur of sentences: A ≈ B iff ⊢ □A ↔ □B. Survives ∧ and □; dies ¬, ∨, truth; ⊥ ≈ Con. Novelty unchecked.

**Re-sorted known results (the method's main yield)**
- MVT, FTA, Taylor bound, exp law without the series product: classical proofs re-sorted as blur lines.
- Hasse bound over ℤ/p in existing lines (no import); Gelfand, Cauchy–Schwarz, Hasse as Amplify book examples.
- Loop D (adeles blurred by ℚ×, moves kept) = Connes' space; finite cuts reproduce the ζ zeros (Connes–Consani).
- Atoms ladder (free / fair / unfair / atomless / uncomputable) and its two-glue column: RH-type lines are proved where + has atoms and a move respects both glues, open where × is free and + is atomless (ℤ). The known char p / char 0 gap.
- Provability: Lindenbaum (known), ε₀ ladder (Beklemishev), letterless ω + 1 ladder (Boolos).
- Mechanisms that keep roots on one side: all on the known list (Borcea–Brändén, Lee–Yang, Lieb–Sokal, Hurwitz…). Keeper: "a linear gluing keeps root-freeness iff it keeps it on (1 + z)^d".

**Honest verdict**
Strong way to write; real discovery only on finite floors (counting and classifying everything); good at finding gaps and debts. In analysis the from-below blur is usually just the bag test. The method sorts more than it produces.

## 5. The map (MAP-PILOT, quick, not rigorous)

57 hand-run rows of "floor → Dies line → cheapest build → what appears". Six generations from ℕ reach most of an undergraduate degree; seven reach schemes and categories. Every run-1 row lands in a known field.
- E lines (missing solution) build algebra and number theory.
- L lines (ladder doesn't close) build analysis.
- M lines (moves) build groups, geometry, topology.
- G lines (local vs global) build sheaves, adeles, complex analysis.
- **C lines (counting, cancellation) are where the open edges are:** RH, capacity of C₇, Lindelöf, finite lattice representation.
Reached badly: statistics, numerics, optimisation, PDE estimates.

## 6. The edge (Riemann / Amplify)

- RH over ℤ/p is proved by a move (Frobenius) that respects both + and × and rescales a positive form. ℤ has no such move: every break in transferring the curve proofs is exactly that missing move (a ch1 Dies line).
- Gluings keep a root-free region; only Amplify moves its edge. RH = moving ℤ's edge from 1 to ½.
- Tower of levels: 1 Blur, 2 Moves/loops, 3 Amplify, 4 Source, 5 Transfer. All converge on one construction problem: an object for ℤ carrying a move and a size.
- Searches for new mechanisms (~25 families, ~1,500 cases) found nothing new. Lesson: brute force finds new small theorems when the question is "classify everything here", and only rediscovers when aimed at a famous mechanism.

## 7. Open questions

1. Adopt drafts F8 Loop and Z12 Amplify into ch0? (E's call.)
2. Apply the ch21 Taylor remainder edit?
3. Name of the system (Looking Away recommended).
4. Specialist check of the ℤ/n and matrix counts (T10–T23) and of the cap / 17/19 note.
5. Literature check thread (blocked).
6. Interval-arithmetic proof of the cap; origin of 0.015.
7. Shape of the "equally provable" blur on sentences with letters.
8. Chapter generator: machine version on finite floors; push run 2 near the open edges.
9. Write the proofs (deferred by E).

## 8. Where to look

| Topic | File |
|---|---|
| Rules | textbook/ch0-rules.tex |
| Analysis + complex plan | textbook/plans/WORKPLAN-2.md |
| Algebra plan | textbook/plans/ALGEBRA-PATH.md |
| Chapter designs | textbook/plans/designs/ |
| Loop rule, Riemann | riemann/LOOP-RULE.md, riemann/FINDINGS-graphs.md |
| Amplify | riemann/amplify/SUMMARY.md |
| Mechanisms | riemann/mechanisms/FINDINGS.md |
| Provability | provability/FINDINGS.md |
| Atoms | atoms/ATOMS-TABLE.md |
| Abstraction (origins) | abs/ABS-000-summary.md |
| Map survey | map/MAP-PILOT.md |
| Build route to the territories | textbook/plans/TERRITORIES.md |
| The books | textbook/building0-blur.pdf (+ stubs for Buildings 1, 2); textbook/README.md |
