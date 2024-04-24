def surface_Area(b, h): 
    # Find the slant height of the pyramid
    s = ((b/2)**2 + h**2)**0.5
    
    # Calculate the surface area of the pyramid
    base_area = b**2
    lateral_area = 2 * b * s / 2
    total_surface_area = base_area + lateral_area
    
    return total_surface_area

# Examples




def check(candidate):
    assert surface_Area(3,4) == 33
    assert surface_Area(4,5) == 56
    assert surface_Area(1,2) == 5

check(surface_Area)