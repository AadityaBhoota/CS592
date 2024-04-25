def tuple_str_int(test_str):
    tuple_str = test_str[1:-1].split(',')
    int_tuple = tuple(int(num) for num in tuple_str)
    return int_tuple

# Test cases




def check(candidate):
    assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
    assert tuple_str_int("(1, 2, 3)") == (1, 2, 3)
    assert tuple_str_int("(4, 5, 6)") == (4, 5, 6)
    assert tuple_str_int("(7, 81, 19)") == (7, 81, 19)

check(tuple_str_int)