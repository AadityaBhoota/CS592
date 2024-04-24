def find_Volume(l, b, h):
    """
    Calculates the volume of a triangular prism.

    Args:
        l (float): Length of the base of the triangular prism.
        b (float): Width of the base of the triangular prism.
        h (float): Height of the triangular prism.

    Returns:
        float: The volume of the triangular prism.
    """
    area_of_base = 0.5 * l * b
    volume = area_of_base * h
    return volume

def check(candidate):
    assert find_Volume(10,8,6) == 240
    assert find_Volume(3,2,2) == 6
    assert find_Volume(1,2,1) == 1

check(find_Volume)