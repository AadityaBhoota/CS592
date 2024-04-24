import cmath

def convert(numbers):
    '''
    Write a python function to convert complex numbers to polar coordinates.

    Examples:
    convert(1) == (1.0, 0.0)
    convert(4) == (4.0, 0.0)
    convert(5) == (5.0, 0.0)
    '''
    if isinstance(numbers, (int, float)):
        # If the input is a real number, convert it to a complex number
        numbers = complex(numbers)

    # Use the cmath module to get the magnitude (modulus) and phase (argument)
    magnitude = abs(numbers)
    phase = cmath.phase(numbers)

    return (magnitude, phase)

def check(candidate):
    assert convert(1) == (1.0, 0.0)
    assert convert(4) == (4.0,0.0)
    assert convert(5) == (5.0,0.0)

check(convert)