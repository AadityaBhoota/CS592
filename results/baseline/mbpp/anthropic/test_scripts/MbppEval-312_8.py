import math

def volume_cone(r, h):
    """
    Calculates the volume of a cone.

    Args:
        r (float): The radius of the cone's base.
        h (float): The height of the cone.

    Returns:
        float: The volume of the cone.
    """
    volume = (1 / 3) * math.pi * r ** 2 * h
    return volume

def check(candidate):
    assert math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001)
    assert math.isclose(volume_cone(10,15), 1570.7963267948965, rel_tol=0.001)
    assert math.isclose(volume_cone(19,17), 6426.651371693521, rel_tol=0.001)

check(volume_cone)