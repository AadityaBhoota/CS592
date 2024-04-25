def sum_series(n):
    total_sum = 0
    
    for i in range(n // 2 + 1):
        term = n - 2*i
        total_sum += term
    
    return total_sum

def check(candidate):
    assert sum_series(6) == 12
    assert sum_series(10) == 30
    assert sum_series(9) == 25

check(sum_series)