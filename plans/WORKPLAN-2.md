# Work plan 2: analysis onward, and the road to complex analysis

Written 11 Nov 2026 (evening) in the thread "Build the textbook work plan", after WORKPLAN.md Tasks 1–6 were finished.
E's decisions (19:43, 11 Nov): finish the import clean-up, then continue with analysis; proofs are done all together later, not now; plan the path; say how the book reaches complex analysis.

Read first: `WORKPLAN.md` sections 0, 2, 3 (what the book is, the hard rules, the test "is the blur doing the work"). They still hold, with two changes:

- There IS a LaTeX compiler now. `python3 build.py` builds `book-single.pdf` and reports errors and lines more than 10pt too wide. A chapter is not finished until this is clean. (In a new container: `apt-get install -y --no-install-recommends texlive-latex-base texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended`.)
- New heading convention: a theorem that is not a blur line says so in its heading ("Imported", or "From Chapter n, Tk"). Prefer to turn it into a Survives line, a Dies line, an "at most one", or a "closed" line.

State of the book: Part I Chapters 1–22, Part II Chapters II.1–II.4, 97 pages. New chapters are appended; never renumber.

Who does what: every task below is a **sketch, not a finished design**. Each needs a full design (Fable), shown to E and agreed, before it is built. Building from an agreed design, scripts and map pages can be done on Opus. Any change to Chapter 0 is E's decision.

Rule of thumb found on 11 Nov, to use in every design: **the blur proves "at most one" and "this is kept"; it never proves "at least one".** Existence comes from only three places: Build, "closed" (completeness, Chapter 4/5 G3), and the one construction behind a Select chapter. So design each chapter to need existence once, and get everything else from "only one" and from Survives lines.

---

## Step A. Finish the import clean-up (small)

### A1. Chapter 23: ℂ is closed (the fundamental theorem of algebra) — DONE 11 Nov (ch23-c-is-closed.tex, design in ch23-design.md)

Line: `polynomials over ℂ → roots · from: Chapters 7, 10, 13, 21 · survives, dies`.
Same shape as the mean value theorem (Chapter 11, T6): a lowest point exists because something survives; a local line says a lowest point cannot be anywhere but at a root.

- Add to Chapter 13 one line: "closed boxes survive": a continuous map on a closed box of ℝⁿ takes a lowest and a highest value (Chapter 5, G3, halving place by place). Chapter 10, T2 is the case n = 1.
- (Far away is large.) For p of degree ≥ 1, |p(z)| > |p(0)| outside some disc. So |p| has a lowest point on ℂ.
- (Dies: "lowest point" where p ≠ 0.) Around a, p(a + h) = p(a) + c hᵏ + higher powers, exactly (Chapter 7 normal form re-centred; no limit). Choose h with c hᵏ pointing against p(a): needs k-th roots in ℂ, from Chapter 8, T2 (n·y = a has n solutions in the circle) through the wrapping of Chapter 10, T7. Then |p(a + h)| < |p(a)| for small h.
- Theorem: the lowest point is a root. Then Chapter 10, T11 loses its "classical, long" note and cites this chapter.
- Check script: for random complex polynomials, the descent direction of the third bullet lowers |p|; k-th roots by the wrapping.

### A2. Stay imported (reported in Remarks only)
Weierstrass (Chapter 20, R4), Borel (Chapter 21, R1), Ostrowski (Chapter 19, R4). Nothing later relies on them, except B5 below, which needs the circle form of Weierstrass and says so.

---

## Step B. Analysis

Order: B1, B2, B3, B4, B5, B6. B1 is independent of the rest. B2–B4 are the measure block and must come in order. B5 needs only Chapter 20; B6 needs B4 and B5.

