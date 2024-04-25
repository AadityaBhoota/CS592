import math

def triangle_area(r):
    # Step 0: Find the height of the triangle inscribed in the semicircle
    h = r
    
    # Step 1: Calculate the base of the triangle using the Pythagorean theorem
    b = 2 * math.sqrt(r**2 - h**2)
    
    # Step 2: Calculate the area of the triangle
    area = 0.5 * b * h
    
    return area

def check(candidate):
    assert triangle_area(-1) == None
    assert triangle_area(0) == 0
    assert triangle_area(2) == 4

check(triangle_area)