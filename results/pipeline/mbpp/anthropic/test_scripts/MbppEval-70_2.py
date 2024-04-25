def find_equal_tuple(Input):
    """
    Write a function to find whether all the given tuples have equal length or not.

    Examples:
    find_equal_tuple([(11, 22, 33), (44, 55, 66)]) == 'All tuples have same length'
    find_equal_tuple([(1, 2, 3), (4, 5, 6, 7)]) == 'All tuples do not have same length'
    find_equal_tuple([(1, 2), (3, 4)]) == 'All tuples have same length'
    find_equal_tuple([]) == 'Input should not be an empty list'
    """
    if not Input:
        return "Input should not be an empty list"

    reference_length = None
    for tup in Input:
        if reference_length is None:
            reference_length = len(tup)
        elif len(tup) != reference_length:
            return "All tuples do not have same length"

    return "All tuples have same length"

def check(candidate):
    assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
    assert get_equal([(1, 2, 3), (4, 5, 6, 7)]) == False
    assert get_equal([(1, 2), (3, 4)]) == True

check(find_equal_tuple)