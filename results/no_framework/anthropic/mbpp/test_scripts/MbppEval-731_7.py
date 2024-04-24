import math

def lateralsurface_cone(r, h):
    """
    Calculates the lateral surface area of a cone given the radius (r) and height (h).

    Args:
        r (float): Radius of the cone.
        h (float): Height of the cone.

    Returns:
        float: Lateral surface area of the cone.
    """
    slant_length = math.sqrt(r**2 + h**2)
    lateral_surface_area = math.pi * r * slant_length
    return lateral_surface_area

def check(candidate):
    assert lateralsurface_cone(5,12)==204.20352248333654
    assert lateralsurface_cone(10,15)==566.3586699569488
    assert lateralsurface_cone(19,17)==1521.8090132193388

check(lateralsurface_cone)