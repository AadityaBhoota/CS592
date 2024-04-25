def max_fill(grid, capacity):
    total_water = sum(sum(row) for row in grid)
    if total_water == 0:
        return 0

    rows, cols = len(grid), len(grid[0])
    buckets_needed = 0

    for col in range(cols):
        water_in_col = sum(row[col] for row in grid)
        buckets_needed += math.ceil(water_in_col / capacity)

    return buckets_needed

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