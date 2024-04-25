def min_Jumps(steps, d): 
    total_distance = abs(d)
    number_of_jumps = total_distance / steps
    return number_of_jumps

# Test the function


def check(candidate):
    assert min_Jumps((3,4),11)==3.5
    assert min_Jumps((3,4),0)==0
    assert min_Jumps((11,14),11)==1

check(min_Jumps)