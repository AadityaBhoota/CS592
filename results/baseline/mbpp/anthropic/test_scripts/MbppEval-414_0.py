def overlapping(list1, list2):
    """
    Write a Python function to check whether any value in a sequence exists in a sequence or not.

    Examples:
    overlapping([1,2,3,4,5],[6,7,8,9]) == False
    overlapping([1,2,3],[4,5,6]) == False
    overlapping([1,4,5],[1,4,5]) == True
    """
    return any(item in list2 for item in list1)

def check(candidate):
    assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
    assert overlapping([1,2,3],[4,5,6]) == False
    assert overlapping([1,4,5],[1,4,5]) == True

check(overlapping)