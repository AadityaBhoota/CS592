import math

def max_fill(grid, capacity):
    total_wells = len(grid)
    units_per_well = len(grid[0])
    
    total_times_fill_needed = 0
    
    for col in range(units_per_well):
        for row in range(total_wells):
            if grid[row][col] == 1:
                total_times_fill_needed += 1
    
    total_water_to_extract = total_times_fill_needed * capacity

    total_times_bucket_empty = math.ceil(total_water_to_extract / capacity)
    
    return total_times_bucket_empty

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