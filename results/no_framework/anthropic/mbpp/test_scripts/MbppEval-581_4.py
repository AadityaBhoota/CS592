import math

def surface_Area(b, s):
    """
    Calculates the surface area of a square pyramid with a given base edge and height.

    Args:
        b (float): The length of the base edge.
        s (float): The height of the pyramid.

    Returns:
        float: The surface area of the square pyramid.
    """
    # Calculate the length of the slant height
    slant_height = math.sqrt(b**2 + s**2)

    # Calculate the surface area
    surface_area = b**2 + 4 * (0.5 * b * slant_height)

    return round(surface_area, 2)

def check(candidate):
    assert surface_Area(3,4) == 33
    assert surface_Area(4,5) == 56
    assert surface_Area(1,2) == 5

check(surface_Area)