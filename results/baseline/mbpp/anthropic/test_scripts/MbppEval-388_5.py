def highest_Power_of_2(n):
    """
    Write a python function to find the highest power of 2 that is less than or equal to n.

    Examples:
    highest_Power_of_2(10) == 8
    highest_Power_of_2(19) == 16
    highest_Power_of_2(32) == 32
    """
    # Base case: if n is 0 or less, return 0
    if n <= 0:
        return 0

    # Initialize the result to 1 (which is 2^0)
    result = 1

    # Shift the bits of 1 to the left until the result is greater than n
    while result <= n:
        result <<= 1

    # Shift the bits of the result back to the right to get the highest power of 2 less than or equal to n
    return result >> 1

def check(candidate):
    assert highest_Power_of_2(10) == 8
    assert highest_Power_of_2(19) == 16
    assert highest_Power_of_2(32) == 32

check(highest_Power_of_2)