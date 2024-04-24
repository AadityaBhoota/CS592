def similar_elements(test_tup1, test_tup2):
    '''
    Write a function to find the shared elements from the given two lists.

    Examples:
    similar_elements((3, 4, 5, 6),(5, 7, 4, 10)) == (4, 5)
    similar_elements((1, 2, 3, 4),(5, 4, 3, 7)) == (3, 4)
    similar_elements((11, 12, 14, 13),(17, 15, 14, 13)) == (13, 14)
    '''
    return tuple(set(test_tup1) & set(test_tup2))

def check(candidate):
    assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))
    assert set(similar_elements((1, 2, 3, 4),(5, 4, 3, 7))) == set((3, 4))
    assert set(similar_elements((11, 12, 14, 13),(17, 15, 14, 13))) == set((13, 14))

check(similar_elements)