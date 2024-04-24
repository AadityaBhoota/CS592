def tuple_str_int(test_str):
    # Remove the opening and closing parentheses
    test_str = test_str[1:-1]
    # Split the string by commas and convert each part to an integer
    parts = [int(part.strip()) for part in test_str.split(',')]
    # Create a tuple from the list of integers
    int_tuple = tuple(parts)
    return int_tuple

# Test the function with examples




def check(candidate):
    assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
    assert tuple_str_int("(1, 2, 3)") == (1, 2, 3)
    assert tuple_str_int("(4, 5, 6)") == (4, 5, 6)
    assert tuple_str_int("(7, 81, 19)") == (7, 81, 19)

check(tuple_str_int)