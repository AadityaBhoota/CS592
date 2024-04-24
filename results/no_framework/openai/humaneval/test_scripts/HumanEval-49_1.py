def modp(n: int, p: int):
    result = 1
    base = 2

    n = n % (p - 1)  # reduce n modulo p-1 to avoid large exponents

    while n > 0:
        if n % 2 == 1:
            result = (result * base) % p
        base = (base * base) % p
        n //= 2

    return result



METADATA = {}


def check(candidate):
    assert candidate(3, 5) == 3
    assert candidate(1101, 101) == 2
    assert candidate(0, 101) == 1
    assert candidate(3, 11) == 8
    assert candidate(100, 101) == 1
    assert candidate(30, 5) == 4
    assert candidate(31, 5) == 3


check(modp)