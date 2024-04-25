def even_ele(test_tuple, even_fnc): 
    even_elements = []
    for element in test_tuple:
        if isinstance(element, tuple):
            even_tuple = even_ele(element, even_fnc)
            if even_tuple:
                even_elements.append(even_tuple)
        else:
            if even_fnc(element):
                even_elements.append(element)
    return tuple(even_elements)

def check(candidate):
    assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
    assert extract_even((5, 6, (8, 7, (4, 8)), 7, 9)) == (6, (8, (4, 8)))
    assert extract_even((5, 6, (9, 8, (4, 6)), 8, 10)) == (6, (8, (4, 6)), 8, 10)

check(even_ele)