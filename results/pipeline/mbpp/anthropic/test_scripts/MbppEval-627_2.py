def find_First_Missing(array, start=0, array_length=None):
    '''
    Write a python function to find the smallest missing number from a sorted list of natural numbers.

    Examples:
    find_First_Missing([0,1,2,3],0,3) == 4
    find_First_Missing([0,1,2,6,9],0,4) == 3
    find_First_Missing([2,3,5,8,9],0,4) == 0
    '''
    
    # Check if the array is empty
    if not array:
        return 0
    
    # Check if the array starts with 0 and has length 1
    if array[0] == 0 and len(array) == 1:
        return 1
    
    # If array_length is not provided, set it to the length of the array
    if array_length is None:
        array_length = len(array)
    
    # Iterate through the array
    for i in range(start, array_length):
        if array[i] != i:
            return i
    
    # If no missing number is found, return the length of the array
    return array_length

def check(candidate):
    assert find_First_Missing([0,1,2,3]) == 4
    assert find_First_Missing([0,1,2,6,9]) == 3
    assert find_First_Missing([2,3,5,8,9]) == 0

check(find_First_Missing)