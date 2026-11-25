# Pre-registration GP-1: the generator procedure for decisive objects (frozen 25 Nov 2026, before scoring)

E (22:14 25 Nov): "how would we have found those decisive objects? are there other methods?"

The Dial rule (PREREG-v2.md) says *what kind* of object wins: one whose supply grows with a parameter the prover chooses. GP-1 says *how to produce candidates*. It is seven written questions. Each one turns the target into candidate (object, dial) pairs. The Dial rule's D3 test (supply against cost) then prunes them.

## The seven generators

| # | generator | the question to write down | produces |
|---|---|---|---|
| G1 | **Count and vanish** (auxiliary object) | What is the cheapest object (polynomial, function, section) that must vanish on or fit the set? Compare the dimension of objects of size k with the number of conditions, then ask what limits how much a nonzero object of size k can vanish (degree, Bezout, Schwartz–Zippel). | Thue–Siegel, Stepanov, Dvir, polynomial partitioning |
| G2 | **Integer and small** | Which quantities attached to the objects are integers (determinants, resultants, norms, Hankel determinants)? Can one of growing size be made analytically smaller than 1? Then it is 0. | Liouville, Pólya–Bertrandias, Dimitrov |
| G3 | **Tensorise** (amplify) | Does the measured quantity multiply or add under some product, power or lift (tensor power, Sym^k, theta lift, k variables, k copies), while the loss stays fixed? Then run k → ∞. | Deligne's squaring, Maynard, theta ladder, Gilmer-type entropy |
| G4 | **Rank encoding** | Encode the forbidden pattern as a matrix or tensor. Is its rank (or slice rank, or an eigenvalue) small, while the set forces it to be large? | Croot–Lev–Pach, slice rank, Huang |
| G5 | **Potential with growing increment** | Is there a bounded quantity that each step raises? Does the raise grow (not stay fixed) as the step size grows? | energy and density increments, Taylor–Wiles patching, compression |
| G6 | **Dual certificate** | Write the bound as an optimisation problem. The decisive object is the dual witness: compute it numerically at small sizes, then guess its exact form from its zeros and symmetries. | Delsarte LP, Cohn–Elkies, flag algebras |
| G7 | **Home move** | Is there a space (variety, group, field) whose point counts, cohomology or class group *is* the quantity? Move the problem there. | Kuga–Sato, Parshin's trick, cyclotomic fields |

**Procedure.** Run all seven, keep what passes D3, rank, and output the top 3. The procedure is meant to be area-free: it does not ask what the neighbouring field uses. **Claim under test:** GP-1 beats the null ("three most-used tools next door") on first transplants, where the decisive object came from another area.

## Held-out backtest (episodes never used for v1, v2 or GP-1)

H1 sphere packing in dim 8 (Viazovska 2016) · H2 Kadison–Singer (Marcus–Spielman–Srivastava 2013) · H3 Erdős distinct distances (Guth–Katz 2010) · H4 primes in arithmetic progressions (Green–Tao 2004) · H5 Polynomial Freiman–Ruzsa over F_2 (Gowers–Green–Manners–Tao 2023) · H6 Catalan (Mihăilescu 2002) · H7 3-AP bounds (Kelley–Meka 2023) · H8 existence of designs (Keevash 2014) · H9 Erdős discrepancy (Tao 2015) · H10 Mordell (Faltings 1983, the first proof).

GP-1 was derived from E1–E10, so it is in-sample there. These ten are held out from the derivation, **but still contaminated**, because I know their proofs. Scoring is the same as v1: hit, partial, false lead, or miss, each against the null.
