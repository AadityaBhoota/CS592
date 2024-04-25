import math

def is_polite(n):
    """
    Find the nth polite number.
    """
    k = 1
    while True:
        # Solve the equation n = k * (2a + k - 1) / 2 for a
        a = (n - k * (k - 1) // 2) / k
        if a.is_integer() and a > 0:
            return int(a + (k - 1) / 2)
        k += 1

def check(candidate):
    assert is_polite(7) == 11
    assert is_polite(4) == 7
    assert is_polite(9) == 13

check(is_polite)