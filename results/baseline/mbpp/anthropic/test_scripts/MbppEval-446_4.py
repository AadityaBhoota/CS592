from collections import Counter

def count_Occurrence(tup, lst):
    """
    Write a python function to count the occurrence of all elements of list in a tuple.

    Examples:
    count_Occurrence(('a', 'a', 'c', 'b', 'd'), ['a', 'b']) == 3
    count_Occurrence((1, 2, 3, 1, 4, 6, 7, 1, 4), [1, 4, 7]) == 6
    count_Occurrence((1, 2, 3, 4, 5, 6), [1, 2]) == 2
    """
    count = 0
    for item in lst:
        count += tup.count(item)
    return count

def check(candidate):
    assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3
    assert count_Occurrence((1, 2, 3, 1, 4, 6, 7, 1, 4),[1, 4, 7]) == 6
    assert count_Occurrence((1,2,3,4,5,6),[1,2]) == 2

check(count_Occurrence)