import math

def lateralsuface_cylinder(r, h):
    """
    Write a function to find the lateral surface area of a cylinder.

    Examples:
    lateralsuface_cylinder(10, 5) == 314.1592653589793
    lateralsuface_cylinder(4, 5) == 125.66370614359172
    lateralsuface_cylinder(4, 10) == 251.32741228718345
    """
    lateral_surface_area = 2 * math.pi * r * h
    return round(lateral_surface_area, 10)

def check(candidate):
    assert math.isclose(lateralsuface_cylinder(10,5), 314.15000000000003, rel_tol=0.001)
    assert math.isclose(lateralsuface_cylinder(4,5), 125.66000000000001, rel_tol=0.001)
    assert math.isclose(lateralsuface_cylinder(4,10), 251.32000000000002, rel_tol=0.001)

check(lateralsuface_cylinder)