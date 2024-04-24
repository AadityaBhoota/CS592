import math

def lateralsurface_cone(r, h):
    """
    Calculates the lateral surface area of a cone given the radius (r) and the height (h).

    Args:
        r (float): The radius of the cone.
        h (float): The height of the cone.

    Returns:
        float: The lateral surface area of the cone.
    """
    # Calculate the slant height of the cone
    slant_height = math.sqrt(r**2 + h**2)

    # Calculate the lateral surface area
    lateral_surface_area = math.pi * r * slant_height

    return lateral_surface_area

def check(candidate):
    assert lateralsurface_cone(5,12)==204.20352248333654
    assert lateralsurface_cone(10,15)==566.3586699569488
    assert lateralsurface_cone(19,17)==1521.8090132193388

check(lateralsurface_cone)