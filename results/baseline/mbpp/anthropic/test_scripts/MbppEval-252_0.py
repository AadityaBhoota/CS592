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
        # If the input is a real number, convert it to a complex number
        numbers = complex(numbers)
    elif isinstance(numbers, complex):
        # If the input is already a complex number, use it as is
        pass
    else:
        raise TypeError("Input must be a real number or a complex number.")

    # Convert the complex number to polar coordinates
    magnitude = abs(numbers)
    angle = cmath.phase(numbers)

    return (magnitude, angle)

def check(candidate):
    assert convert(1) == (1.0, 0.0)
    assert convert(4) == (4.0,0.0)
    assert convert(5) == (5.0,0.0)

check(convert)