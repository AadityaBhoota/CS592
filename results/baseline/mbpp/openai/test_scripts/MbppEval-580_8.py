def even_ele(test_tuple, even_fnc): 
    if isinstance(test_tuple, tuple):
        return tuple(even_ele(elem, even_fnc) for elem in test_tuple if even_fnc(elem))
    else:
        return test_tuple % 2 == 0

# Test cases
test_tuple1 = (4, 5, (7, 6, (2, 4)), 6, 8)


test_tuple2 = (5, 6, (8, 7, (4, 8)), 7, 9)


test_tuple3 = (5, 6, (9, 8, (4, 6)), 8, 10)


def check(candidate):
    assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
    assert extract_even((5, 6, (8, 7, (4, 8)), 7, 9)) == (6, (8, (4, 8)))
    assert extract_even((5, 6, (9, 8, (4, 6)), 8, 10)) == (6, (8, (4, 6)), 8, 10)

check(even_ele)