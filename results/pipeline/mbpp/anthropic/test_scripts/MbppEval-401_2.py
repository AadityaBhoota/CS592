def add_nested_tuples(test_tup1, test_tup2):
    if len(test_tup1) != len(test_tup2):
        raise ValueError("Input tuples must have the same number of inner tuples.")

    result = []
    for i in range(len(test_tup1)):
        new_tuple = (test_tup1[i][0] + test_tup2[i][0], test_tup1[i][1] + test_tup2[i][1])
        result.append(new_tuple)

    return tuple(result)

def check(candidate):
    assert add_nested_tuples(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((7, 10), (7, 14), (3, 10), (8, 13))
    assert add_nested_tuples(((2, 4), (5, 6), (3, 10), (2, 11)), ((7, 8), (4, 10), (2, 2), (8, 4))) == ((9, 12), (9, 16), (5, 12), (10, 15))
    assert add_nested_tuples(((3, 5), (6, 7), (4, 11), (3, 12)), ((8, 9), (5, 11), (3, 3), (9, 5))) == ((11, 14), (11, 18), (7, 14), (12, 17))

check(add_nested_tuples)