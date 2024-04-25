def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Check if n is divisible by 2
    while n % 2 == 0:
        largest_factor = 2
        n //= 2

    # Check if n is divisible by odd numbers
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            largest_factor = i
            n //= i

    # If n is a prime number greater than 2, then n is the largest prime factor
    if n > 2:
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