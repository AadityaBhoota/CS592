def surfacearea_cube(l):
    """
    Find the surface area of a cube of a given size.

    Args:
        l (int or float): Length of one side of the cube.

    Returns:
        int or float: The surface area of the cube.
    """
    return 6 * l ** 2

def check(candidate):
    assert surfacearea_cube(5)==150
    assert surfacearea_cube(3)==54
    assert surfacearea_cube(10)==600

check(surfacearea_cube)