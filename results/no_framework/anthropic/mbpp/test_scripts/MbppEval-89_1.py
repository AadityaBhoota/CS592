def closest_num(N):
    """
    Write a function to find the closest smaller number than n.

    Examples:
    closest_num(11) == 10
    closest_num(7) == 6
    closest_num(12) == 11
    """
    if N <= 1:
        return None  # No smaller number exists for 1 or less

    # Iterate through the numbers from N-1 to 1 to find the closest smaller number
    for i in range(N-1, 0, -1):
        if N % i == 0:
            return i

    return 1  # If no other number is found, return 1 as the closest smaller number

def check(candidate):
    assert closest_num(11) == 10
    assert closest_num(7) == 6
    assert closest_num(12) == 11

check(closest_num)