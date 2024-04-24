def tuple_str_int(test_str):
    # Remove the parentheses and split the string by commas
    tuple_str = test_str[1:-1].split(',')
    
    # Convert each element to an integer and create a tuple
    int_tuple = tuple(int(x) for x in tuple_str)
    
    return int_tuple

# Test cases




def check(candidate):
    assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
    assert tuple_str_int("(1, 2, 3)") == (1, 2, 3)
    assert tuple_str_int("(4, 5, 6)") == (4, 5, 6)
    assert tuple_str_int("(7, 81, 19)") == (7, 81, 19)

check(tuple_str_int)