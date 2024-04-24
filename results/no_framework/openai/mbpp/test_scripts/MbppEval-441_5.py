def surfacearea_cube(l):
    """
    This function calculates the surface area of a cube given its side length.

    Parameters:
    l (int): Side length of the cube

    Returns:
    int: Surface area of the cube
    """
    return 6 * l * l

# Test the function




def check(candidate):
    assert surfacearea_cube(5)==150
    assert surfacearea_cube(3)==54
    assert surfacearea_cube(10)==600

check(surfacearea_cube)