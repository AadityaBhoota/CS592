def check_type(test_tuple):
    if len(test_tuple) == 0:  # Check if the tuple is empty
        return True
    
    first_type = type(test_tuple[0])  # Get the data type of the first element in the tuple
    
    for item in test_tuple[1:]:  # Iterate through the elements starting from the second element
        if type(item) != first_type:  # Check if the data type of the element is not equal to the data type of the first element
            return False
    
    return True  # If all types match, return True

def check(candidate):
    assert check_type((5, 6, 7, 3, 5, 6) ) == True
    assert check_type((1, 2, "4") ) == False
    assert check_type((3, 2, 1, 4, 5) ) == True

check(check_type)