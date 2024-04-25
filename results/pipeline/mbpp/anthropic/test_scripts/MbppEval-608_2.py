from math import e, factorial

def bell_Number(n):
    """
    Find the nth Bell number.
    
    Parameters:
    n (int): The index of the Bell number to find.
    
    Returns:
    int: The nth Bell number.
    """
    return round(e ** sum((-1)**k * factorial(n) / (factorial(k) * factorial(n-k)) for k in range(n+1)))

def check(candidate):
    assert bell_Number(2) == 2
    assert bell_Number(3) == 5
    assert bell_Number(4) == 15

check(bell_Number)