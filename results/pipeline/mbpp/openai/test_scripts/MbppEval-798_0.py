def _sum(arr):
    total_sum = 0
    for num in arr:
        total_sum += num
    return total_sum

# Test cases




def check(candidate):
    assert _sum([1, 2, 3]) == 6
    assert _sum([15, 12, 13, 10]) == 50
    assert _sum([0, 1, 2]) == 3

check(_sum)