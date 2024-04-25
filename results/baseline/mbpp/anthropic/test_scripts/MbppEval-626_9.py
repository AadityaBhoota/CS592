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
        # The largest triangle that can be inscribed in a semicircle has its vertices at the endpoints of the semicircle and the midpoint of the diameter.
        # The base of the triangle is the diameter of the semicircle, which is 2r.
        # The height of the triangle is the radius of the semicircle, which is r.
        # The area of the triangle is (1/2) * base * height.
        area = 0.5 * 2 * r * r
        return area

def check(candidate):
    assert triangle_area(-1) == None
    assert triangle_area(0) == 0
    assert triangle_area(2) == 4

check(triangle_area)