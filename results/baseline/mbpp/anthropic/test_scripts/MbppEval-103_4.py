def eulerian_num(n, m):
    """
    Calculates the Eulerian number a(n, m).

    Args:
        n (int): The value of n in the Eulerian number a(n, m).
        m (int): The value of m in the Eulerian number a(n, m).

    Returns:
        int: The Eulerian number a(n, m).
    """
    if m < 0 or m > n:
        return 0
    if m == 0 or m == n:
        return 1

    # Use the recurrence relation to calculate the Eulerian number
    return (n - m + 1) * eulerian_num(n - 1, m - 1) + (m + 1) * eulerian_num(n - 1, m)

def check(candidate):
    assert eulerian_num(3, 1) == 4
    assert eulerian_num(4, 1) == 11
    assert eulerian_num(5, 3) == 26

check(eulerian_num)