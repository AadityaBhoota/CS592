def overlapping(list1, list2):
    '''
    Check whether any value in list1 exists in list2 or not.
    
    Returns:
    True if there is an overlapping value, False otherwise.
    '''
    for item in list1:
        if item in list2:
            return True
    return False

# Examples




def check(candidate):
    assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
    assert overlapping([1,2,3],[4,5,6]) == False
    assert overlapping([1,4,5],[1,4,5]) == True

check(overlapping)