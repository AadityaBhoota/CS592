def add_tuple(test_list, test_tup):
    if not isinstance(test_list, list) or not isinstance(test_tup, tuple):
        raise TypeError("The first argument should be a list and the second argument should be a tuple.")

    tuple_list = list(test_tup)
    test_list.extend(tuple_list)
    return test_list

def check(candidate):
    assert add_tuple([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]
    assert add_tuple([6, 7, 8], (10, 11)) == [6, 7, 8, 10, 11]
    assert add_tuple([7, 8, 9], (11, 12)) == [7, 8, 9, 11, 12]

check(add_tuple)