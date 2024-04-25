def max_element(l: list):
    """Return maximum element in the list."""
    if not l:
        return None  # return None for an empty list
    
    max_num = l[0]
    for num in l[1:]:
        if num > max_num:
            max_num = num
    
    return max_num



METADATA = {}


def check(candidate):
    assert candidate([1, 2, 3]) == 3
    assert candidate([5, 3, -5, 2, -3, 3, 9, 0, 124, 1, -10]) == 124

check(max_element)