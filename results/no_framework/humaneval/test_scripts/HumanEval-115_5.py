def max_fill(grid, capacity):
    if not grid or not grid[0]:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    
    total_fill = 0
    
    for j in range(cols):
        for i in range(rows):
            row = rows - 1 - i
            if grid[row][j] == 1:
                fill = min(capacity, total_fill)
                total_fill -= fill
                grid[row][j] = 0
                total_fill += (capacity - fill)
    
    return total_fill

# Test the function with the provided examples
grid1 = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
capacity1 = 1
print(max_fill(grid1, capacity1))  # Output: 6

grid2 = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
capacity2 = 2
print(max_fill(grid2, capacity2))  # Output: 5

grid3 = [[0,0,0], [0,0,0]]
capacity3 = 5
print(max_fill(grid3, capacity3))  # Output: 0

def check(candidate):


    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1) == 6, "Error"
    assert candidate([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2) == 5, "Error"
    assert candidate([[0,0,0], [0,0,0]], 5) == 0, "Error"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate([[1,1,1,1], [1,1,1,1]], 2) == 4, "Error"
    assert candidate([[1,1,1,1], [1,1,1,1]], 9) == 2, "Error"


check(max_fill)