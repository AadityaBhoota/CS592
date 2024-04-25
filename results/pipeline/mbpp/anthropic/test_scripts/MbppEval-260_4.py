def newman_prime(n):
    """
    Find the nth Newman-Shanks-Williams prime number.
    """
    if n == 1:
        return 3
    if n == 2:
        return 5
    
    a = 3
    b = 5
    for _ in range(n-2):
        a, b = b, a + b
    
    return b

def check(candidate):
    assert newman_prime(3) == 7
    assert newman_prime(4) == 17
    assert newman_prime(5) == 41

check(newman_prime)