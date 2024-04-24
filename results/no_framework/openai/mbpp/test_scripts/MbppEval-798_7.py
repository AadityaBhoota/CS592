def _sum(arr):
    return sum(arr)

# Test the function with the provided examples




def check(candidate):
    assert _sum([1, 2, 3]) == 6
    assert _sum([15, 12, 13, 10]) == 50
    assert _sum([0, 1, 2]) == 3

check(_sum)