import math

def surfacearea_sphere(r):
    """
    Calculates the surface area of a sphere with a given radius.

    Args:
        r (float): The radius of the sphere.

    Returns:
        float: The surface area of the sphere.
    """
    surface_area = 4 * math.pi * r**2
    return surface_area

def check(candidate):
    assert math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001)
    assert math.isclose(surfacearea_sphere(15), 2827.4333882308138, rel_tol=0.001)
    assert math.isclose(surfacearea_sphere(20), 5026.548245743669, rel_tol=0.001)

check(surfacearea_sphere)