def largest_prime_factor(n: int):
    # Initialize the largest prime factor
    max_prime = 1
  
    # Remove all factors of 2 from n
    while n % 2 == 0:
        max_prime = 2
        n = n // 2
  
    # After this, n must be odd. We can skip 2 for the next iteration.

    # Try all odd factors up to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            max_prime = i
            n = n // i
  
    # If n is a prime greater than 2
    if n > 2:
        max_prime = n

    return max_prime

# Test cases





METADATA = {}


def check(candidate):
    assert candidate(15) == 5
    assert candidate(27) == 3
    assert candidate(63) == 7
    assert candidate(330) == 11
    assert candidate(13195) == 29


check(largest_prime_factor)