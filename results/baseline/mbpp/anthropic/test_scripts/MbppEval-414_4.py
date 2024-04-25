def overlapping(list1, list2):
    """
    Write a python function to check whether any value in a sequence exists in a sequence or not.

    Examples:
    overlapping([1,2,3,4,5],[6,7,8,9]) == False
    overlapping([1,2,3],[4,5,6]) == False
    overlapping([1,4,5],[1,4,5]) == True
    """
    for item in list1:
        if item in list2:
            return True
    for item in list2:
        if item in list1:
            return True
    return False

def check(candidate):
    assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
    assert overlapping([1,2,3],[4,5,6]) == False
    assert overlapping([1,4,5],[1,4,5]) == True

check(overlapping)