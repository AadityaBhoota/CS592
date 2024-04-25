import math

def lateralsuface_cylinder(r, h):
    """
    Calculates the lateral surface area of a cylinder.

    Args:
        r (float): The radius of the cylinder.
        h (float): The height of the cylinder.

    Returns:
        float: The lateral surface area of the cylinder.
    """
    return 2 * math.pi * r * h

def check(candidate):
    assert math.isclose(lateralsuface_cylinder(10,5), 314.15000000000003, rel_tol=0.001)
    assert math.isclose(lateralsuface_cylinder(4,5), 125.66000000000001, rel_tol=0.001)
    assert math.isclose(lateralsuface_cylinder(4,10), 251.32000000000002, rel_tol=0.001)

check(lateralsuface_cylinder)