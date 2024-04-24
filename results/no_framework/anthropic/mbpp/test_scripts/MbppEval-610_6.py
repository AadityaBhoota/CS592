def remove_kth_element(list1, k):
    """
    Write a python function which takes a list and returns a list with the same elements, but the k'th element removed.

    Examples:
    remove_kth_element([1,1,2,3,4,4,5,1],3) == [1, 1, 3, 4, 4, 5, 1]
    remove_kth_element([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4],4) == [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
    remove_kth_element([10, 10, 15, 19, 18, 18, 17, 26, 26, 17, 18, 10],5) == [10,10,15,19, 18, 17, 26, 26, 17, 18, 10]
    """
    return list1[:k] + list1[k+1:]

def check(candidate):
    assert remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]
    assert remove_kth_element([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4],4)==[0, 0, 1, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
    assert remove_kth_element([10, 10, 15, 19, 18, 18, 17, 26, 26, 17, 18, 10],5)==[10,10,15,19, 18, 17, 26, 26, 17, 18, 10]

check(remove_kth_element)