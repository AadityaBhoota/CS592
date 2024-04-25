def bell_Number(n):
    import math
    bell_triangle = [[0 for _ in range(n)] for _ in range(n)]
    bell_triangle[0][0] = 1
    for i in range(1, n):
        bell_triangle[i][0] = bell_triangle[i-1][i-1]
        for j in range(1, i+1):
            bell_triangle[i][j] = bell_triangle[i][j-1] + bell_triangle[i-1][j-1]
    return bell_triangle[n-1][-1]

def check(candidate):
    assert bell_Number(2) == 2
    assert bell_Number(3) == 5
    assert bell_Number(4) == 15

check(bell_Number)