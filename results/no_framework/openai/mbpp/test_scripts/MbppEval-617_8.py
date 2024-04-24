def min_Jumps(steps, d, x): 
    '''
    Calculate the minimum number of jumps required of given length to reach a point of form (d, 0) from origin in a 2D plane.

    Parameters:
    steps (int): Number of steps that can be taken in one jump.
    d (int): The x-coordinate of the target point.
    x (int): The y-coordinate of the target point.

    Returns:
    float: The minimum number of jumps required.

    Examples:
    min_Jumps(3, 4, 11) == 3.5
    min_Jumps(3, 4, 0) == 0
    min_Jumps(11, 14, 11) == 1
    '''

    # Calculate the absolute distance from the origin to the target point
    distance = abs(d)

    # Calculate the number of jumps required to reach the target point
    jumps = distance / steps

    # If the target point has the same y-coordinate, return the number of jumps
    if x == 0:
        return jumps

    # Otherwise, calculate the additional jump distance needed to reach the target point
    remaining_distance = abs(x)

    # If the remaining distance is less than the number of steps taken in the last jump, add another jump
    if remaining_distance < steps:
        jumps += 1
    # Otherwise, calculate the fractional part of the jump required to reach the exact target point
    else:
        jumps += remaining_distance / steps

    return jumps

# Test the function with example inputs




def check(candidate):
    assert min_Jumps((3,4),11)==3.5
    assert min_Jumps((3,4),0)==0
    assert min_Jumps((11,14),11)==1

check(min_Jumps)