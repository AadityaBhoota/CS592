def tuple_str_int(test_str):
    clean_str = test_str.replace("(", "").replace(")", "").replace(",", "")
    int_str_list = clean_str.split(',')
    int_list = [int(num) for num in int_str_list]
    int_tuple = tuple(int_list)
    
    return int_tuple

def check(candidate):
    assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
    assert tuple_str_int("(1, 2, 3)") == (1, 2, 3)
    assert tuple_str_int("(4, 5, 6)") == (4, 5, 6)
    assert tuple_str_int("(7, 81, 19)") == (7, 81, 19)

check(tuple_str_int)