def common(l1: list, l2: list):
    common_elements = list(set(l1) & set(l2))  # Find common elements using set intersection
    common_elements.sort()  # Sort the common elements
    return common_elements

# Testing the function with the provided examples





METADATA = {}


def check(candidate):
    assert candidate([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]
    assert candidate([5, 3, 2, 8], [3, 2]) == [2, 3]
    assert candidate([4, 3, 2, 8], [3, 2, 4]) == [2, 3, 4]
    assert candidate([4, 3, 2, 8], []) == []


check(common)