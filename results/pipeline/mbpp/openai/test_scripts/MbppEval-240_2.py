def replace_list(list1, list2):
    new_list = list(list1)  # Create a new list by copying all elements from list1
    if len(new_list) > 0:
        new_list[-1:] = list2  # Replace the last element of new_list with elements from list2
    return new_list

def check(candidate):
    assert replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8])==[1, 3, 5, 7, 9, 2, 4, 6, 8]
    assert replace_list([1,2,3,4,5],[5,6,7,8])==[1,2,3,4,5,6,7,8]
    assert replace_list(["red","blue","green"],["yellow"])==["red","blue","yellow"]

check(replace_list)