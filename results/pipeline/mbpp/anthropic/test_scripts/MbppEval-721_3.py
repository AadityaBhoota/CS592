def maxAverageOfPath(cost):
    n = len(cost)
    total_cost = [[0] * n for _ in range(n)]
    num_cells = [[0] * n for _ in range(n)]
    
    # Initialize the first row and first column
    total_cost[0][0] = cost[0][0]
    num_cells[0][0] = 1
    for i in range(1, n):
        total_cost[0][i] = total_cost[0][i-1] + cost[0][i]
        num_cells[0][i] = num_cells[0][i-1] + 1
        total_cost[i][0] = total_cost[i-1][0] + cost[i][0]
        num_cells[i][0] = num_cells[i-1][0] + 1
    
    # Fill the rest of the matrix
    for i in range(1, n):
        for j in range(1, n):
            total_cost[i][j] = max(total_cost[i-1][j], total_cost[i][j-1]) + cost[i][j]
            num_cells[i][j] = max(num_cells[i-1][j], num_cells[i][j-1]) + 1
    
    # Find the maximum average
    max_average = 0
    for i in range(n):
        max_average = max(max_average, total_cost[n-1][i] / num_cells[n-1][i])
    
    return max_average

def check(candidate):
    assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
    assert maxAverageOfPath([[2, 3, 4], [7, 6, 5], [8, 4, 10]]) == 6.2
    assert maxAverageOfPath([[3, 4, 5], [8, 7, 6], [9, 5, 11]]) == 7.2
    assert maxAverageOfPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 5.8

check(maxAverageOfPath)