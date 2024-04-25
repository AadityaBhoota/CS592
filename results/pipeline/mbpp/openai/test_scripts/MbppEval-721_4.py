def maxAverageOfPath(cost):
    n = len(cost)
    if n == 0:
        return 0
    
    cumulative_cost = [[0 for _ in range(n)] for _ in range(n)]
    cumulative_cost[0][0] = cost[0][0]
    
    for i in range(1, n):
        cumulative_cost[i][0] = cumulative_cost[i-1][0] + cost[i][0]
    
    for j in range(1, n):
        cumulative_cost[0][j] = cumulative_cost[0][j-1] + cost[0][j]
    
    for i in range(1, n):
        for j in range(1, n):
            cumulative_cost[i][j] = cost[i][j] + min(cumulative_cost[i-1][j], cumulative_cost[i][j-1])
    
    num_cells_visited = [[0 for _ in range(n)] for _ in range(n)]
    num_cells_visited[0][0] = 1
    
    for i in range(1, n):
        num_cells_visited[i][0] = 1
    
    for j in range(1, n):
        num_cells_visited[0][j] = 1
    
    for i in range(1, n):
        for j in range(1, n):
            num_cells_visited[i][j] = num_cells_visited[i-1][j] + num_cells_visited[i][j-1]
    
    max_average = cumulative_cost[n-1][n-1] / num_cells_visited[n-1][n-1]
    
    return max_average

def check(candidate):
    assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
    assert maxAverageOfPath([[2, 3, 4], [7, 6, 5], [8, 4, 10]]) == 6.2
    assert maxAverageOfPath([[3, 4, 5], [8, 7, 6], [9, 5, 11]]) == 7.2
    assert maxAverageOfPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 5.8

check(maxAverageOfPath)