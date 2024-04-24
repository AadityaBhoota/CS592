def min_val(listval):
    """
    Write a function to find the minimum value in a given heterogeneous list.

    Examples:
    min_val(['Python', 3, 2, 4, 5, 'version']) == 2
    min_val(['Python', 15, 20, 25]) == 15
    min_val(['Python', 30, 20, 40, 50, 'version']) == 20
    """
    # Initialize the minimum value to a large number
    min_value = float('inf')

    # Iterate through the list and update the minimum value
    for item in listval:
        if isinstance(item, (int, float)):
            min_value = min(min_value, item)

    # If the list contains no numeric values, return None
    return min_value if min_value != float('inf') else None

def check(candidate):
    assert min_val(['Python', 3, 2, 4, 5, 'version'])==2
    assert min_val(['Python', 15, 20, 25])==15
    assert min_val(['Python', 30, 20, 40, 50, 'version'])==20

check(min_val)