def tuple_str_int(test_str):
    test_str = test_str.replace('(', '').replace(')', '')  # Remove parentheses
    int_list = [int(x) for x in test_str.split(',')]  # Convert string to list of integers
    return tuple(int_list)  # Convert list to tuple and return

# Test cases




def check(candidate):
    assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
    assert tuple_str_int("(1, 2, 3)") == (1, 2, 3)
    assert tuple_str_int("(4, 5, 6)") == (4, 5, 6)
    assert tuple_str_int("(7, 81, 19)") == (7, 81, 19)

check(tuple_str_int)