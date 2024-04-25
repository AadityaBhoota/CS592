def surfacearea_cube(l):
    """
    Write a function to find the surface area of a cube of a given size.

    Examples:
    surfacearea_cube(5) == 150
    surfacearea_cube(3) == 54
    surfacearea_cube(10) == 600
    """
    return 6 * (l ** 2)

def check(candidate):
    assert surfacearea_cube(5)==150
    assert surfacearea_cube(3)==54
    assert surfacearea_cube(10)==600

check(surfacearea_cube)