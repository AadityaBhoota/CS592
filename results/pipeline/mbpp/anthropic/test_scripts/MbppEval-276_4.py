import math

def volume_cylinder(r, h):
    return math.pi * r**2 * h

def check(candidate):
    assert math.isclose(volume_cylinder(10,5), 1570.7500000000002, rel_tol=0.001)
    assert math.isclose(volume_cylinder(4,5), 251.32000000000002, rel_tol=0.001)
    assert math.isclose(volume_cylinder(4,10), 502.64000000000004, rel_tol=0.001)

check(volume_cylinder)