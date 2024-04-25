def find_First_Missing(array, start=0, end=None):
    if end is None:
        end = len(array) - 1

    for i in range(start, end + 1):
        if array[i] != i:
            return i
    
    return end + 1

def check(candidate):
    assert find_First_Missing([0,1,2,3]) == 4
    assert find_First_Missing([0,1,2,6,9]) == 3
    assert find_First_Missing([2,3,5,8,9]) == 0

check(find_First_Missing)