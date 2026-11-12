# Design: Chapter 26. Null sets, and "almost everywhere"

Status: design for E to agree. Not built. Machine check: `ch26-check.py` (run 11 Nov, every line True; the last two lines of that script are illustrations, not tests).

**Title line:** maps on a stretch → maps up to a null set · from: Chapters 4, 5, 10, 20 · blur
**Sentence under the title:** Glue two maps when they differ only on a set too thin to have a length. The value at a point dies. Nothing continuous is glued, and that is because the line cannot be cut.

Shape: blur only. One hard line (T1), and it is not imported: it comes from Chapter 5, T8.

## Given
- G1 Chapter 20, D1: the stretch b ≤ x ≤ c, F[b,c], C[b,c], + and × place by place; "comes near point by point".
- G2 Chapter 5: rungs, T8 (one-way: near every point, then everywhere).
- G3 Chapter 4: sequences; ℚ is listed by a sequence (to confirm at build where the book says this; if nowhere, add it as a line here with the list by denominators).

## Definitions
- D1 An **open stretch** is b′ < x < c′; its length is c′ − b′.
- D2 A set N of reals is **null** if for every rung k there is a sequence of open stretches that together hold every member of N, with every finite sum of their lengths < 10⁻ᵏ.
- D3 A statement about points holds **almost everywhere** if the points where it fails form a null set.

## The blur
On F[b,c]. O = {+, ×, h∘ (composing with any map h : ℝ → ℝ afterwards), limit point by point of a sequence}.
- B1 (From below.) Glue f ∼ g whenever f = g almost everywhere.
- B2 (From above.) Postponed, and said so: the questions that give this blur from above are integrals, and they are Chapter 27's. Until then the gluings are the bag test.

## Propositions
- P1 (Null sets: parts.) Every part of a null set is null. A single point is null.
- P2 (Null sets: a sequence of them.) If N₀, N₁, N₂, … are null, the set of all their members is null. (Give Nᵢ a cover at rung k + i + 1. The lengths add to less than 10⁻ᵏ/9.)
  Honest note: this picks one cover for each Nᵢ, a sequence of choices. For sets of points (P3) the covers are written down and nothing is chosen.
- P3 (ℚ is null.) So is every set listed by a sequence.
- P4 (A true blur.) ∼ chains (P2 for two sets) and respects + and ×, and h∘f ∼ h∘g for every h.
- P5 (Dies.) (i) The value at a point: f = 1 at ½ and 0 elsewhere is glued to 0. (ii) Composing in front: with h the constant ½, f∘h = 1 and 0∘h = 0 everywhere. (iii) "Continuous": the map χ that is 1 on ℚ and 0 elsewhere (Chapter 12, R3) is glued to 0. (iv) The largest value.
- P6 (Survives: limits of sequences.) If fₙ ∼ gₙ for every n, and fₙ comes near f point by point almost everywhere, then gₙ comes near f almost everywhere. (P2.) The order survives in the form "f ≤ g almost everywhere", a one-way blur (L8).
- P7 (Why not a smaller blur. A Dies line for the rival.) "Differ at finitely many points" is also a true blur respecting + and ×. It does not respect limits of sequences: fₙ := 1 on the first n rationals is glued to 0 for each n, and its limit χ is not. So P6 is what the word "sequence" in D2 buys.

## Theorems
- **T1 (A stretch is not null.)** If b < c, the stretch b ≤ x ≤ c is not null. More exactly: open stretches that together hold it have lengths adding to more than c − b.
  Route, two steps. (a) Finitely many are enough: let P(x, y) say "finitely many of the given open stretches hold all of x ≤ t ≤ y". P chains, and holds near every point because each point lies in one open stretch. Chapter 5, T8. (b) For finitely many: walk from b, each time taking a stretch that holds the current point; the right ends pass c, and the lengths add to more than c − b.
- **T2 (Nothing continuous is glued.)** If f and g are in C[b,c] and f ∼ g, then f = g. So C[b,c] → bags is an inside, and ∫ of Chapter 12 is untouched. (If f(a) ≠ g(a) they differ on a whole stretch around a: T1.)
- **T3 (Over ℚ everything is glued.)** Run this chapter on ℚ in place of ℝ: every set is null (P3), so all maps share one bag. Length needs the closing-up of Chapter 4. Twin: ℚ can be cut (Chapter 5, T1 fails there) and its stretches are null; ℝ cannot be cut and its stretches are not.
- T4 (A null set leaves no gap.) If N is null, every open stretch holds a point outside N. (T1.)

## Remarks
- R1 (A ladder of three blurs.) Differ at finitely many points; differ on a set listed by a sequence; differ on a null set. Each is blurrier than the one before. The second already respects limits of sequences. The third is chosen because of what appears in Chapter 27: there it is exactly "∫|f − g| = 0".
- R2 (Null is not small in number.) The middle-thirds set, left after removing the open middle third of each stretch again and again, is covered by 2ᵏ stretches of length 3⁻ᵏ, so it is null. It cannot be listed by a sequence (classical, not proved here).
- R3 (What was hard.) Only T1, and its proof is Chapter 5, T8 once. The blur did not prove it; "the line cannot be cut" did.
- R4 (Old names.) Null set: set of Lebesgue measure zero. T1 step (a): Heine–Borel. Bags: functions modulo null functions. R2: Cantor set.
- R5 (Machine check.) P3 for 400 rationals at rungs 0, 1, 3; the shares of P2; T1 step (b) on 600 random finite covers; R2's totals.

## Exercises (each to be worked before building)
- E1 Cover the whole numbers by open stretches of total length < 10⁻³.
- E2 Show the set of all x with x² rational is null.
- E3 Give two maps glued here whose largest values differ.
- E4 In T1(b), where is "open" used? Cover 0 ≤ x ≤ 1 by the two closed stretches 0 ≤ x ≤ ½ and ½ ≤ x ≤ 1 and compare.
- E5 Is "f is 0 somewhere" kept by ∼? Is "f is 0 almost everywhere"?

## Edits elsewhere when built
ch0-map row 26 and an arrow from "limits of maps". Chapter 12, R3: add "(Chapter 26 begins this.)".
