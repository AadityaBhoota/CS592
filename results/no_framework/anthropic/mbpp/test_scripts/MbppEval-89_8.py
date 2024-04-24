def closest_num(N):
    """
    Write a function to find the closest smaller number than n.

    Examples:
    closest_num(11) == 10
    closest_num(7) == 6
    closest_num(12) == 11
    """
    if N <= 0:
        return None  # Return None for non-positive inputs

    closest = N - 1
    while closest >= 0 and not closest < N:
        closest -= 1

    return closest

def check(candidate):
    assert closest_num(11) == 10
    assert closest_num(7) == 6
    assert closest_num(12) == 11

check(closest_num)