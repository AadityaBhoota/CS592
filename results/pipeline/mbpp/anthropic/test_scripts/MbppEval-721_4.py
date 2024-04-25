def maxAverageOfPath(cost):
    N = len(cost)
    dp = [[0] * N for _ in range(N)]
    
    # Base cases
    dp[0][0] = cost[0][0]
    
    # Compute the maximum average path
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                dp[i][j] = dp[i][j-1] + cost[i][j]
            elif j == 0:
                dp[i][j] = dp[i-1][j] + cost[i][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + cost[i][j]
    
    return dp[N-1][N-1] / (2*N - 1)

def check(candidate):
    assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
    assert maxAverageOfPath([[2, 3, 4], [7, 6, 5], [8, 4, 10]]) == 6.2
    assert maxAverageOfPath([[3, 4, 5], [8, 7, 6], [9, 5, 11]]) == 7.2
    assert maxAverageOfPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 5.8

check(maxAverageOfPath)