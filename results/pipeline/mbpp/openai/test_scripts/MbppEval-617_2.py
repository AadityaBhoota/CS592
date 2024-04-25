import math

def min_Jumps(steps, d): 
    distance = abs(d) # Calculate the distance from origin to point (d, 0)
    jumps_required = distance / steps # Calculate the number of jumps required to cover that distance
    return jumps_required

def check(candidate):
    assert min_Jumps((3,4),11)==3.5
    assert min_Jumps((3,4),0)==0
    assert min_Jumps((11,14),11)==1

check(min_Jumps)