import math

def is_not_prime(n):
    '''
    Write a python function to identify non-prime numbers.

    Examples:
    is_not_prime(2) == False
    is_not_prime(10) == True
    is_not_prime(35) == True
    '''
    if n <= 1:
        return True
    if n == 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return True
    return False

def check(candidate):
    assert is_not_prime(2) == False
    assert is_not_prime(10) == True
    assert is_not_prime(35) == True
    assert is_not_prime(37) == False

check(is_not_prime)