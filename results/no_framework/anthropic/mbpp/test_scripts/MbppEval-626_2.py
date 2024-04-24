import math

def triangle_area(r):
    """
    Finds the area of the largest triangle that can be inscribed in a semicircle with a given radius.

    Args:
        r (float): The radius of the semicircle.

    Returns:
        float: The area of the largest triangle that can be inscribed in the semicircle.
    """
    if r < 0:
        return -1
    elif r == 0:
        return 0
    else:
        return (math.pi * r**2) / 4

def check(candidate):
    assert triangle_area(-1) == None
    assert triangle_area(0) == 0
    assert triangle_area(2) == 4

check(triangle_area)