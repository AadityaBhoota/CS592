def maxAverageOfPath(cost):
    n = len(cost)  # Size of the square matrix

    # Initialize a 2D array to store the maximum average up to cell [i][j]
    max_avg = [[0] * n for _ in range(n)]

    # Calculate the maximum average for the first row and first column
    max_avg[0][0] = cost[0][0]
    for i in range(1, n):
        max_avg[i][0] = (max_avg[i - 1][0] * i + cost[i][0]) / (i + 1)
        max_avg[0][i] = (max_avg[0][i - 1] * i + cost[0][i]) / (i + 1)

    # Fill the rest of the array
    for i in range(1, n):
        for j in range(1, n):
            max_avg[i][j] = max(max_avg[i - 1][j], max_avg[i][j - 1]) + cost[i][j]

    # Return the maximum average
    return max_avg[n - 1][n - 1] / (2 * n - 1)

# Test the function with the given examples




def check(candidate):
    assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
    assert maxAverageOfPath([[2, 3, 4], [7, 6, 5], [8, 4, 10]]) == 6.2
    assert maxAverageOfPath([[3, 4, 5], [8, 7, 6], [9, 5, 11]]) == 7.2
    assert maxAverageOfPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 5.8

check(maxAverageOfPath)