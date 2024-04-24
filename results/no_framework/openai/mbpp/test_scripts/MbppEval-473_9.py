def tuple_intersection(test_list1, test_list2):
    set1 = set(tuple(sorted(x)) for x in test_list1)
    set2 = set(tuple(sorted(x)) for x in test_list2)
    intersection = set1.intersection(set2)
    return set(tuple(sorted(x)) for x in intersection)

# Test cases




def check(candidate):
    assert tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)] , [(5, 4), (3, 4), (6, 5), (9, 11)]) == {(4, 5), (3, 4), (5, 6)}
    assert tuple_intersection([(4, 1), (7, 4), (11, 13), (17, 14)] , [(1, 4), (7, 4), (16, 12), (10, 13)]) == {(4, 7), (1, 4)}
    assert tuple_intersection([(2, 1), (3, 2), (1, 3), (1, 4)] , [(11, 2), (2, 3), (6, 2), (1, 3)]) == {(1, 3), (2, 3)}

check(tuple_intersection)