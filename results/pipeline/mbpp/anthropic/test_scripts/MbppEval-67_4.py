def bell_number(n):
    """
    Calculate the Bell number for the given input n.
    
    Args:
        n (int): The input value to calculate the Bell number for.
    
    Returns:
        int: The Bell number for the given input n.
    """
    if n == 0:
        return 1
    
    bell = [0] * (n + 1)
    bell[0] = 1
    
    for i in range(1, n + 1):
        for j in range(i):
            bell[i] += bell[j] * binomial(i, j)
    
    return bell[n]

def binomial(n, k):
    """
    Calculate the binomial coefficient C(n, k).
    
    Args:
        n (int): The total number of elements.
        k (int): The number of elements to choose.
    
    Returns:
        int: The binomial coefficient C(n, k).
    """
    return factorial(n) // (factorial(k) * factorial(n - k))

def factorial(n):
    """
    Calculate the factorial of the given number n.
    
    Args:
        n (int): The number to calculate the factorial for.
    
    Returns:
        int: The factorial of the given number n.
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)

def check(candidate):
    assert bell_number(2)==2
    assert bell_number(10)==115975
    assert bell_number(56)==6775685320645824322581483068371419745979053216268760300

check(bell_number)