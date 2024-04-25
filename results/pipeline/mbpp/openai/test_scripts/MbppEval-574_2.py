def surfacearea_cylinder(r, h):
    top_bottom_area = 2 * 3.14159 * r**2
    side_area = 2 * 3.14159 * r * h
    total_area = top_bottom_area + side_area
    return total_area

def check(candidate):
    assert surfacearea_cylinder(10,5)==942.45
    assert surfacearea_cylinder(4,5)==226.18800000000002
    assert surfacearea_cylinder(4,10)==351.848

check(surfacearea_cylinder)