### B1. Chapter 24: Highest and lowest points; inverting a map
**Split on 11 Nov:** Chapter 24 is highest and lowest points only (design: `ch24-design.md`). Contraction and inverting a map become Chapter 25, and every chapter number below moves up by one (null sets 26, integrable maps 27, L² 28, Fourier 29 and 30). Caution for the Chapter 25 design: "has an inverse nearby" is NOT kept by the tangent blur at one point (x + 2x² sin(1/x) has slope 1 at 0 and is not one-to-one near 0); it needs the tangent at every nearby point, changing continuously.
Closes the two calculus gaps noted in the 10 Nov review.

- (Rung 2 in several variables.) Chapter 21 run on ℝⁿ at rung 2: the straight bag holds value + covector + a quadratic part.
- A Survives/Dies pair, the twin of Chapter 11, T5: where the covector is 0 and the quadratic part is positive on every non-zero arrow, "a is a lowest point nearby" is kept by the rung-2 blur. It dies when the quadratic part is 0 somewhere: x⁴ and −x⁴ share a bag at rung 2 (and at rung 3).
- (Contraction, on floor one.) State the contraction line for ℝⁿ and for C[b,c] here, in Part I, so that Part I does not cite II.4 (rule F7). II.4, T5 then becomes "the same line for every complete row".
- (Inverting.) If the covector part of F : ℝⁿ → ℝⁿ at a is one-to-one, F is one-to-one near a and the inverse is differentiable: "having an inverse survives the tangent blur where the tangent has one". Proof route: contraction. Dies when the tangent has none: x ↦ x³ at 0 has an inverse but no differentiable one; x ↦ x² has none.
- Risk to check in design: exact hypotheses (C¹), and the witness lines.

### B2. Chapter 25: Null sets, and "almost everywhere" (a blur)
Line: `maps on a stretch → maps up to null sets · from: Chapters 4, 12, 20 · blur`.

- D: a set is null if for every rung k it can be covered by a sequence of stretches of total length < 10⁻ᵏ (M2: sequences).
- Survives lines about null sets: a part of a null set; a sequence of null sets together (the 10⁻ᵏ is shared out as 10⁻ᵏ/2ⁱ). A stretch of positive length is NOT null (needs closed stretches: Chapter 5, T7 style; this is the one real theorem and must be designed with care).
- Blur: f ∼ g iff f and g differ only on a null set. Respects +, ×, and h∘f for any map h. From above: which question? To settle in design; if none is honest, say "the gluings are the bag test".
- Dies: the value at any one point; "continuous" (χ of ℚ ∼ 0, the map of Chapter 12, R3). Survives: the integral, on C[b,c] (two continuous maps glued here are equal, so nothing is lost on C: say so).
- ℚ is null: the first place where "countable" matters. No choice rule is used.

### B3. Chapter 26: Integrable maps (the Lebesgue integral as a closing-up)
Line: `C[b,c] → integrable maps · from: Chapters 4, 12, 20, 25 · build, select, blur`.
E's standing preference "appear instead of build" decides the route: do not build measures first.

- A third nearness on C[b,c], next to M and point-by-point (Chapter 20): **mean nearness**, f I_k g iff ∫|f − g| < 10⁻ᵏ. Its bottom is equality on C[b,c]. M-near gives mean-near; not the reverse (the tents of Chapter 20, P9 scaled down).
- Run Chapter 4 with it: sequences in C[b,c] that come near themselves in the mean; glue when ∫|fₙ − gₙ| comes near 0. The bags are the integrable maps, L¹.
- Survives: +, scaling, and ∫ (it respects mean nearness with m = k: the cheapest Survives line in the book). So ∫ is defined on every bag for free.
- Closed (F5): running again adds nothing.
- The hard line, to design carefully or import openly: each bag is the bag of an actual map, up to the blur of Chapter 25 (a sub-sequence comes near point by point outside a null set). Without it the members are only bags of sequences.
- The table this chapter is for: three nearnesses × what survives a limit.
  - continuity: survives M; dies point by point and in the mean.
  - ∫: survives M and the mean; dies point by point (tents) **unless** the sequence stays below one integrable map: then it survives. That exception is dominated convergence; "only grows" is monotone convergence. Both are stated as Survives lines with their Dies witness beside them.
