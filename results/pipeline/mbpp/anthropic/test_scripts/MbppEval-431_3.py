def common_element(list1, list2):
    has_common_element = False
    for item in list1:
        if item in list2:
            has_common_element = True
            break
    return has_common_element

def check(candidate):
    assert common_element([1,2,3,4,5], [5,6,7,8,9])==True
    assert common_element([1,2,3,4,5], [6,7,8,9])==None
    assert common_element(['a','b','c'], ['d','b','e'])==True

check(common_element)