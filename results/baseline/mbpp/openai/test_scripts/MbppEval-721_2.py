def maxAverageOfPath(cost):
    n = len(cost)  # Size of the square matrix
    max_avg = [[0 for _ in range(n)] for _ in range(n)]

    # Initialize the maximum average for the starting cell
    max_avg[0][0] = cost[0][0]

    # Calculate the max average path
    for i in range(1, n):
        max_avg[i][0] = max_avg[i - 1][0] + cost[i][0] / (i + 1)
        max_avg[0][i] = max_avg[0][i - 1] + cost[0][i] / (i + 1)
    
    for i in range(1, n):
        for j in range(1, n):
            max_avg[i][j] = max(max_avg[i-1][j], max_avg[i][j-1]) + cost[i][j] / (i + j + 1)

    return max_avg[n - 1][n - 1]

# Test cases




def check(candidate):
    assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
    assert maxAverageOfPath([[2, 3, 4], [7, 6, 5], [8, 4, 10]]) == 6.2
    assert maxAverageOfPath([[3, 4, 5], [8, 7, 6], [9, 5, 11]]) == 7.2
    assert maxAverageOfPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 5.8

check(maxAverageOfPath)