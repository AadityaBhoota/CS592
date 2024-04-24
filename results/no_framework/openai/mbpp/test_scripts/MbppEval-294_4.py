def max_val(listval):
    # Filter out non-numeric values from the list
    num_list = [x for x in listval if isinstance(x, (int, float))]
    
    if num_list:
        return max(num_list)
    else:
        return None

# Test the function with the provided examples




def check(candidate):
    assert max_val(['Python', 3, 2, 4, 5, 'version'])==5
    assert max_val(['Python', 15, 20, 25])==25
    assert max_val(['Python', 30, 20, 40, 50, 'version'])==50

check(max_val)