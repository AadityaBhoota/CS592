import math

def min_Jumps(steps, d): 
    if d == 0:
        return 0
    
    distance = math.sqrt(d**2)
    jumps = distance / steps
    return round(jumps, 1)

# Testing the function with given examples




def check(candidate):
    assert min_Jumps((3,4),11)==3.5
    assert min_Jumps((3,4),0)==0
    assert min_Jumps((11,14),11)==1

check(min_Jumps)