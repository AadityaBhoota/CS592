import math

def circle_circumference(r):
    """
    Calculates the circumference of a circle.

    Args:
        r (float): The radius of the circle.

    Returns:
        float: The circumference of the circle.
    """
    circumference = 2 * math.pi * r
    return round(circumference, 3)

def check(candidate):
    assert math.isclose(circle_circumference(10), 62.830000000000005, rel_tol=0.001)
    assert math.isclose(circle_circumference(5), 31.415000000000003, rel_tol=0.001)
    assert math.isclose(circle_circumference(4), 25.132, rel_tol=0.001)

check(circle_circumference)