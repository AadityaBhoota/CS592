import cmath

def convert(numbers):
    '''
    Write a python function to convert complex numbers to polar coordinates.

    Examples:
    convert(1) == (1.0, 0.0)
    convert(4) == (4.0, 0.0)
    convert(5) == (5.0, 0.0)
    convert(1+2j) == (2.2360679774997898, 1.1071487177940904)
    convert(1-2j) == (2.2360679774997898, -1.1071487177940904)
    '''
    if isinstance(numbers, (int, float)):
        # If the input is a real number, the polar coordinates are:
        # magnitude = the number itself
        # angle = 0.0 (since the angle is 0 radians)
        return (float(numbers), 0.0)
    else:
        # If the input is a complex number, use cmath.polar() to get the
        # magnitude and angle in polar coordinates
        return cmath.polar(complex(numbers))

def check(candidate):
    assert convert(1) == (1.0, 0.0)
    assert convert(4) == (4.0,0.0)
    assert convert(5) == (5.0,0.0)

check(convert)