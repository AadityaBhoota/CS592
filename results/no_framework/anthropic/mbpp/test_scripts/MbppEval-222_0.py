def check_type(test_tuple):
    """
    Checks if all the elements in the given tuple have the same data type.

    Args:
        test_tuple (tuple): The tuple to be checked.

    Returns:
        bool: True if all elements have the same data type, False otherwise.
    """
    if len(test_tuple) == 0:
        return True

    data_type = type(test_tuple[0])
    for element in test_tuple:
        if type(element) != data_type:
            return False

    return True

def check(candidate):
    assert check_type((5, 6, 7, 3, 5, 6) ) == True
    assert check_type((1, 2, "4") ) == False
    assert check_type((3, 2, 1, 4, 5) ) == True

check(check_type)