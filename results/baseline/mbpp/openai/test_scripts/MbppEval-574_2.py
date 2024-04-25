import math

def surfacearea_cylinder(r, h):
    # Calculate the lateral surface area of the cylinder
    lateral_surface_area = 2 * math.pi * r * h

    # Calculate the top and bottom surface areas of the cylinder
    top_bottom_surface_area = 2 * math.pi * r**2

    # Total surface area is the sum of lateral, top, and bottom surface areas
    total_surface_area = lateral_surface_area + top_bottom_surface_area

    return round(total_surface_area, 3)

# Test cases




def check(candidate):
    assert surfacearea_cylinder(10,5)==942.45
    assert surfacearea_cylinder(4,5)==226.18800000000002
    assert surfacearea_cylinder(4,10)==351.848

check(surfacearea_cylinder)