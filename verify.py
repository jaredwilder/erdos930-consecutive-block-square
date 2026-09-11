#!/usr/bin/env python3
"""Exact verifier for the released Erdős #930 results.

Standard library only.

Checks:
- the length-4 square-product witness;
- its factorisations and squarefree-part mechanism;
- three smaller exact witnesses;
- the first displayed Pell-family values;
- uniqueness of the length-4 square witness for a<=120, b<=6000;
- both length-3 Pell families with their recurrences;
- the three length-2 cubes;
- the length-5 square-class collision that overlaps.
"""
from math import isqrt, prod

FAILURES = []


def check(label, got, want):
    ok = got == want
    print(f"  {label:<58} {'PASS' if ok else f'FAIL got={got!r} want={want!r}'}")
    if not ok:
        FAILURES.append(label)


def factorize(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def squarefree_part(n):
    return prod(p for p, e in factorize(n).items() if e % 2)


def is_square(n):
    r = isqrt(n)
    return r * r == n


def block_product(a, length):
    return prod(range(a, a + length))


def test_length4_witness():
    print("Length-4 witness")
    p1 = block_product(33, 4)
    p2 = block_product(1680, 4)
    total = p1 * p2

    check("P1", p1, 1413720)
    check("P2", p2, 7994422608480)
    check("P1 factorisation", factorize(p1),
          {2: 3, 3: 3, 5: 1, 7: 1, 11: 1, 17: 1})
    check("P2 factorisation", factorize(p2),
          {2: 5, 3: 3, 5: 1, 7: 1, 11: 1, 17: 1, 29: 2, 41: 2})
    check("squarefree part of P1", squarefree_part(p1), 39270)
    check("squarefree part of P2", squarefree_part(p2), 39270)
    check("combined product", total, 11301875130060345600)
    check("combined product is square", is_square(total), True)
    check("square root", isqrt(total), 3361826160)


def test_smaller_witnesses():
    print("\nSmaller witnesses")
    cases = [
        ((1, 2), (8, 9), 12),
        ((2, 3), (24, 25), 60),
        ((1, 2, 3), (48, 49, 50), 840),
    ]
    for left, right, root in cases:
        total = prod(left) * prod(right)
        check(f"{left} x {right}", total, root * root)


def test_pell_family():
    print("\nPell family")
    for c in [8, 49, 288, 1681, 9800]:
        value = 2 * c * (c + 1)
        check(f"2*{c}*({c}+1) is square", is_square(value), True)


def test_length4_uniqueness(amax=120, bmax=6000):
    print(f"\nLength-4 square search: a<={amax}, b<={bmax}")

    # Precompute square classes of all relevant blocks so the exhaustive search
    # compares exact squarefree parts rather than repeatedly factoring products.
    sf = {a: squarefree_part(block_product(a, 4))
          for a in range(2, bmax + 1)}

    found = []
    for a in range(2, amax + 1):
        for b in range(a + 4, bmax + 1):
            if sf[a] == sf[b]:
                total = block_product(a, 4) * block_product(b, 4)
                if is_square(total):
                    found.append((a, b, isqrt(total)))

    check("square-product pairs", found, [(33, 1680, 3361826160)])


def test_length3_families():
    """Two infinite Pell families at length 3."""
    print("Two infinite Pell families at length 3")

    def overlap(a, b, k=3):
        return set(range(a, a + k)) & set(range(b, b + k))

    print("  Family A: {a,a+1,a+2} with {2a,2a+1,2a+2},  (4a+5)^2 - 8y^2 = 9")
    A = [73, 2521, 85681, 2910673, 98877241]
    for a in A:
        p1, p2 = block_product(a, 3), block_product(2 * a, 3)
        check(f"    a = {a:<9} blocks disjoint", overlap(a, 2 * a), set())
        check("      product is a square", is_square(p1 * p2), True)
        check("      (a+2)(2a+1) is a square", is_square((a + 2) * (2 * a + 1)), True)
    for i in range(len(A) - 2):
        check("    recurrence 34a(n) - a(n-1) + 40",
              34 * A[i + 1] - A[i] + 40, A[i + 2])
    p = block_product(73, 3) * block_product(146, 3)
    check("    {73,74,75} with {146,147,148}", p, 1286908736400)
    check("      square root", isqrt(p), 1134420)

    print("  Family B: {a,a+1,a+2} with {2a+2,2a+3,2a+4},  (4a+3)^2 - 8y^2 = 9")
    B = [12, 432, 14700, 499392, 16964652]
    for a in B:
        p1, p2 = block_product(a, 3), block_product(2 * a + 2, 3)
        check(f"    a = {a:<9} blocks disjoint", overlap(a, 2 * a + 2), set())
        check("      product is a square", is_square(p1 * p2), True)
        check("      a(2a+3) is a square", is_square(a * (2 * a + 3)), True)
    for i in range(len(B) - 2):
        check("    recurrence 34a(n) - a(n-1) + 24",
              34 * B[i + 1] - B[i] + 24, B[i + 2])
    p = block_product(12, 3) * block_product(26, 3)
    check("    {12,13,14} with {26,27,28}", p, 42928704)
    check("      square root", isqrt(p), 6552)


def _icbrt(n):
    r = round(n ** (1.0 / 3.0))
    for c in (r - 2, r - 1, r, r + 1, r + 2):
        if c > 0 and c ** 3 == n:
            return c
    return None


def test_cubes():
    """Three length-2 pairs whose product is a cube and not a square."""
    print("Three perfect cubes at length 2")
    for a, b, root in ((11, 242, 198), (32, 242, 396), (539, 3024, 13860)):
        P = block_product(a, 2) * block_product(b, 2)
        check(f"  {{{a},{a+1}}} with {{{b},{b+1}}} is a cube", _icbrt(P), root)
        check("    and is not a square", is_square(P), False)


def test_length5_near_miss():
    """The one square-class collision at length 5 overlaps, so it is not an instance."""
    print("The length-5 near-miss")
    p1, p2 = block_product(4, 5), block_product(5, 5)
    check("  squarefree parts agree", squarefree_part(p1), squarefree_part(p2))
    check("    both equal 105", squarefree_part(p1), 105)
    check("  the product IS a square", is_square(p1 * p2), True)
    check("  but the blocks overlap",
          bool(set(range(4, 9)) & set(range(5, 10))), True)
    check("    because 4 and 9 are squares", squarefree_part(4), squarefree_part(9))


def main():
    test_length4_witness()
    test_smaller_witnesses()
    test_pell_family()
    test_length3_families()
    test_cubes()
    test_length5_near_miss()
    test_length4_uniqueness()

    print()
    if FAILURES:
        print(f"FAILED: {len(FAILURES)} check(s)")
        for label in FAILURES:
            print("  " + label)
        return 1
    print("ALL CHECKS PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
