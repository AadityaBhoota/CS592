def check_type(test_tuple):
    data_types = set([type(item) for item in test_tuple])
    return len(data_types) == 1

# Test cases




def check(candidate):
    assert check_type((5, 6, 7, 3, 5, 6) ) == True
    assert check_type((1, 2, "4") ) == False
    assert check_type((3, 2, 1, 4, 5) ) == True

check(check_type)