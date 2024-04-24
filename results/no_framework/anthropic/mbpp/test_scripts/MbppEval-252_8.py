import cmath

def convert(numbers):
    """
    Write a Python function to convert complex numbers to polar coordinates.

    Examples:
    convert(1) == (1.0, 0.0)
    convert(4) == (4.0, 0.0)
    convert(5) == (5.0, 0.0)
    """
    if isinstance(numbers, (int, float)):
        return (numbers, 0.0)
    elif isinstance(numbers, complex):
        return (abs(numbers), cmath.phase(numbers))
    else:
        raise TypeError("Input must be an integer, float, or complex number.")

def check(candidate):
    assert convert(1) == (1.0, 0.0)
    assert convert(4) == (4.0,0.0)
    assert convert(5) == (5.0,0.0)

check(convert)