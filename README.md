# Erdős #930 — perfect powers from disjoint consecutive blocks

**Author:** Jared Wilder  
**First public timestamp:** 2026-09-11

This repository is the dedicated human and citation home for the released Erdős #930 results. Cross-problem audit material that briefly appeared here has been moved to `jaredwilder/erdos-counterexample-queue`.

## Problem

For every `r`, does there exist a `k` such that whenever `I_1,...,I_r` are pairwise-disjoint intervals of consecutive positive integers, all of length at least `k`, the total product

\[
\prod_{i=1}^r\prod_{m\in I_i}m
\]

is not a perfect power?

The results here concern the `r=2` lower-threshold side.

## A length-4 square-product pair

The two disjoint blocks

\[
I_1=\{33,34,35,36\},\qquad
I_2=\{1680,1681,1682,1683\}
\]

have products

\[
\prod I_1=1{,}413{,}720
=2^3 3^3 5\cdot7\cdot11\cdot17,
\]

and

\[
\prod I_2=7{,}994{,}422{,}608{,}480
=2^5 3^3 5\cdot7\cdot11\cdot17\cdot29^2\cdot41^2.
\]

Their squarefree parts are equal:

\[
2\cdot3\cdot5\cdot7\cdot11\cdot17=39270.
\]

Therefore

\[
\prod I_1\prod I_2
=11{,}301{,}875{,}130{,}060{,}345{,}600
=3{,}361{,}826{,}160^2.
\]

So any threshold that works for `r=2` must satisfy

\[
\boxed{k\ge5}.
\]

This strengthens the earlier released length-3 obstruction.

## Smaller exact examples

The release also contains

\[
\{1,2\}\cup\{8,9\}:\qquad 1\cdot2\cdot8\cdot9=144=12^2,
\]

\[
\{2,3\}\cup\{24,25\}:\qquad 2\cdot3\cdot24\cdot25=3600=60^2,
\]

and

\[
\{1,2,3\}\cup\{48,49,50\}:\qquad 705600=840^2.
\]

## Infinite Pell family at length 2

If

\[
(2c+1)^2-2s^2=1,
\]

then

\[
2c(c+1)=s^2.
\]

Hence, whenever the blocks are disjoint,

\[
\{1,2\},\qquad \{c,c+1\}
\]

have square combined product. The positive Pell solutions give infinitely many such examples; the first nondegenerate values of `c` are

`8, 49, 288, 1681, 9800, ...`.

A second equivalent-style Pell construction was recovered in the earlier archive using the fixed block `{2,3}` and the equation `x^2-24y^2=1`.

## Finite search record

`verify.py` independently recomputes the displayed length-4 witness and exhaustively searches all pairs of length-4 blocks with

- first start `a <= 120`,
- second start `b <= 6000`.

Within that box the pair `(a,b)=(33,1680)` is the unique square-product pair.

A wider historical search was also recorded in the source estate, but the canonical verifier in this repository deliberately states only the range it reproduces itself.

## Verification

```bash
python verify.py
```

The verifier uses only the Python standard library. It checks the exact factorisations, square root, equal squarefree parts, the smaller witnesses, the first Pell-family values, and the exhaustive length-4 search box above.

## Scope

The result `k>=5` is exact for the lower-threshold side of `r=2`. It does **not** establish that `k=5` works, nor does it settle the full `forall r exists k` problem.

Historical novelty of the length-4 pair has not yet been adjudicated by a dedicated literature search; correctness and novelty are recorded separately.

## Provenance

Earlier copies of the #930 material remain in `unpublished-math-papers/erdos930-perfect-power-intervals/` and in release-day forensic records. Those are provenance mirrors. This repository is the preferred subject home.
