def newman_prime(n):
    """
    Finds the nth Newman-Shanks-Williams prime number.
    """
    if n == 1:
        return 2
    
    newman_primes = [2]
    p = 3
    while len(newman_primes) < n:
        if is_prime(p) and is_prime(2 ** p - 1):
            newman_primes.append(2 ** p - 1)
        p += 2
    
    return newman_primes[n - 1]

def is_prime(n):
    """
    Checks if a number is prime.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def check(candidate):
    assert newman_prime(3) == 7
    assert newman_prime(4) == 17
    assert newman_prime(5) == 41

check(newman_prime)