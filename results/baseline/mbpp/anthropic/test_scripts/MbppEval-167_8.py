def next_power_of_2(n):
    """
    Finds the smallest power of 2 greater than or equal to n.

    Parameters:
    n (int): The number to find the next power of 2 for.

    Returns:
    int: The smallest power of 2 greater than or equal to n.
    """
    if n == 0:
        return 1
    
    # Find the next power of 2 greater than n
    return 2 ** (n - 1).bit_length()

def check(candidate):
    assert next_power_of_2(0) == 1
    assert next_power_of_2(5) == 8
    assert next_power_of_2(17) == 32

check(next_power_of_2)