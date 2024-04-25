def add_tuple(test_list, test_tup):
    """
    Write a function to add the given tuple to the given list.

    Examples:
    add_tuple([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]
    add_tuple([6, 7, 8], (10, 11)) == [6, 7, 8, 10, 11]
    add_tuple([7, 8, 9], (11, 12)) == [7, 8, 9, 11, 12]
    """
    return test_list + list(test_tup)

def check(candidate):
    assert add_tuple([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]
    assert add_tuple([6, 7, 8], (10, 11)) == [6, 7, 8, 10, 11]
    assert add_tuple([7, 8, 9], (11, 12)) == [7, 8, 9, 11, 12]

check(add_tuple)