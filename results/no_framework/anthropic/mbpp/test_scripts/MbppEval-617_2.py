import math

def min_Jumps(steps, d):
    """
    Write a function to check for the number of jumps required of given length to reach a point of form (d, 0) from origin in a 2d plane.

    Args:
        steps (int): The length of each jump.
        d (int): The distance to be reached from the origin.

    Returns:
        float: The minimum number of jumps required to reach the point (d, 0).
    """
    if d == 0:
        return 0

    distance = abs(d)
    jumps = distance // steps
    remainder = distance % steps

    if remainder == 0:
        return jumps
    else:
        return jumps + 1

def check(candidate):
    assert min_Jumps((3,4),11)==3.5
    assert min_Jumps((3,4),0)==0
    assert min_Jumps((11,14),11)==1

check(min_Jumps)