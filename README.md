# A square from two blocks of four consecutive integers

Author: Jared Wilder. First public timestamp: 2026-09-11.

## The result

Two disjoint blocks of four consecutive integers whose combined product is a perfect square:

```
I1 = {33, 34, 35, 36}          I2 = {1680, 1681, 1682, 1683}

33 · 34 · 35 · 36                    =         1 413 720  =  2^3 · 3^3 · 5 · 7 · 11 · 17
1680 · 1681 · 1682 · 1683            = 7 994 422 608 480  =  2^5 · 3^3 · 5 · 7 · 11 · 17 · 29^2 · 41^2

product = 11 301 875 130 060 345 600 =  2^8 · 3^6 · 5^2 · 7^2 · 11^2 · 17^2 · 29^2 · 41^2

                                     =  3 361 826 160 ^ 2
```

`P1 · P2` is a square exactly when `P1` and `P2` lie in the same square class, that is when their
squarefree parts agree. Both squarefree parts are

```
2 · 3 · 5 · 7 · 11 · 17 = 39270
```

`P2` carries the additional factor `29^2 · 41^2`, which is a square and so does not change its class.

The square class is the **squarefree part** (primes with odd exponent), not the radical. The radical
of `P1` is 39270 and the radical of `P2` is 46 692 030; those differ, and comparing them gives the
wrong answer for this pair.

## Search range

Over all pairs of length-4 blocks with `a <= 120` and `b <= 6000`, this is the only such pair. It is
still the only one over `a <= 200`, `b <= 30 000`. No length-5 pair exists in that range.

The `a <= 120`, `b <= 6000` sweep used the full perfect-power test (gcd of all prime exponents at
least 2), so no pair of any exponent is missed there. The wider sweeps test for squares.

## The known small pairs

```
{1,2} u {8,9}        ->        144 = 12^2
{2,3} u {24,25}      ->       3600 = 60^2
{1,2,3} u {48,49,50} ->    705 600 = 840^2
```

and the infinite family `{1,2} u {c, c+1}` with `c = 8, 49, 288, 1681, 9800, ...` from
`(2c+1)^2 - 2s^2 = 1`, giving `144, 4900, 166464, 5654884, 192099600`. This family is
`2c(c+1) = s^2`. The value `c = 1` is degenerate, since then `I2 = I1` and the blocks are not
disjoint.

## Literature status

Not searched. The length-4 pair is new relative to the internal source that declared its own search
box empty, and to this estate. Historical novelty is a separate question from correctness, and it is
open here.

## Verification

```bash
python verify.py
```

Standard library only. 38 checks, exit 0. It recomputes the factorisations, confirms the square by
exact integer square root, re-derives the uniqueness sweep from scratch, and checks each refutation
below.

---

# Six refuted dossiers

Ten research dossiers were located in an internal mine and never read. Six of the ten central claims
are false. Two of those six were stated as closures of open problems.

## 1. A family that fails at its own first case

The dossier states:

> *"Fix any k >= 2 and set I1 = [k, 2k-1], I2 = [4k, 5k-1]. Then the product of I2 equals the
> product of 4m over m in I1 ... Hence the product is a perfect square ... for every k >= 2 ...
> So no universal threshold k(r) exists ... any affirmative close is impossible for r >= 2."*

| k | I1 | I2 | product | factorisation | perfect power |
|---|---|---|---|---|---|
| 2 | {2,3} | {8,9} | **432** | `2^4 · 3^3` | no |
| 3 | {3,4,5} | {12,13,14} | 131 040 | `2^5 · 3^2 · 5 · 7 · 13` | no |
| 4 | {4,5,6,7} | {16,..,19} | 78 140 160 | `2^8 · 3^3 · 5 · 7 · 17 · 19` | no |
| 5 | {5,..,9} | {20,..,24} | 77 119 257 600 | `2^10 · 3^5 · 5^2 · 7^2 · 11 · 23` | no |

`4 · I1` is not `I2`. Multiplying consecutive integers by 4 gives spacing 4:

```
k=2:   4 · {2,3}    = {8, 12}         I2 = {8, 9}
k=3:   4 · {3,4,5}  = {12, 16, 20}    I2 = {12, 13, 14}
```

The same dossier identifies and kills this construction in its own audit section, then reintroduces
it as a fresh route and uses it to declare the problem closed.

## 2. `gcd(n!-1, m!-1) = 1`

The dossier proves that every prime `p` dividing `n!-1` satisfies `p > n`, which is true, then
concludes that for `m > n` the prime `p` divides `m!`, giving `gcd = 1`. That step needs `p <= m`
and has only `p > n`.

```
4! - 1 = 23        8! - 1 = 40319 = 23 · 1753        gcd(23, 40319) = 23
```

`p = 23 > 8 = m`, so `8!` is not divisible by 23. Nine failures with `n, m <= 25`:

```
(4,8)=23  (4,11)=23  (4,21)=23  (5,11)=17  (5,15)=17
(8,11)=23 (8,21)=23  (11,15)=17 (11,21)=23
```

The dossier's check window is `{2,...,7}`, one step short of the first failure.

