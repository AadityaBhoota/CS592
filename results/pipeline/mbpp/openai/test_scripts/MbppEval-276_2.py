import math

def volume_cylinder(r, h):
    '''
    Calculates the volume of a cylinder given its radius and height.
    
    :param r: radius of the cylinder
    :param h: height of the cylinder
    :return: calculated volume of the cylinder
    '''
    pi = math.pi
    volume = pi * r**2 * h
    
    return volume

def check(candidate):
    assert math.isclose(volume_cylinder(10,5), 1570.7500000000002, rel_tol=0.001)
    assert math.isclose(volume_cylinder(4,5), 251.32000000000002, rel_tol=0.001)
    assert math.isclose(volume_cylinder(4,10), 502.64000000000004, rel_tol=0.001)

check(volume_cylinder)