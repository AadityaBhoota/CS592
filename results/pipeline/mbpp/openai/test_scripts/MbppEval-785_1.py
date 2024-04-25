def tuple_str_int(test_str):
    test_str = test_str[1:-1]  # Remove the leading and trailing parentheses
    num_strings = test_str.split(',')
    num_ints = [int(num) for num in num_strings]
    int_tuple = tuple(num_ints)
    return int_tuple

def check(candidate):
    assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
    assert tuple_str_int("(1, 2, 3)") == (1, 2, 3)
    assert tuple_str_int("(4, 5, 6)") == (4, 5, 6)
    assert tuple_str_int("(7, 81, 19)") == (7, 81, 19)

check(tuple_str_int)