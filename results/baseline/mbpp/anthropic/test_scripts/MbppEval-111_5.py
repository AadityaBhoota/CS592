def common_in_nested_lists(nestedlist):
    """
    Write a function to find the common elements in given nested lists.

    Examples:
    common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]) == [18, 12]
    common_in_nested_lists([[12, 5, 23, 25, 45], [7, 11, 5, 23, 28], [1, 5, 8, 18, 23, 16]]) == [5, 23]
    common_in_nested_lists([[2, 3, 4, 1], [4, 5], [6, 4, 8], [4, 5], [6, 8, 4]]) == [4]
    """
    # Convert the nested list to a set of elements
    flat_set = set([item for lst in nestedlist for item in lst])

    # Find the common elements by iterating through the nested list and counting the occurrences
    common_elements = [elem for elem in flat_set if all(elem in lst for lst in nestedlist)]

    return sorted(common_elements)

def check(candidate):
    assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
    assert set(common_in_nested_lists([[12, 5, 23, 25, 45], [7, 11, 5, 23, 28], [1, 5, 8, 18, 23, 16]]))==set([5,23])
    assert set(common_in_nested_lists([[2, 3,4, 1], [4, 5], [6,4, 8],[4, 5], [6, 8,4]]))==set([4])

check(common_in_nested_lists)