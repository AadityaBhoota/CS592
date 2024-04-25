def maxAverageOfPath(cost):
    n = len(cost)
    max_average = 0
    
    def generate_paths(i, j, path, total_cost):
        nonlocal max_average
        
        if i == n-1 and j == n-1:
            average_cost = total_cost / (len(path) + 1)
            max_average = max(max_average, average_cost)
            return
        
        if i < n-1:
            generate_paths(i+1, j, path + [(i+1, j)], total_cost + cost[i+1][j])
        
        if j < n-1:
            generate_paths(i, j+1, path + [(i, j+1)], total_cost + cost[i][j+1])
    
    generate_paths(0, 0, [(0, 0)], cost[0][0])
    return max_average

def check(candidate):
    assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
    assert maxAverageOfPath([[2, 3, 4], [7, 6, 5], [8, 4, 10]]) == 6.2
    assert maxAverageOfPath([[3, 4, 5], [8, 7, 6], [9, 5, 11]]) == 7.2
    assert maxAverageOfPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 5.8

check(maxAverageOfPath)