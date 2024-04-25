def surface_Area(b, s):
    base_area = b ** 2
    face_area = 4 * ((b * s) / 2)
    total_area = base_area + face_area
    return total_area

def check(candidate):
    assert surface_Area(3,4) == 33
    assert surface_Area(4,5) == 56
    assert surface_Area(1,2) == 5

check(surface_Area)