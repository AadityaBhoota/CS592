def count_X(tup, x):
    """
    Write a python function that takes in a tuple and an element and counts the occurrences of the element in the tuple.

    Examples:
    count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 4) == 0
    count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 10) == 3
    count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 8) == 4
    """
    return tup.count(x)

def check(candidate):
    assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4) == 0
    assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),10) == 3
    assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),8) == 4

check(count_X)