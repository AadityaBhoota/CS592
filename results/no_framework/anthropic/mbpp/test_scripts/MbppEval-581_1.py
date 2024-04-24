import math

def surface_Area(b, s):
    """
    Calculates the surface area of a square pyramid given the base edge and height.

    Args:
    b (float): The length of the base edge.
    s (float): The height of the pyramid.

    Returns:
    float: The surface area of the square pyramid.
    """
    base_area = b ** 2
    slant_length = math.sqrt(b ** 2 + s ** 2)
    lateral_area = 4 * (0.5 * b * slant_length)
    surface_area = base_area + lateral_area
    return round(surface_area, 2)

def check(candidate):
    assert surface_Area(3,4) == 33
    assert surface_Area(4,5) == 56
    assert surface_Area(1,2) == 5

check(surface_Area)