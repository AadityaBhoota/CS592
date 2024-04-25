import math

def min_Jumps(steps, d):
    total_distance = math.sqrt(d**2)
    jumps = total_distance / steps
    return jumps

def check(candidate):
    assert min_Jumps((3,4),11)==3.5
    assert min_Jumps((3,4),0)==0
    assert min_Jumps((11,14),11)==1

check(min_Jumps)