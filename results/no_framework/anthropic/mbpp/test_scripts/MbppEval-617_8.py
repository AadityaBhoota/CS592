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
    
    # Calculate the number of jumps required
    num_jumps = math.ceil(abs(d) / steps)
    
    # Calculate the distance from the last jump
    last_jump_distance = num_jumps * steps - abs(d)
    
    # Return the total number of jumps, with the last jump distance included
    return num_jumps + last_jump_distance / steps

def check(candidate):
    assert min_Jumps((3,4),11)==3.5
    assert min_Jumps((3,4),0)==0
    assert min_Jumps((11,14),11)==1

check(min_Jumps)