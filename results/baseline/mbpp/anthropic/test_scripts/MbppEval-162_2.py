def sum_series(n):
    """
    Calculates the sum (n - 2*i) from i=0 to n // 2, where n is the input.

    Examples:
    sum_series(6) == 12
    sum_series(10) == 30
    sum_series(9) == 25
    """
    total = 0
    for i in range(n // 2 + 1):
        total += n - 2 * i
    return total

def check(candidate):
    assert sum_series(6) == 12
    assert sum_series(10) == 30
    assert sum_series(9) == 25

check(sum_series)