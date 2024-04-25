def surfacearea_cube(l):
    """
    Calculates the surface area of a cube with the given side length.

    Args:
        l (int or float): The side length of the cube.

    Returns:
        float: The surface area of the cube.
    """
    return 6 * l ** 2

def check(candidate):
    assert surfacearea_cube(5)==150
    assert surfacearea_cube(3)==54
    assert surfacearea_cube(10)==600

check(surfacearea_cube)