def count_no_of_ways(n, k):
    """
    Find the number of ways of painting the fence such that at most 2 adjacent posts
    have the same color for the given fence with n posts and k colors.

    Args:
        n (int): The number of posts in the fence.
        k (int): The number of colors available.

    Returns:
        int: The number of ways to paint the fence.
    """
    if n == 1:
        return k
    if n == 2:
        return k * k

    same = k
    diff = k * (k - 1)

    for i in range(3, n + 1):
        same, diff = diff, (same + diff) * (k - 1)

    return same + diff

def check(candidate):
    assert count_no_of_ways(2, 4) == 16
    assert count_no_of_ways(3, 2) == 6
    assert count_no_of_ways(4, 4) == 228

check(count_no_of_ways)