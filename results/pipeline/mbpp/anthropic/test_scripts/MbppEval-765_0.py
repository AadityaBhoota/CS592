import math

def is_polite(n):
    """
    Find the nth polite number.
    """
    num = 1
    while True:
        if num % n == 0 and num % (n + 1) == 0:
            return num
        num += 1

def check(candidate):
    assert is_polite(7) == 11
    assert is_polite(4) == 7
    assert is_polite(9) == 13

check(is_polite)