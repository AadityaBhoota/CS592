def even_ele(test_tuple, even_fnc=lambda x: x % 2 == 0):
    """
    Remove uneven elements from a nested mixed tuple.

    Args:
        test_tuple (tuple): The input tuple containing mixed elements.
        even_fnc (callable): A function that takes an element and returns True if the element is even, False otherwise.
                            Default is a lambda function that checks if an integer is even.

    Returns:
        tuple: A new tuple with only the even elements.
    """
    result = []
    for element in test_tuple:
        if isinstance(element, tuple):
            result.append(even_ele(element, even_fnc))
        elif even_fnc(element):
            result.append(element)
    return tuple(result)

def check(candidate):
    assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
    assert extract_even((5, 6, (8, 7, (4, 8)), 7, 9)) == (6, (8, (4, 8)))
    assert extract_even((5, 6, (9, 8, (4, 6)), 8, 10)) == (6, (8, (4, 6)), 8, 10)

check(even_ele)