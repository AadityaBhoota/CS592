def remove_kth_element(list1, k):
    '''
    Write a python function which takes a list and returns a list with the same elements, but the k'th element removed.

    Examples:
    remove_kth_element([1,1,2,3,4,4,5,1],3) == [1, 1, 3, 4, 4, 5, 1]
    remove_kth_element([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4],4) == [0, 0, 1, 2, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
    remove_kth_element([10, 10, 15, 19, 18, 18, 17, 26, 26, 17, 18, 10],5) == [10,10,15,19, 18, 17, 26, 26, 17, 18, 10]
    '''
    # Check if the list is empty or the index is out of range
    if not list1 or k < 0 or k >= len(list1):
        return list1

    # Create a copy of the list
    result = list1[:]

    # Remove the k'th element
    del result[k]

    return result

def check(candidate):
    assert remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]
    assert remove_kth_element([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4],4)==[0, 0, 1, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
    assert remove_kth_element([10, 10, 15, 19, 18, 18, 17, 26, 26, 17, 18, 10],5)==[10,10,15,19, 18, 17, 26, 26, 17, 18, 10]

check(remove_kth_element)