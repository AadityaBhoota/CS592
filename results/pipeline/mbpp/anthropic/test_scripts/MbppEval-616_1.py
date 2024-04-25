def tuple_modulo(test_tup1, test_tup2):
    if len(test_tup1) != len(test_tup2):
        return "Error: Tuples must be of the same length."
    return tuple(a % b for a, b in zip(test_tup1, test_tup2))

def check(candidate):
    assert tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)
    assert tuple_modulo((11, 5, 6, 7), (6, 7, 8, 6)) == (5, 5, 6, 1)
    assert tuple_modulo((12, 6, 7, 8), (7, 8, 9, 7)) == (5, 6, 7, 1)

check(tuple_modulo)