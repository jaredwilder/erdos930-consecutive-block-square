# Erdős #930 — perfect powers from disjoint consecutive blocks

For every `r`, does there exist `k` such that any `r` pairwise-disjoint intervals of consecutive positive integers, each of length at least `k`, have combined product that is not a perfect power?

This repository studies the `r=2` lower-threshold side.

## Length 4: `k` must be at least 5

The disjoint blocks

\[
I_1=\{33,34,35,36\},\qquad
I_2=\{1680,1681,1682,1683\}
\]

have equal squarefree product part

\[
2\cdot3\cdot5\cdot7\cdot11\cdot17=39270,
\]

and therefore

\[
\prod I_1\prod I_2
=11{,}301{,}875{,}130{,}060{,}345{,}600
=3{,}361{,}826{,}160^2.
\]

Hence any threshold valid for `r=2` must satisfy

\[
\boxed{k\ge5}.
\]

Smaller square-product examples include

```text
{1,2}     with {8,9}       -> 12^2
{2,3}     with {24,25}     -> 60^2
{1,2,3}   with {48,49,50}  -> 840^2
```

## Infinite Pell families

For length 2, solutions of

\[
(2c+1)^2-2s^2=1
\]

give `2c(c+1)=s²`, so `{1,2}` and `{c,c+1}` have square combined product. The first nondegenerate `c` values are

```text
8, 49, 288, 1681, 9800, ...
```

There are also two infinite length-3 families governed by `X²-8y²=9`:

- `{a,a+1,a+2}` paired with `{2a,2a+1,2a+2}`, beginning `a=73,2521,85681,...`;
- `{a,a+1,a+2}` paired with `{2a+2,2a+3,2a+4}`, beginning `a=12,432,14700,...`.

The corresponding recurrences and factorizations are checked by [`verify.py`](verify.py).

## Cubes at length 2

Three recorded block pairs have combined product a cube but not a square:

```text
{11,12}   with {242,243}    = 198^3
{32,33}   with {242,243}    = 396^3
{539,540} with {3024,3025}  = 13,860^3
```

## Search reductions

Two elementary reductions organize the longer-block search.

**Smooth squarefree reduction.** If the common squarefree part is `Y`-smooth with `Y>=k`, then every prime `p>Y` occurring in a block of length `k` must appear to even valuation in the single term it can divide. This restricts every term to

\[
G(Y)=\{n:\operatorname{sqfree}(n)\text{ is }Y\text{-smooth}\}.
\]

For first block start `a<=A`, taking `Y=A+k-1` makes this reduction complete for that first-start range.

**Pell reduction.** Consecutive members `n,n+1` of `G(Y)` satisfy

\[
n(n+1)=Dm^2,
\]

hence

\[
(2n+1)^2-D(2m)^2=1.
\]

Thus runs in `G(Y)` can be enumerated through finitely many Pell ladders.

The source search found no disjoint length-5 pair in the tested smooth classes, but that is search evidence rather than a proof that `k=5` works.

## Verification

```bash
python verify.py
```

The standard-library verifier checks the displayed factorizations, the Pell-family initial values and recurrences, the cube examples, and an exhaustive length-4 search with

```text
first start  a <= 120
second start b <= 6000.
```

Within that box, `(a,b)=(33,1680)` is the unique length-4 square-product pair.

The repository proves the lower-threshold obstruction `k>=5` for `r=2`; it does not prove that `k=5` suffices or settle the general `forall r exists k` problem.

Author: Jared Wilder.
