def remove_nested(test_tup):
    non_nested_elements = []
    for element in test_tup:
        if not isinstance(element, tuple):
            non_nested_elements.append(element)
    return tuple(non_nested_elements)

def check(candidate):
    assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)
    assert remove_nested((2, 6, 8, (5, 7), 11)) == (2, 6, 8, 11)
    assert remove_nested((3, 7, 9, (6, 8), 12)) == (3, 7, 9, 12)
    assert remove_nested((3, 7, 9, (6, 8), (5,12), 12)) == (3, 7, 9, 12)

check(remove_nested)