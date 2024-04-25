def check_none(test_tup):
    for item in test_tup:
        if item is None:
            return True
    return False

# Testing the function with the examples provided



def check(candidate):
    assert check_none((10, 4, 5, 6, None)) == True
    assert check_none((7, 8, 9, 11, 14)) == False
    assert check_none((1, 2, 3, 4, None)) == True

check(check_none)