import math

def min_Jumps(steps, d):
    if d == 0:
        return 0
    elif d % steps == 0:
        return d // steps
    else:
        return math.ceil(d / steps)

def check(candidate):
    assert min_Jumps((3,4),11)==3.5
    assert min_Jumps((3,4),0)==0
    assert min_Jumps((11,14),11)==1

check(min_Jumps)