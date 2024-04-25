import math

def triangle_area(r):
    """
    Write a python function to find the area of the largest triangle that can be inscribed in a semicircle with a given radius.

    Examples:
    triangle_area(0) == 0
    triangle_area(-1) == -1
    triangle_area(2) == 4
    """
    if r < 0:
        return -1
    elif r == 0:
        return 0
    else:
        # The largest triangle that can be inscribed in a semicircle has its base
        # equal to the diameter of the semicircle, and its height equal to the
        # radius of the semicircle.
        base = 2 * r
        height = r
        return 0.5 * base * height

def check(candidate):
    assert triangle_area(-1) == None
    assert triangle_area(0) == 0
    assert triangle_area(2) == 4

check(triangle_area)