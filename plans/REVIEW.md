# Review: how the books use the method

Written 12 Nov 2026 (late), after reading `rules.tex` and all three buildings as they stand in the shared folder (identical to `main` at 29a0b2a). Nothing in the chapters was changed. E chooses what to apply.

---

## Verdict

1. **Chapters 1 to 21 use the method as an engine.** Each chapter makes one floor by one blur. B1 and B2 name the same O, Appears is proved by a named separating context, every Dies has a witness, names come only after the blur, and the Arrow checks each reused sign (C3). The theorems are few and are consequences of the blur lines. This is the method working as designed.

2. **From Chapter 22 on, and in most of Buildings 1 and 2, the method turns into a lens and then, in places, into labels.** The chapters stay correct, honest and often elegant, but the content increasingly comes from classical arguments (estimates, counts, Cauchy's formula, Sylow counting) with blur words attached. Of the 16 chapters 22 to 37, six have no Blur line at all, and only about seven have a real Appears line. The Notation and Arrow slots vanish from Chapter 20 on. In Building 2, Part II, there is no floor and almost no blur. The chapters are research reports.

3. **The drift is real, but half of it is healthy.** Proof sketches, the "where existence came from" remark, twin tables (v_p, ord, rung) and the honest Dies witnesses are improvements that the early chapters lack. The unhealthy half is this. Chapters claim a blur they do not have. Appears lines become empty ("the gluings are the bag test"). Classical names become the primary names. And load-bearing classical steps slip in as "reported" or "deferred".

4. **Imports are the most urgent finding.** Project memory says only three imports remain (Weierstrass, Borel, Ostrowski), and all three sit in remarks. The tonight build added **12 load-bearing steps that are not earned**. Later lines depend on them, and they are not marked Imported in the sense of the rules. The worst are the at-most-one line of the cubic's group law (Building 1, III.1 T2), Cauchy's theorem for C¹ maps (Building 0, ch32 G4, with a circular "payment" in ch33), and all of Building 2, Chapter 2. Full list in §4.

5. **Large structural change is needed in three places, not everywhere.** (a) Chapter 0 must admit the chapter kinds the books actually use, so that chapters stop pretending to blur. (b) Amplify (Z11) must leave Chapter 0, because it is a theorem that relies on Chapters 20, 33 and 34. (c) Building 2, Part II should become field notes, not a book part. Forcing a blur into every late chapter is **not** recommended. It would manufacture fake blurs.

---

## 1. The baseline (Chapters 1 to 5)

What the early chapters do every time, and what the later ones should be measured against:

| Slot | What it claims | Example |
|---|---|---|
| B1 | a few gluings, with "Respects:" | Ch3: the single pair n ∼ 0, respects + |
| B2 | one question, the **same** O | Ch3: "is a multiple of n", respects + |
| Appears | B1 = B2 by Z4 and Z5, **with the separating context named** | Ch3: z = −x; Ch1: the swap (b,a) |
| Survives / Dies | each with its reason or witness | Ch2 P4.2: place-by-place sum dies, (1,2)⊕(1,3) |
| Notation | names only after the blur | Ch1 N1: ℤ := 𝒫/∼ |
| Arrow | old → new, inside or picture; C3's four steps for each sign | Ch1 P6, R4 |
| Theorems | short, read off the new floor | Ch2 T1 to T7 |
| Remarks | other blurs, failures, old names last | Ch3 R1: the survey of all blurs of ℤ |

Two more habits matter. **A failed Appears is a result** (Ch5 P5: nearness is what lies between two blurs that both fail). **Old names live only in Remarks.**

## 2. How the use changes: the evidence

Slot counts, made by script over every chapter (`\lab{B1}`, `\lab{B2}`, the Notation and Arrow subsections, and the words "reported / classical / deferred / not proved / imported"):

| Block | Chapters | Have B1 and B2 | Real Appears (context named, or a genuine agreement) | Notation + Arrow slots | Import-word mentions |
|---|---|---|---|---|---|
| B0 ch1–19 | 19 | 18 (ch15 is a declared Select) | ~16 | 15 | 3 |
| B0 ch20–37 | 18 | 12 | ~7 | 0 (ch21 keeps Arrow only) | 27 |
| B0 Part II | 6 | 3 | 2 (II.1 classes, II.2) | 1 | 9 |
| B0 Part III | 4 | 1 | 1 (III.1) | 0 | 3 |
| B1 (Moves) | 20 | 12 | ~9 | 0 (own template) | 28 |
| B2 (Loops) | 6 | 2 | 1 (Ch1 completeness) | 0 | 32 |

Chapters whose verbs line says "blur" but which contain no Blur line: B0 ch34 ("blur, build"), III.2 ("select, blur"), III.4; B1 II.14, II.15; B2 Ch3, Ch4, Ch5.

The theorem slot also changes character. In Part II, Chapter II.1 still says "stated without proof, like the rest". From Chapter 22 on, nearly every theorem carries a parenthetical classical proof, often four to eight lines long. The proofs, not the blur lines, now carry the chapter.

## 3. Seven drifts

Each drift gives what changed, where, and a judgement.

**D1. "A chapter makes one new floor" quietly stopped being true.** About 20 chapters make no floor. They read an arrow (ch30, ch32, B1 III.2), select from an existing floor (ch22, ch25), count (B1 II.6, II.12, II.15, III.3), survey (ch29, B2 Ch6) or rerun (II.5, B1 II.7). Several say so honestly. B1 II.6 opens with "These are Theorems, not Survives lines". The rules do not have these kinds. *Judgement: the kinds are good and are the method's natural growth (build-only and select-only were already accepted). The rules should catch up. See change S1.*

**D2. From below became empty in analysis.** Chapters 11, 13, 21, 23, 24 and 26 say "the gluings are the bag test; this blur is made from above". The early workplan allowed this sentence as honesty. By now it is the norm in analysis, and an Appears line built on it proves nothing. Ch23 even says "so the two agree at once". Ch24 is worse: its B2 is "keep the question *what is the bag of f × h*", which defines the blur by its own bags (circular). *Judgement: write "B1: none, made from above" and drop the Appears claim, rather than state a vacuous one. Memory already records this as the honest state ("in analysis the from-below blur is just the bag test").*

**D3. The template order dissolved.** The fixed slot order became free-form section names: "Theorems on the rule", "The survey", "Propositions on examples", "The line of this chapter", "Floors with two glues". Theorems now come before Propositions (ch32, ch33). A Name line sits inside the blur section (ch27 N1, ch28 N1). Notation and Arrow are gone from Chapter 20 on. So C3 (lift, survive, descend, agree) is no longer checked for any reused sign. *Judgement: the free-form sections in Building 1 ("a move system acts, the blur forgets the moves, kept questions, a normal form shows they are all") are a good new template and should be named. Losing the Arrow slot in Building 0 is a real loss: it was the anti-label rule.*

**D4. Classical names became primary names.** Early chapters name after the blur, in bag words, and keep old names in Remarks. Later chapters define with classical names in D lines or as headings: H(U) "holomorphic" (ch31 D4), 𝒪_a, "meromorphic germs", "pole", "principal part" (ch34), "elliptic" (ch37 P3), ℘, Pic(C) (B1 III.1 B1), Gal(L/K) (B1 II.13 D1), n_p, Z(G), "solvable" (B1 II.14 D1). *Judgement: medium-priority drift against "bags over labels". Easy to reverse. Name the bag in plain words first, and put the classical symbol in Remarks.*

**D5. "Survives" became a badge.** Early, "Survives" is the L2/L3 claim that a blur respects an operation or keeps a question. Later it labels any theorem with a hypothesis: "Survives on C¹: inverting" (ch25 T3), "Survives: Q positive" (ch24 T2), "Survives: the arrow respects the moves" (B1 III.2 T2). Some of these are true kept-question claims (ch23 T1 really is a question kept on a rung bag). Others are ordinary theorems. *Judgement: keep the word for L2/L3 claims only, naming the blur and the question. Otherwise write "Theorem".*

**D6. Rules were stretched without being changed.** Rule S2 allows only finitary operations, and L7 asks every Blur line to name its O. Yet:
- ch26 puts "limit point by point of a sequence" in O, an infinitary operation;
- ch33 puts f ↦ f′ in O;
- ch35's O is "the dot with a fixed a, read as *is it 0?*", which is a question, not an operation;
- B1 II.4, II.8, II.9 say "O: none beyond the moves";
- B2 Ch5's blur ("forget the order and brackets, keep the bag of atoms") is on no stated floor and names no O.

*Judgement: analysis genuinely needs "respects limits". Add it as a rule (change R4) rather than smuggling it into O.*

**D7. "Glued" started to mean "near".** III.2 T1 is titled "Averages are glued to ½ in the mean square", and similar wording appears in Part III. Chapter 5's central theorem (T1) is that **no blur can stand for near**. *Judgement: small but philosophically important. Fix the wording ("come near ½ in S").*

## 4. "Reported, not proved": the count, and which are hidden imports

About 40 distinct steps are flagged reported, classical, deferred or not proved. Chapters 1 to 18 have almost none. I sorted every one by a single test: **does a later line depend on it?**

### A. Load-bearing and not earned: hidden imports (12)

| # | Where | Step | What depends on it | Note |
|---|---|---|---|---|
| 1 | B1 III.1 T2 | "a function on C with no affine pole is a polynomial function" (classical, deferred) | the at-most-one of the group law; III.1 T3; all of III.3 | The chapter's one hard line rests on it. |
| 2 | B0 ch32 G4 | Stokes and closed⇒exact for C¹ coefficients ("to be checked") | Cauchy (T2), deforming loops (T3), Cauchy's formula (T5), so ch33–37 | **Circular payment**: ch33 T2 says "this pays ch32 G4", but ch33 T1 uses ch32 T5, which needs G4. Must be earned directly. |
| 3 | B0 ch33 T2 | term-by-term differentiation over ℂ: "its proof runs the same" as ch20 T4 | smoothness; ch33 T3; ch34 | Short to earn, but at present asserted. |
| 4 | B0 ch37 T2, T4 | residue theorem on a parallelogram ("ch34 T3, run with that edge in place of a circle") | T3 (no single simple pole), T4, T8; B1 III.2 | ch34 T3 is proved only for circles. |
| 5 | B0 ch35 G3 | "det = 0 exactly when the lists are dependent, over every field, by Z7" | T1, T3 (three on a line); ch36; B1 III.1 | **Rule misuse**: "exactly when" is not an equation, so Z7 does not carry it (Z8). Part II's II.5 cannot be cited from floor one (F7). |
| 6 | B0 ch27 T3 | bags of L¹ are maps up to null sets (classical, deferred) | T4 (pays ch26 B2); ch28 G3; ch30 G3/P3; III.2 | Probably earnable from T2 plus one estimate. |
| 7 | B1 III.3 T2 | at most ℓ² points with ℓP = O over ℤ/p (classical) | "at most two clocks" | |
| 8 | B1 III.3 T3 | Hasse bound: two classical inputs reported (rationality with the mirror, and a rough bound) | headline of the chapter; B2 Ch4 P3 | Memory says the Hasse bound is "no longer an import". The book disagrees, so one of them needs updating. |
| 9 | B2 Ch1 T5 | incompleteness (reported) | B2 Ch2 G1 | |
| 10 | B2 Ch2 G1–G3 | Hilbert–Bernays–Löb conditions, Löb's theorem, Solovay's depth reading | **the whole chapter** | Breaks C1: Given lines must cite an earlier proof. |
| 11 | B2 Ch3 T1 | three verdicts reported (Tate, class field theory, Connes) | stated as a Theorem | Should be a Remark. |
| 12 | B2 Ch4 P3, T3 | the Weil route's two inputs; Li's ladder | the Amplify examples | Honest in text, but presented as propositions. |

Smaller gaps of the same kind: ch33 T4 uses "in one piece" without defining it; ch29 T1's "rationals first, then continuity" skips the lifting step.

### B. Deferred, within the method's reach (not imports)

ch9 T5 (clocks inside the circle); ch27 T5.1 and T5.2 (dominated and monotone convergence, used nowhere); II.5 P12 (Cayley–Hamilton, an equation, so Z7 plus the polynomial identity over ℤ would do it without the density argument); II.6 T1 (the middle step of Jordan–von Neumann); ch29 R2 (Weierstrass now earnable from Fejér).

### C. Remarks only (honest pointers, no line depends on them)

Ostrowski (ch19 R4), Weierstrass (ch20 R4, II.4 T4), Borel (ch21 R1), Cantor set uncountable (ch26 R2), Jordan–von Neumann (ch28 T5), du Bois-Reymond (ch29 R3), Goursat (ch31 R2, avoided by the Select), orders on k(x) (ch34 R2), zero count on the cubic (ch36 R3), uniformisation (ch37 R4, B1 III.2 R2), the word problem (B1 Ch2 T4), Hasse–Minkowski, Mordell–Weil, the converse of Galois, Carlitz, Beurling, Redheffer, Weil positivity. These are fine as they stand.

## 5. What the later chapters do better (keep)

- **"Where existence came from."** A one-line remark stating the single source of existence (closed, a Build, a count). It is the rule of thumb "blur proves at most one and kept; existence from Build or completeness", made visible. Retrofit it to ch1–21.
- **Reasons in parentheses.** Most later lines carry a one-line reason. That serves the deferred-proof plan better than bare statements.
- **Twin tables.** v_p / ord_a / provability rung; ℤ_p / jets / germs (ch33 R1, ch34 R1, B2 Ch2 T3). This is the method's real power as a survey tool.
- **Genuine new blur readings**, which are the best evidence the method scales:
  - Cauchy–Riemann as "the tangent commutes with J" (ch31 T1);
  - rigidity as "the germ blur glues nothing" (ch33);
  - ch26's B2, postponed and paid by an integral in ch27 T4;
  - Fejér's average as a positive blur that removes the Weierstrass import (ch29);
  - the Galois correspondence as an Appears line (B1 II.13 T3);
  - the matrix-moves template (B1 II.4, II.8–II.10);
  - associativity of the cubic's law for free, from a blur of a free group (B1 III.1 P1);
  - completeness as Appears and incompleteness as Appears failing (B2 Ch1 T3, T5).

## 6. Suggested changes

### Structural, and necessary

**S1. Name the chapter kinds in Chapter 0.** Replace "A chapter makes one new floor" with a short list of kinds, each with its own slots:
- Blur (the present table);
- Build-only (C5, exists);
- Select (pin by tests, at most one, build once; ch12, ch15, ch22, ch25, ch31 D4, ch37 T5);
- Arrow (read one arrow: what it respects, its W4 blur, inside or picture; ch30, ch32);
- Count (existence from a count, said openly; B1 II.6, II.12, II.15, III.3);
- Table (F2–F4);
- Rerun (Z7 and Z8 sorting; II.5, B1 II.7).

The verbs line must then match the kind. *Why necessary:* about 20 chapters already are these kinds, and half of them claim a blur they do not have. Without S1 the only choices are fake blurs or broken rules.

**S2. Move Z11 (Amplify) out of Chapter 0.** Chapter 0 says it is "the only place the method is stated" and that its theorems are "about blurs". Z11 is a theorem about power sums, and its proof uses convergence of power series and poles (Chapters 20, 33, 34). By the spirit of F7, Chapter 0 cannot rely on Chapter 34. Put Z11 as a chapter after ch34 (or keep it as B2 Ch4). Keep in Chapter 0 only the one-way growth blur, which is already ch17's. F8 (Loop) can stay: it is a reading convention and needs no later chapter.

**S3. Building 2, Part II becomes "Field notes: the edge"**, an appendix or a separate document, not a book part. Its four chapters make no floor. Three have no Blur line, Atoms' blur is not a blur under L1–L7, and they carry about 15 reported or classical steps in 9 pages. They are the project's research log written in book format, and they read as theorems when they are findings. Building 2 keeps Part I (Proofs; Equally provable). Chapter 2 is either rebuilt with G1–G3 earned or relabelled "a reading of three reported results". Optionally, if Building 2 becomes too thin, move its Part I into Building 0 as a Part IV, "Words about words".

### Recommended (cheap, mostly mechanical)

**R1. Pay the 12 hidden imports** (§4 A) or move each into its chapter's Given as an explicit "Imported" line, so the ledger is honest. Priority order: #2 (break the ch32/ch33 circle), #5 (a rule misuse), #1 (the group law's hard line), #6, #4, #3. Then #10 (Building 2, Chapter 2).

