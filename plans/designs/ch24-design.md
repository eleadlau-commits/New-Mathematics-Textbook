# Design: Chapter 24. Highest and lowest points

Status: agreed by E and built 11 Nov as ch24-extremes.tex. Machine check: `ch24-check.py` (run 11 Nov, every line True).

Change to WORKPLAN-2: its item B1 held two blurs (rung 2 at one point; tangents at all nearby points). A chapter has one blur, so B1 is split. This is Chapter 24. "Inverting a map" becomes Chapter 25, and the later numbers move up by one.

**Title line:** maps on ℝⁿ → what they do near a point where the tangent is flat · from: Chapters 11, 13, 14, 21 · blur, survives, dies
**Sentence under the title:** Chapter 11 read "rising" off the tangent, and lost it where the slope is 0. One rung up, the question comes back, and is lost again in exactly one case.

Shape: blur only. It is Chapter 21 at rung 2, run on ℝⁿ, and its theorems are one Survives/Dies table, the twin of Chapter 11, T5.

## Given
- G1 Chapter 13: nearness on ℝⁿ, |h|, covectors, "straight" at rung 1, df, T7 closed boxes survive.
- G2 Chapter 21: flat to order k, the rungs ∼_k on maps of one variable, T2 (how far off, with a bound K on the next derivative).
- G3 Chapter 11, T5: where the slope is not 0, "rising" is kept by the tangent blur.
- G4 Chapter 14, T1: det.

## Definitions
- D1 e is **flat to order 2 at a** if e(a) = 0 and e(a + h)/|h|² comes near 0 as h comes near 0.
- D2 A **quadratic part** is a map Q(h) = Σ q_ij h_i h_j with q_ij = q_ji real. A **polynomial of order 2 at a** is c + L(h) + Q(h), with c real, L a covector, Q a quadratic part.
- D3 Q is **positive** if Q(h) > 0 for every h ≠ 0; **negative** if −Q is positive; **of both signs** if Q(h) < 0 < Q(h′) for some h, h′.
- D4 a is a **strict lowest point nearby** of f if f(x) > f(a) for every x ≠ a near enough to a. Likewise highest.

## The blur
O = {+, ×}. Fix a in ℝⁿ.
- B1 (From below.) Glue f ∼₂ g whenever f − g is flat to order 2 at a.
- B2 (From above.) Keep the questions "what is the bag of f·h at rung 2", for every h.
Honest sentence, as in Chapters 11, 13, 21: the gluings are the bag test; this blur is made from above.

## Propositions
- P1 (True blur, a rung.) ∼₂ chains and respects + and ×. f ∼₂ g gives f ∼₁ g (the blur of Chapter 13). For n = 1 it is Chapter 21 at k = 2.
- P2 (Normal forms: at most one.) A bag holds at most one polynomial of order 2 at a. Call the bag **straight at rung 2** if it holds one.
- P3 (When: three slopes are enough.) If f has continuous slopes up to order 3 near a, its bag is straight at rung 2, with c = f(a), L = df_a, q_ij = ½ ∂_i∂_j f(a). (Chapter 21, T2 along each segment a + t·h; the bound K comes from closed boxes survive.) q_ij = q_ji is Chapter 13, T5.
  Honest note: classically two continuous orders suffice. The book asks for three, as Chapter 21, T2 does.
- P4 (A positive Q is large.) If Q is positive there is m > 0 with Q(h) ≥ m·(largest |h_i|)² for every h. (The faces of the cube "largest |h_i| = 1" are finitely many closed boxes; Q takes a lowest value on each, and it is > 0. Then scale.)
- P5 (Reading Q for n = 2.) Q is positive ⇔ q₁₁ > 0 and q₁₁q₂₂ − q₁₂² > 0. Q is of both signs ⇔ q₁₁q₂₂ − q₁₂² < 0. The number q₁₁q₂₂ − q₁₂² is det of Chapter 14 on the rows of Q.

## Theorems (one table)
Let the bag of f at a be straight at rung 2, with normal form c + L + Q.
- **T1 (L ≠ 0: rung 1 already answers.)** a is neither a lowest nor a highest point nearby. (G3 along a line where L ≠ 0.) So only the points with df_a = 0 are left.
- **T2 (Survives: Q positive.)** If L = 0 and Q is positive, "a is a strict lowest point nearby" is yes for the normal form and is kept by ∼₂. (By P4 the normal form is above c + m·s², s the largest |h_i|; what is glued away is smaller than m·s² near a.) Q negative: strict highest point.
- **T3 (Survives: Q of both signs.)** If L = 0 and Q is of both signs, "a is neither" is kept by ∼₂. (Go along h and along h′.)
- **T4 (Dies: every other case.)** If L = 0 and Q is 0 at some h ≠ 0 without being of both signs, the question is not kept. Witnesses, n = 1, all in the bag of 0: x⁴ (lowest), −x⁴ (highest), x³ (neither). n = 2, same bag: x² + y⁴ (lowest) and x² − y⁴ (neither).
- T5 (Where to look.) A continuous f on a closed box has a lowest point (Chapter 13, T7). It lies on the boundary of the box, or at a point where df = 0. (T1.)
- T6 (One variable.) For n = 1, Q(h) = ½f″(a)h²: f′(a) = 0 and f″(a) > 0 give a strict lowest point nearby; f″(a) = 0 decides nothing.

## Remarks
- R1 (The ladder goes on.) In one variable, if rung 2 does not decide, go up: the first k with f⁽ᵏ⁾(a) ≠ 0 decides (k even: lowest or highest by sign; k odd: neither), and exp(−1/x²) of Chapter 21, P8 is decided at no rung. In several variables the higher rungs do not sort so simply; not done here.
- R2 (Twin lines.) Chapter 11, T5: slope ≠ 0 keeps "rising"; dies at slope 0. Here: Q with no zero direction keeps the answer; dies when Q has one. Chapter 23, T1 was the same step for |p|.
- R3 (Not a way to find the lowest point.) T5 gives a list of places to look, nothing more. T2 is about "nearby" only: x³ − 3x has a strict lowest point nearby at 1 and no lowest point on ℝ.
- R4 (Old names.) Q: half the Hessian form. T2–T4: second derivative test; T3: saddle point. P5: Sylvester's criterion for n = 2. Points with df = 0: critical points.
- R5 (Machine check.) P4, T2, T3 on random forms for n = 1, 2, 3 with a random third-order part glued away; the witnesses of T4; P5 on 2000 forms; P3 on exp(x)cos(y) + xy² (error/|h|² shrank tenfold per tenfold step).

## Exercises (each to be worked before building)
- E1 Sort the point (0,0) for x² + xy + y², for x² + 3xy + y², and for x² + 2xy + y².
- E2 Find every point with df = 0 for x³ − 3x + y² and sort each.
- E3 Show x⁴ + y⁴ and −x⁴ − y⁴ share a bag at rung 2 and at rung 3.
- E4 Lowest point of x² + y² − x on the box 0 ≤ x, y ≤ 1, by T5.
- E5 Why does T2 need "strict"? Look at the constant map.

## Edits elsewhere when built
ch0-map: row 24 and one arrow from "jets of every order" (and Chapter 13). contents.tex "Planned". WORKPLAN-2 numbering note.
