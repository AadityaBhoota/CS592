def even_ele(test_tuple, even_fnc):
    """
    Write a function to remove uneven elements in the nested mixed tuple.

    Examples:
    even_ele((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
    even_ele((5, 6, (8, 7, (4, 8)), 7, 9)) == (6, (8, (4, 8)))
    even_ele((5, 6, (9, 8, (4, 6)), 8, 10)) == (6, (8, (4, 6)), 8, 10)
    """
    result = []
    for elem in test_tuple:
        if isinstance(elem, tuple):
            even_tuple = even_fnc(elem)
            if even_tuple:
                result.append(even_tuple)
        elif even_fnc(elem):
            result.append(elem)
    return tuple(result)

def is_even(x):
    return x % 2 == 0

def test_even_ele():
    assert even_ele((4, 5, (7, 6, (2, 4)), 6, 8), is_even) == (4, (6, (2, 4)), 6, 8)
    assert even_ele((5, 6, (8, 7, (4, 8)), 7, 9), is_even) == (6, (8, (4, 8)))
    assert even_ele((5, 6, (9, 8, (4, 6)), 8, 10), is_even) == (6, (8, (4, 6)), 8, 10)

test_even_ele()

def check(candidate):
    assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
    assert extract_even((5, 6, (8, 7, (4, 8)), 7, 9)) == (6, (8, (4, 8)))
    assert extract_even((5, 6, (9, 8, (4, 6)), 8, 10)) == (6, (8, (4, 6)), 8, 10)

check(even_ele)