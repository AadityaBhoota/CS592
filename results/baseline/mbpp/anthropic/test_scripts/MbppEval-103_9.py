def eulerian_num(n, m):
    """
    Write a function to find the Eulerian number a(n, m).

    Examples:
    eulerian_num(3, 1) == 4
    eulerian_num(4, 1) == 11
    eulerian_num(5, 3) == 26
    """
    if m < 0 or m > n:
        return 0
    if m == 0 or m == n:
        return 1
    return (n - m) * eulerian_num(n - 1, m - 1) + (m + 1) * eulerian_num(n - 1, m)

def check(candidate):
    assert eulerian_num(3, 1) == 4
    assert eulerian_num(4, 1) == 11
    assert eulerian_num(5, 3) == 26

check(eulerian_num)