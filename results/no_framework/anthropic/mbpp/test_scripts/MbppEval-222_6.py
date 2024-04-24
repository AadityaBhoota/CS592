def check_type(test_tuple):
    """
    Write a function to check if all the elements in tuple have same data type or not.

    Examples:
    check_type((5, 6, 7, 3, 5, 6)) == True
    check_type((1, 2, "4")) == False
    check_type((3, 2, 1, 4, 5)) == True
    """
    if len(test_tuple) == 0:
        return True

    first_type = type(test_tuple[0])
    for element in test_tuple:
        if type(element) != first_type:
            return False
    return True

def check(candidate):
    assert check_type((5, 6, 7, 3, 5, 6) ) == True
    assert check_type((1, 2, "4") ) == False
    assert check_type((3, 2, 1, 4, 5) ) == True

check(check_type)