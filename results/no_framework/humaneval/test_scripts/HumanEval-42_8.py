def incr_list(l: list) -> list:
    """Return list with elements incremented by 1."""
    return [num + 1 for num in l]

# Test cases





METADATA = {}


def check(candidate):
    assert candidate([]) == []
    assert candidate([3, 2, 1]) == [4, 3, 2]
    assert candidate([5, 2, 5, 2, 3, 3, 9, 0, 123]) == [6, 3, 6, 3, 4, 4, 10, 1, 124]


check(incr_list)