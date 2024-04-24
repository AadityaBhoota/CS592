def even_ele(test_tuple, even_fnc):
    """
    Write a function to remove uneven elements in the nested mixed tuple.

    Args:
        test_tuple (tuple): The input tuple to be processed.
        even_fnc (callable): A function that takes an element and returns True if it is even, False otherwise.

    Returns:
        tuple: A new tuple with only the even elements from the input tuple.
    """
    # Base case: If the element is not a tuple, check if it's even using the even_fnc
    if not isinstance(test_tuple, tuple):
        return test_tuple if even_fnc(test_tuple) else None

    # Recursive case: Process each element in the tuple
    result = tuple(filter(lambda x: x is not None, (even_ele(element, even_fnc) for element in test_tuple)))
    return result

# Example usage




def check(candidate):
    assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
    assert extract_even((5, 6, (8, 7, (4, 8)), 7, 9)) == (6, (8, (4, 8)))
    assert extract_even((5, 6, (9, 8, (4, 6)), 8, 10)) == (6, (8, (4, 6)), 8, 10)

check(even_ele)