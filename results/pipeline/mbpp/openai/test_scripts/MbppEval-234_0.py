def volume_cube(l):
    '''
    Calculate the volume of a cube given its side length.
    
    Parameters:
    l (int or float): Side length of the cube
    
    Returns:
    int or float: Volume of the cube
    '''
    volume = l ** 3
    return volume

def check(candidate):
    assert volume_cube(3)==27
    assert volume_cube(2)==8
    assert volume_cube(5)==125

check(volume_cube)