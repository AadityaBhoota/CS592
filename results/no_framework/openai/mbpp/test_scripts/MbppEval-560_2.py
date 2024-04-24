def union_elements(test_tup1, test_tup2):
    # Convert the tuples to sets for easy union operation
    set1 = set(test_tup1)
    set2 = set(test_tup2)
    
    # Perform union operation on the sets
    union_set = set1.union(set2)
    
    # Sort the elements in the union set and convert it back to a tuple
    sorted_union = tuple(sorted(union_set))
    
    return sorted_union

# Test cases




def check(candidate):
    assert union_elements((3, 4, 5, 6),(5, 7, 4, 10) ) == (3, 4, 5, 6, 7, 10)
    assert union_elements((1, 2, 3, 4),(3, 4, 5, 6) ) == (1, 2, 3, 4, 5, 6)
    assert union_elements((11, 12, 13, 14),(13, 15, 16, 17) ) == (11, 12, 13, 14, 15, 16, 17)

check(union_elements)