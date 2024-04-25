import cmath

def convert(number):
    magnitude, phase = cmath.polar(number)
    return (magnitude, phase)

def check(candidate):
    assert convert(1) == (1.0, 0.0)
    assert convert(4) == (4.0,0.0)
    assert convert(5) == (5.0,0.0)

check(convert)