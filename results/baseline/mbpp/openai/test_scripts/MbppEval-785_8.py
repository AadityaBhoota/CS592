def tuple_str_int(test_str):
    # Removing the parentheses and splitting the string by commas
    values = test_str[1:-1].split(',')
    
    # Converting each value to integer and creating a tuple
    int_tuple = tuple(int(val.strip()) for val in values)
    
    return int_tuple

# Test cases




def check(candidate):
    assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
    assert tuple_str_int("(1, 2, 3)") == (1, 2, 3)
    assert tuple_str_int("(4, 5, 6)") == (4, 5, 6)
    assert tuple_str_int("(7, 81, 19)") == (7, 81, 19)

check(tuple_str_int)