def closest_num(N):
    """
    Write a function to find the closest smaller number than N.

    Examples:
    closest_num(11) == 10
    closest_num(7) == 6
    closest_num(12) == 11
    """
    if N <= 1:
        return None

    for i in range(N-1, 0, -1):
        if N % i == 0:
            return i

    return 1

def check(candidate):
    assert closest_num(11) == 10
    assert closest_num(7) == 6
    assert closest_num(12) == 11

check(closest_num)