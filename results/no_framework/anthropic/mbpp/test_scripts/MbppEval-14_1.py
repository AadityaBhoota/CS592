def find_Volume(l, b, h):
    """
    Write a python function to find the volume of a triangular prism.

    Examples:
    find_Volume(10, 8, 6) == 240
    find_Volume(3, 2, 2) == 6
    find_Volume(1, 2, 1) == 1
    """
    # Calculate the area of the triangle base
    base_area = 0.5 * l * b

    # Calculate the volume of the triangular prism
    volume = base_area * h

    return volume

def check(candidate):
    assert find_Volume(10,8,6) == 240
    assert find_Volume(3,2,2) == 6
    assert find_Volume(1,2,1) == 1

check(find_Volume)