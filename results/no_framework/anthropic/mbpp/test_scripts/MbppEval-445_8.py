def index_multiplication(test_tup1, test_tup2):
    result = []
    for i in range(len(test_tup1)):
        product_tuple = (test_tup1[i][0] * test_tup2[i][0], test_tup1[i][1] * test_tup2[i][1])
        result.append(product_tuple)
    return tuple(result)

def check(candidate):
    assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)) ) == ((6, 21), (12, 45), (2, 9), (7, 30))
    assert index_multiplication(((2, 4), (5, 6), (3, 10), (2, 11)),((7, 8), (4, 10), (2, 2), (8, 4)) ) == ((14, 32), (20, 60), (6, 20), (16, 44))
    assert index_multiplication(((3, 5), (6, 7), (4, 11), (3, 12)),((8, 9), (5, 11), (3, 3), (9, 5)) ) == ((24, 45), (30, 77), (12, 33), (27, 60))

check(index_multiplication)