- Measure appears last: the measure of a set is ∫ of its 0/1 map, when that map is in a bag. Remark: sets with no measure need a rule of choice (Chapter 12, R3).
- Not in this chapter: abstract measure spaces, probability. Probability is a later reuse of the same chapter with "∫ 1 = 1".

### B4. Chapter 27: Square-integrable maps (function spaces)
Line: `C[b,c] → L² · from: Chapters 6, 26 · build, select, blur`. The twin of ℝⁿ (Chapter 6) with a stretch in place of {1,…,n}.

- ⟨f, g⟩ := ∫ f g, the twin of the dot product. (f·g)² ≤ (f·f)(g·g): prove it here once for both; this also pays the debt noted in Chapter 13, D1 (triangle law never proved in Chapter 6).
- Nearness from ∫|f − g|²; close up (Chapter 4 again): L². Survives: +, scaling, ⟨ , ⟩. Dies: ×, (a product of two members need not be a member: witness x^(−1/3) on 0 < x ≤ 1 squared twice).
- Blur of Chapter 6, road "perpendicular": projection onto a closed sub-bag = nearest point. Exists because L² is closed: an existence that comes from "closed", as the method wants.
- Part II follow-up, **II.5 Normed spaces** (the planned Modules, Arrows, One class, Machines move to II.6–II.9): rows ℝⁿ, C[b,c] with largest gap, L¹, L², ℓ²; tests norm, inner, complete; classes: normed, Banach, Hilbert. Table lines to find: which rows pass "inner" (parallelogram law as the test; C[b,c] fails with a witness).

### B5. Chapter 28: Fourier, first part (smooth maps on the circle)
Line: `maps on the circle → lists indexed by ℤ · from: Chapters 8, 10, 12, 20, 22 · survey, arrow`.

