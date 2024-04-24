import math

def volume_cylinder(r, h):
    """
    Calculates the volume of a cylinder given its radius and height.

    Args:
        r (float): The radius of the cylinder.
        h (float): The height of the cylinder.

    Returns:
        float: The volume of the cylinder.
    """
    volume = math.pi * r ** 2 * h
    return volume

def check(candidate):
    assert math.isclose(volume_cylinder(10,5), 1570.7500000000002, rel_tol=0.001)
    assert math.isclose(volume_cylinder(4,5), 251.32000000000002, rel_tol=0.001)
    assert math.isclose(volume_cylinder(4,10), 502.64000000000004, rel_tol=0.001)

check(volume_cylinder)