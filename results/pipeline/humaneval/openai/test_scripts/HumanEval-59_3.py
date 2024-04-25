def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def largest_prime_factor(n: int):
    prime_factors = []
    
    # Iterate from 2 to n // 2
    for i in range(2, n // 2 + 1):
        if n % i == 0 and is_prime(i):
            prime_factors.append(i)
    
    # Include n if n is prime
    if is_prime(n):
        prime_factors.append(n)
    
    # Find the largest prime factor
    largest_prime = max(prime_factors)
    
    return largest_prime



METADATA = {}


def check(candidate):
    assert candidate(15) == 5
    assert candidate(27) == 3
    assert candidate(63) == 7
    assert candidate(330) == 11
    assert candidate(13195) == 29


check(largest_prime_factor)