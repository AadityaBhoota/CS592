def min_val(listval):
    # Filter out non-integer values from the list
    int_values = [val for val in listval if isinstance(val, int)]
    
    # Find the minimum value in the list of integers
    if int_values:
        return min(int_values)
    else:
        return None

# Test cases




def check(candidate):
    assert min_val(['Python', 3, 2, 4, 5, 'version'])==2
    assert min_val(['Python', 15, 20, 25])==15
    assert min_val(['Python', 30, 20, 40, 50, 'version'])==20

check(min_val)