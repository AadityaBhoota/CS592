import math

def is_polite(n):
    """
    Write a function to find the nth polite number.

    The polite numbers are the numbers that can be expressed as the sum of two or more consecutive positive integers.

    Examples:
    is_polite(7) == 11
    is_polite(4) == 7
    is_polite(9) == 13
    """
    if n == 1:
        return 1

    k = 1
    while True:
        # Find the sum of k consecutive integers
        # The sum is given by the formula: (k * (k + 1)) // 2
        sum_of_k = (k * (k + 1)) // 2

        # If the sum is greater than or equal to n, then the nth polite number is the sum
        if sum_of_k >= n:
            return sum_of_k

        k += 1

def check(candidate):
    assert is_polite(7) == 11
    assert is_polite(4) == 7
    assert is_polite(9) == 13

check(is_polite)