# What must be made to create genuinely new technology, and why (25 Nov 2026)

E (22:18 25 Nov): "examine what must be made to create genuinely new technology, and why".

Analysis only. The histories are **from memory**, as told in the literature, and they are **survivor stories**: retold after the fact, so they look inevitable. Read the pattern below as a hypothesis. Section 4 checks it against technologies that failed.

## 1. Twelve births (from memory)

| technology | the wall that made it necessary | what existed first, in embryo | what was changed | the small lemma that made it usable |
|---|---|---|---|---|
| interlacing families (Marcus–Spielman–Srivastava 2013) | matrix Chernoff and union bounds lose log n, and Kadison–Singer allows no log | Batson–Spielman–Srivastava sparsifiers (2009): barrier functions on characteristic polynomials; Godsil–Heilmann–Lieb (1972): matching polynomials are real-rooted; Borcea–Brändén real stable polynomials | average **characteristic polynomials**, not matrices | if every average in a tree is real-rooted, some leaf has its largest root ≤ that of the average |
| absorption (Rödl–Ruciński–Szemerédi 2006; Keevash 2014) | the Rödl nibble covers almost everything, and the leftover o(n) can't be fixed | the nibble (1985); hand-made gadgets in matching proofs; algebraic designs (Keevash's template) | build the repair **before** the random part | an absorber can swallow any small leftover |
| Stickelberger + Thaine in Catalan (Mihăilescu 2002) | Baker bounds plus Cassels left a finite but huge search | Stickelberger (1890); Thaine (1988), itself built from Kolyvagin's Euler systems for another wall (BSD) | annihilate class groups with explicit group-ring elements | Thaine's theorem: cyclotomic units annihilate the plus part |
| étale cohomology (Grothendieck, 1960s) | Weil asked for a cohomology in characteristic p; Zariski cohomology of constant sheaves vanishes | sheaf cohomology (Leray, Serre's FAC); Weil's own request | **what counts as an open set**: maps instead of subsets | proper and smooth base change; the Lefschetz trace formula |
| forcing (Cohen 1963) | Gödel's L gives consistency of CH, but nothing adds a new real | countable transitive models; Gödel's L | add a **generic** object, defined by what it avoids | the forcing theorem: truth equals being forced |
| Gowers norms (1998) | Fourier analysis is blind to 4-term progressions | Roth's Fourier argument; Cauchy–Schwarz chains | measure correlation with quadratic phases, not linear | the generalised von Neumann inequality |
| Ricci flow with surgery (Hamilton 1982, Perelman 2002) | the flow forms singularities | Hamilton's flow and his maximum principles | classify singularities via an entropy | Perelman's monotone entropy; κ-noncollapsing |
| perfectoid spaces (Scholze 2012) | weight-monodromy needed char 0 ↔ char p transfer | Fontaine–Wintenberger (1979): one isomorphism of Galois groups | turn one field-level fact into a **geometry** (tilting) | almost purity |
| Taylor–Wiles patching (1995) | the Euler-system approach (Flach) had a gap | Hecke algebras at auxiliary levels | take a limit over growing sets of auxiliary primes | numerical criterion: dimension of tangent space = number of primes |
| distributions (Schwartz 1945) | δ and weak solutions had no home | Sobolev's generalised functions; Heaviside | the object is **what it does to test functions** | duality: every operation transposes |
| probabilistic method (Erdős 1947) | explicit Ramsey constructions were far too weak | counting arguments (Szele) | count the bad cases instead of building a good one | the union bound |
| regularity lemma (Szemerédi 1975) | density versions need a structure-versus-randomness split | his own earlier k = 4 proof | partition into pieces that look random | energy increment (bounded, so it stops) |

## 2. The pattern: four things are made, always in this order

1. **A wall measured as a property P that every existing tool has.** Examples: "loses log n", "leaves o(n)", "blind to quadratic phases", "Zariski-open sets are too big". The wall is not "the problem is hard". It is a *statement about all tools of a type*, often provable as a barrier.
2. **An embryo in a smaller problem, years earlier.** In 11 of 12 cases the key piece had already been built and debugged on a low-stakes problem: sparsifiers, the nibble, Fontaine–Wintenberger, Hamilton's flow, Roth's 3-AP. Typical gap: 5 to 20 years. The new technology is usually a promotion, not a birth.
3. **A change of the basic object, not a new estimate.** In each case the thing being averaged, opened, counted or compared was redefined so that P no longer holds. In our language, **a change of blur**: a new choice of what counts as the same (characteristic polynomials up to their roots; spaces up to étale maps; functions up to what they do to test functions). Our 11 Nov note already said "repair = change floor".
4. **One short lemma that makes the new object composable**, almost always a property that is **kept** under the operations of the proof: real-rootedness kept under averaging, entropy monotone under the flow, absorbers kept under small changes, energy that only goes up. In blur terms this is a Survives line. The new object is worthless until one quantity is shown to survive.

**Why the generators miss this (GP-1).** The generators recombine objects that already exist. A wall stated as "property P of all tools of type T" is inherited by every recombination of tools of type T. Only an object of a new type escapes. And a new type cannot be judged in advance, because the space of possible types has no bound. So it is chosen by the wall (it must break P) and judged by a small win (the embryo problem).

## 3. Can we do it on purpose? Procedure NT-1

1. **State the wall as P.** Write it as a theorem: "every argument of type T loses X". For Lehmer we already have it: every size tool loses about log d at the circle conjugates (DIG-G5, BEST-COURSE §2).
2. **Find the proving ground**: the smallest problem with the same P and low stakes, where one new theorem would prove the new object works. For Lehmer: the bounded-factor parity theorem (s = 2 already proved).
3. **Change the blur.** List what the failing tools compare, average or count. For each one, propose a new notion of sameness under which P fails. This is the step our method is built for, and the one we have used to *sort* results rather than to *build*.
4. **Find the Survives line.** Ask which quantity the new object keeps under the operations the proof needs. No Survives line means no technology: drop the candidate.
5. **Win small, then promote.** Prove one new theorem on the proving ground before scaling up.
6. **Import its library.** The new object usually already has a theory somewhere (real stable polynomials, field-of-norms theory). Search for it once the object is defined.

## 4. The check against failures (the control the survivor stories lack)

Technologies that have not delivered their target, as far as I know (mid-2026): the field with one element (aimed at RH), Hilbert–Pólya operator programmes, de Branges spaces for RH, and inter-universal Teichmüller theory (whose proof of abc is disputed).
- **All of them have steps 1 and 3.** They measured a wall and changed the basic object.
- **Most lack step 2:** no early proving-ground theorem that the old tools could not prove. They also lack step 4: no kept quantity that delivers new inequalities.
- So the separating features are **the small early win and the Survives line**, not the bold new object. That is the honest lesson, and it is the reverse of the romantic story: novelty of the object is cheap; a kept quantity plus one small new theorem is what is rare.

Caveat: this control is four cases, judged by me, and "has not delivered *yet*" is not failure.

## 5. Forward predictions (committed with this file)

The rule says a technology succeeds when it has an early proving-ground theorem and a Survives line. Prediction for 25 Nov 2026 to 25 Nov 2031:
- **Prismatic cohomology** (Bhatt–Scholze) and **condensed mathematics** (Clausen–Scholze): both have early wins. Prediction: each is used in at least one new major theorem by others.
- **The field with one element** and **IUT**: neither has a proving-ground theorem accepted by the field. Prediction: no accepted decisive result unless a small win appears first. If one does, the prediction is re-registered, not scored.
- **Our own case:** the Lehmer parity route has steps 1 and 2. It is missing step 4, a quantity kept along the interlacing pairs. Prediction: it stalls exactly there unless a Survives line is found. That would be the place to put effort.
