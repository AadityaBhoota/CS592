def find_Volume(l, b, h):
    """
    Write a python function to find the volume of a triangular prism.

    Examples:
    find_Volume(10, 8, 6) == 240
    find_Volume(3, 2, 2) == 6
    find_Volume(1, 2, 1) == 1
    """
    volume = 0.5 * l * b * h
    return volume

def check(candidate):
    assert find_Volume(10,8,6) == 240
    assert find_Volume(3,2,2) == 6
    assert find_Volume(1,2,1) == 1

check(find_Volume)