def tuple_str_int(test_str):
    str_nums = test_str.strip('()').split(',')
    int_nums = tuple(int(num) for num in str_nums)
    return int_nums

# Test the function with the provided examples




def check(candidate):
    assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
    assert tuple_str_int("(1, 2, 3)") == (1, 2, 3)
    assert tuple_str_int("(4, 5, 6)") == (4, 5, 6)
    assert tuple_str_int("(7, 81, 19)") == (7, 81, 19)

check(tuple_str_int)