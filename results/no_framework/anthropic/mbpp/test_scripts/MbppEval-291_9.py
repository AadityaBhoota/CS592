def count_no_of_ways(n, k):
    """
    Write a function to find out the number of ways of painting the fence such that at most 2 adjacent posts have the same color for the given fence with n posts and k colors.

    Examples:
    count_no_of_ways(2, 4) == 16
    count_no_of_ways(3, 2) == 6
    count_no_of_ways(4, 4) == 228
    """
    if n == 1:
        return k
    if n == 2:
        return k * k

    same, diff = k, k * (k - 1)
    for i in range(3, n + 1):
        same, diff = diff, (same + diff) * (k - 1)

    return same + diff

def check(candidate):
    assert count_no_of_ways(2, 4) == 16
    assert count_no_of_ways(3, 2) == 6
    assert count_no_of_ways(4, 4) == 228

check(count_no_of_ways)