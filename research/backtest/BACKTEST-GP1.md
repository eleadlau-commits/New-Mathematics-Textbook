# How the decisive objects could have been found, and a backtest of GP-1 (25 Nov 2026)

Rule: PREREG-GP1.md, commit 066cffb (22:16 UTC), scored afterwards. All scores are contaminated by lookahead.

## 1. The four objects E asked about, each from one written question (in-sample)

| object | generator | the question, and how it lands |
|---|---|---|
| Dvir's polynomial (Kakeya over F_q) | G1 count and vanish | "What is the cheapest polynomial that vanishes on K?" Polynomials of degree q − 1 in n variables form a space bigger than \|K\| unless K is huge, so one vanishes on K. Restricted to any line in K it has degree < q but q zeros, so it vanishes on the line's direction, hence everywhere. The dial is the degree. |
| slice rank (cap sets) | G4 rank encoding | "Write the 3-AP-free condition as a tensor." For a cap set it is diagonal, with rank \|A\|. Write it as a polynomial in x + y + z and count monomials: its rank is at most 3·(number of low-degree monomials) ≈ 2.756ⁿ. The dial is the degree cut-off. |
| Dimitrov's Hankel determinant (Schinzel–Zassenhaus) | G2 integer and small | "Which numbers built from α are integers?" Coefficients of a power series attached to α and its conjugates (in Dimitrov's proof, built from α and its powers α², α⁴) are integers, and so are their Hankel determinants. If all conjugates are close to the unit circle, the series converges beyond the capacity bound, the determinants of growing size are < 1, hence 0, so the series is rational. That contradicts irreducibility. The dial is the determinant size. |
| theta lifts (RH, claimed) | G3 tensorise | "Which move adds one unit of vanishing order and keeps the character data?" Start from the smallest group and climb the rank ladder. The dial is the number of lifts, about √X. |

Each takes one question, plus one standard fact from another area. That is the point: the null ("tools next door") does not ask the question, because the answer lives elsewhere. Dvir's answer came from coding theory and number theory, slice rank from Croot–Lev–Pach, Dimitrov's from Pólya's rationality theorem.

## 2. Held-out backtest (H1–H10, never used for building the rules)

| # | episode | GP-1 output (top 3) | decisive object | GP-1 | null |
|---|---|---|---|---|---|
| H1 | sphere packing, dim 8 | G6: the Cohn–Elkies dual witness, whose zeros sit at the E8 norms √(2n), so build it from the E8 theta series and modular forms | magic function from (quasi)modular forms | **hit** | hit (Cohn–Elkies numerics were next door) |
| H2 | Kadison–Singer | G4 eigenvalue bound; G5 iteration; G6 dual (Bourgain–Tzafriri) | expected characteristic polynomials, interlacing families, real stable polynomials | **miss** | miss |
| H3 | distinct distances | G1 polynomial partitioning in degree D; G7 move to lines in ℝ³ (Elekes–Sharir) | exactly those two | **hit** | hit (the joints proof was next door) |
| H4 | Green–Tao | G5 energy increment; G6 duality (dense model); G7 move to a pseudorandom majorant | transference with a Goldston–Yıldırım majorant | **partial** | partial (Szemerédi, GY weights) |
| H5 | PFR over F_2 | G3 entropy over copies; G5 decrement of entropic distance | entropic Ruzsa distance decrement | **hit** | hit (Tao's entropy version was next door) |
| H6 | Catalan | G7 move to Q(ζ_p); G2 integer and small (Baker bounds) | Stickelberger annihilation of the class group, plus cyclotomic units | **partial** (home right, object missed) | partial |
| H7 | 3-AP bounds | G5 density increment with growing gain (sifting, almost periodicity) | that, plus spectral positivity | **hit** | partial (Bloom–Sisask was next door) |
| H8 | designs | G5 iteration (nibble) | randomised algebraic construction plus absorption | **miss** | miss |
| H9 | Erdős discrepancy | G3/G5 entropy decrement over scales; G7 move to multiplicative functions | entropy decrement plus Matomäki–Radziwiłł, after the Polymath reduction | **hit** | partial |
| H10 | Mordell (Faltings) | G7 Parshin's map to abelian varieties; G1 auxiliary polynomial (the Thue–Vojta line) | Faltings height, isogeny estimates, Tate conjecture via Parshin | **partial** (G1 names the later Vojta proof) | partial |

**GP-1: 5 hits, 3 partial, 2 misses. Null: 3 hits, 5 partial, 2 misses.**
- GP-1 beats the null only on H7 and H9, both by one notch, and both are judgement calls.
- On the three "first transplant" episodes it was built to win (H1, H2, H6), it is no better: H1 is a tie, H2 and H6 are misses for both.

## 3. Reading

- **The generators are roughly the canon of proof methods.** A strong mathematician carries most of them. GP-1 helps when the decisive object is a *known technique carried into a new place*: it finds Dvir, slice rank, Dimitrov and theta lifts in one question each. It does not help when the object is *new technology* (interlacing families, absorption, Stickelberger annihilation).
- **On held-out data the advantage over the null is small.** Transplants usually happen soon after a near miss next door (joints before distinct distances; Cohn–Elkies before Viazovska), so by the time of the proof the null already contains the tool.
- **The honest place for GP-1 is the forward test**, especially on problems with no recent near miss next door. That is where a transplant would be found by the question and not by the neighbourhood.

## 4. Other methods for finding decisive objects

- **Dual-certificate numerics (G6, made concrete).** Solve the small cases numerically, read off the witness's zeros and symmetries, then guess the exact object. This is how the sphere-packing magic function was located before anyone could write it down. It is the method most likely to find something new, and it costs computation rather than insight.
- **Interrogate the extremal example.** The decisive object must be tight, or nearly tight, on the extremizers (H4 in our habits). Ask what tight object the extremizer carries: for Lehmer's polynomial, resultants that are ±1.
- **Invert the barrier.** Each barrier (relativisation, Davenport–Heilbronn, Beurling) says what the object must *not* be. List the properties the fake models lack, and demand the object uses one.
- **Make the problem bigger** until a symmetry appears (H3 in our habits): GRH for all characters at once, Kakeya in all directions.
- **Ask who would solve it** (H9), then list their objects. This is a cheap proxy for cross-area reach.
- **Computer search for structure.** Enumerate small cases and look for an invariant (Huang's signing was found by hand, but the same kind of search can find it).

## 5. Forward additions (GP-1 rows, committed with this file)

F1 Lehmer is owned by the Lehmer thread's dial-object search, so no new rows here.

| # | problem | new GP-1 candidates beyond FORWARD-v2.md |
|---|---|---|
| F2 | sunflower | G6: an LP or flag-algebra dual certificate for spread families, computed at small k |
| F3 | union-closed | G6: the dual witness of the LP over weightings, at small universe size, then guess its exact form |
| F4 | unit distances | G7: the extremal configuration is a Gaussian-integer lattice, so move to norms in ℤ[i] and towers above it; G2: integer counts of representations by norms that must be small |
| F7 | ω = 2 | G6: the dual of the asymptotic-rank optimisation, found numerically |