**R2. An import ledger at the front of each building.** One table: the line, what it imports, whether it is load-bearing, and the plan to earn it. Update memory's "only three imports remain".

**R3. Restore Notation and Arrow in Building 0, ch20–37.** At minimum, one Arrow line per chapter with C3 for each reused sign. This is the cheapest single repair of D3 and D4.

**R4. Add a rule for limits.** For example: "L10. A blur may be asked to respect limits for a stated nearness (Chapter 5, D4); the chapter must say which." Then remove infinitary operations from O lists (ch26, ch33), and replace ch35's O by its honest form (no O; the blur is on a bag with questions only).

**R5. Fix empty and circular Appears lines.** ch23, ch24, ch26 (until ch27), ch11, ch13, ch21: write "B1: none (made from above)" and do not claim Appears. ch24 B2: replace "the bag of f × h" with real questions (value, covector, quadratic part).

**R6. Reserve "Survives" and "glued"** for their rule meanings (D5, D7). Fix III.2 T1's title, and re-label badge-Survives as Theorem.

**R7. Names back to Remarks** (D4): introduce the bag in plain words, and put the classical symbol (Pic, Gal, H(U), 𝒪_a, ℘, n_p) in Old names.

**R8. Refresh the Part I map page.** "The fork" paragraph stops at ch25, while Part I now runs to ch37. Without renumbering, add sub-part headings: Numbers (1–9, 17–19), Maps (10–16, 20–25), In the mean (26–30), Complex (31–34), Curves (35–37). The single 37-chapter "first floor: numbers" no longer says what it holds.

