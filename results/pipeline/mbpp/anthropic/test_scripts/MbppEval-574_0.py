import math

def surfacearea_cylinder(r, h):
    """
    Write a function to find the surface area of a cylinder.

    Examples:
    surfacearea_cylinder(10, 5) == 942.4784176044735
    surfacearea_cylinder(4, 5) == 226.18800000000002
    surfacearea_cylinder(4, 10) == 351.848
    """
    surface_area = 2 * math.pi * r * (r + h)
    return surface_area

def check(candidate):
    assert surfacearea_cylinder(10,5)==942.45
    assert surfacearea_cylinder(4,5)==226.18800000000002
    assert surfacearea_cylinder(4,10)==351.848

check(surfacearea_cylinder)