def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    if not l:
        raise ValueError("Input list is empty.")

    l_sorted = sorted(l)
    n = len(l_sorted)

    if n % 2 == 1:
        return l_sorted[n // 2]
    else:
        middle1 = l_sorted[n // 2 - 1]
        middle2 = l_sorted[n // 2]
        return (middle1 + middle2) / 2



METADATA = {}


def check(candidate):
    assert candidate([3, 1, 2, 4, 5]) == 3
    assert candidate([-10, 4, 6, 1000, 10, 20]) == 8.0
    assert candidate([5]) == 5
    assert candidate([6, 5]) == 5.5
    assert candidate([8, 1, 3, 9, 9, 2, 7]) == 7 


check(median)