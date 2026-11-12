# Design: Chapter 25. Inverting a map

Status: agreed by E and built 11 Nov as ch25-inverting.tex. Machine check: `ch25-check.py` (run 11 Nov, every line True).

**Title line:** maps ℝⁿ → ℝⁿ → their inverses near a point · from: Chapters 5, 10, 11, 13, 14 · select, survives, dies
**Sentence under the title:** A straight map can be inverted exactly when its determinant is not 0. Does that answer survive the tangent blur? Not on the whole bag. It does on the maps whose tangent changes continuously.

Shape: no new blur. The chapter reads the tangent blur of Chapter 13 once more, asks one question of its normal form, and finds the question dies on the bag and survives after a Select. This is the first chapter where Select is what rescues a Survives line.

## Given
- G1 Chapter 13: tangent blur at a, straight bags, DF_a, T2 (composing survives on straight bags).
- G2 Chapter 14: a linear map L of ℝⁿ has an inverse ⇔ det L ≠ 0. (To confirm at build that Chapter 14, T3–T4 say this; if not, add the line there.)
- G3 Chapter 11, T5.1 (rising chains), T6. Chapter 10, T1 (intervals survive), T3 (continuity survives inverting).
- G4 Chapter 5, G3: ℝ is closed. Chapter 20, T1: C[b,c] is closed.

## Definitions
- D1 (Select.) F : ℝⁿ → ℝⁿ is **C¹ near a** if its bag is straight at every point x near a and DF_x respects nearness in x.
- D2 F **can be inverted near a** if there is a box U around a on which F is one-to-one, the values of F on U cover a box around F(a), and the inverse G is C¹ near F(a).
- D3 A **contraction** of a closed box B is a map T : B → B with |T(x) − T(y)| ≤ q·|x − y| for one fixed q < 1.

## The blur
The tangent blur at a (Chapter 13, B1/B2), O = {+, ×, composing}. Nothing new is glued. The question asked: "can it be inverted near a?"

## Propositions
- P1 (The normal form answers.) The affine map c + L(x − a) can be inverted ⇔ det L ≠ 0. Then the inverse is affine, with linear part L⁻¹.
- P2 (Tangents of inverses are inverse: a Survives line.) If F and G are inverse to each other, F straight at a and G straight at F(a), then DG·DF = 1. So det DF_a ≠ 0. (G1: composing survives.) In particular: where det DF_a = 0 no inverse has a tangent.
- **P3 (Dies on the whole bag.)** f(x) = x + 2x² sin(1/x), f(0) = 0, has a slope at every point, shares the bag of x at 0 (slope 1), and is one-to-one on no interval around 0: its slope is −1 at every 1/(2πm). So the answer "yes" of the normal form is not kept by the tangent blur at one point.
- P4 (Dies where det = 0.) x³ and x² share the bag of 0 at 0. x³ is one-to-one (its inverse has no slope at 0, as P2 says); x² is not one-to-one near 0. So there even "one-to-one" is not answered.

## Theorems
- **T1 (One variable: rising chains.)** If f is C¹ near a and f′(a) ≠ 0, then f can be inverted near a, and the inverse g has g′(f(x)) = 1/f′(x). (f′ keeps its sign near a because it respects nearness; then G3: f rises or falls on an interval, its values form an interval, the inverse is continuous; then the slope.)
- **T2 (Contraction: exactly one fixed point.)** A contraction T of a closed box has exactly one x with T(x) = x, and x₀, T(x₀), T(T(x₀)), … comes near it from any start.
  At most one: |x − y| ≤ q|x − y| forces x = y. This half is a blur-style "only one" line. At least one: the steps shrink like qᵏ, so the sequence settles; G4.
  T2.1 The same for a contraction, in the nearness M, of a closed part of C[b,c]. (Used later for differential equations.) II.4, T5 is then this line for every complete row.
- **T3 (Survives on C¹: inverting.)** If F is C¹ near a and det DF_a ≠ 0, then F can be inverted near a, and DG = (DF)⁻¹ at matching points.
  Route: compose with the inverse of DF_a so the tangent at a is the identity. Then φ(x) = x − F(x) has tangent 0 at a, so on a small box |φ(x) − φ(y)| ≤ ½|x − y| (C¹, with Chapter 11, T6 along segments). One-to-one follows. For y near F(a), x ↦ φ(x) + y is a contraction of the box; its fixed point solves F(x) = y. Existence comes from T2, that is, from "closed": the one place it should.
- **T4 (Level sets are graphs.)** If F : ℝ² → ℝ is C¹ near (a, b), F(a, b) = 0 and ∂_y F(a, b) ≠ 0, then near (a, b) the points with F = 0 are the graph of exactly one C¹ map y = g(x), and g′ = −∂ₓF/∂_yF. (T3 for (x, y) ↦ (x, F(x, y)).)
  Example: the circle x² + y² = 1 near (0.6, 0.8), slope −x/y. Dies at (1, 0): no graph over x there.

## Remarks
- R1 (Why P3 is not a failure of T3.) In P3 the slope does not respect nearness at 0. D1 is exactly the Select that removes it.
- R2 (Nearby does not chain in ℝⁿ.) In one variable T1 chains: f′ ≠ 0 on an interval gives one-to-one on the interval (Chapter 5, T8). In ℝ² it does not: exp on ℂ, (x, y) ↦ (eˣ cos y, eˣ sin y), has det = e²ˣ ≠ 0 everywhere and takes the same value at y and y + 2π. Chapter 5, T8 needs the order of ℝ.
- R3 (Old friends.) T1 gives the slope 1/y of the inverse of exp (Chapter 22, P2; Chapter 12, T5) and the slopes of k-th roots.
- R4 (Old names.) T3: inverse function theorem. T2: Banach's fixed point theorem. T4: implicit function theorem. D1: continuously differentiable.
- R5 (Machine check.) P3 (slopes −1 and +3 arbitrarily near 0); P4; T3 on 215 random maps of ℝ² (the contraction solved F(x) = y in at most 8 steps, and the tangent of the inverse matched the inverse of the tangent); T4 on the circle; R2.

## Exercises (each to be worked before building)
- E1 Where can (x, y) ↦ (x² − y², 2xy) be inverted nearby? Which chapter's map is it?
- E2 Show x ↦ cos(x)/2 is a contraction of −1 ≤ x ≤ 1 and find its fixed point to three places.
- E3 Near which points of x³ + y³ = 3xy is the set a graph over x, by T4?
- E4 Find the slope of the inverse of x + x³ at the value 2.
- E5 In P3, what goes wrong in the route of T3?

## Edits elsewhere when built
p2-ch4-metric-spaces T5: add "(Chapter 25, T2 is the case of a closed box.)". ch0-map row 25 and an arrow from "tangents on ℝⁿ". Chapter 14 line for G2 if missing.
