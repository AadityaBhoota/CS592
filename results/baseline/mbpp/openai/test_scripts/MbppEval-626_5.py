import math

def triangle_area(r):
    if r <= 0:
        return r

    base = r
    height = 2*r
    area = 0.5 * base * height

    return area

# Test the function




def check(candidate):
    assert triangle_area(-1) == None
    assert triangle_area(0) == 0
    assert triangle_area(2) == 4

check(triangle_area)