def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics)."""
    result = 1
    while n > 0:
        if n & 1:  # Check if the least significant bit is set
            result = (result * 2) % p
        n >>= 1  # Shift n one bit to the right
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