def overlapping(list1, list2):
    '''
    Check whether any value in list1 exists in list2 or not.
    
    Args:
    list1: First list of values
    list2: Second list of values
    
    Returns:
    bool: True if any value in list1 exists in list2, False otherwise
    '''
    for item in list1:
        if item in list2:
            return True
    return False

# Test cases




def check(candidate):
    assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
    assert overlapping([1,2,3],[4,5,6]) == False
    assert overlapping([1,4,5],[1,4,5]) == True

check(overlapping)