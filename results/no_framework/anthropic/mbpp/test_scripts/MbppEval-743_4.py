def rotate_right(lst, m, n):
    """
    Rotates the given list `lst` by `m` elements to the right direction.
    
    Args:
        lst (list): The list to be rotated.
        m (int): The number of elements to rotate the list by.
        n (int): The length of the list.
    
    Returns:
        list: The rotated list.
    """
    return lst[n-m:] + lst[:n-m]

def check(candidate):
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2)==[9, 10, 1, 2, 3, 4, 5, 6, 7, 8]
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],5)==[6, 7, 8, 9, 10, 1, 2, 3, 4, 5]

check(rotate_right)