def min_val(listval):
    """
    Write a function to find the minimum value in a given heterogeneous list.

    Examples:
    min_val(['Python', 3, 2, 4, 5, 'version']) == 2
    min_val(['Python', 15, 20, 25]) == 15
    min_val(['Python', 30, 20, 40, 50, 'version']) == 20
    """
    numbers = [num for num in listval if isinstance(num, (int, float))]
    if numbers:
        return min(numbers)
    else:
        return None

def check(candidate):
    assert min_val(['Python', 3, 2, 4, 5, 'version'])==2
    assert min_val(['Python', 15, 20, 25])==15
    assert min_val(['Python', 30, 20, 40, 50, 'version'])==20

check(min_val)