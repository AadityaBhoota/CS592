import cmath

def convert(numbers):
    complex_number = numbers + 0j
    polar_coordinates = cmath.polar(complex_number)
    return polar_coordinates

def check(candidate):
    assert convert(1) == (1.0, 0.0)
    assert convert(4) == (4.0,0.0)
    assert convert(5) == (5.0,0.0)

check(convert)