# Work order for the textbook build session

Written 11 Nov 2026 by the planning session (Fable) for the build session (Opus).
E approved the plan in the thread "Write old mathematics as a textbook myself".
Read this whole file before writing anything. Then do the tasks in order, one at a time.

## 0. What the book is, in five lines

- A textbook of old mathematics written by three verbs: Build, Select, Blur. Rules are in `ch0-rules.tex`. Read it first, in full.
- Every chapter makes one new floor and is written as lines: Given, Definitions, Blur (B1 from below, B2 from above), Propositions (Bags, Normal forms, Survives, Dies, Appears), Notation, Arrow, Theorems, Remarks, Exercises.
- E's standing worry: **do not fall back to a traditional textbook with a blur section attached.** The blur must do the work. A list of imported classical theorems is the failure mode.
- No proofs are written in the LaTeX (statements only), but every statement must be true, and checked by a small script where a computer can check it.
- E is not a specialist. Plain words, short lines, no hype.

## 1. State of the files (all in `/mnt/project-files/textbook/`)

Part I, numbering after the 11 Nov renumber (do NOT renumber again; append new chapters at the end):

| No. | File | Subject |
|---|---|---|
| 0 | ch0-rules | the rules (S, M1–M7, L1–L9, Z1–Z10, W, C, F) |
| 1–4 | ch1-integers, ch2-rationals, ch3-congruences, ch4-reals | ℤ, ℚ, ℤ/n, ℝ |
| 5 | ch5-nearness | NEW. cells, likeness N_k, "respects nearness", "comes near" |
| 6 | ch6-arrays | ℝⁿ, four roads |
| 7 | ch7-polynomials | ℝ[x], roads to ℂ, dual numbers |
| 8 | ch8-circle | ℝ/ℤ |
| 9 | ch9-angles | corners in ℝ² |
| 10 | ch10-functions | maps, continuity, germs, exp, π |
| 11 | ch11-derivative | flat, straight bags |
| 12 | ch12-integral | area rule A1–A4 |
| 13–16 | ch13-several-variables, ch14-signed-area, ch15-the-arrow-d, ch16-stokes | forms |
| 17 | ch17-magnitudes | sizes of sequences |

Part II: p2-ch0-map, p2-ch1-table (II.1), p2-ch2-any-ring (II.2), p2-ch3-vector-spaces (II.3).
`retired/p2-ch4-epsilon-delta.tex` is retired (replaced by Chapter 5). Do not restore it.

Tools:
- `python3 build.py` rebuilds `book.tex` and `book-single.tex` from the `ORDER` list inside it and runs the checks. To add a chapter, add its file name to `ORDER`, then run it. It must print `ok` for every file.
- There is **no LaTeX compiler** in the container. Never say a file compiles. Say "not compiled".
- Check scripts are named `chN-check.py`. sympy and numpy may need `pip install sympy` again in a new container.

## 2. Hard rules (each one was broken at least once yesterday)

1. **B1 and B2 must name the same O** (rule L7). If B1 respects `+, ×`, so does B2. A different O is a different blur and the Appears line is then false.
2. **Verify every citation with grep before writing it.** `grep -n 'lab{T6}' ch4-reals.tex`. Never cite a line from memory. Never cite a label that does not exist.
3. **Floor one never cites floor two** (rule F7). A Part I chapter may mention Part II only inside a Remark, as a pointer. `build.py` reports violations.
4. **A Survives or Dies line needs its witness or its reason.** Dies: one pair x ~ y with different answers. Check the witness by hand or by script.
5. **Every exercise must be true and doable from the chapter.** Yesterday one exercise asked for something impossible.
6. **A theorem must make sense on the bag it is stated on.** Yesterday a theorem about "f is in C" was stated on C itself.
7. **Chapter title block:** copy the pattern of `ch5-nearness.tex` lines 1–7 exactly (`\section*`, `\phantomsection\addcontentsline`, centred "arrow · from · verbs" line, tagline). Inner headings are `\subsection*`.
8. **Use only macros defined in `preamble.tex`** or standard amsmath/amssymb. No new packages.
9. **Honesty.** If a claim is a classical theorem whose proof is long, say so in the line. If a count comes from this project and has not been checked by a specialist, write "found in this project, machine-checked for small cases, not yet checked by a specialist".
10. **After each chapter:** run its check script, run `build.py`, add one row to the table in `ch0-map.tex` (do not touch the diagram), update the "Planned" line in `contents.tex`, append three lines to `/tmp/claude/memory/team/silo/textbook-coaching.md`, and tell E in at most 120 words what the chapter blurs, what appears, what dies, and what was machine-checked.

