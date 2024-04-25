def sum_odd(l, r):
    sum = 0
    for num in range(l, r+1):
        if num % 2 != 0:
            sum += num
    return sum

def check(candidate):
    assert sum_in_range(2,5) == 8
    assert sum_in_range(5,7) == 12
    assert sum_in_range(7,13) == 40

check(sum_odd)