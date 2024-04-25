def find_equal_tuple(input_tuples):
    """
    Write a function to find whether all the given tuples have equal length or not.

    Examples:
    find_equal_tuple([(11, 22, 33), (44, 55, 66)], 3) == 'All tuples have same length'
    find_equal_tuple([(1, 2, 3), (4, 5, 6, 7)], 3) == 'All tuples do not have same length'
    find_equal_tuple([(1, 2), (3, 4)], 2) == 'All tuples have same length'
    """
    # Get the length of the first tuple
    first_length = len(input_tuples[0])

    # Check if all tuples have the same length
    for tuple_item in input_tuples:
        if len(tuple_item) != first_length:
            return 'All tuples do not have same length'

    return 'All tuples have same length'

def check(candidate):
    assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
    assert get_equal([(1, 2, 3), (4, 5, 6, 7)]) == False
    assert get_equal([(1, 2), (3, 4)]) == True

check(find_equal_tuple)