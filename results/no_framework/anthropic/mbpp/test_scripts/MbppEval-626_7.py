import math

def triangle_area(r):
    """
    Find the area of the largest triangle that can be inscribed in a semicircle with a given radius.

    Args:
    r (float): The radius of the semicircle.

    Returns:
    float: The area of the largest inscribed triangle.
    """
    if r < 0:
        return -1
    if r == 0:
        return 0

    # The base of the triangle is the diameter of the semicircle, which is 2r
    base = 2 * r

    # The height of the triangle is the radius of the semicircle, which is r
    height = r

    # Calculate the area of the triangle using the formula: Area = 1/2 * base * height
    area = 0.5 * base * height

    return area

def check(candidate):
    assert triangle_area(-1) == None
    assert triangle_area(0) == 0
    assert triangle_area(2) == 4

check(triangle_area)