import math

def min_Jumps(steps, d):
    # Calculate the Euclidean distance using Pythagorean theorem
    distance = math.sqrt(d**2)
    
    # Calculate the number of jumps required
    jumps = distance / steps

    return jumps

# Test cases




def check(candidate):
    assert min_Jumps((3,4),11)==3.5
    assert min_Jumps((3,4),0)==0
    assert min_Jumps((11,14),11)==1

check(min_Jumps)