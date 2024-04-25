def surfacearea_cube(l):
    surface_area = 6 * l**2
    return surface_area

def check(candidate):
    assert surfacearea_cube(5)==150
    assert surfacearea_cube(3)==54
    assert surfacearea_cube(10)==600

check(surfacearea_cube)