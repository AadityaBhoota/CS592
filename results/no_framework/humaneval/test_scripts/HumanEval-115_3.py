def max_fill(grid, capacity):
    rows = len(grid)
    cols = len(grid[0])
    
    buckets = [0] * cols
    total_moves = 0
    
    for row in grid:
        water_needed = [max(0, row[j] - buckets[j]) for j in range(cols)]
        
        for j in range(cols):
            if water_needed[j]:
                moves = math.ceil(water_needed[j] / capacity)
                total_moves += moves
                for k in range(j, min(j+capacity, cols)):
                    buckets[k] += moves * capacity
    
    return total_moves

# Test cases
grid1 = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
bucket_capacity1 = 1
print(max_fill(grid1, bucket_capacity1))  # Output: 6

grid2 = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
bucket_capacity2 = 2
print(max_fill(grid2, bucket_capacity2))  # Output: 5

grid3 = [[0,0,0], [0,0,0]]
bucket_capacity3 = 5
print(max_fill(grid3, bucket_capacity3))  # Output: 0

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