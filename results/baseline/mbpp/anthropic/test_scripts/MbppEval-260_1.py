def is_prime(n):
    """
    Helper function to check if a number is prime.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def newman_prime(n):
    """
    Find the nth Newman–Shanks–Williams prime number.
    """
    if n < 1:
        raise ValueError("n must be a positive integer")
    
    count = 0
    num = 2
    while count < n:
        if is_prime(num) and is_prime(num + 2) and is_prime(num + 6):
            count += 1
        num += 1
    
    return num - 1

def check(candidate):
    assert newman_prime(3) == 7
    assert newman_prime(4) == 17
    assert newman_prime(5) == 41

check(newman_prime)