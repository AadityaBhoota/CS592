def even_ele(test_tuple, even_fnc):
    result = []
    for item in test_tuple:
        if isinstance(item, tuple):
            nested_result = even_ele(item, even_fnc)
            if even_fnc(len(nested_result)):
                result.append(nested_result)
        else:
            if even_fnc(item):
                result.append(item)
    return tuple(result)

def check(candidate):
    assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
    assert extract_even((5, 6, (8, 7, (4, 8)), 7, 9)) == (6, (8, (4, 8)))
    assert extract_even((5, 6, (9, 8, (4, 6)), 8, 10)) == (6, (8, (4, 6)), 8, 10)

check(even_ele)