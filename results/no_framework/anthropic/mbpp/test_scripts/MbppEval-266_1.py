def lateralsurface_cube(l):
    """
    Write a function to find the lateral surface area of a cube given its side length.

    Examples:
    lateralsurface_cube(5) == 100
    lateralsurface_cube(9) == 324
    lateralsurface_cube(10) == 400
    """
    return 4 * l * l

def check(candidate):
    assert lateralsurface_cube(5)==100
    assert lateralsurface_cube(9)==324
    assert lateralsurface_cube(10)==400

check(lateralsurface_cube)