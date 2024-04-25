def rotate_right(arr, m, n):
    rotate_count = m
    slice_size = n
    
    rotated_arr = arr[-slice_size:] + arr[:-slice_size]
    
    while rotate_count > 0:
        rotated_arr = rotated_arr[-slice_size:] + rotated_arr[:-slice_size]
        rotate_count -= 1
    
    return rotated_arr

# Test cases




def check(candidate):
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2)==[9, 10, 1, 2, 3, 4, 5, 6, 7, 8]
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],5)==[6, 7, 8, 9, 10, 1, 2, 3, 4, 5]

check(rotate_right)