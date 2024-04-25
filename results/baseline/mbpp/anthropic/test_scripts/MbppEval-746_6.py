import math

def sector_area(r, a):
    """
    Calculates the area of a sector given the radius and angle.
    
    Parameters:
    r (float): The radius of the sector.
    a (float): The angle of the sector in degrees.
    
    Returns:
    float: The area of the sector, or None if the angle is larger than 360 degrees.
    """
    if a > 360:
        return None
    else:
        return (math.pi * r**2 * (a / 360))

def check(candidate):
    assert sector_area(4,45)==6.283185307179586
    assert sector_area(9,45)==31.808625617596654
    assert sector_area(9,361)==None

check(sector_area)