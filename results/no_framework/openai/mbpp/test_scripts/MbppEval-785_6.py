def tuple_str_int(test_str):
    # Remove parentheses and split the string by commas
    str_nums = test_str[1:-1].split(',')
    
    # Convert string numbers to integers
    int_nums = tuple(map(int, str_nums))
    
    return int_nums

# Test cases




def check(candidate):
    assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
    assert tuple_str_int("(1, 2, 3)") == (1, 2, 3)
    assert tuple_str_int("(4, 5, 6)") == (4, 5, 6)
    assert tuple_str_int("(7, 81, 19)") == (7, 81, 19)

check(tuple_str_int)