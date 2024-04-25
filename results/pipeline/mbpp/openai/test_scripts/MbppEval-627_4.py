def find_First_Missing(array, start=0, end=None):
    if end is None:
        end = len(array)
    
    # Ensure start and end are within bounds
    start = max(start, 0)
    end = min(end, len(array)
    
    # Find the smallest missing number
    for i in range(start, end):
        if array[i] != i:
            return i

    return end

def check(candidate):
    assert find_First_Missing([0,1,2,3]) == 4
    assert find_First_Missing([0,1,2,6,9]) == 3
    assert find_First_Missing([2,3,5,8,9]) == 0

check(find_First_Missing)