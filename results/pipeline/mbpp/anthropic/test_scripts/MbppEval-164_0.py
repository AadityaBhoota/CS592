import math

def div_sum(n):
    """
    Write a function to determine the sum of the divisors of an integer.
    
    Args:
        n (int): The integer to find the divisor sum for.
    
    Returns:
        int: The sum of the divisors of `n`.
    """
    divisor_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisor_sum += i
    return divisor_sum

def areEquivalent(a, b):
    """
    Determine if the sum of the divisors of two integers are the same.
    
    Args:
        a (int): The first integer.
        b (int): The second integer.
    
    Returns:
        bool: True if the sum of the divisors of `a` and `b` are the same, False otherwise.
    """
    return div_sum(a) == div_sum(b)

def check(candidate):
    assert are_equivalent(36, 57) == False
    assert are_equivalent(2, 4) == False
    assert are_equivalent(23, 47) == True

check(div_sum)