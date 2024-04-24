import math

def surfacearea_cylinder(r, h):
    base_area = math.pi * r ** 2
    lateral_area = 2 * math.pi * r * h
    total_area = 2 * base_area + lateral_area
    return round(total_area, 2)

# Test cases




def check(candidate):
    assert surfacearea_cylinder(10,5)==942.45
    assert surfacearea_cylinder(4,5)==226.18800000000002
    assert surfacearea_cylinder(4,10)==351.848

check(surfacearea_cylinder)