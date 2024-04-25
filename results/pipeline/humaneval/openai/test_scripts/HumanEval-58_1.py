def common(l1: list, l2: list):
    unique_set1 = set(l1)
    unique_set2 = set(l2)
    
    common_elements = unique_set1.intersection(unique_set2)
    sorted_common_elements = sorted(common_elements)
    
    return sorted_common_elements



METADATA = {}


def check(candidate):
    assert candidate([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]
    assert candidate([5, 3, 2, 8], [3, 2]) == [2, 3]
    assert candidate([4, 3, 2, 8], [3, 2, 4]) == [2, 3, 4]
    assert candidate([4, 3, 2, 8], []) == []


check(common)