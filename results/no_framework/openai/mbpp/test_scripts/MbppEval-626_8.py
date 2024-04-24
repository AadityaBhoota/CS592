import math

def triangle_area(r):
    if r <= 0:
        return r
    
    base = 2 * math.sqrt(2) * r
    height = r
    area = 0.5 * base * height
    return area

# Testing the function with the provided examples




def check(candidate):
    assert triangle_area(-1) == None
    assert triangle_area(0) == 0
    assert triangle_area(2) == 4

check(triangle_area)