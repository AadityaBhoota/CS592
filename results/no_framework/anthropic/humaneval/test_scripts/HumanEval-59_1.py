def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    i = 2
    largest_factor = 1

    while i * i <= n:
        if n % i == 0:
            largest_factor = i
            n //= i
        else:
            i += 1

    if n > 1:
        largest_factor = n

    return largest_factor



METADATA = {}


def check(candidate):
    assert candidate(15) == 5
    assert candidate(27) == 3
    assert candidate(63) == 7
    assert candidate(330) == 11
    assert candidate(13195) == 29


check(largest_prime_factor)