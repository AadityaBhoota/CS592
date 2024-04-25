import math

def triangle_area(r):
    if r < 0:
        return -1
    
    side_length = 2 * r  # Side length of the equilateral triangle inscribed in the semicircle
    area = (math.sqrt(3) / 4) * side_length**2  # Area of the equilateral triangle
    
    return area

def check(candidate):
    assert triangle_area(-1) == None
    assert triangle_area(0) == 0
    assert triangle_area(2) == 4

check(triangle_area)