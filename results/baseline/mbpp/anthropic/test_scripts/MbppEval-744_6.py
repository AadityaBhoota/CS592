def check_none(test_tup):
    """
    Write a function to check if the given tuple has any None value or not.

    Examples:
    check_none((10, 4, 5, 6, None)) == True
    check_none((7, 8, 9, 11, 14)) == False
    check_none((1, 2, 3, 4, None)) == True
    """
    return any(value is None for value in test_tup)

def check(candidate):
    assert check_none((10, 4, 5, 6, None)) == True
    assert check_none((7, 8, 9, 11, 14)) == False
    assert check_none((1, 2, 3, 4, None)) == True

check(check_none)