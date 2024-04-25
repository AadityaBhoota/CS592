import math

def min_Jumps(steps, d):
    """
    Write a function to check for the number of jumps required of given length to reach a point of form (d, 0) from origin in a 2D plane.

    Args:
        steps (int): The length of each jump.
        d (int): The target distance from the origin.

    Returns:
        float: The minimum number of jumps required to reach the target distance.
    """
    if d == 0:
        return 0
    
    # Calculate the minimum number of jumps required using the formula
    # min_jumps = ceil(d / steps)
    min_jumps = math.ceil(abs(d) / steps)
    
    # If the target distance is not divisible by the jump length, return the minimum jumps with a fractional part
    if d % steps != 0:
        return min_jumps
    else:
        return min_jumps - 1

def check(candidate):
    assert min_Jumps((3,4),11)==3.5
    assert min_Jumps((3,4),0)==0
    assert min_Jumps((11,14),11)==1

check(min_Jumps)