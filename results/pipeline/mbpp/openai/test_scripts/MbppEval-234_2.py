def volume_cube(l):
    '''
    This function calculates the volume of a cube given its side length.
    
    :param l: side length of the cube
    :return: volume of the cube
    '''
    volume = l**3
    return volume

def check(candidate):
    assert volume_cube(3)==27
    assert volume_cube(2)==8
    assert volume_cube(5)==125

check(volume_cube)