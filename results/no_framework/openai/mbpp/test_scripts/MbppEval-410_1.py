def min_val(listval):
    # Filter out non-numeric values from the list
    num_list = [item for item in listval if isinstance(item, (int, float))]

    if num_list:
        return min(num_list)
    else:
        return None

# Test cases




def check(candidate):
    assert min_val(['Python', 3, 2, 4, 5, 'version'])==2
    assert min_val(['Python', 15, 20, 25])==15
    assert min_val(['Python', 30, 20, 40, 50, 'version'])==20

check(min_val)