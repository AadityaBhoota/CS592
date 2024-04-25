def find_Volume(l, b, h):
    """
    Write a python function to find the volume of a triangular prism.

    Examples:
    find_Volume(10, 8, 6) == 240
    find_Volume(3, 2, 2) == 6
    find_Volume(1, 2, 1) == 1

    Args:
        l (float): Length of the triangular prism.
        b (float): Breadth of the triangular prism.
        h (float): Height of the triangular prism.

    Returns:
        float: The volume of the triangular prism.
    """
    return (1/2) * b * h * l

def check(candidate):
    assert find_Volume(10,8,6) == 240
    assert find_Volume(3,2,2) == 6
    assert find_Volume(1,2,1) == 1

check(find_Volume)