## 3. How to keep the blur doing the work (the test for every chapter)

Before writing, answer these in one line each. If you cannot, the chapter is not designed yet.

- What are the **few** gluings that force everything (from below)? If the only honest answer is "the bag test itself", write that openly in B1: "Here the gluings are the bag test; this blur is made from above."
- What **question** is it the home of (from above)?
- What is the **separating context** for Appears (rule Z5)? Or does Appears **fail**? A failure is a result, not a defect (see Chapter 5, P5 and Chapter 7, R2).
- What tempting thing **dies**, with a witness?
- Is there a **normal form**? If not, say there is none.
- Can the chapter **survey all blurs** of its floor for some O (as Chapter 3 does for ℤ)?
- What happens if the chapter is **run again** on its own result (rule F5, closed)?
- Is some relation here **one-way** (L8) or a **likeness** (L9)? Use them; they are the project's own tools.
- Which classical theorems are really **Survives lines** of an arrow? State them that way first, old name in the Remarks.

## 4. Tasks

### Task 1. Recast Chapters 10, 11, 13 on top of Chapter 5 (edit, do not rewrite)

Goal: no hand-written ε–δ line remains in Part I after Chapter 5.

Chapter 10 (functions):
- D4: replace the ε–δ sentence by "f is *continuous at a* if f respects nearness at a (Chapter 5, N4)". Keep the label.
- B1: add the sentence "Here the gluings are the bag test; this blur is made from above (B2)."
- T1 and T2: restate as lines about the arrow f, under a heading "What every continuous map keeps": T1 "(Intervals survive.) If f is in C, the picture of an interval is an interval." T2 "(Closed stretches survive.) The picture of a stretch b ≤ x ≤ c is a stretch m ≤ y ≤ M." Put the old sentences after them as "In other words: …". Old names stay in R5.
- Add after P8 a survey line: "(A family of blurs.) For any set Z of reals, 'f and g agree on Z' is a blur of C respecting + and ×. Z = {a} is the value blur; Z = ℝ is equality; the germ blur glues f and g when they agree on near_k(a) for some rung k (Chapter 5, N2)." Check each claim.
- Add a theorem at the end of "the turn": "(ℂ is closed for Chapter 7.) Every polynomial of degree ≥ 1 with coefficients in ℂ has a root in ℂ. So running Chapter 7 on ℂ and gluing any d of degree ≥ 1 with a field as result gives ℂ again: nothing new appears. (Classical; the proof uses T2 in two variables and is long.)" Add "fundamental theorem of algebra" to Old names.
- T7 "w is continuous": fine. R1: no change.

Chapter 11 (derivative):
- D2: replace by "e is *flat at a* if e(a) = 0 and e(x)/(x − a) comes near 0 as x comes near a: for every rung k there is a rung m with 0 < |x − a| < 10^(-m) ⇒ e(x)/(x − a) N_k 0 (Chapter 5)." Keep the label. Check that P4.1, P7 still read correctly.
- B1: add the same honesty sentence as in Chapter 10.

Chapter 13 (several variables):
- D1: define N_k on ℝⁿ by "|x − y| < 10^(-k)" and say it has P9–P12 of Chapter 5 (check each: + survives, nested, two steps, bottom). Continuity = respects nearness at a.
- D2: flat by the same pattern.

