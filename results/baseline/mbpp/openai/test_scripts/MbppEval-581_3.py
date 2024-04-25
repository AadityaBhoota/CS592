def surface_Area(b, s):
    # Calculate the slant height of the pyramid
    slant_height = (b**2 + s**2)**0.5

    # Calculate the lateral surface area of the pyramid
    lateral_surface_area = 0.5 * b * slant_height

    # Calculate the base area of the pyramid
    base_area = b**2

    # Calculate the total surface area of the pyramid
    total_surface_area = lateral_surface_area + base_area

    return total_surface_area

# Test the function




# Additional test case


def check(candidate):
    assert surface_Area(3,4) == 33
    assert surface_Area(4,5) == 56
    assert surface_Area(1,2) == 5

check(surface_Area)