def replace_list(list1, list2):
    last_element_list1 = list1[-1]
    list1.pop()
    list1.extend(list2)
    return list1

def check(candidate):
    assert replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8])==[1, 3, 5, 7, 9, 2, 4, 6, 8]
    assert replace_list([1,2,3,4,5],[5,6,7,8])==[1,2,3,4,5,6,7,8]
    assert replace_list(["red","blue","green"],["yellow"])==["red","blue","yellow"]

check(replace_list)