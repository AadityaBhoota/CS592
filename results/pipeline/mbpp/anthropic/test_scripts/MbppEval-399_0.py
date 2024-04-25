def bitwise_xor(test_tup1, test_tup2):
    result = []
    for i in range(len(test_tup1)):
        result.append(test_tup1[i] ^ test_tup2[i])
    return tuple(result)

def check(candidate):
    assert bitwise_xor((10, 4, 6, 9), (5, 2, 3, 3)) == (15, 6, 5, 10)
    assert bitwise_xor((11, 5, 7, 10), (6, 3, 4, 4)) == (13, 6, 3, 14)
    assert bitwise_xor((12, 6, 8, 11), (7, 4, 5, 6)) == (11, 2, 13, 13)

check(bitwise_xor)