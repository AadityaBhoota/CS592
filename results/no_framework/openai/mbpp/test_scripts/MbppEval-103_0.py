def eulerian_num(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        dp[i][0] = 1
        for j in range(1, m + 1):
            if i >= 2:
                dp[i][j] = (i - 1) * dp[i - 1][j] + (j + 1) * dp[i - 1][j - 1]
    
    return dp[n][m]

# Test cases




def check(candidate):
    assert eulerian_num(3, 1) == 4
    assert eulerian_num(4, 1) == 11
    assert eulerian_num(5, 3) == 26

check(eulerian_num)