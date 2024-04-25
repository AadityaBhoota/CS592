def common_in_nested_lists(nestedlist):
    """
    Finds the common elements in the given nested lists.

    Args:
        nestedlist (list): A list of lists containing integers.

    Returns:
        list: A list of common elements.
    """
    if not nestedlist:
        return []

    # Convert the first list to a set
    common_elements = set(nestedlist[0])

    # Iterate through the remaining lists and find the common elements
    for i in range(1, len(nestedlist)):
        common_elements &= set(nestedlist[i])

    return sorted(list(common_elements))

def check(candidate):
    assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
    assert set(common_in_nested_lists([[12, 5, 23, 25, 45], [7, 11, 5, 23, 28], [1, 5, 8, 18, 23, 16]]))==set([5,23])
    assert set(common_in_nested_lists([[2, 3,4, 1], [4, 5], [6,4, 8],[4, 5], [6, 8,4]]))==set([4])

check(common_in_nested_lists)