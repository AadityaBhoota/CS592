def rotate_right(list, m):
    '''
    Write a function to rotate a given list by specified number of items to the right direction. 
    Examples:
    rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3,4) == [8, 9, 10, 1, 2, 3, 4, 5, 6]
    rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2,2) == [9, 10, 1, 2, 3, 4, 5, 6, 7, 8]
    rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],5,2) == [6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8]
    '''
return lst_copy

def check(candidate):
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2)==[9, 10, 1, 2, 3, 4, 5, 6, 7, 8]
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],5)==[6, 7, 8, 9, 10, 1, 2, 3, 4, 5]

check(rotate_right)