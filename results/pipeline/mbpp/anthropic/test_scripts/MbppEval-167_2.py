def next_power_of_2(n):
    """
    Write a python function to find the smallest power of 2 greater than or equal to n.

    Examples:
    next_Power_Of_2(0) == 1
    next_Power_Of_2(5) == 8
    next_Power_Of_2(17) == 32
    """
    if n == 0:
        return 1
    return (n - 1) | (n - 1) + 1

def check(candidate):
    assert next_power_of_2(0) == 1
    assert next_power_of_2(5) == 8
    assert next_power_of_2(17) == 32

check(next_power_of_2)