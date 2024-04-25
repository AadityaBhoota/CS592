def common_element(list1, list2):
    set_list1 = set(list1)
    
    for elem in list2:
        if elem in set_list1:
            return True
    
    return False

def check(candidate):
    assert common_element([1,2,3,4,5], [5,6,7,8,9])==True
    assert common_element([1,2,3,4,5], [6,7,8,9])==None
    assert common_element(['a','b','c'], ['d','b','e'])==True

check(common_element)