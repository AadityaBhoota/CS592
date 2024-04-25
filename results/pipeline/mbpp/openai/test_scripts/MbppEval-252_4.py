import cmath

def convert(numbers):
    numbers = complex(numbers, 0)
    polar_coordinates = cmath.polar(numbers)
    magnitude, phase = polar_coordinates
    return magnitude, phase

def check(candidate):
    assert convert(1) == (1.0, 0.0)
    assert convert(4) == (4.0,0.0)
    assert convert(5) == (5.0,0.0)

check(convert)