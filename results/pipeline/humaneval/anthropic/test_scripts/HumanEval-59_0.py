def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    max_prime = 2
    i = 2
    
    while i * i <= n:
        if n % i == 0:
            max_prime = max(max_prime, i)
        i += 1
    
    if max_prime == 2:
        return n
    else:
        return max_prime



METADATA = {}


def check(candidate):
    assert candidate(15) == 5
    assert candidate(27) == 3
    assert candidate(63) == 7
    assert candidate(330) == 11
    assert candidate(13195) == 29


check(largest_prime_factor)