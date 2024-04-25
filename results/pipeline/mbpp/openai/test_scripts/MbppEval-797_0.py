def sum_odd(n):
    sum_odd = 0
    
    for num in range(1, n+1):
        if num % 2 != 0:
            sum_odd += num
    
    return sum_odd

def check(candidate):
    assert sum_in_range(2,5) == 8
    assert sum_in_range(5,7) == 12
    assert sum_in_range(7,13) == 40

check(sum_odd)