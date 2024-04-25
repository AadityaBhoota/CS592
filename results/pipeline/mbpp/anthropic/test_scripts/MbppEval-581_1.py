def surface_Area(b, s):
    base_area = b ** 2
    slant_area = 0.5 * b * s
    surface_area = base_area + 4 * slant_area
    return surface_area

def check(candidate):
    assert surface_Area(3,4) == 33
    assert surface_Area(4,5) == 56
    assert surface_Area(1,2) == 5

check(surface_Area)