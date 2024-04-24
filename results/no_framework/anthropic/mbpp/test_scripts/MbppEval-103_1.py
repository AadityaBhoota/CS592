def eulerian_num(n, m):
    """
    Calculates the Eulerian number a(n, m).

    The Eulerian number a(n, m) is the number of permutations of the set {1, 2, ..., n}
    in which there are exactly m elements that are greater than the next element.

    Args:
        n (int): The number of elements in the set.
        m (int): The number of elements that are greater than the next element.

    Returns:
        int: The Eulerian number a(n, m).
    """
    if m < 0 or m > n - 1:
        return 0
    if m == 0 or m == n - 1:
        return 1

    return (m * eulerian_num(n - 1, m - 1) + (n - m) * eulerian_num(n - 1, m))

def check(candidate):
    assert eulerian_num(3, 1) == 4
    assert eulerian_num(4, 1) == 11
    assert eulerian_num(5, 3) == 26

check(eulerian_num)