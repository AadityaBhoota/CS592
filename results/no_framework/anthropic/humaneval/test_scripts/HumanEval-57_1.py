def monotonic(l: list) -> bool:
    """Return True if list elements are monotonically increasing or decreasing.

    Args:
        l (list): The input list to check for monotonicity.

    Returns:
        bool: True if the list is monotonic, False otherwise.
    """
    is_increasing = all(l[i] <= l[i+1] for i in range(len(l)-1))
    is_decreasing = all(l[i] >= l[i+1] for i in range(len(l)-1))
    return is_increasing or is_decreasing



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