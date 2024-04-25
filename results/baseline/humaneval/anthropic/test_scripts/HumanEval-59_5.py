def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.
    """
    if n <= 1:
        raise ValueError("n must be greater than 1")
    if is_prime(n):
        raise ValueError("n must not be a prime number")

    largest_factor = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            largest_factor = i
            while n % i == 0:
                n //= i
        i += 1

    if n > 1:
        largest_factor = n

    return largest_factor

def is_prime(n: int) -> bool:
    """
    Check if a number is prime.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage:





METADATA = {}


def check(candidate):
    assert candidate(15) == 5
    assert candidate(27) == 3
    assert candidate(63) == 7
    assert candidate(330) == 11
    assert candidate(13195) == 29


check(largest_prime_factor)