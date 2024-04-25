def check_distinct(test_tup):
    """
    Write a function to check if given tuple contains no duplicates.

    Examples:
    check_distinct((1, 4, 5, 6, 1, 4)) == False
    check_distinct((1, 4, 5, 6)) == True
    check_distinct((2, 3, 4, 5, 6)) == True
    """
    return len(set(test_tup)) == len(test_tup)

def check(candidate):
    assert check_distinct((1, 4, 5, 6, 1, 4)) == False
    assert check_distinct((1, 4, 5, 6)) == True
    assert check_distinct((2, 3, 4, 5, 6)) == True

check(check_distinct)