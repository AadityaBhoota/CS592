def tuple_str_int(test_str):
    # Remove the parentheses and split the string based on commas
    str_nums = test_str[1:-1].split(',')
    
    # Convert each string number to integer
    int_nums = [int(num) for num in str_nums]
    
    # Create integer tuple from the list
    int_tuple = tuple(int_nums)
    
    return int_tuple

# Test cases




def check(candidate):
    assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
    assert tuple_str_int("(1, 2, 3)") == (1, 2, 3)
    assert tuple_str_int("(4, 5, 6)") == (4, 5, 6)
    assert tuple_str_int("(7, 81, 19)") == (7, 81, 19)

check(tuple_str_int)