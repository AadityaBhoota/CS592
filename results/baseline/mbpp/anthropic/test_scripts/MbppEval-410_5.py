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

    # Iterate through the list
    for item in listval:
        # Check if the item is a number
        if isinstance(item, (int, float)):
            # Update the minimum value if the current item is smaller
            min_value = min(min_value, item)

    # If no numbers were found, return None
    if min_value == float('inf'):
        return None

    return min_value

def check(candidate):
    assert min_val(['Python', 3, 2, 4, 5, 'version'])==2
    assert min_val(['Python', 15, 20, 25])==15
    assert min_val(['Python', 30, 20, 40, 50, 'version'])==20

check(min_val)