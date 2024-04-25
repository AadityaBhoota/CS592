def surfacearea_cylinder(r,h):
    lateral_area = 2 * 3.14159 * r * h
    base_area = 2 * 3.14159 * r ** 2
    total_area = lateral_area + base_area
    return total_area

def check(candidate):
    assert surfacearea_cylinder(10,5)==942.45
    assert surfacearea_cylinder(4,5)==226.18800000000002
    assert surfacearea_cylinder(4,10)==351.848

check(surfacearea_cylinder)