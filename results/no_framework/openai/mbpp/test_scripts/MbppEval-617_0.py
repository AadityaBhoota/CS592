def min_Jumps(x, y, d): 
    # Calculate the distance from the origin to the point (d, 0) using Pythagorean theorem
    distance = ((d - x)**2 + y**2)**0.5

    # Calculate the number of jumps required
    jumps = distance / d

    return jumps

# Test Cases




def check(candidate):
    assert min_Jumps((3,4),11)==3.5
    assert min_Jumps((3,4),0)==0
    assert min_Jumps((11,14),11)==1

check(min_Jumps)