def sum_series(n):
    total = 0
    for i in range(n // 2 + 1):
        total += n - 2 * i
    return total

# Test cases




def check(candidate):
    assert sum_series(6) == 12
    assert sum_series(10) == 30
    assert sum_series(9) == 25

check(sum_series)