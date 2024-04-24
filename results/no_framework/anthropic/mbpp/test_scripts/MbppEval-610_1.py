def remove_kth_element(list1, k):
    """
    Remove the kth element from the given list.
    
    Args:
        list1 (list): The input list.
        k (int): The index of the element to be removed (0-based).
    
    Returns:
        list: The new list with the kth element removed.
    """
    if k < 0 or k >= len(list1):
        raise IndexError("Index out of range")
    
    return list1[:k] + list1[k+1:]

def check(candidate):
    assert remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]
    assert remove_kth_element([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4],4)==[0, 0, 1, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
    assert remove_kth_element([10, 10, 15, 19, 18, 18, 17, 26, 26, 17, 18, 10],5)==[10,10,15,19, 18, 17, 26, 26, 17, 18, 10]

check(remove_kth_element)