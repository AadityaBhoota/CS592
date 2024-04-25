import math

def triangle_area(r):
    if r < 0:
        return -1
    
    # Height of equilateral triangle (which is the radius of the semicircle) is half the side length
    side = 2 * r  
    area = (math.sqrt(3) / 4) * side**2

    return area

# Test cases




def check(candidate):
    assert triangle_area(-1) == None
    assert triangle_area(0) == 0
    assert triangle_area(2) == 4

check(triangle_area)