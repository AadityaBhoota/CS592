def find_equal_tuple(tuples_list, length):
    for tuple_elem in tuples_list:
        if len(tuple_elem) != length:
            return 'All tuples do not have same length'
    
    return 'All tuples have same length'

def check(candidate):
    assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
    assert get_equal([(1, 2, 3), (4, 5, 6, 7)]) == False
    assert get_equal([(1, 2), (3, 4)]) == True

check(find_equal_tuple)