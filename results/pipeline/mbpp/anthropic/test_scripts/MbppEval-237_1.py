from collections import Counter

def check_occurences(test_list):
    tuple_count = {}

    for tup in test_list:
        if tup in tuple_count:
            tuple_count[tup] += 1
        else:
            tuple_count[tup] = 1

    return tuple_count

def check(candidate):
    assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)] ) == {(1, 3): 2, (2, 5): 2, (3, 6): 1}
    assert check_occurences([(4, 2), (2, 4), (3, 6), (6, 3), (7, 4)] ) == {(2, 4): 2, (3, 6): 2, (4, 7): 1}
    assert check_occurences([(13, 2), (11, 23), (12, 25), (25, 12), (16, 23)] ) == {(2, 13): 1, (11, 23): 1, (12, 25): 2, (16, 23): 1}

check(check_occurences)