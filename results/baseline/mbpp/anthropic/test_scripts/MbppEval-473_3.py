def tuple_intersection(test_list1, test_list2):
    """
    Find the tuple intersection of elements in the given tuple list irrespective of their order.

    Args:
        test_list1 (list): A list of tuples.
        test_list2 (list): Another list of tuples.

    Returns:
        set: A set of tuples representing the intersection of the two input lists.
    """
    # Convert the lists to sets of tuples
    set1 = set(tuple(sorted(t)) for t in test_list1)
    set2 = set(tuple(sorted(t)) for t in test_list2)

    # Find the intersection of the two sets
    intersection = set1.intersection(set2)

    return intersection

def check(candidate):
    assert tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)] , [(5, 4), (3, 4), (6, 5), (9, 11)]) == {(4, 5), (3, 4), (5, 6)}
    assert tuple_intersection([(4, 1), (7, 4), (11, 13), (17, 14)] , [(1, 4), (7, 4), (16, 12), (10, 13)]) == {(4, 7), (1, 4)}
    assert tuple_intersection([(2, 1), (3, 2), (1, 3), (1, 4)] , [(11, 2), (2, 3), (6, 2), (1, 3)]) == {(1, 3), (2, 3)}

check(tuple_intersection)