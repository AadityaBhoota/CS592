def find_Volume(l, b, h):
    """
    Write a python function to find the volume of a triangular prism.

    Parameters:
    l (int or float): The length of the triangular prism.
    b (int or float): The base of the triangular prism.
    h (int or float): The height of the triangular prism.

    Returns:
    int or float: The volume of the triangular prism.

    Examples:
    find_Volume(10, 8, 6) == 240
    find_Volume(3, 2, 2) == 6
    find_Volume(1, 2, 1) == 1
    """
    volume = 1/2 * b * h * l
    return volume

def check(candidate):
    assert find_Volume(10,8,6) == 240
    assert find_Volume(3,2,2) == 6
    assert find_Volume(1,2,1) == 1

check(find_Volume)