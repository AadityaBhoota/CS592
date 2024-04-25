def even_ele(test_tuple, even_fnc):
    if not test_tuple:
        return ()
    
    even_elements = []
    
    for elem in test_tuple:
        if isinstance(elem, tuple):
            even_elements.append(even_ele(elem, even_fnc))
        elif even_fnc(elem):
            even_elements.append(elem)
    
    return tuple(even_elements)

def check(candidate):
    assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
    assert extract_even((5, 6, (8, 7, (4, 8)), 7, 9)) == (6, (8, (4, 8)))
    assert extract_even((5, 6, (9, 8, (4, 6)), 8, 10)) == (6, (8, (4, 6)), 8, 10)

check(even_ele)