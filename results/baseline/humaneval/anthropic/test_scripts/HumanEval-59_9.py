def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n <= 1:
        raise ValueError("Input must be greater than 1")
    if is_prime(n):
        raise ValueError("Input must not be a prime number")

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

def is_prime(n: int) -> bool:
    """Return True if n is a prime number, False otherwise."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True



METADATA = {}


def check(candidate):
    assert candidate(15) == 5
    assert candidate(27) == 3
    assert candidate(63) == 7
    assert candidate(330) == 11
    assert candidate(13195) == 29


check(largest_prime_factor)