def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    # Convert the lists to sets to get unique elements
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the common elements using set intersection
    common_elements = list(set1.intersection(set2))
    
    # Sort the common elements
    common_elements.sort()
    
    return common_elements



METADATA = {}


def check(candidate):
    assert candidate([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]
    assert candidate([5, 3, 2, 8], [3, 2]) == [2, 3]
    assert candidate([4, 3, 2, 8], [3, 2, 4]) == [2, 3, 4]
    assert candidate([4, 3, 2, 8], []) == []


check(common)