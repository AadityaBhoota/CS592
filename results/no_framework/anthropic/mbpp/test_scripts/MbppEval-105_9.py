def count(lst):
    """
    Write a python function to count true booleans in the given list.

    Examples:
    count([True,False,True]) == 2
    count([False,False]) == 0
    count([True,True,True]) == 3
    """
    return sum(1 for item in lst if item)

def check(candidate):
    assert count([True,False,True]) == 2
    assert count([False,False]) == 0
    assert count([True,True,True]) == 3

check(count)