def min_val(listval):
    min_value = float('inf')
    for element in listval:
        if isinstance(element, (int, float)):
            min_value = min(min_value, element)
    return min_value

def check(candidate):
    assert min_val(['Python', 3, 2, 4, 5, 'version'])==2
    assert min_val(['Python', 15, 20, 25])==15
    assert min_val(['Python', 30, 20, 40, 50, 'version'])==20

check(min_val)