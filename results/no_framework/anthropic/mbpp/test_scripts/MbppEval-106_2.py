def add_lists(test_list, test_tup):
    '''
    Write a function to append the given list to the given tuples.

    Examples:
    add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)
    add_lists([6, 7, 8], (10, 11)) == (10, 11, 6, 7, 8)
    add_lists([7, 8, 9], (11, 12)) == (11, 12, 7, 8, 9)
    '''
    return test_tup + tuple(test_list)

def check(candidate):
    assert add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)
    assert add_lists([6, 7, 8], (10, 11)) == (10, 11, 6, 7, 8)
    assert add_lists([7, 8, 9], (11, 12)) == (11, 12, 7, 8, 9)

check(add_lists)