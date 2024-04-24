def min_val(listval):
    """
    Write a function to find the minimum value in a given heterogeneous list.

    Examples:
    min_val(['Python', 3, 2, 4, 5, 'version']) == 2
    min_val(['Python', 15, 20, 25]) == 15
    min_val(['Python', 30, 20, 40, 50, 'version']) == 20
    """
    # Filter out non-numerical values
    numeric_list = [x for x in listval if isinstance(x, (int, float))]
    
    # If the list is empty or contains no numeric values, return None
    if not numeric_list:
        return None
    
    # Find the minimum value in the numeric list
    return min(numeric_list)

def check(candidate):
    assert min_val(['Python', 3, 2, 4, 5, 'version'])==2
    assert min_val(['Python', 15, 20, 25])==15
    assert min_val(['Python', 30, 20, 40, 50, 'version'])==20

check(min_val)