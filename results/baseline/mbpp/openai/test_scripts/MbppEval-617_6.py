def min_Jumps(x, y, d):
    '''
    Function to calculate the minimum number of jumps required to reach a point at (x, y) from the origin in a 2D plane of given fixed length d.

    Parameters:
    x (int): x-coordinate of the point to reach
    y (int): y-coordinate of the point to reach
    d (int): fixed length of each jump

    Returns:
    float: minimum number of jumps required
    '''

    distance = (x**2 + y**2) ** 0.5
    return distance / d

# Test cases




def check(candidate):
    assert min_Jumps((3,4),11)==3.5
    assert min_Jumps((3,4),0)==0
    assert min_Jumps((11,14),11)==1

check(min_Jumps)