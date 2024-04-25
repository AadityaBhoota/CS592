import math

def min_Jumps(steps, d):
    n = 1
    while True:
        total_distance = n * steps * math.sqrt(2)
        if total_distance == d:
            return n
        elif total_distance < d:
            n += 1
        else:
            return n + (d - (n-1) * steps * math.sqrt(2)) / (steps * math.sqrt(2))

def check(candidate):
    assert min_Jumps((3,4),11)==3.5
    assert min_Jumps((3,4),0)==0
    assert min_Jumps((11,14),11)==1

check(min_Jumps)