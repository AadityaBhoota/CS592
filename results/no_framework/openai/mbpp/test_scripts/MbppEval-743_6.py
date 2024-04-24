def rotate_right(lst, n, m):
    # Calculate the effective number of rotations
    rotations = n % len(lst)
    # Rotate the list to the right by the specified number of positions
    rotated_list = lst[-rotations:] + lst[:-rotations]
    # Repeat the rotation 'm' times
    for _ in range(m - 1):
        rotated_list = rotated_list[-rotations:] + rotated_list[:-rotations]
    return rotated_list

# Test cases




def check(candidate):
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2)==[9, 10, 1, 2, 3, 4, 5, 6, 7, 8]
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],5)==[6, 7, 8, 9, 10, 1, 2, 3, 4, 5]

check(rotate_right)