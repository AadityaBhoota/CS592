from math import ceil, sqrt

def min_Jumps(steps, d):
    """
    Write a function to check for the number of jumps required of given length to reach a point of form (d, 0) from origin in a 2d plane.

    Args:
        steps (int): The length of each jump.
        d (int): The target distance from the origin.

    Returns:
        float: The minimum number of jumps required to reach the target distance.
    """
    if d == 0:
        return 0
    
    # Calculate the minimum number of jumps required to reach the target distance
    distance = abs(d)
    jumps = ceil(distance / steps)
    
    # Calculate the actual distance reached by the jumps
    actual_distance = jumps * steps
    
    # Check if the target distance can be reached exactly
    if actual_distance == distance:
        return jumps
    else:
        # Calculate the additional distance that needs to be covered
        remaining_distance = actual_distance - distance
        
        # Calculate the minimum number of additional jumps required
        additional_jumps = ceil(sqrt(remaining_distance**2) / steps)
        
        # Return the total number of jumps
        return jumps + additional_jumps

def check(candidate):
    assert min_Jumps((3,4),11)==3.5
    assert min_Jumps((3,4),0)==0
    assert min_Jumps((11,14),11)==1

check(min_Jumps)