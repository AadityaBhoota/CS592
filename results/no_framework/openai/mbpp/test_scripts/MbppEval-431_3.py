def common_element(list1, list2):
    return any(elem in list1 for elem in list2)

# Test cases




def check(candidate):
    assert common_element([1,2,3,4,5], [5,6,7,8,9])==True
    assert common_element([1,2,3,4,5], [6,7,8,9])==None
    assert common_element(['a','b','c'], ['d','b','e'])==True

check(common_element)