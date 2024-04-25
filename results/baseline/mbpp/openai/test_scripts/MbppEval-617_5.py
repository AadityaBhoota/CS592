import math

def min_Jumps(steps_x, steps_y, d):
    # Calculate the Euclidean distance from the origin to the target point
    distance = math.sqrt(d**2)
    
    # Calculate the total number of steps needed to reach the target point
    total_steps = distance / math.sqrt(steps_x**2 + steps_y**2)
    
    return total_steps

# Test cases




def check(candidate):
    assert min_Jumps((3,4),11)==3.5
    assert min_Jumps((3,4),0)==0
    assert min_Jumps((11,14),11)==1

check(min_Jumps)