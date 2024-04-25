import cmath

def convert(numbers):
    # Use cmath.polar to convert the complex number to polar form
    polar_coordinates = cmath.polar(numbers)
    
    # Return the polar coordinates as a tuple of the form (r, phi)
    return polar_coordinates

def check(candidate):
    assert convert(1) == (1.0, 0.0)
    assert convert(4) == (4.0,0.0)
    assert convert(5) == (5.0,0.0)

check(convert)