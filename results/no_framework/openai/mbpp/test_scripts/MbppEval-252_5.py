import cmath

def convert(number):
    try:
        num = complex(number)
        polar = cmath.polar(num)
        return polar
    except ValueError:
        return "Input should be a numeric value."

# Testing the function with the provided examples




def check(candidate):
    assert convert(1) == (1.0, 0.0)
    assert convert(4) == (4.0,0.0)
    assert convert(5) == (5.0,0.0)

check(convert)