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

    # Calculate the number of full jumps required
    full_jumps = d // steps

    # Calculate the remaining distance
    remaining_distance = d % steps

    # If the remaining distance is 0, return the number of full jumps
    if remaining_distance == 0:
        return full_jumps

    # Calculate the number of additional jumps required
    additional_jumps = 1 if remaining_distance > 0 else 0

    # Calculate the total number of jumps
    total_jumps = full_jumps + additional_jumps

    # Calculate the actual distance covered
    actual_distance = full_jumps * steps

    # Calculate the fraction of the last jump
    fraction_of_last_jump = remaining_distance / steps

    # Return the total number of jumps, including the fraction of the last jump
    return total_jumps + fraction_of_last_jump

def check(candidate):
    assert min_Jumps((3,4),11)==3.5
    assert min_Jumps((3,4),0)==0
    assert min_Jumps((11,14),11)==1

check(min_Jumps)