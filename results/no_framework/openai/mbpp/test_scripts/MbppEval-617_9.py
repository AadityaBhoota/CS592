import math

def min_Jumps(steps, d, target_x): 
    # Calculate the number of jumps required to reach the target_x coordinate
    if target_x == 0:
        return 0
    else:
        jump_distance = math.sqrt(steps**2 + d**2)
        num_jumps = abs(target_x) / jump_distance
        return num_jumps

# Test the function with some example cases




def check(candidate):
    assert min_Jumps((3,4),11)==3.5
    assert min_Jumps((3,4),0)==0
    assert min_Jumps((11,14),11)==1

check(min_Jumps)