def surface_Area(b, s):
    # Calculate the area of the base
    base_area = b**2

    # Calculate the lateral surface area
    lateral_area = b * s / 2 * 4

    # Calculate the total surface area
    total_area = base_area + lateral_area

    return total_area





def check(candidate):
    assert surface_Area(3,4) == 33
    assert surface_Area(4,5) == 56
    assert surface_Area(1,2) == 5

check(surface_Area)