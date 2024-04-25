def rotate_right(lst, m, k):
    """
    Rotates a list to the right by m positions, k times.

    Args:
        lst (list): The input list to be rotated.
        m (int): The number of positions to rotate the list to the right.
        k (int): The number of times the rotation should be performed.

    Returns:
        list: The rotated list.
    """
    for _ in range(k):
        lst = lst[-m:] + lst[:-m]
    return lst

def check(candidate):
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2)==[9, 10, 1, 2, 3, 4, 5, 6, 7, 8]
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],5)==[6, 7, 8, 9, 10, 1, 2, 3, 4, 5]

check(rotate_right)