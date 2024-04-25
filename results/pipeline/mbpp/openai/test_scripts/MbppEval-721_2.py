def maxAverageOfPath(cost):
    n = len(cost)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    count = [[0 for _ in range(n)] for _ in range(n)]

    dp[0][0] = cost[0][0]
    count[0][0] = 1

    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + cost[i][0]
        count[i][0] = count[i-1][0] + 1

    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + cost[0][j]
        count[0][j] = count[0][j-1] + 1

    for i in range(1, n):
        for j in range(1, n):
            top = dp[i-1][j] + cost[i][j]
            left = dp[i][j-1] + cost[i][j]
            if top >= left:
                dp[i][j] = top
                count[i][j] = count[i-1][j] + 1
            else:
                dp[i][j] = left
                count[i][j] = count[i][j-1] + 1

    return dp[n-1][n-1] / count[n-1][n-1]

def check(candidate):
    assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
    assert maxAverageOfPath([[2, 3, 4], [7, 6, 5], [8, 4, 10]]) == 6.2
    assert maxAverageOfPath([[3, 4, 5], [8, 7, 6], [9, 5, 11]]) == 7.2
    assert maxAverageOfPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 5.8

check(maxAverageOfPath)