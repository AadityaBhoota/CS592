def find_Volume(l,b,h) : 
    '''
    Write a python function to find the volume of a triangular prism.

    Examples:
    find_Volume(10,8,6) == 240
    find_Volume(3,2,2) == 6
    find_Volume(1,2,1) == 1
    '''
def find_volume(l, b, h):
    # Step 1: Calculate the volume of the triangular prism
    base_area = 0.5 * b * h
    volume = base_area * l
    return volume

# Testing the function




def check(candidate):
    assert find_Volume(10,8,6) == 240
    assert find_Volume(3,2,2) == 6
    assert find_Volume(1,2,1) == 1

check(find_Volume)