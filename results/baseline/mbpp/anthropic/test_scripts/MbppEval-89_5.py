def closest_num(N):
    """
    Find the closest smaller number than the given number N.

    Examples:
    closest_num(11) == 10
    closest_num(7) == 6
    closest_num(12) == 11
    """
    # Check if N is already the smallest number
    if N <= 1:
        return None

    # Iterate from N-1 to 1 to find the closest smaller number
    for i in range(N-1, 0, -1):
        if i % 1 == 0:
            return i

    # If no smaller number is found, return None
    return None

def check(candidate):
    assert closest_num(11) == 10
    assert closest_num(7) == 6
    assert closest_num(12) == 11

check(closest_num)