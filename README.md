# A square from two blocks of four consecutive integers

**And six refuted dossiers, two of which claimed to close open Erdős problems.**

Author: Jared Wilder. Published 2026-09-11.

Ten research dossiers were located in an internal mine and never read. This is what reading them
found. **Every number below was recomputed independently with exact integer arithmetic.**

---

## The new object

Two disjoint blocks of **four** consecutive integers whose combined product is a perfect square:

```
I1 = {33, 34, 35, 36}          I2 = {1680, 1681, 1682, 1683}

33 · 34 · 35 · 36                    =         1 413 720  =  2^3 · 3^3 · 5 · 7 · 11 · 17
1680 · 1681 · 1682 · 1683            = 7 994 422 608 480  =  2^5 · 3^3 · 5 · 7 · 11 · 17 · 29^2 · 41^2

product = 11 301 875 130 060 345 600 =  2^8 · 3^6 · 5^2 · 7^2 · 11^2 · 17^2 · 29^2 · 41^2

                                     =  3 361 826 160 ^ 2
```

Checked by exact integer square root: `isqrt(11301875130060345600)^2` returns the number itself.

### Why it works

`P1 * P2` is a square exactly when `P1` and `P2` lie in the **same square class**, meaning their
squarefree parts agree. Here both squarefree parts are

```
2 · 3 · 5 · 7 · 11 · 17 = 39270
```

`P2` carries the extra factor `29^2 · 41^2`, which is already a square and so does not move it out of
the class.

> A note on the invariant, because it is easy to get wrong: the **radical** (product of distinct
> primes) of `P1` is 39270 while the radical of `P2` is 46 692 030. Those differ. The right
> invariant is the **squarefree part** (product of primes with odd exponent), which is 39270 for
> both. Comparing radicals gives the wrong answer here.

### It is not one of many

Searched independently over all pairs of length-4 blocks with `a <= 120`, `b <= 6000`:
**exactly one** such pair exists, and it is this one. A wider sweep to `a <= 200`, `b <= 30 000`
finds no others, and **no length-5 analogue** appears in that range.

The smaller box was searched with the full perfect-power test (gcd of all prime exponents at least
2), so nothing of any exponent is missed there. The wider sweeps test for squares only.

### Scope, stated plainly

- **The dossier declared this box empty.** Its text reads: *"no k=4 witness found in exact sweep
  b <= 5000, a <= 60; genus-1 wall."* The witness sits inside that box.
- **"New" here means new relative to the dossier and to this estate. It has not been checked against
  the literature**, and a result of this shape may well be known. Anyone citing it should check
  first.
- The k=5 null result is a **search bound, not a theorem**.

### The known small companions, all re-verified

```
{1,2} u {8,9}        ->        144 = 12^2
{2,3} u {24,25}      ->       3600 = 60^2
{1,2,3} u {48,49,50} ->    705 600 = 840^2
```

and an infinite family `{1,2} u {c, c+1}` with `c = 8, 49, 288, 1681, 9800, ...` from the Pell
equation `(2c+1)^2 - 2s^2 = 1`, giving `144, 4900, 166464, 5654884, 192099600`. Correct and almost
certainly classical, since it is just `2c(c+1) = s^2`. The listed `c = 1` is degenerate: `I2 = I1`,
not disjoint, and that was unflagged.

---

## The same dossier "closes" the problem with a family that fails at its first case

The dossier states:

> *"Fix any k >= 2 and set I1 = [k, 2k-1], I2 = [4k, 5k-1]. Then the product of I2 equals the
> product of 4m over m in I1 ... Hence the product is a perfect square ... for **every** k >= 2 ...
> So no universal threshold k(r) exists ... any affirmative close is impossible for r >= 2."*

**It fails at k = 2.**

| k | I1 | I2 | product | factorisation | perfect power? |
|---|---|---|---|---|---|
| **2** | {2,3} | {8,9} | **432** | `2^4 · 3^3` | **no** (exponent gcd 1) |
| 3 | {3,4,5} | {12,13,14} | 131 040 | `2^5 · 3^2 · 5 · 7 · 13` | no |
| 4 | {4,5,6,7} | {16,..,19} | 78 140 160 | `2^8 · 3^3 · 5 · 7 · 17 · 19` | no |
| 5 | {5,..,9} | {20,..,24} | 77 119 257 600 | `2^10 · 3^5 · 5^2 · 7^2 · 11 · 23` | no |

The false step is that `4 * I1` is not `I2`. Multiplying a block of consecutive integers by 4 gives
spacing 4, not spacing 1:

```
k=2:   4 * {2,3}    = {8, 12}         vs   I2 = {8, 9}
k=3:   4 * {3,4,5}  = {12, 16, 20}    vs   I2 = {12, 13, 14}
```

**This exact error is identified and killed elsewhere in the same dossier**, in its own audit
section, and then reintroduced as a "fresh route" and used to declare an open problem closed.

---

## Five more refutations, each with an explicit witness

### `gcd(n!-1, m!-1) = 1` is false

The dossier proves *"every prime p dividing n!-1 satisfies p > n"* — which is true — and then
concludes that for `m > n`, `p` divides `m!`, so `gcd = 1`. **That needs `p <= m`, and it only has
`p > n`.**

```
4! - 1 = 23        8! - 1 = 40319 = 23 · 1753        gcd(23, 40319) = 23
```

Here `p = 23 > 8 = m`, so `8!` is not divisible by 23. Nine failures with `n, m <= 25`:

```
(4,8)=23  (4,11)=23  (4,21)=23  (5,11)=17  (5,15)=17
(8,11)=23 (8,21)=23  (11,15)=17 (11,21)=23
```

**The dossier's own check window is `{2,...,7}` — it stops one step short of the first failure.**

