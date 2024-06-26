def max_element(l: list):
    """Return maximum element in the list."""
    return max(l)

# Test cases
if __name__ == "__main__":
    print(max_element([1, 2, 3]))  # Output: 3
    print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123



METADATA = {}


def check(candidate):
    assert candidate([1, 2, 3]) == 3
    assert candidate([5, 3, -5, 2, -3, 3, 9, 0, 124, 1, -10]) == 124

check(max_element)