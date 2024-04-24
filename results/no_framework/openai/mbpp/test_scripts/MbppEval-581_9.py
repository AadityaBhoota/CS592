def surface_Area(b, s):
    base_area = b**2
    side_area = b * s / 2
    total_area = base_area + 2 * side_area
    return total_area

# Test cases




def check(candidate):
    assert surface_Area(3,4) == 33
    assert surface_Area(4,5) == 56
    assert surface_Area(1,2) == 5

check(surface_Area)