def unique_Element(arr):
    """
    Write a python function to check whether a list of numbers contains only one distinct element or not.

    Examples:
    unique_Element([1,1,1],3) == 'YES'
    unique_Element([1,2,1,2],4) == 'NO'
    unique_Element([1,2,3,4,5],5) == 'NO'
    """
    if len(set(arr)) == 1:
        return 'YES'
    else:
        return 'NO'

def check(candidate):
    assert unique_Element([1,1,1]) == True
    assert unique_Element([1,2,1,2]) == False
    assert unique_Element([1,2,3,4,5]) == False

check(unique_Element)