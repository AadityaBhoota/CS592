def surface_Area(b, s):
    # Calculate the slant height of the pyramid
    l = ((b/2)**2 + s**2)**0.5
    
    # Calculate the surface area of the square pyramid
    area = b*b + 2*b*l
    
    return area

# Test cases




def check(candidate):
    assert surface_Area(3,4) == 33
    assert surface_Area(4,5) == 56
    assert surface_Area(1,2) == 5

check(surface_Area)