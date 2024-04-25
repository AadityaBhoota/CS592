def min_val(listval):
    for item in listval:
        if isinstance(item, int):
            min_value = item
            break
    else:
        return None
    
    for item in listval:
        if isinstance(item, int) and (min_value is None or item < min_value):
            min_value = item
    
    return min_value

def check(candidate):
    assert min_val(['Python', 3, 2, 4, 5, 'version'])==2
    assert min_val(['Python', 15, 20, 25])==15
    assert min_val(['Python', 30, 20, 40, 50, 'version'])==20

check(min_val)