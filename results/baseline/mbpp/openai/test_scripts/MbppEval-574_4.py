import math

def surfacearea_cylinder(r, h):
    # Formula for surface area of a cylinder: 2πr² + 2πrh
    area_side = 2 * math.pi * r * h
    area_top_bottom = 2 * math.pi * r**2
    total_area = area_side + area_top_bottom

    return round(total_area, 3)

# Test cases




def check(candidate):
    assert surfacearea_cylinder(10,5)==942.45
    assert surfacearea_cylinder(4,5)==226.18800000000002
    assert surfacearea_cylinder(4,10)==351.848

check(surfacearea_cylinder)