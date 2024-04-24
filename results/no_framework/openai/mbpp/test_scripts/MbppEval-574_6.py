import math

def surfacearea_cylinder(r, h):
    # calculate the surface area of a cylinder
    surface_area = 2 * math.pi * r * (r + h)

    return round(surface_area, 2)

# Test the function with the examples




def check(candidate):
    assert surfacearea_cylinder(10,5)==942.45
    assert surfacearea_cylinder(4,5)==226.18800000000002
    assert surfacearea_cylinder(4,10)==351.848

check(surfacearea_cylinder)