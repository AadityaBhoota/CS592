def surface_Area(b,s): 
    '''
    Write a python function to find the surface area of a square pyramid with a given base edge and height.

    Examples:
    surface_Area(3,4) == 33
    surface_Area(4,5) == 56
    surface_Area(1,2) == 5
    '''
def surface_area(b, s):
    base_area = b * b
    face_area = 0.5 * b * s
    total_area = base_area + 4 * face_area
    return total_area

def check(candidate):
    assert surface_Area(3,4) == 33
    assert surface_Area(4,5) == 56
    assert surface_Area(1,2) == 5

check(surface_Area)