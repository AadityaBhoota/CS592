def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    largest_factor = 2
    while n > 1:
        if n % largest_factor == 0:
            n //= largest_factor
        else:
            largest_factor += 2
    return largest_factor



METADATA = {}


def check(candidate):
    assert candidate(15) == 5
    assert candidate(27) == 3
    assert candidate(63) == 7
    assert candidate(330) == 11
    assert candidate(13195) == 29


check(largest_prime_factor)