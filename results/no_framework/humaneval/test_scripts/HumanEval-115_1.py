def max_fill(grid, capacity):
    rows = len(grid)
    cols = len(grid[0])
    total_units = sum([sum(row) for row in grid])
    
    buckets_needed = math.ceil(total_units / capacity)
    
    return buckets_needed

# Test cases
print(max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1))  # Output: 6
print(max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2))  # Output: 5
print(max_fill([[0,0,0], [0,0,0]], 5))  # Output: 0

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