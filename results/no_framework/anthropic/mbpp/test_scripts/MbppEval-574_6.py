import math

def surfacearea_cylinder(r, h):
    """
    Calculates the surface area of a cylinder.

    Parameters:
    r (float): The radius of the cylinder.
    h (float): The height of the cylinder.

    Returns:
    float: The surface area of the cylinder.
    """
    surface_area = 2 * math.pi * r * (r + h)
    return round(surface_area, 5)

def check(candidate):
    assert surfacearea_cylinder(10,5)==942.45
    assert surfacearea_cylinder(4,5)==226.18800000000002
    assert surfacearea_cylinder(4,10)==351.848

check(surfacearea_cylinder)