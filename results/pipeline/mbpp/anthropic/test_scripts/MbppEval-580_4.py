def even_ele(test_tuple, even_fnc):
    def is_even(x):
        return even_fnc(x)

    new_tuple = ()
    for element in test_tuple:
        if isinstance(element, tuple):
            new_tuple += (even_ele(element, even_fnc),)
        elif is_even(element):
            new_tuple += (element,)
    return new_tuple

def check(candidate):
    assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
    assert extract_even((5, 6, (8, 7, (4, 8)), 7, 9)) == (6, (8, (4, 8)))
    assert extract_even((5, 6, (9, 8, (4, 6)), 8, 10)) == (6, (8, (4, 6)), 8, 10)

check(even_ele)