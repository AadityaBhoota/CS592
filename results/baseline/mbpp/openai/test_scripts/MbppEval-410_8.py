def min_val(listval):
    numeric_vals = [val for val in listval if isinstance(val, (int, float))]
    if not numeric_vals:
        return None

    return min(numeric_vals)

# Test cases




def check(candidate):
    assert min_val(['Python', 3, 2, 4, 5, 'version'])==2
    assert min_val(['Python', 15, 20, 25])==15
    assert min_val(['Python', 30, 20, 40, 50, 'version'])==20

check(min_val)