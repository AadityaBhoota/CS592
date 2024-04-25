def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    common_dict = {}
    for item in l1:
        if item in common_dict:
            common_dict[item] += 1
        else:
            common_dict[item] = 1
    for item in l2:
        if item in common_dict:
            common_dict[item] += 1
    return sorted(common_dict.keys())



METADATA = {}


def check(candidate):
    assert candidate([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]
    assert candidate([5, 3, 2, 8], [3, 2]) == [2, 3]
    assert candidate([4, 3, 2, 8], [3, 2, 4]) == [2, 3, 4]
    assert candidate([4, 3, 2, 8], []) == []


check(common)