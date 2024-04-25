def rotate_right(lst, n, m):
    rotated = lst[-m % len(lst):] + lst[:-m % len(lst)]
    return rotated

# Examples




def check(candidate):
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2)==[9, 10, 1, 2, 3, 4, 5, 6, 7, 8]
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],5)==[6, 7, 8, 9, 10, 1, 2, 3, 4, 5]

check(rotate_right)