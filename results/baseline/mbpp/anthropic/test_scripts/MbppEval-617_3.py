import math

def min_Jumps(steps, d):
    """
    Write a function to check for the number of jumps required of given length to reach a point of form (d, 0) from origin in a 2d plane.

    Examples:
    min_Jumps(3, 4, 11) == 3.5
    min_Jumps(3, 4, 0) == 0
    min_Jumps(11, 14, 11) == 1
    """
    if d == 0:
        return 0
    
    distance = abs(d)
    num_jumps = distance // steps
    remaining_distance = distance % steps
    
    if remaining_distance == 0:
        return num_jumps
    else:
        return num_jumps + 0.5

def check(candidate):
    assert min_Jumps((3,4),11)==3.5
    assert min_Jumps((3,4),0)==0
    assert min_Jumps((11,14),11)==1

check(min_Jumps)