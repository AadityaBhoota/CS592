def next_power_of_2(n):
    """
    Write a python function to find the smallest power of 2 greater than or equal to n.

    Examples:
    next_power_of_2(0) == 1
    next_power_of_2(5) == 8
    next_power_of_2(17) == 32
    """
    if n == 0:
        return 1
    
    power = 1
    while power < n:
        power *= 2
    
    return power

def check(candidate):
    assert next_power_of_2(0) == 1
    assert next_power_of_2(5) == 8
    assert next_power_of_2(17) == 32

check(next_power_of_2)