Chapter 7 (polynomials), one added line after P9 in "Four roads":
- "(All of them.) Every blur of ℝ[x] respecting + and × is ∼_d for exactly one d that is 0 or has leading coefficient 1. (From T3, as Chapter 3, R1 for ℤ.)" d = 0 is equality, d = 1 is one bag. Verify Chapter 3's label first.

Chapter 15 (the arrow d):
- Change the verbs line to "select". Rename the section "Blur" to "The blur of the arrow d (W4)" and replace the B1/B2 labels by one line: "By W4 the arrow d has a blur: ω ∼ ω′ iff dω = dω′. It is not made from gluings; it is read off the arrow." Keep P1–P3. This chapter is a Select chapter and should say so in one sentence under the title.

Check: `grep -n 'varepsilon' ch1[0-3]*.tex` should show ε only as the dual-number letter in Chapter 11 and in Old names.

### Task 2. Chapter 18: Divisibility and primes (new file `ch18-divisibility.tex`)

Line: `ℤ under × → sizes by division · from: Chapters 1 and 3 · one-way blur, blur`.
This is the chapter for one-way blurs (L8). It is not optional decoration: the project's own results are about them.

Design (verify every claim):
- Given: ℤ with G1–G8 of Chapter 2's Given list (cite Chapter 1 lines as Chapter 2 does), and Chapter 3, P2 (division with remainder) and R1 (all blurs of ℤ respecting + are "same remainder mod n"). grep the labels.
- D1 (one-way, L8): a | b iff b = a × c for some c. Reflexive, chains. Respects ×. Does not respect +: witness 1 | 2 and 1 | 3 gives nothing; use 2 | 2, 2 | 4 … find a correct witness by script (a | b, a′ | b′, but not a + a′ | b + b′; e.g. 2 | 4 and 3 | 3, 5 ∤ 7).
- B1 (from below): one gluing, −1 ∼ 1, respecting ×. B2 (from above): questions "d divides x", one for each d, respecting ×. Same O.
- Bags: a ∼ b iff b = a or b = −a. Normal forms: a ≥ 0. So ℕ is the bag of normal forms: the chapter undoes Chapter 1's sign.
- Appears: B1 = B2. Sandwich: d | −x iff d | x. Separating context: if b ≠ ±a then a ∤ b or b ∤ a; the question "a divides x" separates. Also state: the two-way part of | is exactly this blur (L8).
- Survives: ×, |a|, the one-way |. Dies: the sign; +; and ≤ is replaced: | is an order on bags that is not total (2 and 3).
- Shape of the order: 1 is below everything, 0 is above everything (everything divides 0). Say it; it surprises.
- Appears next: a bag is *prime* if it is not the bag of 1 and nothing lies strictly between the bag of 1 and it. (Atoms.)
- Theorems: every a other than 0, ±1 is above some prime (from G8). p | ab ⇒ p | a or p | b (from Chapter 3, P2/R1; say the proof route). Unique factorisation. Infinitely many primes.
- The order from above: for each prime p the question v_p(a) = how many times p divides a (a ≠ 0). Theorem: a | b iff v_p(a) ≤ v_p(b) for every p. So the one-way blur is known by questions with ordered answers. gcd and lcm are min and max place by place.
- Link to Chapter 3 (the nice one): among the blurs "mod n" of ℤ, "mod n is blurrier than mod m" (L4) iff n | m. So blurrier-than, on the blurs of ℤ, *is* divisibility. Check for n, m ≤ 60 by script.
- Remark (project result, exact wording required): "The one-way blurs of ℤ/n that respect × and are orders have been counted in this project: 7, 27, 21, 11, 177 for n = 4, 6, 8, 9, 12. Found in this project, machine-checked, not yet checked by a specialist." Do not add other numbers unless you recompute them with `/mnt/project-files/abs/quord.py` or `quord_n.py` and show the output.
- Check script `ch18-check.py`: the + witness; a | b iff valuations compare, for 1 ≤ a, b ≤ 2000; gcd/lcm as min/max; blurrier iff divides for n, m ≤ 60; unique factorisation for n ≤ 5000.

