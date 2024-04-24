def max_fill(grid, capacity):
    m, n = len(grid), len(grid[0])
    total_water = sum(sum(row) for row in grid)
    if total_water == 0:
        return 0
    
    buckets_used = 0
    for j in range(n):
        water_collected = 0
        for i in range(m):
            water_collected += grid[i][j]
            if water_collected >= capacity or (i == m-1 and water_collected > 0):
                buckets_used += math.ceil(water_collected / capacity)
                water_collected = 0
    
    return buckets_used

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