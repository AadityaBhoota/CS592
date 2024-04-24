def min_Jumps(steps, d, x):
    # Calculate the total distance from origin to the point (d, 0)
    total_distance = abs(d - x)
    
    # Calculate the number of complete jumps
    complete_jumps = total_distance // steps
    
    # Calculate the remaining distance after complete jumps
    remaining_distance = total_distance % steps
    
    # Calculate the additional jump if the remaining distance is non-zero
    if remaining_distance > 0:
        additional_jump = 0.5
    else:
        additional_jump = 0
    
    # Calculate the total number of jumps required
    total_jumps = complete_jumps + additional_jump

    return total_jumps

# Test cases




def check(candidate):
    assert min_Jumps((3,4),11)==3.5
    assert min_Jumps((3,4),0)==0
    assert min_Jumps((11,14),11)==1

check(min_Jumps)