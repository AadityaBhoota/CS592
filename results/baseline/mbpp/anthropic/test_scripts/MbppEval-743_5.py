def rotate_right(lst, m, n):
    """
    Rotates a given list to the right by m positions, n times.
    
    Args:
        lst (list): The list to be rotated.
        m (int): The number of positions to rotate the list to the right.
        n (int): The number of times to perform the rotation.
    
    Returns:
        list: The rotated list.
    """
    for _ in range(n):
        lst = lst[-m:] + lst[:-m]
    return lst

def check(candidate):
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2)==[9, 10, 1, 2, 3, 4, 5, 6, 7, 8]
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],5)==[6, 7, 8, 9, 10, 1, 2, 3, 4, 5]

check(rotate_right)