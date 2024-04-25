def modp(n: int, p: int) -> int:
    """Return 2^n modulo p (be aware of numerics)."""
    if n == 0:
        return 1
    
    result = 1
    for _ in range(n):
        result = (result * 2) % p
    
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