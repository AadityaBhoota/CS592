def maxAverageOfPath(cost):
    n = len(cost)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = cost[i][j] / 1
            elif i == 0:
                dp[i][j] = (cost[i][j] + dp[i][j - 1] * (j + 1)) / (j + 1)
            elif j == 0:
                dp[i][j] = (cost[i][j] + dp[i - 1][j] * (i + 1)) / (i + 1)
            else:
                dp[i][j] = max((cost[i][j] + dp[i][j - 1] * (j + 1)) / (j + 1),
                               (cost[i][j] + dp[i - 1][j] * (i + 1)) / (i + 1))

    return dp[n-1][n-1]

# Test the function with the given examples




def check(candidate):
    assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
    assert maxAverageOfPath([[2, 3, 4], [7, 6, 5], [8, 4, 10]]) == 6.2
    assert maxAverageOfPath([[3, 4, 5], [8, 7, 6], [9, 5, 11]]) == 7.2
    assert maxAverageOfPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 5.8

check(maxAverageOfPath)