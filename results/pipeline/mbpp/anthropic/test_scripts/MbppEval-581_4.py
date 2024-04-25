def surface_Area(b, h):
    surface_area = b**2 + 2 * b * h
    return surface_area

def check(candidate):
    assert surface_Area(3,4) == 33
    assert surface_Area(4,5) == 56
    assert surface_Area(1,2) == 5

check(surface_Area)