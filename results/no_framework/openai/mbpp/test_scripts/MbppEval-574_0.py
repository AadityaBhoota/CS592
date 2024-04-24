import math

def surfacearea_cylinder(r, h):
    # Surface area of a cylinder: 2*pi*r^2 + 2*pi*r*h
    area = 2 * math.pi * r**2 + 2 * math.pi * r * h
    return round(area, 2)

# Test cases




def check(candidate):
    assert surfacearea_cylinder(10,5)==942.45
    assert surfacearea_cylinder(4,5)==226.18800000000002
    assert surfacearea_cylinder(4,10)==351.848

check(surfacearea_cylinder)