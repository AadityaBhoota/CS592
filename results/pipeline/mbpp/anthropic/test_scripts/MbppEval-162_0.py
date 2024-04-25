def sum_series(n):
    """
    Write a function to calculate the sum (n - 2*i) from i=0 to n // 2, for instance n + (n-2) + (n-4)... (until n-x =< 0).

    Examples:
    sum_series(6) == 12
    sum_series(10) == 30
    sum_series(9) == 25
    """
    num_terms = n // 2 + 1
    sum_formula = n * num_terms - 2 * (num_terms * (num_terms - 1)) // 2
    return sum_formula

def check(candidate):
    assert sum_series(6) == 12
    assert sum_series(10) == 30
    assert sum_series(9) == 25

check(sum_series)