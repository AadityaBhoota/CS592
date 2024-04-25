from math import tan, pi

def area_polygon(s, l):
    '''
    Write a function to calculate the area of a regular polygon given the length and number of its sides.

    Args:
        s (int): Number of sides of the regular polygon.
        l (float): Length of each side of the regular polygon.

    Returns:
        float: Area of the regular polygon.
    '''
    area = (s * l**2) / (4 * tan(pi / s))
    return round(area, 10)

def check(candidate):
    assert math.isclose(area_polygon(4, 20), 400., rel_tol=0.001)
    assert math.isclose(area_polygon(10, 15), 1731.197, rel_tol=0.001)
    assert math.isclose(area_polygon(9, 7), 302.909, rel_tol=0.001)

check(area_polygon)