The correct statement is in the same file: `gcd(m!-1, n!-1)` divides `(n+1)(n+2)···m - 1`. That
holds for all `2 <= n < m <= 21` with no violations, and it repairs the false claim.

A second item in the same dossier gives `S in (1.253498755679455, 1.253498755679566)` as an
enclosure. `S = 1.2534987556999534716...`, which is `2.04 x 10^-11` above the stated upper endpoint.

## 3. A graph lemma false in the only case at issue

The dossier argues that every subgraph of `K_m` is complete, so chromatic number `m` forces the
subgraph to be `K_m` and therefore to contain a triangle, and concludes the problem is settled
FALSE for every `r >= 3`.

Subgraphs are obtained by deleting vertices and edges, so the subgraphs of `K_m` are all graphs on
at most `m` vertices. `K_4` contains `C_4`.

The salvage, `H` inside `K_n` with chromatic number `n` implies `H = K_n`, holds for finite `n`
(checked exhaustively for `n = 2, 3, 4`) and fails for infinite `m`, which is the case the problem
concerns. The disjoint union of `K_1, K_2, K_3, ...` sits inside `K_{aleph_0}`, has chromatic number
`aleph_0`, and is not complete or connected.

`K_{aleph_0}` is also not a counterexample to the original statement. Take graphs `G_k` with
chromatic number `k` and girth greater than `r` (Erdős 1959). Their disjoint union has infinite
chromatic number, no odd cycle of length at most `r`, and embeds in `K_{aleph_0}`.

The same file calls this lemma FALSE in another block.

## 4. Partition values off by one index

| dossier | truth |
|---|---|
| `p(7) = 22` | `p(7) = 15 = 3 · 5`, and `22 = p(8)` |
| `p(11) = 101` | `p(11) = 56 = 2^3 · 7`, and `101 = p(13)` |

The prime 11 enters at `k = 6` through `p(6) = 11`, not at `k = 7`. The claimed entry points 7 and 11
are not entry points, since `p(7)` and `p(11)` are smooth. The claimed strictly decreasing gap
reaching `-50` is not monotone and its minimum for `n <= 60` is `-18`.

## 5. A coverage lemma that fails at its smallest instance

> *"For every greedy sequence (any start n) and every k >= 1: the partial reciprocal sum is at least
> `1 - (k+1)/(a_{k+1} - 1)`."*

Start `n = 4`, `k = 1`. The sequence begins `4, 5`. Left side `1/4`, right side `1 - 2/4 = 1/2`.

The proof opens with "every `m` in `[1, a_{k+1}-1]` is a consecutive sum", which is false for any
start `n >= 2`, since nothing below `n` is representable. The lemma holds for `n = 1` and is stated
for any start.

## 6. Right conclusion, wrong witness

A lemma `v_0(n) >= 2 for every n >= 5` is filed with the counterexample `n = 15`, justified as
"15 = 3 · 5, so omega = 1". The line writes a two-prime factorisation and reads it as one prime.
`omega(15) = 2`.

The lemma is false. The witnesses at least 5 are `n = 7, 8, 16`. The dossier computes `v_0(7) = 1`
two lines away.

---

# What survives

**An `O(sqrt n)` finite reduction.** If `n+k` has two distinct prime factors both greater than `k`,
then `n+k >= (k+1)(k+2)`, so `k` is at most about `sqrt n`. This turns a per-`n` infinite question
into a bounded check. For all `n <= 3000` the reduced window and the full range agree exactly. The
census is `{n <= 3000 : v_0(n) <= 1} = {2, 3, 4, 7, 8, 16}`.

**Five exact modular-covering certificates**, each verified periodic:

```
A = {1}    gaps 2, 2, 2, ...        residues {1} mod 2
A = {2}    gaps 1, 4 repeating      residues {2,3} mod 5
A = {3}    gaps 1, 1, 6 repeating   residues {3,4,5} mod 8
```

**A forbidden-triple normalisation.** `{a,b,c}` is forbidden if and only if `a = dx, b = dy, c = dz`
with `x, y, z` pairwise coprime and distinct. Verified over all triples in `[60]`. The companion
values `f_3(1..8) = 1, 2, 2, 3, 3, 3, 3, 4` are correct; a second table in the same file giving
`1, 2, 2, 3, 4, 4, 4, 5` is wrong. The `log_2` lower bound is not tight: `f_3(9) = 5` with
extremizer `{2,3,4,8,9}` against a bound of 4.

# The four shapes of failure

Across ten dossiers the errors repeat:

1. **Sampled, then stated universally.** The `gcd = 1` claim is checked to `n, m <= 7`; the first
   failure is `(4, 8)`.
2. **An error the same file already caught, reintroduced as a fresh route.** The `4 · I1`
   construction and the graph lemma, each killed in one section and load-bearing in another.
3. **Right conclusion, wrong witness.** A false lemma offered with a counterexample that is not one.
4. **Contradictory tables inside one file.** Three sequences for the same set, three value tables,
   two values for the same constant.

The attack apparatus around these claims ran in full and caught none of the six. In two cases it ran
against the truth: the correct kill was already on record, and a later route restated the killed
error as a closure.

## License

Apache-2.0.
