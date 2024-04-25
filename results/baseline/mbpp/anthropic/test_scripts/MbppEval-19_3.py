def test_duplicate(arraynums):
    '''
    Write a function to find whether a given array of integers contains any duplicate element.

    Examples:
    test_duplicate(([1,2,3,4,5])) == False
    test_duplicate(([1,2,3,4, 4])) == True
    test_duplicate([1,1,2,2,3,3,4,4,5]) == True
    '''
    # Convert the array to a set to remove duplicates
    unique_set = set(arraynums)
    
    # If the length of the set is the same as the length of the original array,
    # it means there are no duplicates
    return len(unique_set) != len(arraynums)

def check(candidate):
    assert test_duplicate(([1,2,3,4,5]))==False
    assert test_duplicate(([1,2,3,4, 4]))==True
    assert test_duplicate([1,1,2,2,3,3,4,4,5])==True

check(test_duplicate)