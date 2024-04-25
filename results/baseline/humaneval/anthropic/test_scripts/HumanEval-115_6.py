def max_fill(grid, capacity):
    m, n = len(grid), len(grid[0])
    total_water = sum(sum(row) for row in grid)
    if total_water == 0:
        return 0

    # Iterate over each row and find the maximum number of buckets needed to empty the row
    max_buckets = 0
    for row in grid:
        water_in_row = sum(row)
        buckets_needed = math.ceil(water_in_row / capacity)
        max_buckets = max(max_buckets, buckets_needed)

    # Calculate the total number of times the buckets need to be lowered
    return max_buckets * m

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