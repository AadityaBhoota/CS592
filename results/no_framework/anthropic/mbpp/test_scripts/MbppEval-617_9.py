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

    # Calculate the minimum number of jumps required
    jumps = math.ceil(abs(d) / steps)

    # Calculate the final position after the jumps
    final_position = jumps * steps * (1 if d >= 0 else -1)

    # Calculate the distance between the final position and the target
    distance = abs(final_position - d)

    # If the distance is less than the step size, return the number of jumps plus the fractional part
    if distance < steps:
        return jumps + distance / steps
    else:
        return jumps

def check(candidate):
    assert min_Jumps((3,4),11)==3.5
    assert min_Jumps((3,4),0)==0
    assert min_Jumps((11,14),11)==1

check(min_Jumps)