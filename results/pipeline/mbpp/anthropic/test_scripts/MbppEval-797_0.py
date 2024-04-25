def sum_odd(l, r):
    total = 0
    for num in range(l, r+1):
        if num % 2 == 1:
            total += num
    return total

def check(candidate):
    assert sum_in_range(2,5) == 8
    assert sum_in_range(5,7) == 12
    assert sum_in_range(7,13) == 40

check(sum_odd)