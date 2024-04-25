import math

def is_not_prime(n):
    if n < 2:
        return True
    
    if n == 2:
        return False
    
    sqrt_n = math.isqrt(n)  # Calculate the square root of n

    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            return True  # n is not a prime number

    return False  # n is a prime number

def check(candidate):
    assert is_not_prime(2) == False
    assert is_not_prime(10) == True
    assert is_not_prime(35) == True
    assert is_not_prime(37) == False

check(is_not_prime)