The correct statement is sitting in the same file: `gcd(m!-1, n!-1)` **divides**
`(n+1)(n+2)···m - 1`. That one is true, verified for all `2 <= n < m <= 21` with zero violations,
and it is the exact repair for the false claim.

A second item in the same dossier presents `S in (1.253498755679455, 1.253498755679566)` as a
rigorous enclosure. The true value is `1.2534987556999534716...`, which sits **2.04 x 10^-11 above
the claimed upper endpoint**.

### A graph lemma that is false for the only case the problem is about

The dossier argues: *"every subgraph of `K_m` is a complete graph, so chromatic number `m` forces the
subgraph to be `K_m` itself, which contains a triangle"*, and concludes the problem is *"settled:
FALSE for every r >= 3"*.

A subgraph is obtained by deleting vertices **and edges**, so the subgraphs of `K_m` are all graphs
on at most `m` vertices. `K_4` contains `C_4`, which is not complete.

The salvage *"H inside K_n with chromatic number n implies H = K_n"* is **true for finite n**
(verified exhaustively for n = 2, 3, 4) and **false for infinite m**, which is the only case in
question. Witness: the disjoint union of `K_1, K_2, K_3, ...` has chromatic number `aleph_0`, sits
inside `K_{aleph_0}`, and is not complete, or even connected.

And `K_{aleph_0}` is not a counterexample to the original statement at all: take graphs `G_k` with
chromatic number `k` and girth greater than `r` (Erdős 1959), and their disjoint union has infinite
chromatic number, no short odd cycle, and embeds in `K_{aleph_0}`. **That is the opposite of the
dossier's conclusion.**

The same file separately calls this very lemma *"FALSE"* in another block.

### Partition values off by an index

| the dossier says | the truth |
|---|---|
| `p(7) = 22` | `p(7) = 15 = 3 · 5`   (22 is `p(8)`) |
| `p(11) = 101` | `p(11) = 56 = 2^3 · 7`   (101 is `p(13)`) |

Consequences: the prime 11 enters at `k = 6` via `p(6) = 11`, not at `k = 7`; the claimed entry
points 7 and 11 are not entry points at all, since `p(7)` and `p(11)` are both smooth; and the
claimed strictly decreasing gap reaching `-50` is neither strictly decreasing nor reaching `-50`
(the minimum for `n <= 60` is `-18`).

### A coverage lemma that fails at its smallest instance

*"For every greedy sequence (any start n) and every k >= 1: the partial reciprocal sum is at least
`1 - (k+1)/(a_{k+1} - 1)`."*

Start `n = 4`, `k = 1`: the sequence begins `4, 5`, so the left side is `1/4 = 0.25` and the right
side is `1 - 2/4 = 0.5`. The proof's opening line, *"every m in `[1, a_{k+1}-1]` is a consecutive
sum"*, is false for any start `n >= 2`, because nothing below `n` is ever representable. It holds for
`n = 1` and is stated for *any* start.

### Right conclusion, wrong witness

A lemma *"v_0(n) >= 2 for every n >= 5"* is filed with *"counterexample on record: n = 15"*, justified
as *"15 = 3 · 5, so omega = 1"*. The line writes a two-prime factorisation and then calls it one
prime. `omega(15) = 2`, so 15 is not a counterexample.

The lemma **is** false, and the genuine witnesses at least 5 are `n = 7, 8, 16`. The dossier computes
`v_0(7) = 1` two lines away without noticing it has already killed its own lemma.

---

## What survives, and is worth having

**An `O(sqrt n)` finite reduction.** If `n+k` has two distinct prime factors both greater than `k`,
then `n+k >= (k+1)(k+2)`, so `k` is at most about `sqrt n`. That turns a per-`n` infinite question
into a bounded check. Verified exhaustively: for **all `n <= 3000`**, the reduced window and the full
range give identical answers, zero discrepancies. The associated census is
`{n <= 3000 : v_0(n) <= 1} = {2, 3, 4, 7, 8, 16}`.

**Five exact modular-covering certificates**, all verified periodic:

```
A = {1}    ->  gaps 2, 2, 2, ...        residues {1} mod 2
A = {2}    ->  gaps 1, 4 repeating      residues {2,3} mod 5
A = {3}    ->  gaps 1, 1, 6 repeating   residues {3,4,5} mod 8
```

**A forbidden-triple normalisation**: `{a,b,c}` is forbidden if and only if `a = dx, b = dy, c = dz`
with `x, y, z` pairwise coprime and distinct. Verified over **all triples in `[60]`** with zero
violations. Its companion values `f_3(1..8) = 1, 2, 2, 3, 3, 3, 3, 4` are correct, and one table in
the same file giving `1, 2, 2, 3, 4, 4, 4, 5` is wrong. Also worth noting: the `log_2` lower bound is
not tight, since `f_3(9) = 5` with extremizer `{2,3,4,8,9}` against a bound of 4.

---

## The four shapes these failures take

They are not random slips. Across ten dossiers they repeat:

1. **Sampled, then stated universally.** The `gcd = 1` claim is checked to `n, m <= 7`; the first
   failure is `(4, 8)`.
2. **An error the same file already caught, reintroduced later as a fresh route.** The `4 * I1`
   construction is killed in one section and used to close the problem in another. The graph lemma
   is called FALSE in one block and load-bearing in another.
3. **Right conclusion, wrong witness.** A lemma is genuinely false and the counterexample offered
   for it is not a counterexample.
4. **Mutually contradictory tables inside one file.** Three different sequences for the same set,
   three different value tables, two different values for the same constant.

The attack apparatus around these claims ran in full and caught none of the six refutations. In two
cases it ran *against* the truth: the correct kill was already on record, and a later route restated
the killed error as a closure.

## License

Apache-2.0.
