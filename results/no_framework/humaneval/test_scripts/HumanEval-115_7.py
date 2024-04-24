def max_fill(grid, capacity):
    required_ops = 0

    for row in grid:
        bucket_count = 0
        for well in row:
            if well == 1:
                bucket_count += 1
                if bucket_count == capacity:
                    required_ops += 1
                    bucket_count = 0

        if bucket_count > 0:
            required_ops += 1

    return required_ops

# Test the function with the provided examples
grid1 = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
capacity1 = 1
print(max_fill(grid1, capacity1))  # Output: 6

grid2 = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
capacity2 = 2
print(max_fill(grid2, capacity2))  # Output: 5

grid3 = [[0,0,0], [0,0,0]]
capacity3 = 5
print(max_fill(grid3, capacity3))  # Output: 0

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