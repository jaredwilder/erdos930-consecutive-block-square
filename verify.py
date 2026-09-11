#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Standalone verifier. Standard library only -- no sympy, no numpy.

    python verify.py

Checks the new square witness, re-derives its uniqueness in a search box from
scratch, and confirms each of the refutations. Exit 0 means everything
reproduced.
"""
from __future__ import annotations

import sys
from math import gcd, isqrt, prod, factorial

FAILURES = []


def check(label, got, want):
    ok = got == want
    print("  %-56s %s" % (label, "PASS" if ok else "FAIL got=%r want=%r" % (got, want)))
    if not ok:
        FAILURES.append(label)


def factorize(n):
    """Trial division. Returns {prime: exponent}."""
    f, d = {}, 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def squarefree_part(n):
    """Product of primes with ODD exponent. This is the square-class invariant.

    NOT the radical: the radical multiplies every distinct prime regardless of
    exponent, and comparing radicals gives the wrong answer for this witness.
    """
    return prod(p for p, e in factorize(n).items() if e % 2)


def radical(n):
    return prod(factorize(n))


def is_square(n):
    r = isqrt(n)
    return r * r == n


def test_witness():
    print("The new witness: two blocks of four consecutive integers")
    I1 = list(range(33, 37))
    I2 = list(range(1680, 1684))
    P1, P2 = prod(I1), prod(I2)
    check("I1 is four consecutive integers", I1, [33, 34, 35, 36])
    check("I2 is four consecutive integers", I2, [1680, 1681, 1682, 1683])
    check("the blocks are disjoint", set(I1).isdisjoint(I2), True)
    check("P1", P1, 1413720)
    check("P2", P2, 7994422608480)
    check("P1 factorisation", factorize(P1), {2: 3, 3: 3, 5: 1, 7: 1, 11: 1, 17: 1})
    check("P2 factorisation", factorize(P2),
          {2: 5, 3: 3, 5: 1, 7: 1, 11: 1, 17: 1, 29: 2, 41: 2})
    T = P1 * P2
    check("the combined product", T, 11301875130060345600)
    check("it is a perfect square", is_square(T), True)
    check("its square root", isqrt(T), 3361826160)
    print()
    print("  the mechanism -- same square class, not same radical:")
    check("squarefree_part(P1)", squarefree_part(P1), 39270)
    check("squarefree_part(P2)", squarefree_part(P2), 39270)
    check("  and they are equal", squarefree_part(P1) == squarefree_part(P2), True)
    check("radical(P1) and radical(P2) DIFFER", radical(P1) == radical(P2), False)
    check("  radical(P1)", radical(P1), 39270)
    check("  radical(P2)", radical(P2), 46692030)


def test_uniqueness(amax=120, bmax=6000):
    print("Uniqueness of the length-4 witness, re-derived from scratch")
    found = []
    for a in range(2, amax + 1):
        I1 = list(range(a, a + 4))
        p1 = prod(I1)
        s1 = squarefree_part(p1)
        for b in range(a + 4, bmax + 1):
            I2 = list(range(b, b + 4))
            if set(I1) & set(I2):
                continue
            if squarefree_part(prod(I2)) != s1:
                continue
            t = p1 * prod(I2)
            if is_square(t):
                found.append((a, b, isqrt(t)))
    check("pairs with a<=%d, b<=%d" % (amax, bmax), found, [(33, 1680, 3361826160)])


def test_family_fails():
    print("The dossier family: I1=[k,2k-1], I2=[4k,5k-1], claimed square for every k>=2")
    for k in (2, 3, 4, 5):
        I1 = list(range(k, 2 * k))
        I2 = list(range(4 * k, 5 * k))
        p = prod(I1) * prod(I2)
        g = 0
        for e in factorize(p).values():
            g = gcd(g, e)
        check("k=%d product %d is NOT a perfect power" % (k, p), g <= 1, True)
    print("  the false step -- 4*I1 has spacing 4, so it is not I2:")
    check("4*{2,3}", [4 * x for x in range(2, 4)], [8, 12])
    check("  but I2 is", list(range(8, 10)), [8, 9])


def test_gcd_claim():
    print("The claim gcd(n!-1, m!-1) = 1")
    bad = []
    for n in range(2, 26):
        for m in range(n + 1, 26):
            g = gcd(factorial(n) - 1, factorial(m) - 1)
            if g != 1:
                bad.append((n, m, g))
    check("failures with n,m <= 25", bad,
          [(4, 8, 23), (4, 11, 23), (4, 21, 23), (5, 11, 17), (5, 15, 17),
           (8, 11, 23), (8, 21, 23), (11, 15, 17), (11, 21, 23)])
    check("4!-1", factorial(4) - 1, 23)
    check("8!-1 factorisation", factorize(factorial(8) - 1), {23: 1, 1753: 1})
    check("gcd(4!-1, 8!-1)", gcd(factorial(4) - 1, factorial(8) - 1), 23)
    print("  the dossier checked n,m in {2..7}; the first failure is (4,8)")
    print()
    print("  the correct statement in the same file: the gcd DIVIDES (n+1)...m - 1")
    viol = []
    for n in range(2, 22):
        for m in range(n + 1, 22):
            g = gcd(factorial(n) - 1, factorial(m) - 1)
            if (prod(range(n + 1, m + 1)) - 1) % g != 0:
                viol.append((n, m))
    check("violations for 2<=n<m<=21", viol, [])


def test_partitions():
    print("Partition values")
    p = [1] + [0] * 20
    for k in range(1, 21):
        for i in range(k, 21):
            p[i] += p[i - k]
    check("p(6)", p[6], 11)
    check("p(7)  -- dossier said 22", p[7], 15)
    check("p(8)  -- which is where 22 comes from", p[8], 22)
    check("p(11) -- dossier said 101", p[11], 56)
    check("p(13) -- which is where 101 comes from", p[13], 101)


def main():
    for fn in (test_witness, test_uniqueness, test_family_fails,
               test_gcd_claim, test_partitions):
        fn()
        print()
    if FAILURES:
        print("FAILED: %d check(s)" % len(FAILURES))
        for f in FAILURES:
            print("   " + f)
        return 1
    print("ALL CHECKS PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
