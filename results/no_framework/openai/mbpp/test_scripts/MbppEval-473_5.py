def tuple_intersection(test_list1, test_list2):
    # Convert each tuple in both lists to a set
    set1 = {frozenset(item) for item in test_list1}
    set2 = {frozenset(item) for item in test_list2}
    
    # Find the intersection of sets
    intersection = set1.intersection(set2)
    
    # Convert the sets back to tuples and return the result
    return {tuple(item) for item in intersection}

def check(candidate):
    assert tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)] , [(5, 4), (3, 4), (6, 5), (9, 11)]) == {(4, 5), (3, 4), (5, 6)}
    assert tuple_intersection([(4, 1), (7, 4), (11, 13), (17, 14)] , [(1, 4), (7, 4), (16, 12), (10, 13)]) == {(4, 7), (1, 4)}
    assert tuple_intersection([(2, 1), (3, 2), (1, 3), (1, 4)] , [(11, 2), (2, 3), (6, 2), (1, 3)]) == {(1, 3), (2, 3)}

check(tuple_intersection)