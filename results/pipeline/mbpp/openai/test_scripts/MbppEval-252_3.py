import cmath

def convert(numbers):
    if isinstance(numbers, (int, float)):
        complex_number = complex(numbers)
    elif isinstance(numbers, complex):
        complex_number = numbers
    else:
        raise ValueError("Input must be a real or complex number.")
    
    return cmath.polar(complex_number)

def check(candidate):
    assert convert(1) == (1.0, 0.0)
    assert convert(4) == (4.0,0.0)
    assert convert(5) == (5.0,0.0)

check(convert)