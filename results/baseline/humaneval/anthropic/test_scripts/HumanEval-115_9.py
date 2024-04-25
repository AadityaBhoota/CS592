def max_fill(grid, capacity):
    total_water = sum(sum(row) for row in grid)
    if total_water == 0:
        return 0

    rows, cols = len(grid), len(grid[0])
    water_filled = 0
    bucket_drops = 0

    for col in range(cols):
        col_water = 0
        for row in range(rows):
            col_water += grid[row][col]
            if col_water >= capacity:
                bucket_drops += 1
                col_water -= capacity
        water_filled += col_water

    return bucket_drops + math.ceil((total_water - water_filled) / capacity)

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