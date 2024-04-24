def volume_cube(l):
    """
    Write a function to find the volume of a cube given its side length.

    Examples:
    volume_cube(3) == 27
    volume_cube(2) == 8
    volume_cube(5) == 125
    """
    return l ** 3

def check(candidate):
    assert volume_cube(3)==27
    assert volume_cube(2)==8
    assert volume_cube(5)==125

check(volume_cube)