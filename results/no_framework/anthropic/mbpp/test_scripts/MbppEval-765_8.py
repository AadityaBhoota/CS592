import math

def is_polite(n):
    """
    Write a function to find the nth polite number.

    A polite number is a number that can be expressed as the sum of two or more
    consecutive positive integers.

    Examples:
    is_polite(7) == 11
    is_polite(4) == 7
    is_polite(9) == 13
    """
    if n <= 0:
        return 0

    num = 1
    while True:
        # Check if the number is polite
        for i in range(1, num // 2 + 1):
            if sum(range(i, i + num - 1)) == num:
                n -= 1
                if n == 0:
                    return num
        num += 1

# Test cases




def check(candidate):
    assert is_polite(7) == 11
    assert is_polite(4) == 7
    assert is_polite(9) == 13

check(is_polite)