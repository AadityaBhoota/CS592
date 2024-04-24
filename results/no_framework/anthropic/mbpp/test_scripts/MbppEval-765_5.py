import math

def is_polite(n):
    """
    Write a function to find the nth polite number.

    Examples:
    is_polite(7) == 11
    is_polite(4) == 7
    is_polite(9) == 13
    """
    start = 1
    while True:
        # Check if the sum of consecutive integers starting from `start` is equal to `n`
        total = 0
        for i in range(start, n+1):
            total += i
            if total == n:
                return n
            elif total > n:
                break
        start += 1

    # If no such sequence of consecutive integers is found, return -1
    return -1

def check(candidate):
    assert is_polite(7) == 11
    assert is_polite(4) == 7
    assert is_polite(9) == 13

check(is_polite)