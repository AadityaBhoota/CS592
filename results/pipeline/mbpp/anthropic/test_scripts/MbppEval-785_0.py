def tuple_str_int(test_str):
    """
    Write a function to convert tuple string to integer tuple.

    Examples:
    tuple_str_int("(7, 8, 9)") == (7, 8, 9)
    tuple_str_int("(1, 2, 3)") == (1, 2, 3)
    tuple_str_int("(4, 5, 6)") == (4, 5, 6)
    """
    if not test_str or not test_str.startswith("(") or not test_str.endswith(")"):
        raise ValueError("Invalid input string format")

    stripped_str = test_str.strip("()")
    elements = [int(elem.strip()) for elem in stripped_str.split(",")]
    return tuple(elements)

def check(candidate):
    assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
    assert tuple_str_int("(1, 2, 3)") == (1, 2, 3)
    assert tuple_str_int("(4, 5, 6)") == (4, 5, 6)
    assert tuple_str_int("(7, 81, 19)") == (7, 81, 19)

check(tuple_str_int)