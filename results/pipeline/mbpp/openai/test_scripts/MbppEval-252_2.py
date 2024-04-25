import cmath

def convert(complex_number):
    return cmath.polar(complex_number)

numbers = [1, 4, 5]
polar_coords = []

for number in numbers:
    polar_coords.append(convert(complex(number)))



def check(candidate):
    assert convert(1) == (1.0, 0.0)
    assert convert(4) == (4.0,0.0)
    assert convert(5) == (5.0,0.0)

check(convert)