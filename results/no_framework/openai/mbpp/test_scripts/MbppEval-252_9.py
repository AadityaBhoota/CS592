import cmath

def convert(number):
    if isinstance(number, (int, float)):
        complex_number = number
    else:
        raise ValueError("Input must be an integer or a float.")

    polar = cmath.polar(complex(complex_number))
    return polar

# Test Cases




def check(candidate):
    assert convert(1) == (1.0, 0.0)
    assert convert(4) == (4.0,0.0)
    assert convert(5) == (5.0,0.0)

check(convert)