### Optional

**O1. One proof convention.** Adopt the later convention (a one-line reason in parentheses on every Survives, Dies, Appears and Theorem line) and backfill ch1–21 when proofs are written.

**O2. Retrofit "where existence came from"** to ch1–21. In most early chapters the answer is "M5: bags exist", which is itself worth saying.

### Considered and decided against

- **Rewriting the late chapters so that each one blurs.** Not needed. Where the honest content is a count, an estimate or an arrow, a forced blur would be worse than S1's honest kind.
- **Renumbering or merging the buildings.** The three-building shape (blur, moves, loops) is sound. Only Building 2, Part II is misfiled.
- **Removing the inline proofs** to restore the early "statements only" look. They are an improvement (O1).

---

## Appendix: chapter by chapter

**Engine**: the blur lines produce the chapter's main result. **Lens**: the blur reorganises a classical argument, and the content comes from estimates, counts or classical proofs. **Label**: blur words attached; the chapter would read the same without them. (*) means skimmed rather than read line by line.

**Building 0, Part I.**
- Engine: 1–5, 6 (build-only), 7–10*, 11, 12*, 13–19*, 20, 21, 22 (Select, with the law from "only one"), 26, 27, 31, 33, 35.
- Lens: 23 (vacuous Appears, good Survives pairing), 24 (circular B2), 25 (no blur; a Select rescues a Survives line), 28 (right angles keep cancellation), 29 (survey plus positive blur), 32, 34, 36, 37.
- Label: 30 (Parseval as an arrow; no blur work).

**Building 0, Part II.** Engine: II.1, II.2*, II.3*. Lens: II.4*, II.6. Label: II.5 (a rerun, but honest; S1's "rerun" kind would make it Engine).

**Building 0, Part III.** Engine: III.1. Lens: III.3*, III.4*. Label: III.2 (no blur despite its verbs line).

**Building 1.**
- Engine: 1, 2, II.1*, II.2*, II.3, II.4, II.5*, II.8, II.9, II.10, II.13, III.1 (but see import #1).
- Lens: II.6 (says so), II.7*, II.11*, II.12*, II.14, II.15, III.2.
- Label: III.3.

**Building 2.** Engine: Ch1. Lens: Ch2 (on three imported Givens), Ch4. Label: Ch3, Ch5, Ch6.

Tally: Engine 44, Lens 22, Label 7 (73 chapters). Every Label chapter, and all but two Lens chapters, sit after Chapter 21 or in the newer parts.
