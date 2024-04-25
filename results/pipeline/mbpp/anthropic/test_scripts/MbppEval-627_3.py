def find_First_Missing(array, start=0, end=None):
    if not array:
        return 0
    
    if array[0] != 0:
        return 0
    
    if array[-1] == len(array) - 1:
        return len(array)
    
    if end is None:
        end = len(array) - 1
    
    while start <= end:
        middle = (start + end) // 2
        if array[middle] == middle + start:
            start = middle + 1
        else:
            end = middle - 1
    
    return start

def check(candidate):
    assert find_First_Missing([0,1,2,3]) == 4
    assert find_First_Missing([0,1,2,6,9]) == 3
    assert find_First_Missing([2,3,5,8,9]) == 0

check(find_First_Missing)