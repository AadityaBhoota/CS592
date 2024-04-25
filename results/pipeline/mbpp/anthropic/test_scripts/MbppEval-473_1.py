def tuple_intersection(test_list1, test_list2):
    intersection_set = set()

    for tup in test_list1:
        reversed_tup = (tup[1], tup[0])
        if tup in test_list2 or reversed_tup in test_list2:
            intersection_set.add(tup)

    for tup in test_list2:
        reversed_tup = (tup[1], tup[0])
        if tup in test_list1 or reversed_tup in test_list1:
            intersection_set.add(tup)

    return intersection_set

def check(candidate):
    assert tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)] , [(5, 4), (3, 4), (6, 5), (9, 11)]) == {(4, 5), (3, 4), (5, 6)}
    assert tuple_intersection([(4, 1), (7, 4), (11, 13), (17, 14)] , [(1, 4), (7, 4), (16, 12), (10, 13)]) == {(4, 7), (1, 4)}
    assert tuple_intersection([(2, 1), (3, 2), (1, 3), (1, 4)] , [(11, 2), (2, 3), (6, 2), (1, 3)]) == {(1, 3), (2, 3)}

check(tuple_intersection)