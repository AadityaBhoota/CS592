def common_element(list1, list2):
    '''
    Write a function that takes two lists and returns True if they have at least one common element.

    Examples:
    common_element([1,2,3,4,5], [5,6,7,8,9]) == True
    common_element([1,2,3,4,5], [6,7,8,9]) == False
    common_element(['a','b','c'], ['d','b','e']) == True
    '''
    for item in list1:
        if item in list2:
            return True
    return False

def check(candidate):
    assert common_element([1,2,3,4,5], [5,6,7,8,9])==True
    assert common_element([1,2,3,4,5], [6,7,8,9])==None
    assert common_element(['a','b','c'], ['d','b','e'])==True

check(common_element)