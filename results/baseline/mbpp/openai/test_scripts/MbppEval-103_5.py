def eulerian_num(n, m):
    if m == 0:
        return 1
    if n == 0:
        return 0
    if m > n + 1:
        return 0
    return (n - m + 1) * eulerian_num(n - 1, m - 1) + (m + 1) * eulerian_num(n - 1, m)

# Test cases




def check(candidate):
    assert eulerian_num(3, 1) == 4
    assert eulerian_num(4, 1) == 11
    assert eulerian_num(5, 3) == 26

check(eulerian_num)