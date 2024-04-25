import math

def surface_Area(b, s):
    l = math.sqrt(b**2 + s**2)
    
    area = b**2 + 2*b*l
    
    return area

def check(candidate):
    assert surface_Area(3,4) == 33
    assert surface_Area(4,5) == 56
    assert surface_Area(1,2) == 5

check(surface_Area)