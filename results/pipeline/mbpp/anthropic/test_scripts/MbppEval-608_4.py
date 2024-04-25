def bell_Number(n):
    """
    Finds the nth Bell number.
    
    Args:
        n (int): The index of the Bell number to be calculated.
    
    Returns:
        int: The nth Bell number.
    """
    if n == 0:
        return 1
    
    bell_numbers = [0] * (n + 1)
    bell_numbers[0] = 1
    
    for i in range(1, n + 1):
        for j in range(i):
            bell_numbers[i] += (binomial(i, j) * bell_numbers[j])
    
    return bell_numbers[n]

def binomial(n, k):
    """
    Calculates the binomial coefficient C(n, k).
    
    Args:
        n (int): The total number of elements.
        k (int): The number of elements being chosen.
    
    Returns:
        int: The binomial coefficient C(n, k).
    """
    return factorial(n) // (factorial(k) * factorial(n - k))

def factorial(n):
    """
    Calculates the factorial of a given number.
    
    Args:
        n (int): The number to calculate the factorial for.
    
    Returns:
        int: The factorial of the given number.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def check(candidate):
    assert bell_Number(2) == 2
    assert bell_Number(3) == 5
    assert bell_Number(4) == 15

check(bell_Number)