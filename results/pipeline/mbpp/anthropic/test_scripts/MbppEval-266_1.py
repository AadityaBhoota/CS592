def lateralsurface_cube(side_length):
    """
    Calculates the lateral surface area of a cube given its side length.

    Args:
        side_length (float): The length of one side of the cube.

    Returns:
        float: The lateral surface area of the cube.
    """
    return 4 * side_length * side_length

def check(candidate):
    assert lateralsurface_cube(5)==100
    assert lateralsurface_cube(9)==324
    assert lateralsurface_cube(10)==400

check(lateralsurface_cube)