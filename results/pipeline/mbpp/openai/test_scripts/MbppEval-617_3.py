import math

def min_Jumps(steps, x, y):
    x_distance = abs(x)
    y_distance = abs(y)

    total_distance = math.sqrt(x_distance**2 + y_distance**2)

    jumps = total_distance / steps

    if total_distance % steps == 0:
        return jumps
    else:
        return jumps + 0.5

def check(candidate):
    assert min_Jumps((3,4),11)==3.5
    assert min_Jumps((3,4),0)==0
    assert min_Jumps((11,14),11)==1

check(min_Jumps)