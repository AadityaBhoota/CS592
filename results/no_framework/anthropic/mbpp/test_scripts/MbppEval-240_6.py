def replace_list(list1, list2):
    """
    Write a function that takes in two lists and replaces the last element of the first list with the elements of the second list.

    Examples:
    replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8]) == [1, 3, 5, 7, 9, 2, 4, 6, 8]
    replace_list([1,2,3,4,5],[5,6,7,8]) == [1,2,3,4,5,6,7,8]
    replace_list(["red","blue","green"],["yellow"]) == ["red","blue","yellow"]
    """
    # Get the last index of the first list
    last_index = len(list1) - 1

    # Replace the last element with the elements of the second list
    return list1[:last_index] + list2

def check(candidate):
    assert replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8])==[1, 3, 5, 7, 9, 2, 4, 6, 8]
    assert replace_list([1,2,3,4,5],[5,6,7,8])==[1,2,3,4,5,6,7,8]
    assert replace_list(["red","blue","green"],["yellow"])==["red","blue","yellow"]

check(replace_list)