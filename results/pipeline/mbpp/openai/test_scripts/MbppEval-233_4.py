def lateralsuface_cylinder(r,h):
    '''
    Write a function to find the lateral surface area of a cylinder.

    Examples:
    lateralsuface_cylinder(10,5) == 314.15000000000003
    lateralsuface_cylinder(4,5) == 125.66000000000001
    lateralsuface_cylinder(4,10) == 251.32000000000002
    '''
import math

def lateralsurface_cylinder(r, h):
    lateral_surface_area = 2 * math.pi * r * h
    return lateral_surface_area

def check(candidate):
    assert math.isclose(lateralsuface_cylinder(10,5), 314.15000000000003, rel_tol=0.001)
    assert math.isclose(lateralsuface_cylinder(4,5), 125.66000000000001, rel_tol=0.001)
    assert math.isclose(lateralsuface_cylinder(4,10), 251.32000000000002, rel_tol=0.001)

check(lateralsuface_cylinder)