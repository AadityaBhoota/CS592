def find_equal_tuple(Input, length):
    all_lengths = [len(t) for t in Input]
    
    if all(length == l for l in all_lengths):
        return 'All tuples have same length'
    else:
        return 'All tuples do not have same length'

def check(candidate):
    assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
    assert get_equal([(1, 2, 3), (4, 5, 6, 7)]) == False
    assert get_equal([(1, 2), (3, 4)]) == True

check(find_equal_tuple)