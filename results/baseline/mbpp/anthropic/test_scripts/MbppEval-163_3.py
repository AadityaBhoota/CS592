from math import tan, pi

def area_polygon(s, l):
    """
    Calculates the area of a regular polygon given the length and number of its sides.

    Args:
    s (int): The number of sides of the polygon.
    l (float): The length of each side of the polygon.

    Returns:
    float: The area of the regular polygon.
    """
    area = (s * l ** 2) / (4 * tan(pi / s))
    return area

def check(candidate):
    assert math.isclose(area_polygon(4, 20), 400., rel_tol=0.001)
    assert math.isclose(area_polygon(10, 15), 1731.197, rel_tol=0.001)
    assert math.isclose(area_polygon(9, 7), 302.909, rel_tol=0.001)

check(area_polygon)