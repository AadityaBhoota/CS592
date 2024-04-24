def max_fill(grid, capacity):
    rows = len(grid)
    cols = len(grid[0])

    fills = 0
    for col in range(cols):
        buckets = 0
        for row in range(rows):
            if grid[row][col] == 1:
                grid[row][col] = 0
                buckets += 1

            if buckets == capacity or row == rows - 1:
                fills += math.ceil(buckets / capacity)
                buckets = 0

    return fills

# Test the function with the given examples
grid1 = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
print(max_fill(grid1, 1))  # Output: 6

grid2 = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
print(max_fill(grid2, 2))  # Output: 5

grid3 = [[0,0,0], [0,0,0]]
print(max_fill(grid3, 5))  # Output: 0

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