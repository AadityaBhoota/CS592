def min_val(listval):
    min_int = None
    for val in listval:
        if isinstance(val, int):
            if min_int is None or val < min_int:
                min_int = val
    return min_int

def check(candidate):
    assert min_val(['Python', 3, 2, 4, 5, 'version'])==2
    assert min_val(['Python', 15, 20, 25])==15
    assert min_val(['Python', 30, 20, 40, 50, 'version'])==20

check(min_val)