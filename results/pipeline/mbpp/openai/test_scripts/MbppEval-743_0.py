def rotate_right(lst, items, positions):
    effective_positions = positions % len(lst)
    rotated_elements = lst[-effective_positions - items : -effective_positions]
    rotated_elements = rotated_elements[-items:] + rotated_elements[:-items]
    
    final_rotated_list = lst[:-effective_positions - items] + rotated_elements + lst[-effective_positions:]
    
    return final_rotated_list

def check(candidate):
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2)==[9, 10, 1, 2, 3, 4, 5, 6, 7, 8]
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],5)==[6, 7, 8, 9, 10, 1, 2, 3, 4, 5]

check(rotate_right)