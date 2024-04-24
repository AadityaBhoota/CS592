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

    # Calculate the number of full jumps
    full_jumps = d // steps
    remaining_distance = d % steps

    # If the remaining distance is 0, return the number of full jumps
    if remaining_distance == 0:
        return full_jumps

    # Calculate the number of additional half jumps required
    half_jumps = math.ceil(remaining_distance / (steps / 2))

    return full_jumps + half_jumps

def check(candidate):
    assert min_Jumps((3,4),11)==3.5
    assert min_Jumps((3,4),0)==0
    assert min_Jumps((11,14),11)==1

check(min_Jumps)