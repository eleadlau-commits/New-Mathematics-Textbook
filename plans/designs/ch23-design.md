# Design: Chapter 23. ℂ is closed

Status: agreed by E and built 11 Nov as ch23-c-is-closed.tex. Machine check: `ch23-check.py` (run 11 Nov, all lines True; repeating the local step reached a root in 100 of 100 random polynomials).

**Title line:** polynomials over ℂ → their roots · from: Chapters 7, 8, 10, 13 · survives, dies
**Sentence under the title:** A lowest point exists because closed boxes survive. A lowest point cannot sit where p ≠ 0, because "can be lowered" survives the blur that keeps the first two terms. So the lowest point is a root.

Shape: no new object is made. This chapter is two Survives lines meeting, like the mean value theorem (Chapter 11, T6). It removes the note "classical, long" from Chapter 10, T11.

## One line added to Chapter 13 first
**T7 (Closed boxes survive.)** If f : ℝⁿ → ℝ is continuous, then on a closed box (b_i ≤ x_i ≤ c_i in every place) f takes a largest and a smallest value. From Chapter 5, G3, halving the box one place at a time. Chapter 10, T2 is the case n = 1.

## Given
- G1 ℂ, its + and ×, and |z| with |zw| = |z||w|, |z + w| ≤ |z| + |w| (Chapter 7, T5; Chapter 13, D1 for ℂ read as ℝ²).
- G2 Polynomials with coefficients in ℂ: Chapter 7 run with ℂ in place of ℝ. Normal forms, degree, T4 (roots split off a factor x − t).
- G3 The wrapping w and "every member of S is w(t)" (Chapter 10, T7, T8); n·y = a has exactly n solutions in 𝕋 (Chapter 8, T2).
- G4 Chapter 13, T7 above; Chapter 10, T1 (intervals survive).

## Definitions
- D1 a is a **lowest point** of p if |p(a)| ≤ |p(z)| for every z in ℂ.
- D2 For p and a point a, the **first two terms of p at a**: write p(a + h) = c₀ + c_k hᵏ + (higher powers of h), where c₀ = p(a) and c_k is the first coefficient after c₀ that is not 0.

## The blur (one, named, with its O)
- B1 At a point a and rung k: glue p ∼ q iff p(a + h) − q(a + h) has only powers of h above k. This is the rung of Chapter 21 for polynomials, exact, no limit (Chapter 7, T7 is the rung 1 case). O = {+, ×}. From above: the questions "coefficient of hʲ at a", j ≤ k. They agree (Chapter 7, P5 re-centred). Honest note: the gluings are the bag test again.
- P1 (Normal forms.) Each bag holds exactly one polynomial of degree ≤ k in h. For k as in D2 it is c₀ + c_k hᵏ.

## Propositions
- P2 (Re-centring is exact.) p(a + h) is a polynomial in h of the same degree, with the same leading coefficient. So for degree ≥ 1 the k of D2 exists.
- P3 (k-th roots appear in ℂ.) Every u ≠ 0 in ℂ has exactly k k-th roots. Write u = r·w(t) with r > 0. Then r has one positive k-th root (Chapter 10, T1 on xᵏ) and w(t) has exactly k (G3).
- P4 (Dies in ℝ.) P3 fails over ℝ: −1 has no square root. Witness for the whole chapter: x² + 1 has a lowest point at 0, value 1, and no root.
- P5 (Far away is large.) If p has degree n ≥ 1 and leading coefficient a_n, then |p(z)| ≥ |a_n||z|ⁿ/2 whenever |z| ≥ R := max(1, 2(|a₀| + … + |a_{n−1}|)/|a_n|).

## Theorems
- **T1 (Survives: "can be lowered".)** If p(a) ≠ 0, the answer to "is there h with |p(a + h)| < |p(a)|" is yes for the normal form c₀ + c_k hᵏ, and it is kept by the blur B1 at rung k. So a is not a lowest point of p.
  Reading: pick h₀ with c_k h₀ᵏ = −c₀ (P3). On the normal form, s·h₀ gives c₀(1 − sᵏ). The glued-away part is at most K·s^(k+1), which is smaller than |c₀|sᵏ for small s.
- **T2 (A lowest point exists.)** Every polynomial of degree ≥ 1 has a lowest point. By P5, outside a box |p| is above |p(0)|; inside it, Chapter 13, T7.
- **T3 (ℂ is closed for Chapter 7.)** Every polynomial of degree ≥ 1 over ℂ has a root. T2 gives a lowest point; T1 says it cannot be where p ≠ 0.
- T4 (Normal form of a polynomial over ℂ.) p = a_n (x − t₁)…(x − t_n), and the list of roots is unique up to order. (T3 with Chapter 7, T4, n times; "only one" from Chapter 7, T4.)
- **T5 (Survey: Road 2 is finished.)** Every polynomial over ℝ is a product of real factors of degree 1 and 2. So in Chapter 7, P9.1 the blurs ∼_d of ℝ[x] whose bags form a field are exactly d of degree 1 (bags: ℝ) and d of degree 2 with no real root (bags: ℂ, every time). Gluing polynomials makes no third field out of ℝ.
  To check in the build: the pairing of z with its conjugate, and that ℝ[x]/d is ℂ for every such d, not only x² + 1.

## Remarks
- R1 (Where existence came from.) Once: "closed boxes survive", which is G3 of Chapter 5. Everything else is "this is kept" and "only one". The blur did not produce the root.
- R2 (Not a recipe.) T3 does not say where the root is. Repeating T1 does walk downhill (machine check), but that it arrives is not proved here.
- R3 (Why ℂ and not ℝ.) The only step that uses ℂ is P3. P4 is its Dies witness.
- R4 (Old names.) T3: fundamental theorem of algebra, by the d'Alembert–Argand argument. T1: Argand's inequality. T5: irreducible real polynomials have degree ≤ 2.
- R5 (Ahead.) In the complex analysis chapters T1 becomes "|f| has no lowest point inside unless f is 0 there or constant", for every holomorphic f.

## Exercises (each checked true before building)
- E1 Find h₀ of T1 for p = x² + 1 at a = 0, and an s that lowers |p|.
- E2 For p = x³ − 1 at a = 0 find k and all three choices of h₀.
- E3 Show the bound R of P5 for p = x² − 3x + 5.
- E4 Factor x⁴ + 1 over ℝ as in T5.
- E5 Where does T1 fail if "p(a) ≠ 0" is dropped?

## Edits elsewhere when built
- Chapter 13: add T7. Chapter 10, T11: replace "(Classical. …long.)" by "(Chapter 23, T3.)". Chapter 10, R5 and ch0-map (row 23, one arrow from ℝ[x]/ℂ). contents.tex. "Imported" count falls from four to three.
