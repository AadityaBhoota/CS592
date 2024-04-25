def surface_Area(b, s):
    # Calculate the area of the base of the pyramid
    base_area = b**2

    # Calculate the lateral surface area of the pyramid
    lateral_area = 2 * b * s

    # Calculate the total surface area of the pyramid
    total_area = base_area + lateral_area
    return total_area

def check(candidate):
    assert surface_Area(3,4) == 33
    assert surface_Area(4,5) == 56
    assert surface_Area(1,2) == 5

check(surface_Area)