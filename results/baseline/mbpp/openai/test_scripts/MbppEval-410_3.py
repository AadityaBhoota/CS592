def min_val(listval):
    # Filter out non-numeric values from the list
    numeric_values = [val for val in listval if isinstance(val, (int, float))]

    # If there are no numeric values in the list, return None
    if not numeric_values:
        return None

    # Find the minimum value from the numeric values
    min_value = min(numeric_values)

    return min_value

# Examples




def check(candidate):
    assert min_val(['Python', 3, 2, 4, 5, 'version'])==2
    assert min_val(['Python', 15, 20, 25])==15
    assert min_val(['Python', 30, 20, 40, 50, 'version'])==20

check(min_val)