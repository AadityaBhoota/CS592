def tuple_str_int(test_str):
    """
    Write a function to convert tuple string to integer tuple.

    Examples:
    tuple_str_int("(7, 8, 9)") == (7, 8, 9)
    tuple_str_int("(1, 2, 3)") == (1, 2, 3)
    tuple_str_int("(4, 5, 6)") == (4, 5, 6)
    """
    tuple_str = test_str.strip("()")
    str_list = tuple_str.split(", ")
    int_list = [int(x) for x in str_list]
    return tuple(int_list)

def check(candidate):
    assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
    assert tuple_str_int("(1, 2, 3)") == (1, 2, 3)
    assert tuple_str_int("(4, 5, 6)") == (4, 5, 6)
    assert tuple_str_int("(7, 81, 19)") == (7, 81, 19)

check(tuple_str_int)