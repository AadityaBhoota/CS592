def even_ele(test_tuple, even_fnc):
    result = ()
    
    if even_fnc(test_tuple):
        result = test_tuple
    elif isinstance(test_tuple, tuple):
        result = tuple([even_ele(elem, even_fnc) for elem in test_tuple if not even_fnc(elem)])
    
    return result

def check(candidate):
    assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
    assert extract_even((5, 6, (8, 7, (4, 8)), 7, 9)) == (6, (8, (4, 8)))
    assert extract_even((5, 6, (9, 8, (4, 6)), 8, 10)) == (6, (8, (4, 6)), 8, 10)

check(even_ele)