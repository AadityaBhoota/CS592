import math

def circle_circumference(r):
    """
    Write a function to find the circumference of a circle.

    Examples:
    circle_circumference(10) == 62.83185307179586
    circle_circumference(5) == 31.41592653589793
    circle_circumference(4) == 25.132741228718345
    """
    circumference = 2 * math.pi * r
    return circumference

def check(candidate):
    assert math.isclose(circle_circumference(10), 62.830000000000005, rel_tol=0.001)
    assert math.isclose(circle_circumference(5), 31.415000000000003, rel_tol=0.001)
    assert math.isclose(circle_circumference(4), 25.132, rel_tol=0.001)

check(circle_circumference)