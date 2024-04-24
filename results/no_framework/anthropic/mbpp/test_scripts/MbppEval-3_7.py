import math

def is_not_prime(n):
    """
    Write a python function to identify non-prime numbers.

    Examples:
    is_not_prime(2) == False
    is_not_prime(10) == True
    is_not_prime(35) == True
    """
    if n <= 1:
        return True  # 0 and 1 are not prime
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return True  # n is divisible by i, so it's not prime
    
    return False  # n is prime

def check(candidate):
    assert is_not_prime(2) == False
    assert is_not_prime(10) == True
    assert is_not_prime(35) == True
    assert is_not_prime(37) == False

check(is_not_prime)