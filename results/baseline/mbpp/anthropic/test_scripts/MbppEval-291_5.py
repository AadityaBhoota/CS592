def count_no_of_ways(n, k):
    """
    Write a function to find out the number of ways of painting the fence such that at most 2 adjacent posts have the same color for the given fence with n posts and k colors.

    Examples:
    count_no_of_ways(2, 4) == 16
    count_no_of_ways(3, 2) == 6
    count_no_of_ways(4, 4) == 228
    """
    if n == 0:
        return 0
    if n == 1:
        return k

    same = k  # the number of ways to paint the current post the same as the previous post
    diff = k * (k - 1)  # the number of ways to paint the current post different from the previous post

    for i in range(2, n):
        temp = diff
        diff = (same + diff) * (k - 1)
        same = temp

    return same + diff

def check(candidate):
    assert count_no_of_ways(2, 4) == 16
    assert count_no_of_ways(3, 2) == 6
    assert count_no_of_ways(4, 4) == 228

check(count_no_of_ways)