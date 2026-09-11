#!/usr/bin/env python3
"""Exact verifier for the released Erdős #930 results.

Standard library only.

Checks:
- the length-4 square-product witness;
- its factorisations and squarefree-part mechanism;
- three smaller exact witnesses;
- the first displayed Pell-family values;
- uniqueness of the length-4 square witness for a<=120, b<=6000.
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


def main():
    test_length4_witness()
    test_smaller_witnesses()
    test_pell_family()
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
