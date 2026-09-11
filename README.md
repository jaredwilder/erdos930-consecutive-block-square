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

## Two infinite Pell families at length 3

Beyond the sporadic length-3 example, there are two infinite families, both driven by the same Pell
form `X^2 - 8y^2 = 9`.

**Family A** pairs `{a, a+1, a+2}` with `{2a, 2a+1, 2a+2}`. The combined product is
`4a^2 (a+1)^2 (a+2)(2a+1)`, so it is a square exactly when `(a+2)(2a+1)` is, that is when

`(4a+5)^2 - 8y^2 = 9`.

The first values of `a` are `73, 2521, 85681, 2910673, 98877241, 3358915561`, satisfying
`a(n+1) = 34 a(n) - a(n-1) + 40`. For instance

`{73,74,75}` with `{146,147,148}`:  `405150 * 3176376 = 1286908736400 = 1134420^2`.

**Family B** pairs `{a, a+1, a+2}` with `{2a+2, 2a+3, 2a+4}`. The combined product is
`4(a+1)^2 (a+2)^2 a(2a+3)`, a square exactly when `a(2a+3)` is, that is when

`(4a+3)^2 - 8y^2 = 9`.

The first values of `a` are `12, 432, 14700, 499392, 16964652, 576298800`, satisfying
`a(n+1) = 34 a(n) - a(n-1) + 24`. For instance

`{12,13,14}` with `{26,27,28}`:  `2184 * 19656 = 42928704 = 6552^2`.

A sweep of the shape `b = 2a + c` over `a <= 10^9` found no third family of that form.

## Three perfect cubes at length 2

The combined product can be a perfect power that is not a square. Three length-2 pairs give cubes,
and none of the three is a square:

```
{11,12}   with {242,243}    =         7 762 392 = 2^3 3^6 11^3           =    198^3
{32,33}   with {242,243}    =        62 099 136 = 2^6 3^6 11^3           =    396^3
{539,540} with {3024,3025}  = 2 662 500 456 000 = 2^6 3^6 5^3 7^3 11^3   = 13 860^3
```

Searches for other exponents — cube classes to `10^18`, fifth powers to `10^18`, and every prime
exponent up to 43 over starts below `3 x 10^4` — returned nothing further at any length.

## Two reductions, and what they buy

Both are elementary, and together they replace a bounded search with a complete one over a stated
class.

**Smooth-class reduction.** Suppose the common squarefree part is `Y`-smooth with `Y >= k`. Any prime
`p > Y` then exceeds `k`, so `p` divides at most one of `k` consecutive integers, and its valuation in
the product must already be even on that single term. Hence every term of both blocks lies in

`G(Y) = { n : the squarefree part of n is Y-smooth }`.

Since the common squarefree part divides the first block's product, its prime factors are all at most
`a + k - 1`. **So searching the class `Y = A + k - 1` is complete for every first start `a <= A`.**

**Pell reduction.** Consecutive members `n, n+1` of `G(Y)` satisfy `n(n+1) = D m^2` with `D`
squarefree and `Y`-smooth, which is

`(2n+1)^2 - D (2m)^2 = 1`.

So consecutive pairs inside `G(Y)` are exactly the odd-`x` solutions of classical Pell equations, one
ladder per admissible `D`, and a run of `k` consecutive members is `k-1` of them in sequence. As a
check on the reduction, `D = 105` has fundamental solution `(41,4)` giving `n = 20`, and its next
solution `(3361,328)` gives `n = 1680`, the second block of the length-4 pair above.

## What the reductions establish about longer blocks

Under these reductions the source estate reports **no length-5 pair** in any class it examined,
including the 17-smooth class — which covers every first start `a <= 13` — out to second starts below
`10^1000`, where the complete list of length-5 runs is the seventeen numbers
`{1, ..., 14, 24, 32, 48}`. Lengths 6, 7 and 8 were likewise empty in every box examined.

The single square-class collision at length 5 is `{4,...,8}` with `{5,...,9}`: both products have
squarefree part 105, since `4` and `9` are squares, and their product genuinely is a square — but the
blocks **overlap**, so it is not an instance. The same shape recurs at length 6 with `{2,...,7}` and
`{3,...,8}`.

On the same reductions, the length-4 pair appears isolated rather than the head of a family: the
complete list of length-4 runs in the 17-smooth class below `10^1000` has twenty-three members, and
`1680` is the largest of them.

**These longer-block statements are reported from the source estate's search, not reproduced by the
verifier here**, which continues to state only the box it recomputes itself.

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

The verifier uses only the Python standard library. It checks the exact factorisations, square root, equal squarefree parts, the smaller witnesses, the first Pell-family values, the exhaustive length-4 search box above, both length-3 families with their recurrences, and the three cubes.

## Scope

The result `k>=5` is exact for the lower-threshold side of `r=2`. It does **not** establish that `k=5` works, nor does it settle the full `forall r exists k` problem.

Historical novelty of the length-4 pair, the two length-3 families and the three cubes has not yet been adjudicated by a dedicated literature search; correctness and novelty are recorded separately.

## Provenance

Earlier copies of the #930 material remain in `unpublished-math-papers/erdos930-perfect-power-intervals/` and in release-day forensic records. Those are provenance mirrors. This repository is the preferred subject home.
