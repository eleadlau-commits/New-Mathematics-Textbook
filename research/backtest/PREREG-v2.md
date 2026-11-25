# Pre-registration v2: the Dial rule (frozen 25 Nov 2026)

Built from the failures in BACKTEST-v1.md, so it is **in-sample on E1–E10**. Only the forward test (FORWARD-v2.md) scores it.

## The rule

**D0. The reason.** A decisive step makes the supply of some unit scale with a parameter the prover chooses (a dial), and grow faster than the bill. Routes whose supply is fixed by the problem stall, however many rungs they use.

- **D1 Bill.** Name the unit the proof must collect, and how it grows: from an analogue proof, or from the loss that the best known bound pays (for example "log k per element").
- **D2 Dials.** List every free parameter that sets the size of an auxiliary object: the number of rungs or lifts, a polynomial degree, a determinant size, a tensor power, a number of variables or copies, a tower level, a set of auxiliary primes.
- **D3 Supply against cost.** For each dial, estimate supply(k) and cost(k). Keep a dial only if supply/cost grows without bound or beats the bill. **Reject fixed-gain ladders** outright: the gain per rung must grow, or the rung count must be free and costless.
- **D4 Two shapes.** A *ladder* (many objects, one unit each, a move between them that keeps the measured quantity), or *one big object* (dimension count: polynomials, determinants, ranks).
- **D5 Endgame.** A one-sided form that the units can feed.

**Output:** at most 3 (object, dial) pairs, ranked. **Silent** if no dial passes D3.

## Scoring (unchanged from v1)

- **Hit:** the decisive new object or move is in the top 3.
- Each forward problem also records a **null** written today: the three tools most used on it now.
- The rule earns credit only for hits the null misses.
