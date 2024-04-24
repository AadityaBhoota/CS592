def even_ele(test_tuple):
    def is_even(n):
        return n % 2 == 0

    if isinstance(test_tuple, tuple):
        return tuple(even_ele(t) for t in test_tuple if is_even(t) or isinstance(t, tuple))
    else:
        return test_tuple

# Test cases




def check(candidate):
    assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
    assert extract_even((5, 6, (8, 7, (4, 8)), 7, 9)) == (6, (8, (4, 8)))
    assert extract_even((5, 6, (9, 8, (4, 6)), 8, 10)) == (6, (8, (4, 6)), 8, 10)

check(even_ele)