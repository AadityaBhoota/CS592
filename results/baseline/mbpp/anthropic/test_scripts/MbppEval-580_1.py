def even_ele(test_tuple, even_fnc=lambda x: x % 2 == 0):
    """
    Write a function to remove uneven elements in the nested mixed tuple.

    Args:
        test_tuple (tuple): The input tuple containing even and odd elements.
        even_fnc (callable, optional): A function that takes an element and returns True if the element is even, False otherwise. Defaults to a lambda function that checks if the element is divisible by 2.

    Returns:
        tuple: A new tuple containing only the even elements from the input tuple.
    """
    result = ()
    for element in test_tuple:
        if isinstance(element, tuple):
            result += (even_ele(element, even_fnc),)
        elif even_fnc(element):
            result += (element,)
    return result

def check(candidate):
    assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
    assert extract_even((5, 6, (8, 7, (4, 8)), 7, 9)) == (6, (8, (4, 8)))
    assert extract_even((5, 6, (9, 8, (4, 6)), 8, 10)) == (6, (8, (4, 6)), 8, 10)

check(even_ele)