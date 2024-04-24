def min_val(listval):
    # Filter out non-integer values from the list
    int_values = [x for x in listval if isinstance(x, int)]
    
    # Find the minimum value from the remaining integers
    if len(int_values) > 0:
        min_value = min(int_values)
        return min_value
    else:
        return None

# Test cases




def check(candidate):
    assert min_val(['Python', 3, 2, 4, 5, 'version'])==2
    assert min_val(['Python', 15, 20, 25])==15
    assert min_val(['Python', 30, 20, 40, 50, 'version'])==20

check(min_val)