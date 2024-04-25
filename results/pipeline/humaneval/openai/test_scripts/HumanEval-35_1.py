def max_element(l: list):
    """Return maximum element in the list."""
    
    if not l:
        return None
    
    max_elem = l[0]
    
    for elem in l[1:]:
        if elem > max_elem:
            max_elem = elem
    
    return max_elem



METADATA = {}


def check(candidate):
    assert candidate([1, 2, 3]) == 3
    assert candidate([5, 3, -5, 2, -3, 3, 9, 0, 124, 1, -10]) == 124

check(max_element)