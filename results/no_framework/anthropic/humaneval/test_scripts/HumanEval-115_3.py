def max_fill(grid, capacity):
    """
    Finds the minimum number of times the buckets need to be lowered to empty the wells.

    Args:
        grid (List[List[int]]): A rectangular grid of wells, where each 1 represents a unit of water.
        capacity (int): The capacity of the buckets.

    Returns:
        int: The minimum number of times the buckets need to be lowered to empty the wells.
    """
    rows, cols = len(grid), len(grid[0])
    total_water = sum(sum(row) for row in grid)
    if total_water % capacity != 0:
        return -1  # It's impossible to empty all the wells

    num_buckets = math.ceil(total_water / capacity)
    result = 0

    for col in range(cols):
        water_in_column = sum(row[col] for row in grid)
        result += math.ceil(water_in_column / capacity)

    return result

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