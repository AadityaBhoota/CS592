def bell_Number(n):
    """
    Calculates the nth Bell number.

    Args:
        n (int): The index of the Bell number to calculate.

    Returns:
        int: The nth Bell number.
    """
    if n == 0:
        return 1
    
    bell_numbers = [0] * (n + 1)
    bell_numbers[0] = 1
    
    for i in range(1, n + 1):
        for j in range(i):
            bell_numbers[i] += bell_numbers[j] * bell_numbers[i - j - 1]
    
    return bell_numbers[n]

def check(candidate):
    assert bell_Number(2) == 2
    assert bell_Number(3) == 5
    assert bell_Number(4) == 15

check(bell_Number)