### Task 3. Chapter 19: Mod pᵏ and the p-adic numbers (new file `ch19-p-adic.tex`)

Line: `ℤ → ℤ_p · from: Chapters 3, 4, 5 and 18 · blur ladder, build, select, blur`.
This is the twin of Chapters 4 and 5 where chaining survives. Announce that contrast in the tagline.

Design:
- Given: ℤ, a prime p (Chapter 18), Chapter 3 (≡ mod n is a blur respecting + and ×).
- D: the rungs x ≡_k y iff pᵏ | x − y. Each rung is a **blur** (it chains) and respects + and ×. Nested. Bottom: equality on ℤ. So this is a nearness in the sense of Chapter 5, D4 whose rungs chain: "two steps for one" costs nothing (x ≡_k y ≡_k z ⇒ x ≡_k z). State the reason from Chapter 5, R2: the bag of 0 is closed under +.
- Dies at once: size. pᵏ comes near 0. Witness: 1, p, p², … comes near 0 here and grows without bound for ≤.
- Build sequences of integers (M2); Select those that come near themselves (Chapter 5, N5 with these rungs); Blur: a ∼ b iff for every k eventually a_i ≡_k b_i. B2: question "comes near 0", respecting +. Follow Chapter 4's lines one for one, and say so.
- Normal forms: digits to the left, d_0 + d_1 p + d_2 p² + … with 0 ≤ d_i < p, **exactly one** for each bag. Contrast with decimals, where 0.4999… and 0.5000… are one real. Reason: here chaining survived.
- Notation: ℤ_p. Arrow ℤ → ℤ_p inside. For each k a picture ℤ_p → ℤ/pᵏ respecting + and ×: every clock of Chapter 3 for a power of p is a picture of ℤ_p, and a member of ℤ_p is known by its pictures (a compatible list of remainders).
- Appears: −1 = …(p−1)(p−1)(p−1). 1 + p + p² + … comes near 1/(1 − p). x in ℤ_p has an inverse iff d_0 ≠ 0. For p = 7: x² = 2 has a solution in ℤ_7 (since 3² ≡ 2 mod 7 and the solution lifts rung by rung); x² = 3 has none (not even mod 7).
- Laws: + and × survive; all equations free (Z7). Z8 check: no zero divisors — true for p prime. Remark with witness: for 10 in place of p it fails; there are four x with x² = x in the 10-adic integers (…0, …1, …890625, …109376). Compute them in the script.
- Order ≤ dies (as in Chapter 3). "The line can be cut": ≡_1 on ℤ_p is a blur whose bags are whole neighbourhoods; ℤ_p falls into p pieces. Opposite of Chapter 5, T1.
- Closed: run again on ℤ_p and nothing new appears (twin of Chapter 4, T7).
- Remarks: fractions (rerun Chapter 2) give ℚ_p, with ℚ inside; ℝ and the ℚ_p are different closings-up of ℚ, one for "small is small" and one for each prime ("divisible by a high power is small"). Old theorem (Ostrowski), stated as a remark and marked "not proved here": these are all of them. Old names: p-adic integers, Hensel's lemma, inverse limit, ultrametric.
- Check script `ch19-check.py`: lift √2 in ℤ_7 through 12 rungs; inverse of 1 − p mod pᵏ equals the partial sums; −1 digits; the four 10-adic idempotents mod 10^12; a zero-divisor pair among them.

### Task 4. Chapter 20: Sequences of maps (new file `ch20-sequences-of-maps.tex`)

Line: `maps on a stretch → limits of maps · from: Chapters 4, 5, 10, 12, 17 · build, select, blur`.
Repairs the gap under exp in Chapter 10 (limits were exchanged without a rule).