- Survey (the method's own tool): every continuous arrow 𝕋 → S respecting + is t ↦ w(nt) for exactly one n in ℤ. (Chapter 10, T10 is the cases n = ±1.) So the arrows are listed by ℤ.
- The arrow f ↦ (cₙ), cₙ := ∫₀¹ f(t) w(−nt). Respects +. Survives lines of this arrow: turning the circle by an angle becomes × by w(n·angle); the derivative becomes × by 2πi n. Dies: × becomes something else (convolution): the same loss as place-by-place × in Chapter 6.
- A third ladder: keep only |n| ≤ N. Pictures … → rung N + 1 → rung N, as Chapters 19 and 21.
- When the ladder comes back to f: if f has two continuous derivatives, |cₙ| ≲ 1/n² (Chapter 17) and the sums come near f in M (Chapter 20, T3). Needs "all cₙ = 0 gives f = 0": the circle form of Weierstrass, imported, and marked.
- Honest edge: for merely continuous f the sums can fail at a point (reported); at a jump they overshoot (Gibbs; check numerically).

### B6. Chapter 29: Fourier, second part (the two homes are one)
Line: `L²(𝕋) → ℓ²(ℤ) · from: Chapters 27, 28 · arrow`.

- ℓ²: sequences with Σ|cₙ|² settling; inner product place by place.
- Theorem, the twin of Chapter 10, T8: the arrow of B5 is one-to-one from L²(𝕋) onto ℓ²(ℤ) and keeps the inner product. In the mean, the ladder always comes back to f. So "continuity of f" was never the right Select; "square-integrable" is.
- Dies in this home: the value at a point (Chapter 25). Survives: energy Σ|cₙ|² = ∫|f|².

### Later, not designed here
Differential equations (Chapter 22's c-rule generalised: "at most one" by a kept question, "at least one" by contraction, B1); probability (B3 with ∫1 = 1); topology proper.

---

## Step C. The road to complex analysis

It does **not** depend on Step B. It needs Chapters 9, 13–16, 21, 22 and A1, all written or planned in Step A. So it can be started any time after A1. Four chapters. (The thread "Reach elliptic curves from the book" already noted: Cauchy is a Survives line of Stokes; Liouville is an "at most one". This section fits those in.)

### C1. The complex derivative (Select)
- Run Chapter 11 with ℂ in place of ℝ: flat, tangent classes, straight bags ↔ ℂ[ε].
- Compare with Chapter 13 for the same map seen as ℝ² → ℝ²: its straight bag holds a linear map L of ℝ². **Select** those whose L is "multiply by a complex number". That is the Cauchy–Riemann condition, and it is not a formula to memorise: it says L commutes with i.
- Link to Chapter 9: multiplying both arms of a corner by z is gluing (i) of Chapter 9, B1. So such a map **keeps angles** wherever its derivative is not 0: a Survives line.
- Definition to fix in design: holomorphic := complex derivative at every point, **continuous**. (Dropping "continuous" is a classical theorem, Goursat; report it, do not use it.)

### C2. Cauchy as a Survives line of Stokes
- f is holomorphic ⇔ the 1-form f dz is closed (Chapter 15). One line.
- So Chapter 16 applies as it stands: on a region with no holes f dz is exact and every loop integral is 0 (Cauchy's theorem = Chapter 16, T3/T4). Deforming a loop does not change the integral: the gluing of Chapter 16, T2.
- One hole: by Chapter 16, T5 every closed form on the punctured disc is glued to exactly one multiple of dz/(z − a). Name that multiple: the **residue**. It is a normal-form coordinate in H¹, not a computing trick.
- Cauchy's formula: f(z) dz/(z − a) is glued to f(a) dz/(z − a), because the difference has loop integrals that come near 0 on small circles. So the integral round a is 2πi f(a) times the number of turns (Chapter 16, T6).
- Avoids the Jordan curve theorem: loops are counted by turns, as Chapter 16 already does.

### C3. Rigidity
- Over ℂ the ladder of Chapter 21 **does** reach the germ: a holomorphic map equals the sum of its list near every point. Contrast Chapter 21, P8 (over ℝ it does not). So holomorphic maps are rigid, like polynomials in Chapter 10, T4.
- "At most one" lines: two holomorphic maps on a one-piece region with the same germ at one point are equal. A bounded holomorphic map on all of ℂ is constant (Liouville).
- "Highest point dies inside": |f| has no highest point strictly inside unless f is constant. This is the local step of A1 again; A1 then gets a second, two-line proof.

### C4. Poles and valuations
- ord_a(f): the first rung at which f is not glued to 0. ord(fg) = ord f + ord g; ord(f + g) ≥ the smaller. The twin of v_p (Chapters 18, 19), with (z − a) for p.
- Allow negative order: Laurent lists, the twin of ℚ_p. Chapter 19, R3 again.
- Residue theorem: C2's coordinate, read off the list as its coefficient of (z − a)⁻¹. Counting zeros by turns.
- Then the elliptic-curves road continues: ℂ/Λ (twin of Chapter 8) and ℘ selected (as exp in Chapter 22).

Imports on this road, to be marked: Goursat (avoided by the definition), Riemann mapping (not needed), Jordan curve (avoided).

---

## Suggested order overall
A1 → B1 → B2 → B3 → B4 (+ II.5) → B5 → B6, then C1–C4.
Alternative, if E wants complex analysis sooner: A1 → C1–C4 → B. Nothing in C uses B.

## After each chapter (unchanged from WORKPLAN.md rule 10, plus the compile)
Check script; `python3 build.py` clean (0 errors, nothing > 10pt wide); one row in the table of `ch0-map.tex` **and one arrow in its tree**; update "Planned" in `contents.tex`; three lines in project memory `textbook-build-log`; report to E in at most 120 words: what it blurs, what appears, what dies, what was machine-checked, what is imported.
