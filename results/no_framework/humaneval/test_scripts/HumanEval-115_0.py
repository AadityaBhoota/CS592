def max_fill(grid, capacity):
    total_water = 0
    for row in grid:
        total_water += sum(row)
    return math.ceil(total_water / capacity)

# Example 1
grid1 = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
bucket_capacity1 = 1
output1 = max_fill(grid1, bucket_capacity1)


# Example 2
grid2 = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
bucket_capacity2 = 2
output2 = max_fill(grid2, bucket_capacity2)


# Example 3
grid3 = [[0,0,0], [0,0,0]]
bucket_capacity3 = 5
output3 = max_fill(grid3, bucket_capacity3)



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