def even_ele(test_tuple, even_fnc):
    def extract_even(element):
        if isinstance(element, tuple):
            return tuple(extract_even(e) for e in element)
        elif even_fnc(element):
            return element

    return extract_even(test_tuple)

def check(candidate):
    assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
    assert extract_even((5, 6, (8, 7, (4, 8)), 7, 9)) == (6, (8, (4, 8)))
    assert extract_even((5, 6, (9, 8, (4, 6)), 8, 10)) == (6, (8, (4, 6)), 8, 10)

check(even_ele)