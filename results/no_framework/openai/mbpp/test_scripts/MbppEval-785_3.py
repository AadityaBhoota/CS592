def tuple_str_int(test_str):
    # Remove the parentheses and split the string into a list of integers
    ints = [int(num) for num in test_str.strip('()').split(',')]
    
    # Convert the list of integers to a tuple
    int_tuple = tuple(ints)
    
    return int_tuple

def check(candidate):
    assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
    assert tuple_str_int("(1, 2, 3)") == (1, 2, 3)
    assert tuple_str_int("(4, 5, 6)") == (4, 5, 6)
    assert tuple_str_int("(7, 81, 19)") == (7, 81, 19)

check(tuple_str_int)