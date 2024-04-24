def maxAverageOfPath(cost):
    n = len(cost)
    
    # Initialize a 2D array to store the maximum average path for each cell
    max_avg = [[0] * n for _ in range(n)]
    
    # Calculate the maximum average path for the top-left cell
    max_avg[0][0] = cost[0][0]
    
    # Calculate the maximum average path for the first row
    for j in range(1, n):
        max_avg[0][j] = (max_avg[0][j-1] * j + cost[0][j]) / (j + 1)
    
    # Calculate the maximum average path for the first column
    for i in range(1, n):
        max_avg[i][0] = (max_avg[i-1][0] * i + cost[i][0]) / (i + 1)
    
    # Calculate the maximum average path for the rest of the cells
    for i in range(1, n):
        for j in range(1, n):
            from_above = (max_avg[i-1][j] * i + cost[i][j]) / (i + 1)
            from_left = (max_avg[i][j-1] * j + cost[i][j]) / (j + 1)
            max_avg[i][j] = max(from_above, from_left)
    
    return max_avg[n-1][n-1]

# Test cases




def check(candidate):
    assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
    assert maxAverageOfPath([[2, 3, 4], [7, 6, 5], [8, 4, 10]]) == 6.2
    assert maxAverageOfPath([[3, 4, 5], [8, 7, 6], [9, 5, 11]]) == 7.2
    assert maxAverageOfPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 5.8

check(maxAverageOfPath)