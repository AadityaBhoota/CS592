def find_First_Missing(array, start=0, end=None):
    if end is None:
        end = len(array)
    
    for index in range(end):
        expected_value = start + index
        if array[index] != expected_value:
            return expected_value
        
    return 0

def check(candidate):
    assert find_First_Missing([0,1,2,3]) == 4
    assert find_First_Missing([0,1,2,6,9]) == 3
    assert find_First_Missing([2,3,5,8,9]) == 0

check(find_First_Missing)