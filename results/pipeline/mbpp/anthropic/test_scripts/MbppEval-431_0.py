def common_element(list1, list2):
    common_found = False
    for elem in list1:
        if elem in list2:
            common_found = True
            break
    return common_found

def check(candidate):
    assert common_element([1,2,3,4,5], [5,6,7,8,9])==True
    assert common_element([1,2,3,4,5], [6,7,8,9])==None
    assert common_element(['a','b','c'], ['d','b','e'])==True

check(common_element)