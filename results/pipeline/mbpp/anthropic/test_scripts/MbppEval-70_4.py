def find_equal_tuple(Input):
    """
    Write a function to find whether all the given tuples have equal length or not.

    Examples:
    find_equal_tuple([(11, 22, 33), (44, 55, 66)], 3) == 'All tuples have same length'
    find_equal_tuple([(1, 2, 3), (4, 5, 6, 7)], 3) == 'All tuples do not have same length'
    find_equal_tuple([(1, 2), (3, 4)], 2) == 'All tuples have same length'
    """
    length_set = set()
    for tup in Input:
        length_set.add(len(tup))
    if len(length_set) == 1:
        return "All tuples have same length"
    else:
        return "All tuples do not have same length"

def check(candidate):
    assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
    assert get_equal([(1, 2, 3), (4, 5, 6, 7)]) == False
    assert get_equal([(1, 2), (3, 4)]) == True

check(find_equal_tuple)