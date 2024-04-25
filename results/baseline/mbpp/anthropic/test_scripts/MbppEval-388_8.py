def highest_Power_of_2(n): 
    '''
    Write a python function to find the highest power of 2 that is less than or equal to n.

    Examples:
    highest_Power_of_2(10) == 8
    highest_Power_of_2(19) == 16
    highest_Power_of_2(32) == 32
    '''
def highest_power_of_2(n):
    """
    Find the highest power of 2 that is less than or equal to n.

    Examples:
    highest_power_of_2(10) == 8
    highest_power_of_2(19) == 16
    highest_power_of_2(32) == 32
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