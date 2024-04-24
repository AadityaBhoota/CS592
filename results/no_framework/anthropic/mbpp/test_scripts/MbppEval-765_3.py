import math

def is_polite(n):
    """
    Write a function to find the nth polite number.

    Examples:
    is_polite(7) == 11
    is_polite(4) == 7
    is_polite(9) == 13
    """
    return (n * (n + 1)) // 2 + 1

def check(candidate):
    assert is_polite(7) == 11
    assert is_polite(4) == 7
    assert is_polite(9) == 13

check(is_polite)