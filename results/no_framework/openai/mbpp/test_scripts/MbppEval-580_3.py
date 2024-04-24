def even_ele(test_tuple):
    result = []
    for item in test_tuple:
        if isinstance(item, tuple):
            nested = even_ele(item)
            if nested:
                result.append(nested)
        elif item % 2 == 0:
            result.append(item)
    return tuple(result)

# Testing the function with the provided examples




def check(candidate):
    assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
    assert extract_even((5, 6, (8, 7, (4, 8)), 7, 9)) == (6, (8, (4, 8)))
    assert extract_even((5, 6, (9, 8, (4, 6)), 8, 10)) == (6, (8, (4, 6)), 8, 10)

check(even_ele)