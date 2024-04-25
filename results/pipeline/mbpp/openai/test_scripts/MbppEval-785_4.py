def tuple_str_int(test_str):
    str_elements = test_str.replace('(', '').replace(')', '').split(',')
    int_elements = tuple(int(elem.strip()) for elem in str_elements)
    return int_elements

def check(candidate):
    assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
    assert tuple_str_int("(1, 2, 3)") == (1, 2, 3)
    assert tuple_str_int("(4, 5, 6)") == (4, 5, 6)
    assert tuple_str_int("(7, 81, 19)") == (7, 81, 19)

check(tuple_str_int)