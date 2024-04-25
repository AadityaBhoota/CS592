def volume_cube(l):
    '''
    Write a function to find the volume of a cube given its side length.

    Parameters:
    l (int or float): The side length of the cube.

    Returns:
    int or float: The volume of the cube.

    Examples:
    volume_cube(3) == 27
    volume_cube(2) == 8
    volume_cube(5) == 125
    '''
    volume = l * l * l
    return volume

def check(candidate):
    assert volume_cube(3)==27
    assert volume_cube(2)==8
    assert volume_cube(5)==125

check(volume_cube)