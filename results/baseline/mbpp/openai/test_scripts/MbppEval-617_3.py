import math

def min_Jumps(x, y, d):
    distance = math.sqrt(x**2 + y**2)
    
    if d == 0:
        return 0
    elif distance <= d:
        return 1
    else:
        return math.ceil(d / distance)

# Test cases




def check(candidate):
    assert min_Jumps((3,4),11)==3.5
    assert min_Jumps((3,4),0)==0
    assert min_Jumps((11,14),11)==1

check(min_Jumps)