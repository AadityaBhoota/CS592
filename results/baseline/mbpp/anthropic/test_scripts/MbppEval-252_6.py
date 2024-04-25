import cmath

def convert(numbers):
    '''
    Write a python function to convert complex numbers to polar coordinates.

    Examples:
    convert(1) == (1.0, 0.0)
    convert(4) == (4.0, 0.0)
    convert(5) == (5.0, 0.0)
    convert(1 + 1j) == (1.4142135623730951, 0.7853981633974483)
    convert(2 + 2j) == (2.8284271247461903, 0.7853981633974483)
    '''
    # Convert the input to a complex number
    if isinstance(numbers, (int, float)):
        numbers = complex(numbers)
    
    # Calculate the magnitude and angle of the complex number
    magnitude = abs(numbers)
    angle = cmath.phase(numbers)
    
    return (magnitude, angle)

def check(candidate):
    assert convert(1) == (1.0, 0.0)
    assert convert(4) == (4.0,0.0)
    assert convert(5) == (5.0,0.0)

check(convert)