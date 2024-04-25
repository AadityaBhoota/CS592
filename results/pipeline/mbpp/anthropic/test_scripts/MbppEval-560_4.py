def union_elements(test_tup1, test_tup2):
    """
    Write a function to find the union of the elements of two given tuples and output them in sorted order.

    Examples:
    union_elements((3, 4, 5, 6),(5, 7, 4, 10)) == (3, 4, 5, 6, 7, 10)
    union_elements((1, 2, 3, 4),(3, 4, 5, 6)) == (1, 2, 3, 4, 5, 6)
    union_elements((11, 12, 13, 14),(13, 15, 16, 17)) == (11, 12, 13, 14, 15, 16, 17)
    """
    combined_list = list(test_tup1) + list(test_tup2)
    unique_list = list(set(combined_list))
    sorted_list = sorted(unique_list)
    return tuple(sorted_list)

def check(candidate):
    assert union_elements((3, 4, 5, 6),(5, 7, 4, 10) ) == (3, 4, 5, 6, 7, 10)
    assert union_elements((1, 2, 3, 4),(3, 4, 5, 6) ) == (1, 2, 3, 4, 5, 6)
    assert union_elements((11, 12, 13, 14),(13, 15, 16, 17) ) == (11, 12, 13, 14, 15, 16, 17)

check(union_elements)