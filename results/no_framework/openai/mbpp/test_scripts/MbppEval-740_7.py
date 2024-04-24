def tuple_to_dict(test_tup):
    return dict(zip(test_tup[::2], test_tup[1::2]))

# Test cases




def check(candidate):
    assert tuple_to_dict((1, 5, 7, 10, 13, 5)) == {1: 5, 7: 10, 13: 5}
    assert tuple_to_dict((1, 2, 3, 4, 5, 6)) == {1: 2, 3: 4, 5: 6}
    assert tuple_to_dict((7, 8, 9, 10, 11, 12)) == {7: 8, 9: 10, 11: 12}

check(tuple_to_dict)