def closest_num(N):
    """
    Write a function to find the closest smaller number than n.

    Examples:
    closest_num(11) == 10
    closest_num(7) == 6
    closest_num(12) == 11
    closest_num(0) == None
    """
    if N <= 0:
        return None
    return N - 1

def check(candidate):
    assert closest_num(11) == 10
    assert closest_num(7) == 6
    assert closest_num(12) == 11

check(closest_num)