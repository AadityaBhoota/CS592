def max_fill(grid, capacity):
    rows = len(grid)
    cols = len(grid[0])
    total_water = sum(map(sum, grid))
    remaining_water = total_water
    steps = 0

    while remaining_water > 0:
        buckets_needed = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    buckets_needed += 1

        buckets_needed = math.ceil(buckets_needed / capacity)
        steps += buckets_needed
        remaining_water -= buckets_needed * capacity
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    grid[i][j] = 0

    return steps

# Example 1:
grid1 = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
capacity1 = 1


# Example 2:
grid2 = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
capacity2 = 2


# Example 3:
grid3 = [[0,0,0], [0,0,0]]
capacity3 = 5


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