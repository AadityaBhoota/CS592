def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    largest_prime = 1
    prime = 2
    
    while n > 1:
        if n % prime == 0:
            largest_prime = prime
            n //= prime
        else:
            if prime == 2:
                prime = 3
            else:
                prime += 2
    
    return largest_prime



METADATA = {}


def check(candidate):
    assert candidate(15) == 5
    assert candidate(27) == 3
    assert candidate(63) == 7
    assert candidate(330) == 11
    assert candidate(13195) == 29


check(largest_prime_factor)