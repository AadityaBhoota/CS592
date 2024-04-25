def tuple_str_int(test_str):
    test_str = test_str.strip("()")
    str_elements = test_str.split(",")
    int_elements = [int(element.strip()) for element in str_elements]
    int_tuple = tuple(int_elements)
    return int_tuple

def check(candidate):
    assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
    assert tuple_str_int("(1, 2, 3)") == (1, 2, 3)
    assert tuple_str_int("(4, 5, 6)") == (4, 5, 6)
    assert tuple_str_int("(7, 81, 19)") == (7, 81, 19)

check(tuple_str_int)