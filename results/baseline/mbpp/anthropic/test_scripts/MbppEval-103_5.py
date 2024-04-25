def eulerian_num(n, m):
    """
    Calculate the Eulerian number a(n, m).

    Args:
        n (int): The total number of elements.
        m (int): The number of elements to be chosen.

    Returns:
        int: The Eulerian number a(n, m).
    """
    if m > n or m < 0:
        return 0
    elif m == 0 or m == n:
        return 1
    else:
        return (n - m) * eulerian_num(n - 1, m - 1) + (m + 1) * eulerian_num(n - 1, m)

# Examples




def check(candidate):
    assert eulerian_num(3, 1) == 4
    assert eulerian_num(4, 1) == 11
    assert eulerian_num(5, 3) == 26

check(eulerian_num)