import math

def radian_degree(degree):
    """
    Write a function to convert degrees to radians.

    Examples:
    radian_degree(90) == 1.5707963267948966
    radian_degree(60) == 1.0471975511965976
    radian_degree(120) == 2.0943951023931953
    """
    return math.radians(degree)

def check(candidate):
    assert radian_degree(90)==1.5707963267948966
    assert radian_degree(60)==1.0471975511965976
    assert radian_degree(120)==2.0943951023931953

check(radian_degree)