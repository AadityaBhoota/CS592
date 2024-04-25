def maximize_elements(test_tup1, test_tup2):
    maximized_tuples = []
    for t1, t2 in zip(test_tup1, test_tup2):
        maximized_tuples.append((max(t1[0], t2[0]), max(t1[1], t2[1])))
    return tuple(maximized_tuples)

def check(candidate):
    assert maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 7), (4, 9), (2, 9), (7, 10))
    assert maximize_elements(((2, 4), (5, 6), (3, 10), (2, 11)), ((7, 8), (4, 10), (2, 2), (8, 4))) == ((7, 8), (5, 10), (3, 10), (8, 11))
    assert maximize_elements(((3, 5), (6, 7), (4, 11), (3, 12)), ((8, 9), (5, 11), (3, 3), (9, 5))) == ((8, 9), (6, 11), (4, 11), (9, 12))

check(maximize_elements)