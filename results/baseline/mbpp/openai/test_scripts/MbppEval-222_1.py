def check_type(test_tuple):
    # Get the data type of the first element in the tuple
    elem_type = type(test_tuple[0])
    
    # Check if all elements in the tuple have the same data type as the first element
    for elem in test_tuple:
        if type(elem) != elem_type:
            return False
    return True

# Test cases




def check(candidate):
    assert check_type((5, 6, 7, 3, 5, 6) ) == True
    assert check_type((1, 2, "4") ) == False
    assert check_type((3, 2, 1, 4, 5) ) == True

check(check_type)