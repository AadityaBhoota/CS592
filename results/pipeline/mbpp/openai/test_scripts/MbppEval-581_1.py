def surface_Area(b, s):
    # Step 0: Calculate the perimeter of the base and the slant height
    perimeter = 4 * b
    slant = (b**2 + s**2)**0.5
    
    # Step 1: Calculate the lateral surface area
    LSA = 0.5 * perimeter * slant
    
    # Step 2: Calculate the base area
    B = b**2
    
    # Step 3: Calculate the total surface area
    TSA = LSA + B
    
    return TSA

def check(candidate):
    assert surface_Area(3,4) == 33
    assert surface_Area(4,5) == 56
    assert surface_Area(1,2) == 5

check(surface_Area)