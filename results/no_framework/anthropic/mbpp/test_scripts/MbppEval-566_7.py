def sum_digits(n):
    """
    Write a function to get the sum of the digits of a non-negative integer.

    Examples:
    sum_digits(345) == 12
    sum_digits(12) == 3
    sum_digits(97) == 16
    """
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

def check(candidate):
    assert sum_digits(345)==12
    assert sum_digits(12)==3
    assert sum_digits(97)==16

check(sum_digits)