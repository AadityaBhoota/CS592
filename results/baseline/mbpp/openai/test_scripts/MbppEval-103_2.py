def eulerian_num(n, m): 
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i == 0:
                dp[i][j] = 1 if j == 0 else 0
            else:
                if j == 0:
                    dp[i][j] = (i-1)*dp[i-1][1]
                else:
                    dp[i][j] = (i-j)*dp[i-1][j] + (j+1)*dp[i-1][j-1]
    return dp[n][m]

# Examples




def check(candidate):
    assert eulerian_num(3, 1) == 4
    assert eulerian_num(4, 1) == 11
    assert eulerian_num(5, 3) == 26

check(eulerian_num)