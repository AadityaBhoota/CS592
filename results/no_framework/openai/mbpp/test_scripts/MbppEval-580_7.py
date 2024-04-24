def even_ele(test_tuple):
    if isinstance(test_tuple, tuple):
        return tuple(even_ele(element) for element in test_tuple if not isinstance(element, int) or element % 2 == 0)
    else:
        return test_tuple

# Test cases




def check(candidate):
    assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
    assert extract_even((5, 6, (8, 7, (4, 8)), 7, 9)) == (6, (8, (4, 8)))
    assert extract_even((5, 6, (9, 8, (4, 6)), 8, 10)) == (6, (8, (4, 6)), 8, 10)

check(even_ele)