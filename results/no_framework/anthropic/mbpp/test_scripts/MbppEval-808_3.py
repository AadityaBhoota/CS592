def check_K(test_tup, K):
    """
    Write a function to check if the given tuple contains the value K or not.

    Examples:
    check_K((10, 4, 5, 6, 8), 6) == True
    check_K((1, 2, 3, 4, 5, 6), 7) == False
    check_K((7, 8, 9, 44, 11, 12), 11) == True
    """
    return K in test_tup

def check(candidate):
    assert check_K((10, 4, 5, 6, 8), 6) == True
    assert check_K((1, 2, 3, 4, 5, 6), 7) == False
    assert check_K((7, 8, 9, 44, 11, 12), 11) == True

check(check_K)