def index_multiplication(test_tup1, test_tup2):
    """
    Perform index-wise multiplication of tuple elements in the given two tuples.

    Args:
        test_tup1 (tuple): First tuple of tuples.
        test_tup2 (tuple): Second tuple of tuples.

    Returns:
        tuple: A tuple of tuples, where each inner tuple is the result of multiplying the corresponding elements of the input tuples.
    """
    result = []
    for i in range(len(test_tup1)):
        inner_result = (test_tup1[i][0] * test_tup2[i][0], test_tup1[i][1] * test_tup2[i][1])
        result.append(inner_result)
    return tuple(result)

def check(candidate):
    assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)) ) == ((6, 21), (12, 45), (2, 9), (7, 30))
    assert index_multiplication(((2, 4), (5, 6), (3, 10), (2, 11)),((7, 8), (4, 10), (2, 2), (8, 4)) ) == ((14, 32), (20, 60), (6, 20), (16, 44))
    assert index_multiplication(((3, 5), (6, 7), (4, 11), (3, 12)),((8, 9), (5, 11), (3, 3), (9, 5)) ) == ((24, 45), (30, 77), (12, 33), (27, 60))

check(index_multiplication)