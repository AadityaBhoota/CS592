def sum_series(n):
    upper_limit = n // 2
    total_sum = 0
    
    for i in range(upper_limit + 1):
        total_sum += n - 2*i

    return total_sum

def check(candidate):
    assert sum_series(6) == 12
    assert sum_series(10) == 30
    assert sum_series(9) == 25

check(sum_series)