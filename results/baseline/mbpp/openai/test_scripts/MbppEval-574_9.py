import math

def surfacearea_cylinder(r, h):
    # Calculate the surface area of a cylinder using the formula (2πrh + 2πr^2)
    surface_area = 2 * math.pi * r * h + 2 * math.pi * r**2
    return round(surface_area, 3)

# Test the function with the examples provided




def check(candidate):
    assert surfacearea_cylinder(10,5)==942.45
    assert surfacearea_cylinder(4,5)==226.18800000000002
    assert surfacearea_cylinder(4,10)==351.848

check(surfacearea_cylinder)