Design:
- Fix a stretch b ≤ x ≤ c. C[b,c]: maps continuous at each point of it (Chapter 10 on a stretch; by Chapter 5, T7 they respect nearness uniformly).
- D (a nearness on maps, Chapter 5, D4): f M_k g iff f(x) N_k g(x) for **every** x of the stretch. Check P10, P11 and the bottom (equality). A second family, one for each point: f P_{k,x} g iff f(x) N_k g(x). "Comes near f" for M is uniform convergence; for all the P_{·,x} it is pointwise convergence.
- Dies under pointwise, survives under M — this is the chapter: continuity of the limit. Witness: xⁿ on 0 ≤ x ≤ 1 comes near, point by point, a map with a jump at 1.
- Then run Chapter 4 on C[b,c] with M: sequences of maps that come near themselves; blur by "near at every rung, eventually". Theorem (closed, F5): every such sequence comes near a map in C[b,c]; the chapter adds nothing. C[b,c] is already complete.
- Survives lines (state as "the arrow f ↦ … respects nearness M"): the integral ∫_b^c (Chapter 12) respects M: |∫f − ∫g| ≤ (c − b)·10^(-k). So limits pass through ∫. The derivative does **not** respect M (witness: sin(n²x)/n comes near 0, its derivatives do not). Correct statement: if f_n′ come near g in M and f_n(b) come near a number, then f_n come near an f with f′ = g.
- Series of maps: Σ u_n. Comparison (Chapter 17, T4): if |u_n(x)| ≤ a_n on the stretch and the series of a_n settles, the series of maps comes near a map in M. Power series Σ a_n xⁿ: there is an R (possibly 0 or "no bound") such that it comes near in M on every stretch inside |x| < R; inside, it can be differentiated and integrated term by term. Consequence: exp′ = exp, already used in Chapter 11, T4, is now earned — say this.
- Remarks: old names (uniform convergence, Weierstrass M-test, radius of convergence, Dini not needed). Honest edge (Chapter 17, R2): on the edge |x| = R everything depends on cancellation.
- Check script: sup of |xⁿ − limit| on [0,1] stays 1; on [0, 0.9] falls; ∫ of xⁿ on [0,1] → 0; sin(n²x)/n example; exp partial sums in M on [−3, 3].

### Task 5. Chapter 21: Taylor (new file `ch21-taylor.tex`)

Line: `germs → jets of every order · from: Chapters 7, 10, 11, 20 · blur ladder, select`.
A **ladder of true blurs** (each rung chains), on maps near a point.

Design:
- Rung k at a: f ∼_k g iff f(a) = g(a) and (f(x) − g(x))/(x − a)^k comes near 0 as x comes near a. Rung 0 is the value blur (for continuous maps), rung 1 is Chapter 11. Each is a blur respecting + and ×. Higher k is less blurry.
- Straight at rung k: the bag holds a polynomial of degree ≤ k in (x − a); at most one. The straight bags at rung k match ℝ[x]/(x^(k+1)) of Chapter 7 with + and × (truncate products). For k = 1 this is Chapter 11, P9.
- If f has k derivatives at a, its bag at rung k holds Σ f^(i)(a)(x − a)^i / i!. (Taylor polynomial as normal form.)
- Arrows between rungs: forgetting the top coefficient is a picture from rung k + 1 to rung k: a chain of pictures … → rung 2 → rung 1 → rung 0, the same shape as … → ℤ/p³ → ℤ/p² → ℤ/p in Chapter 19. Say so: (x − a) plays the part of p.
- The bottom of the ladder is **not** the germ. Witness: f(x) = exp(−1/x²), f(0) = 0, is glued to 0 at every rung at a = 0 and has a different germ. So "all Taylor coefficients" forgets something. (Dies: the germ.) Verify numerically.
- Remainder (classical): if f has k + 1 derivatives between a and x, then f(x) − (its polynomial at rung k) = f^(k+1)(t)(x − a)^(k+1)/(k + 1)! for some t between. (From Chapter 11, T6, applied k + 1 times.)
- When the series comes near f (Chapter 20): exp, cos, sin for every x. Not always: the witness above.
- Old names: k-jet, Taylor polynomial, Lagrange remainder, formal power series, analytic, flat function.
- Check script: products truncate correctly against sympy series; the flat witness; remainder bound for exp at several points.

