def count_first_elements(test_tup):
    """
    Write a function to find the number of elements that occurs before the tuple element in the given tuple.

    Examples:
    count_first_elements((1, 5, 7, (4, 6), 10)) == 3
    count_first_elements((2, 9, (5, 7), 11)) == 2
    count_first_elements((11, 15, 5, 8, (2, 3), 8)) == 4
    """
    for i, elem in enumerate(test_tup):
        if isinstance(elem, tuple):
            return i
    return len(test_tup)

def check(candidate):
    assert count_first_elements((1, 5, 7, (4, 6), 10) ) == 3
    assert count_first_elements((2, 9, (5, 7), 11) ) == 2
    assert count_first_elements((11, 15, 5, 8, (2, 3), 8) ) == 4

check(count_first_elements)