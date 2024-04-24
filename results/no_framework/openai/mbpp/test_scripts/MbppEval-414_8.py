def overlapping(list1, list2):
    '''
    Check whether any value in one sequence exists in another sequence.

    Args:
    list1: First sequence.
    list2: Second sequence.

    Returns:
    True if there is an overlap, False otherwise.
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