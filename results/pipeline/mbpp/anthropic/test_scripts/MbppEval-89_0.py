def closest_num(N):
    """
    Write a function to find the closest smaller number than n.

    Examples:
    closest_num(11) == 10
    closest_num(7) == 6
    closest_num(12) == 11
    """
    # Handle edge cases
    if N <= 0:
        return None

    # Convert N to a string and remove the last digit
    N_str = str(N)
    if len(N_str) == 1:
        return None
    closest_str = N_str[:-1]

    # Convert the resulting string back to an integer
    closest = int(closest_str)

    return closest

def check(candidate):
    assert closest_num(11) == 10
    assert closest_num(7) == 6
    assert closest_num(12) == 11

check(closest_num)