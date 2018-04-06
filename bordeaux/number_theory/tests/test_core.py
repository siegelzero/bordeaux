from bordeaux.number_theory.core import (
    gcd,
    gcd_list
)


def test_gcd():
    # Test symmetry of positive inputs
    assert gcd(20, 10) == 10
    assert gcd(10, 20) == 10

    # Test symmetry with one negative input
    assert gcd(-10, 20) == 10
    assert gcd(-20, 10) == 10

    # Test symmetry with two negative inputs
    assert gcd(-10, -10) == 10

    # Basic tests with 1 and an prime
    assert gcd(1, 11213) == 1
    assert gcd(11213, 1) == 1

    # Ensure 0 is handled properly
    assert gcd(0, 10) == 10
    assert gcd(10, 0) == 10
    assert gcd(0, -10) == 10

    # Sanity testing on small numbers
    values = [
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2,
        1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 3, 1,
        1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 1, 2, 1, 4, 1, 2,
        1, 4, 1, 2, 1, 4, 1, 2, 1, 4, 1, 2, 1, 4, 1, 1, 1, 1, 5, 1, 1, 1,
        1, 5, 1, 1, 1, 1, 5, 1, 1, 1, 1, 5, 1, 2, 3, 2, 1, 6, 1, 2, 3, 2,
        1, 6, 1, 2, 3, 2, 1, 6, 1, 2, 1, 1, 1, 1, 1, 1, 7, 1, 1, 1, 1, 1,
        1, 7, 1, 1, 1, 1, 1, 1, 1, 2, 1, 4, 1, 2, 1, 8, 1, 2, 1, 4, 1, 2,
        1, 8, 1, 2, 1, 4, 1, 1, 3, 1, 1, 3, 1, 1, 9, 1, 1, 3, 1, 1, 3, 1,
        1, 9, 1, 1, 1, 2, 1, 2, 5, 2, 1, 2, 1, 10, 1, 2, 1, 2, 5, 2, 1, 2,
        1, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 2, 3, 4, 1, 6, 1, 4, 3, 2, 1, 12, 1, 2, 3, 4, 1, 6, 1, 4, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 13, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2,
        1, 2, 7, 2, 1, 2, 1, 2, 1, 14, 1, 2, 1, 2, 1, 2, 1, 1, 3, 1, 5, 3,
        1, 1, 3, 5, 1, 3, 1, 1, 15, 1, 1, 3, 1, 5, 1, 2, 1, 4, 1, 2, 1, 8,
        1, 2, 1, 4, 1, 2, 1, 16, 1, 2, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 17, 1, 1, 1, 1, 2, 3, 2, 1, 6, 1, 2, 9, 2, 1, 6,
        1, 2, 3, 2, 1, 18, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 19, 1, 1, 2, 1, 4, 5, 2, 1, 4, 1, 10, 1, 4, 1, 2, 5, 4,
        1, 2, 1, 20
    ]

    i = 0
    for a in range(1, 21):
        for b in range(1, 21):
            assert gcd(a, b) == values[i]
            i += 1


def test_gcd_list():
    assert gcd_list([2, 4, 6, 8]) == 2
    assert gcd_list([1, 4, 6, 8]) == 1
    assert gcd_list([-2, 4, 6, 8]) == 2
    assert gcd_list([0, 4, 6, 8]) == 2
    assert gcd_list([2]) == 2
