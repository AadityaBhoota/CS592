def find_First_Missing(array,start=0,end=None):
    '''
    Write a python function to find the smallest missing number from a sorted list of natural numbers.

    Examples:
    find_First_Missing([0,1,2,3],0,3) == 4
    find_First_Missing([0,1,2,6,9],0,4) == 3
    find_First_Missing([2,3,5,8,9],0,4) == 0
    '''
def find_first_missing(array):
    """
    Find the smallest missing number from a sorted list of natural numbers.

    Examples:
    find_first_missing([0, 1, 2, 3]) == 4
    find_first_missing([0, 1, 2, 6, 9]) == 3
    find_first_missing([2, 3, 5, 8, 9]) == 0
    """
    array.sort()
    for i, num in enumerate(array):
        if num != i:
            return i
    return len(array)

def check(candidate):
    assert find_First_Missing([0,1,2,3]) == 4
    assert find_First_Missing([0,1,2,6,9]) == 3
    assert find_First_Missing([2,3,5,8,9]) == 0

check(find_First_Missing)