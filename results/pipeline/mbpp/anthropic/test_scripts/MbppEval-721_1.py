def maxAverageOfPath(cost):
    n = len(cost)
    dp = [[0] * n for _ in range(n)]
    
    # Base case: the average for the top-left cell is the cost of that cell
    dp[0][0] = cost[0][0]
    
    # Fill in the first row and first column
    for i in range(1, n):
        dp[i][0] = (dp[i-1][0] * i + cost[i][0]) / (i + 1)
        dp[0][i] = (dp[0][i-1] * i + cost[0][i]) / (i + 1)
    
    # Fill in the rest of the matrix
    for i in range(1, n):
        for j in range(1, n):
            # The maximum average for the current cell is the maximum of
            # the average of the path coming from the left and the average
            # of the path coming from above
            dp[i][j] = max((dp[i-1][j] * i + cost[i][j]) / (i + 1),
                          (dp[i][j-1] * j + cost[i][j]) / (j + 1))
    
    # The maximum average is the value in the bottom-right cell
    return dp[n-1][n-1]

def check(candidate):
    assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
    assert maxAverageOfPath([[2, 3, 4], [7, 6, 5], [8, 4, 10]]) == 6.2
    assert maxAverageOfPath([[3, 4, 5], [8, 7, 6], [9, 5, 11]]) == 7.2
    assert maxAverageOfPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 5.8

check(maxAverageOfPath)