def monotonic(lst: list):
    """Return True if list elements are monotonically increasing or decreasing."""
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1)) or all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1)



METADATA = {}


def check(candidate):
    assert candidate([1, 2, 4, 10]) == True
    assert candidate([1, 2, 4, 20]) == True
    assert candidate([1, 20, 4, 10]) == False
    assert candidate([4, 1, 0, -10]) == True
    assert candidate([4, 1, 1, 0]) == True
    assert candidate([1, 2, 3, 2, 5, 60]) == False
    assert candidate([1, 2, 3, 4, 5, 60]) == True
    assert candidate([9, 9, 9, 9]) == True


check(monotonic)