import cmath

def convert(number):
    polar = cmath.polar(number)
    return polar

# Test cases




def check(candidate):
    assert convert(1) == (1.0, 0.0)
    assert convert(4) == (4.0,0.0)
    assert convert(5) == (5.0,0.0)

check(convert)