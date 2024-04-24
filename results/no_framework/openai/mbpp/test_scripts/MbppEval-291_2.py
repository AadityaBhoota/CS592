def count_no_of_ways(n, k):
    if n == 0:
        return 0
    same = 0  # number of ways to paint the current post same as the previous one
    diff = k  # number of ways to paint the current post different from the previous one

    for i in range(2, n+1):
        same, diff = diff, (same + diff) * (k - 1)

    return same + diff

# Test the function with the given examples




def check(candidate):
    assert count_no_of_ways(2, 4) == 16
    assert count_no_of_ways(3, 2) == 6
    assert count_no_of_ways(4, 4) == 228

check(count_no_of_ways)