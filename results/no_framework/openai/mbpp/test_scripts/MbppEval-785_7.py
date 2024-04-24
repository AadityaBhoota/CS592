def tuple_str_int(test_str):
    # Remove the parentheses at the beginning and end
    test_str = test_str.strip('()')

    # Split the string into individual elements
    elements = test_str.split(',')

    # Convert the elements to integers and create a tuple
    int_tuple = tuple(int(elem.strip()) for elem in elements)

    return int_tuple

# Test cases




def check(candidate):
    assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
    assert tuple_str_int("(1, 2, 3)") == (1, 2, 3)
    assert tuple_str_int("(4, 5, 6)") == (4, 5, 6)
    assert tuple_str_int("(7, 81, 19)") == (7, 81, 19)

check(tuple_str_int)