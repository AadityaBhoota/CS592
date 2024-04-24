def max_fill(grid, capacity):
    m, n = len(grid), len(grid[0])
    total_water = sum(sum(row) for row in grid)
    if total_water == 0:
        return 0

    bucket_count = 0
    for j in range(n):
        for i in range(m):
            water_in_column = sum(row[j] for row in grid)
            if water_in_column <= capacity:
                bucket_count += math.ceil(water_in_column / capacity)
                for row in grid:
                    row[j] = 0
            else:
                while water_in_column > 0:
                    bucket_count += 1
                    water_in_column -= capacity
                    for k in range(m):
                        if grid[k][j] > 0:
                            grid[k][j] -= min(grid[k][j], capacity)

    return bucket_count

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