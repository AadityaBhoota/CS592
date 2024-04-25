def eulerian_num(n, m):
    eulerian = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        eulerian[i][0] = 1
    for j in range(1, m + 1):
        eulerian[0][j] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            eulerian[i][j] = (i - 1) * eulerian[i - 1][j - 1] + (i - 1) * eulerian[i - 1][j]

    return eulerian[n][m]

def check(candidate):
    assert eulerian_num(3, 1) == 4
    assert eulerian_num(4, 1) == 11
    assert eulerian_num(5, 3) == 26

check(eulerian_num)