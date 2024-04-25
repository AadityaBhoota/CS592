def closest_num(N):
    """
    Write a function to find the closest smaller number than n.
    
    Examples:
    closest_num(11) == 10
    closest_num(7) == 6
    closest_num(12) == 11
    """
    if N == 1:
        return 0
    
    closest = N - 1
    
    for i in range(N - 1, 0, -1):
        if i < N:
            closest = i
            break
    
    return closest

def check(candidate):
    assert closest_num(11) == 10
    assert closest_num(7) == 6
    assert closest_num(12) == 11

check(closest_num)