def surface_Area(b, s):
    # Surface area of a square pyramid = base_area + 0.5 * perimeter of base * slant height
    base_area = b ** 2
    perimeter = 4 * b
    slant_height = ((s ** 2) + (b ** 2)) ** 0.5
    surface_area = base_area + 0.5 * perimeter * slant_height
    return surface_area

# Test cases




def check(candidate):
    assert surface_Area(3,4) == 33
    assert surface_Area(4,5) == 56
    assert surface_Area(1,2) == 5

check(surface_Area)