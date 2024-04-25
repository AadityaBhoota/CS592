def common_element(list1, list2):
    has_common = False
    for element in list1:
        if element in list2:
            has_common = True
            break
    return has_common

def check(candidate):
    assert common_element([1,2,3,4,5], [5,6,7,8,9])==True
    assert common_element([1,2,3,4,5], [6,7,8,9])==None
    assert common_element(['a','b','c'], ['d','b','e'])==True

check(common_element)