def surface_Area(b, s):
    base_area = b**2
    side_area = 2 * b * ((b**2 + (s**2))**0.5)
    total_area = base_area + side_area
    return total_area

# Test the function with the provided examples




def check(candidate):
    assert surface_Area(3,4) == 33
    assert surface_Area(4,5) == 56
    assert surface_Area(1,2) == 5

check(surface_Area)