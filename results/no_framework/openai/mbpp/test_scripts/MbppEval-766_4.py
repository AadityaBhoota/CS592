def pair_wise(l1):
    pairs = []
    for i in range(len(l1) - 1):
        pairs.append((l1[i], l1[i+1]))
    return pairs

# Test the function with the provided examples




def check(candidate):
    assert pair_wise([1,1,2,3,3,4,4,5])==[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
    assert pair_wise([1,5,7,9,10])==[(1, 5), (5, 7), (7, 9), (9, 10)]
    assert pair_wise([5,1,9,7,10])==[(5, 1), (1, 9), (9, 7), (7, 10)]
    assert pair_wise([1,2,3,4,5,6,7,8,9,10])==[(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)]

check(pair_wise)