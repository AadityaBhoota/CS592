def max_fill(grid, capacity):
    water_needed = 0
    for row in grid:
        for well in row:
            water_needed += well
    return math.ceil(water_needed / capacity)

# Test cases
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