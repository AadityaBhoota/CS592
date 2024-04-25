def find_equal_tuple(input_data):
    """
    Write a function to find whether all the given tuples have equal length or not.

    Args:
        input_data (list): A list of tuples.

    Returns:
        str: A message indicating whether all tuples have the same length or not.
    """
    if not input_data:
        return "Input list is empty."

    first_tuple_length = len(input_data[0])
    for tup in input_data:
        if len(tup) != first_tuple_length:
            return "All tuples do not have the same length."

    return "All tuples have the same length."

def check(candidate):
    assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
    assert get_equal([(1, 2, 3), (4, 5, 6, 7)]) == False
    assert get_equal([(1, 2), (3, 4)]) == True

check(find_equal_tuple)