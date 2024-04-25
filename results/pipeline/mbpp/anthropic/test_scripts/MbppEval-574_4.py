import math

def surfacearea_cylinder(r, h):
    surface_area = 2 * math.pi * r**2 + 2 * math.pi * r * h
    return round(surface_area, 5)

def check(candidate):
    assert surfacearea_cylinder(10,5)==942.45
    assert surfacearea_cylinder(4,5)==226.18800000000002
    assert surfacearea_cylinder(4,10)==351.848

check(surfacearea_cylinder)