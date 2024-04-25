def tuple_modulo(test_tup1, test_tup2):
    if len(test_tup1) != len(test_tup2):
        return "Error: Input tuples must be of the same length."

    result = []

    for i in range(len(test_tup1)):
        result.append(test_tup1[i] % test_tup2[i])

    return tuple(result)

def check(candidate):
    assert tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)
    assert tuple_modulo((11, 5, 6, 7), (6, 7, 8, 6)) == (5, 5, 6, 1)
    assert tuple_modulo((12, 6, 7, 8), (7, 8, 9, 7)) == (5, 6, 7, 1)

check(tuple_modulo)