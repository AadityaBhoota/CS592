def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]
    """
    l1.sort()
    l2.sort()

    result = []
    i, j = 0, 0

    while i < len(l1) and j < len(l2):
        if l1[i] == l2[j]:
            result.append(l1[i])
            i += 1
            j += 1
        elif l1[i] < l2[j]:
            i += 1
        else:
            j += 1

    return result



METADATA = {}


def check(candidate):
    assert candidate([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]
    assert candidate([5, 3, 2, 8], [3, 2]) == [2, 3]
    assert candidate([4, 3, 2, 8], [3, 2, 4]) == [2, 3, 4]
    assert candidate([4, 3, 2, 8], []) == []


check(common)