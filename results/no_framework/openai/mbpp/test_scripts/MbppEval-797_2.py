def sum_odd(l, r):
    return sum(x for x in range(l, r + 1) if x % 2 != 0)

# Test cases




def check(candidate):
    assert sum_in_range(2,5) == 8
    assert sum_in_range(5,7) == 12
    assert sum_in_range(7,13) == 40

check(sum_odd)