import cmath

def convert(num):
    """
    Convert a complex number to polar coordinates.

    Args:
        num (complex): The complex number to be converted.

    Returns:
        tuple: A tuple containing the magnitude and angle of the complex number.
    """
    magnitude = abs(num)
    angle = cmath.phase(num)
    return (magnitude, angle)

def check(candidate):
    assert convert(1) == (1.0, 0.0)
    assert convert(4) == (4.0,0.0)
    assert convert(5) == (5.0,0.0)

check(convert)