def add_pairwise(test_tup):
    """
    Write a function to find the pairwise addition of the neighboring elements of the given tuple.

    Examples:
    add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)
    add_pairwise((2, 6, 8, 9, 11)) == (8, 14, 17, 20)
    add_pairwise((3, 7, 9, 10, 12)) == (10, 16, 19, 22)
    """
    result = []
    for i in range(len(test_tup) - 1):
        result.append(test_tup[i] + test_tup[i+1])
    return tuple(result)

def check(candidate):
    assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)
    assert add_pairwise((2, 6, 8, 9, 11)) == (8, 14, 17, 20)
    assert add_pairwise((3, 7, 9, 10, 12)) == (10, 16, 19, 22)

check(add_pairwise)