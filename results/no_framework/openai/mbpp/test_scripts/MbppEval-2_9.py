def similar_elements(test_tup1, test_tup2):
    # Convert the tuples to sets for easier comparison
    set1 = set(test_tup1)
    set2 = set(test_tup2)
    
    # Find the common elements using set intersection
    common_elements = set1.intersection(set2)
    
    # Convert the common elements back to tuple and return
    return tuple(common_elements)

# Testing the function with the provided examples




def check(candidate):
    assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))
    assert set(similar_elements((1, 2, 3, 4),(5, 4, 3, 7))) == set((3, 4))
    assert set(similar_elements((11, 12, 14, 13),(17, 15, 14, 13))) == set((13, 14))

check(similar_elements)