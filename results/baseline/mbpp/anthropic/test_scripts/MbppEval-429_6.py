def and_tuples(test_tup1, test_tup2):
    """
    Write a function to extract the elementwise and tuples from the given two tuples.

    Examples:
    and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)
    and_tuples((1, 2, 3, 4), (5, 6, 7, 8)) == (1, 2, 3, 0)
    and_tuples((8, 9, 11, 12), (7, 13, 14, 17)) == (0, 9, 10, 0)
    """
    result = []
    for i in range(len(test_tup1)):
        result.append(test_tup1[i] & test_tup2[i])
    return tuple(result)

def check(candidate):
    assert and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)
    assert and_tuples((1, 2, 3, 4), (5, 6, 7, 8)) == (1, 2, 3, 0)
    assert and_tuples((8, 9, 11, 12), (7, 13, 14, 17)) == (0, 9, 10, 0)

check(and_tuples)