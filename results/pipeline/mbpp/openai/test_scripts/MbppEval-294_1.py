def max_val(listval):
    max_value = None
    for val in listval:
        if isinstance(val, (int, float)):
            if max_value is None or val > max_value:
                max_value = val
    return max_value

def check(candidate):
    assert max_val(['Python', 3, 2, 4, 5, 'version'])==5
    assert max_val(['Python', 15, 20, 25])==25
    assert max_val(['Python', 30, 20, 40, 50, 'version'])==50

check(max_val)