### Task 6. Chapter II.4: Metric spaces (new file `p2-ch4-metric-spaces.tex`)

Line: `systems with a distance → classes · from: Chapters I.4, I.5, I.8, I.10, I.19, I.20 · table, class, blur`.
The planned chapters Modules, Arrows, One class, Machines become II.5–II.8: update the table in `p2-ch0-map.tex`, the "Planned" line in `contents.tex`, and the pointer in `p2-ch3-vector-spaces.tex` R5.

Design:
- Rows: ℚ, ℝ, ℝⁿ, the circle with d of I.8, C[b,c] with the largest gap (I.20), ℤ with the p-adic distance p^(-v) (I.19), ℤ_p, and a three-point row with all distances 1.
- Tests: `dist` (d ≥ 0, d = 0 only for equal points, symmetric, triangle); `complete` (comes near itself ⇒ comes near something); `bounded`; `compact` (every sequence has a part that comes near something); `onepiece` (cannot be cut, as in I.5, T1); `chains` (d(x, z) ≤ max(d(x, y), d(y, z)): every rung is a blur).
- Fill the table truthfully, row by row. Known answers to verify: ℚ fails complete; ℝ fails bounded and compact, passes onepiece; a closed stretch passes compact; ℤ_p passes complete, compact, chains, fails onepiece; ℤ with p-adic distance fails complete; C[b,c] passes complete, fails compact; the three-point row passes everything except onepiece.
- Classes that appear: metric space; complete; compact. And one the method cares about: `chains` separates the rows where a ladder of true blurs is enough (I.19) from the rows where likeness is needed (I.5). State as a theorem: a row with at least two points passing `chains` fails `onepiece`.
- One variable row X: the nearness of X from d (I.5, D4); "respects nearness" for maps between rows; Chapter I.4 run on X (the completion): theorem, the result is closed (F5) and X sits inside; ℝ is the result for ℚ, ℤ_p for ℤ with the p-adic distance, C[b,c] for the polynomials on the stretch (classical, Weierstrass, mark as long). Contraction theorem on a complete row.
- The blur on rows: glue two rows when a one-to-one onto map respects nearness both ways. What survives: complete? No — witness: ℝ and the open stretch 0 < x < 1 are glued by a map respecting nearness **at each point** both ways, one complete and one not; with **uniform** respect both ways, complete survives. This distinction is the content; get it exactly right.
- No machine check is possible for most of this; say so, and check the finite row and the p-adic triangle law by script.

## 5. Order and stopping rule

Do Task 1, then 2, 3, 4, 5, 6. After each task stop and report to E (rule 10 above). If a design line turns out false or unclear, do not improvise around it: write the chapter without that line, and tell E exactly which line and why. A shorter true chapter is better than a complete false one.

Not for this session: measure and the Lebesgue integral, Fourier series, function spaces, and proofs. They are planned later and need their own design.

## 5a. Who does what (Opus builds, Fable designs and checks)

Opus (build session) does: writing chapters from the finished designs in section 4, check scripts, `build.py`, the map and contents pages.

Fable (planning session, the thread "Write old mathematics as a textbook myself") is needed for exactly three things. The build session must stop and hand back to E instead of doing them:

1. **Designing a chapter that has no design in this file.** Measure and Lebesgue, Fourier, function spaces, and anything else not in section 4. Do not design them in the build session.
2. **Checking the lines that can be quietly false:** every Appears line, every Dies witness, every remark that says something fails, same O in B1 and B2. Riskiest spots in this work order: Task 6 (the "complete survives or not" line) and the Appears lines of Task 3.
3. **Any change to Chapter 0.** Do not add, change or reinterpret a rule in `ch0-rules.tex`, and do not introduce a new primitive or a new kind of blur. If a chapter seems to need one, stop and tell E which line and why.

## 6. What the planning session will check afterwards

Every Appears line; every Dies witness; every theorem; every remark that says something fails; B1/B2 same O; citations; whether each chapter passes the test of section 3.
