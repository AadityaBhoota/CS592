def max_val(listval):
    """
    Write a function to find the maximum value in a given heterogeneous list.

    Examples:
    max_val(['Python', 3, 2, 4, 5, 'version']) == 5
    max_val(['Python', 15, 20, 25]) == 25
    max_val(['Python', 30, 20, 40, 50, 'version']) == 50
    """
    max_value = float('-inf')
    for item in listval:
        if isinstance(item, (int, float)):
            max_value = max(max_value, item)
    return max_value

def check(candidate):
    assert max_val(['Python', 3, 2, 4, 5, 'version'])==5
    assert max_val(['Python', 15, 20, 25])==25
    assert max_val(['Python', 30, 20, 40, 50, 'version'])==50

check(max_val)