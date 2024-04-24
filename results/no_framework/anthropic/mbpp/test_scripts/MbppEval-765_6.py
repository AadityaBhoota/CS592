import math

def is_polite(n):
    """
    Find the nth polite number.

    Polite numbers are positive integers that can be expressed as the sum of two
    or more consecutive positive integers.

    Args:
        n (int): The index of the polite number to find.

    Returns:
        int: The nth polite number.
    """
    polite_number = 0
    count = 0
    i = 1

    while count < n:
        start = i
        while start * (start + 1) // 2 <= polite_number + i:
            start += 1
        polite_number = start * (start + 1) // 2
        count += 1
        i += 1

    return polite_number

def check(candidate):
    assert is_polite(7) == 11
    assert is_polite(4) == 7
    assert is_polite(9) == 13

check(is_polite)