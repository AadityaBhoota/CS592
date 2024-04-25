def maxAverageOfPath(cost):
    n = len(cost)
    avg_matrix = [[0]*n for _ in range(n)]
    
    # Calculate the average matrix
    avg_matrix[0][0] = cost[0][0]
    for i in range(1, n):
        avg_matrix[i][0] = avg_matrix[i-1][0] + cost[i][0]
        avg_matrix[0][i] = avg_matrix[0][i-1] + cost[0][i]
    
    for i in range(1, n):
        for j in range(1, n):
            avg_matrix[i][j] = cost[i][j] + max(avg_matrix[i-1][j], avg_matrix[i][j-1])
    
    return avg_matrix[n-1][n-1] / (2*n - 1)

# Test the function with the provided examples




def check(candidate):
    assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
    assert maxAverageOfPath([[2, 3, 4], [7, 6, 5], [8, 4, 10]]) == 6.2
    assert maxAverageOfPath([[3, 4, 5], [8, 7, 6], [9, 5, 11]]) == 7.2
    assert maxAverageOfPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 5.8

check(maxAverageOfPath)