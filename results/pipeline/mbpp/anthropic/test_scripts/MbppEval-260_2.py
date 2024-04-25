def newman_prime(n):
    """
    Find the nth Newman-Shanks-Williams prime number.
    
    Args:
        n (int): The index of the Newman-Shanks-Williams prime number to find.
    
    Returns:
        int: The nth Newman-Shanks-Williams prime number.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    
    primes = []
    i = 1
    while len(primes) < n:
        candidate = 2 ** i - 1
        if all(candidate % p != 0 for p in primes):
            primes.append(candidate)
        i += 1
    
    return primes[n - 1]

def check(candidate):
    assert newman_prime(3) == 7
    assert newman_prime(4) == 17
    assert newman_prime(5) == 41

check(newman_prime)