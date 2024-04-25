import math

def lateralsurface_cone(r, h):
    """
    Finds the lateral surface area of a cone given the radius (r) and the height (h).

    Parameters:
    r (float): The radius of the cone.
    h (float): The height of the cone.

    Returns:
    float: The lateral surface area of the cone.
    """
    lateral_surface_area = math.pi * r * math.sqrt(r**2 + h**2)
    return lateral_surface_area

# Examples




def check(candidate):
    assert lateralsurface_cone(5,12)==204.20352248333654
    assert lateralsurface_cone(10,15)==566.3586699569488
    assert lateralsurface_cone(19,17)==1521.8090132193388

check(lateralsurface_cone)