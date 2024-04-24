def highest_power_of_2(n):
    """
    Find the highest power of 2 that is less than or equal to n.

    Args:
        n (int): The input number.

    Returns:
        int: The highest power of 2 that is less than or equal to n.
    """
    power = 0
    while (2 ** (power + 1)) <= n:
        power += 1
    return 2 ** power

def check(candidate):
    assert highest_Power_of_2(10) == 8
    assert highest_Power_of_2(19) == 16
    assert highest_Power_of_2(32) == 32

check(highest_Power_of_2)